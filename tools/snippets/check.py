#!/usr/bin/env python3
"""Compiles the Haxe code examples of the documented repositories.

  python3 tools/snippets/check.py --src DIR [filter]

Extracts the ```haxe blocks of the doc comments (`/** */` in .hx files) and of the Markdown files
(README...) of each repository of sources.json (checked out in DIR/<id>), wraps each one in the
context it assumes (see context.py) and type checks it with the Haxe compiler (`--no-output`).
Needs Haxe and the libraries as haxelib (dev) libraries. Prints one line per example and a summary;
the exit code is 1 if an example fails.
"""
import json, os, re, subprocess, sys, tempfile, textwrap, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import context

REPOS = [r["id"] for r in json.load(open(os.path.join(ROOT, "sources.json")))["repos"]]
SKIP_DIRS = {".git", "docs", "node_modules", "bin"}


def extract(src):
	"""[(repo, rel path, line, code)] of the ```haxe blocks."""
	res = []
	for repo in REPOS:
		base = os.path.join(src, repo)
		for d, dirs, files in os.walk(base):
			dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
			for f in sorted(files):
				p = os.path.join(d, f)
				rel = os.path.relpath(p, src).replace(os.sep, "/")
				if f.endswith(".hx"):
					txt = open(p, encoding="utf-8", errors="replace").read()
					for m in re.finditer(r"/\*\*(.*?)\*\*/", txt, re.S):
						for b in re.finditer(r"```haxe[ \t]*\r?\n(.*?)```", m.group(1), re.S):
							line = txt.count("\n", 0, m.start(1) + b.start()) + 1
							res.append((repo, rel, line, b.group(1)))
				elif f.endswith(".md"):
					txt = open(p, encoding="utf-8", errors="replace").read()
					for b in re.finditer(r"```haxe[ \t]*\r?\n(.*?)```", txt, re.S):
						res.append((repo, rel, txt.count("\n", 0, b.start()) + 1, b.group(1)))
	return res


def key(rel, code):
	first = next((l.strip() for l in code.split("\n") if l.strip()), "")
	return "%s :: %s" % (rel, first)


def clean(code):
	code = textwrap.dedent(code.replace("\r", "").replace("\t", "    "))
	# `...` lines stand for omitted code
	return "\n".join(l for l in code.split("\n") if l.strip().strip(".") != "" or l.strip() == "")


def build(repo, rel, code, ctx):
	"""(hxml lines, Snippet.hx source) for an example."""
	env = context.ENVS[ctx.get("env", context.DEFAULT_ENV[repo])]
	code = clean(code)
	mode = ctx.get("mode")
	if mode is None:
		mode = "module" if re.search(r"^(@:\S+\s+)*(class|interface|typedef|enum|abstract)\s", code, re.M) else "body"
	module, members, body = "", "", ""
	if "wrap" in ctx:
		module = ctx["wrap"].replace("{code}", code)
	elif mode == "module":
		module = code
	elif mode == "members":
		members = code
	elif mode == "members-body":
		# class members, then statements after the `split` marker line
		marker = ctx["split"]
		i = code.index(marker)
		members, body = code[:i], code[i:]
	elif mode == "split":
		# top-level declarations go to the module, the rest is the body
		lines, mod, rest, depth, in_decl = code.split("\n"), [], [], 0, False
		for l in lines:
			if depth == 0 and re.match(r"^(@:\S+\s+)*(class|interface|typedef|enum|abstract)\s", l):
				in_decl = True
			(mod if in_decl else rest).append(l)
			if in_decl:
				depth += l.count("{") - l.count("}")
				if depth == 0 and "}" in l:
					in_decl = False
		module, body = "\n".join(mod), "\n".join(rest)
	else:
		body = code
	src = "\n".join([
		env.get("imports", ""),
		ctx.get("imports", ""),
		module,
		ctx.get("module", ""),
		"class Snippet%s%s {" % (" extends " + env["base"] if env.get("base") else "",
			" implements " + ctx["implements"] if ctx.get("implements") else ""),
		env.get("members", ""),
		ctx.get("members", ""),
		members,
		"\tfunction test() {",
		ctx.get("locals", ""),
		body,
		"\t}",
		"\tstatic function main() {}",
		"}",
	])
	hxml = env["hxml"] + ctx.get("hxml", [])
	return hxml, src


def run(src_dir, flt=None):
	examples = extract(src_dir)
	ok = fail = skip = 0
	failures = []
	tmp = tempfile.mkdtemp(prefix="snippets")
	for repo, rel, line, code in examples:
		k = key(rel, code)
		if flt and flt not in k:
			continue
		ctx = context.CONTEXT.get(k, {})
		if "skip" in ctx:
			print("skip %s:%d  (%s)" % (rel, line, ctx["skip"]))
			skip += 1
			continue
		hxml, source = build(repo, rel, code, ctx)
		d = os.path.join(tmp, hashlib.sha1(k.encode()).hexdigest()[:10])
		os.makedirs(d, exist_ok=True)
		open(os.path.join(d, "Snippet.hx"), "w").write(source)
		args = ["haxe", "-cp", d, "-main", "Snippet", "--no-output", "-D", "resourcesPath=" + os.path.join(HERE, "res")]
		for h in hxml:
			args += h.replace("$SRC", src_dir).split(" ", 1) if " " in h else [h]
		p = subprocess.run(args, capture_output=True, text=True, cwd=os.path.join(src_dir, repo))
		if p.returncode == 0:
			print("ok   %s:%d" % (rel, line))
			ok += 1
		else:
			print("FAIL %s:%d  [%s]" % (rel, line, k))
			err = "\n".join(l.replace(d + "/", "") for l in (p.stderr + p.stdout).strip().split("\n")[:8])
			print(textwrap.indent(err, "     "))
			failures.append(k)
			fail += 1
	print("\n%d ok, %d failed, %d skipped" % (ok, fail, skip))
	return fail


if __name__ == "__main__":
	src = sys.argv[sys.argv.index("--src") + 1] if "--src" in sys.argv else os.path.join(ROOT, "src")
	rest = [a for i, a in enumerate(sys.argv[1:], 1) if a != "--src" and sys.argv[i - 1] != "--src"]
	sys.exit(1 if run(src, rest[0] if rest else None) else 0)
