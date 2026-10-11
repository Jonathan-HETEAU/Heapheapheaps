#!/usr/bin/env python3
"""Builds the unified Heaps documentation portal.

  python3 tools/build.py assemble --src DIR   # DIR holds a checkout of each repo of sources.json (DIR/<id>)
  python3 tools/build.py render              # content/ -> site/ (HTML + Markdown + dox sites + search)
  python3 tools/build.py all --src DIR

assemble: copies the generated docs of each repo (docs/api/md, docs/deps, docs/api/html) into content/,
rewrites their links (sources -> GitHub, other repos -> portal pages), links the fully qualified type names
to their page in any repo, and writes the llms.txt files and the home page.
render: converts content/ to a static HTML site in site/, keeping the Markdown files next to the pages.
"""
import json, os, re, shutil, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
SITE = os.path.join(ROOT, "site")
CFG = json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))
REPOS = CFG["repos"]
BASE = CFG["baseUrl"]

LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")
TYPE_RE = re.compile(r"(?<![\[\w])`([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+)`(?!\]\()")
LLMS_ENTRY_RE = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)(?::\s*(.*))?$")


def write(path, text):
	os.makedirs(os.path.dirname(path), exist_ok=True)
	open(path, "w", encoding="utf-8").write(text)


def rel(from_file, to_file):
	return os.path.relpath(to_file, os.path.dirname(from_file)).replace(os.sep, "/")


# ------------------------------------------------------------------ assemble
def map_repo_path(repo, p):
	"""Portal path (relative to content/) of a file of a repo, or None if it stays on GitHub."""
	for prefix, dest in (("docs/api/md/", "api/%s/" % repo["id"]), ("docs/deps/", "deps/%s/" % repo["id"])):
		if p.startswith(prefix):
			return dest + p[len(prefix):]
	if p == "docs/llms.txt":
		return "llms/%s.txt" % repo["id"]
	return None


def github_url(repo, p):
	return "https://github.com/%s/blob/%s/%s" % (repo["github"], repo["branch"], p)


def rewrite_links(text, repo, src_rel, out_rel):
	"""Rewrites the relative links of a repo file `src_rel` copied to `content/out_rel`."""
	def sub(m):
		label, target = m.group(1), m.group(2)
		if re.match(r"^[a-z]+:", target) or target.startswith("#"):
			return m.group(0)
		path, _, anchor = target.partition("#")
		resolved = os.path.normpath(os.path.join(os.path.dirname(src_rel), path)).replace(os.sep, "/")
		if resolved.startswith(".."):
			return m.group(0)
		dest = map_repo_path(repo, resolved)
		if dest is None:
			url = github_url(repo, resolved)
		else:
			url = rel(out_rel, dest)
		return "[%s](%s%s)" % (label, url, "#" + anchor if anchor else "")
	return LINK_RE.sub(sub, text)


def link_types(text, out_rel, index, skip=None):
	"""Links the `fully.qualified.Type` names (outside code blocks and links) to their page."""
	out, in_code = [], False
	for line in text.split("\n"):
		if line.lstrip().startswith("```"):
			in_code = not in_code
		if not in_code and "`" in line:
			def sub(m):
				name = m.group(1)
				target = index.get(name)
				if target is None or target == skip:
					return m.group(0)
				return "[`%s`](%s)" % (name, rel(out_rel, target))
			# do not touch the labels of existing links
			parts, last = [], 0
			for lm in LINK_RE.finditer(line):
				parts.append(TYPE_RE.sub(sub, line[last:lm.start()]))
				parts.append(lm.group(0))
				last = lm.end()
			parts.append(TYPE_RE.sub(sub, line[last:]))
			line = "".join(parts)
		out.append(line)
	return "\n".join(out)


def type_index(src):
	"""Fully qualified type name -> portal path of its page, for all the repos."""
	index = {}
	for repo in REPOS:
		md = os.path.join(src, repo["id"], "docs", "api", "md")
		for d, _, files in os.walk(md):
			for f in files:
				if f.endswith(".md") and f != "README.md":
					p = os.path.relpath(os.path.join(d, f), md).replace(os.sep, "/")
					index.setdefault(p[:-3].replace("/", "."), "api/%s/%s" % (repo["id"], p))
	return index


def intro_text(src, repo, out_rel=None):
	"""The description of a repo (intro of its llms.txt), links rewritten for `content/out_rel`, or absolute without out_rel."""
	intro, _ = read_llms(src, repo)
	text = " ".join(intro).lstrip("> ").strip()
	text = rewrite_links(text, repo, "docs/llms.txt", out_rel or "x")
	if out_rel is None:
		text = LINK_RE.sub(lambda m: m.group(0) if re.match(r"^[a-z]+:", m.group(2)) else "[%s](%s%s)" % (m.group(1), BASE, m.group(2)), text)
	return text


def read_llms(src, repo):
	"""(intro lines, [(section, [(name, path, summary)])]) of the llms.txt of a repo."""
	lines = open(os.path.join(src, repo["id"], "docs", "llms.txt"), encoding="utf-8").read().split("\n")
	intro, sections = [], []
	for l in lines[1:]:
		if l.startswith("## "):
			sections.append((l[3:].strip(), []))
		elif sections:
			m = LLMS_ENTRY_RE.match(l)
			if m:
				sections[-1][1].append((m.group(1), m.group(2), m.group(3) or ""))
		elif l.strip() and not l.startswith("Each link") :
			intro.append(l)
	return intro, sections


def assemble(src):
	for d in ("api", "deps", "llms", "guides"):
		shutil.rmtree(os.path.join(CONTENT, d), ignore_errors=True)
	index = type_index(src)
	stats = []
	for repo in REPOS:
		rdir = os.path.join(src, repo["id"])
		n = 0
		for sub in ("docs/api/md", "docs/deps"):
			base = os.path.join(rdir, sub)
			for d, _, files in os.walk(base):
				for f in files:
					src_rel = os.path.relpath(os.path.join(d, f), rdir).replace(os.sep, "/")
					out_rel = map_repo_path(repo, src_rel)
					if not f.endswith(".md"):
						os.makedirs(os.path.dirname(os.path.join(CONTENT, out_rel)), exist_ok=True)
						shutil.copy(os.path.join(rdir, src_rel), os.path.join(CONTENT, out_rel))
						continue
					text = open(os.path.join(rdir, src_rel), encoding="utf-8").read()
					text = rewrite_links(text, repo, src_rel, out_rel)
					if sub == "docs/api/md":
						own = out_rel if f != "README.md" else None
						text = link_types(text, out_rel, index, own)
						n += f != "README.md"
					write(os.path.join(CONTENT, out_rel), text)
		stats.append((repo, n))
	write_llms(src, index)
	copy_guides()
	write_home(src, stats)
	print("assembled: %d types, %s" % (len(index), ", ".join("%s %d" % (r["id"], n) for r, n in stats)))


def guides():
	"""[(file, title, summary)] of guides/*.md, in name order."""
	res = []
	gdir = os.path.join(ROOT, "guides")
	for f in sorted(os.listdir(gdir)) if os.path.isdir(gdir) else []:
		if not f.endswith(".md") or f == "README.md":
			continue
		text = open(os.path.join(gdir, f), encoding="utf-8").read()
		title = next((l[2:].strip() for l in text.split("\n") if l.startswith("# ")), f[:-3])
		summary = next((l[2:].strip() for l in text.split("\n") if l.startswith("> ")), "")
		res.append((f, title, summary))
	return res


def copy_guides():
	gdir = os.path.join(ROOT, "guides")
	if not os.path.isdir(gdir):
		return
	for d, _, files in os.walk(gdir):
		for f in files:
			p = os.path.relpath(os.path.join(d, f), gdir)
			os.makedirs(os.path.dirname(os.path.join(CONTENT, "guides", p)), exist_ok=True)
			shutil.copy(os.path.join(d, f), os.path.join(CONTENT, "guides", p))


def write_llms(src, index):
	repos_llms = []
	for repo in REPOS:
		intro, sections = read_llms(src, repo)
		out = "llms/%s.txt" % repo["id"]
		intro = ["> " + intro_text(src, repo)]
		L = ["# %s API" % repo["name"], ""] + intro + ["",
			"Each link points to the Markdown page of a type: signatures, documentation, inheritance and platform availability.",
			"Full text of all the pages: %s" % (BASE + "llms/%s-full.txt" % repo["id"]), ""]
		full = ["# %s API (full text)" % repo["name"], ""] + intro + [""]
		count = 0
		for title, entries in sections:
			L.append("## " + title)
			L.append("")
			for name, path, summary in entries:
				page = index.get(name) or map_repo_path(repo, os.path.normpath(os.path.join("docs", path)).replace(os.sep, "/"))
				L.append("- [%s](%s)%s" % (name, BASE + page, ": " + summary if summary else ""))
				count += 1
				fp = os.path.join(CONTENT, page)
				if os.path.exists(fp):
					full.append(open(fp, encoding="utf-8").read().rstrip() + "\n\n---\n")
			L.append("")
		write(os.path.join(CONTENT, out), "\n".join(L))
		write(os.path.join(CONTENT, "llms/%s-full.txt" % repo["id"]), "\n".join(full))
		repos_llms.append((repo, intro, count))

	L = ["# Heaps documentation", "",
		"> Unified documentation of the Heaps game engine (Haxe) and of its libraries: HxBit (serialization and networking), DomKit (UI components and CSS), hlsteam (Steamworks for HashLink) and Hide (the editor and its `hrt` runtime: prefabs, FX, shader graphs).", "",
		"The API reference is generated from the doc comments of the sources. Every page is plain Markdown: fetch the `.md` URLs.", ""]
	g = guides()
	if g:
		L += ["## Guides", ""]
		for f, title, summary in g:
			L.append("- [%s](%s)%s" % (title, BASE + "guides/" + f, ": " + summary if summary else ""))
		L.append("")
	L += ["## API reference", ""]
	for repo, intro, count in repos_llms:
		desc = intro[0][2:]
		L.append("- [%s](%s): %d types. %s" % (repo["name"], BASE + "llms/%s.txt" % repo["id"], count, desc))
	L += ["", "## Optional", ""]
	for repo, _, _ in repos_llms:
		L.append("- [%s full text](%s): all the API pages of %s in one file" % (repo["name"], BASE + "llms/%s-full.txt" % repo["id"], repo["name"]))
		L.append("- [%s file dependencies](%s): modules, packages and dependency cycles" % (repo["name"], BASE + "deps/%s/DEPENDENCIES.md" % repo["id"]))
	write(os.path.join(CONTENT, "llms.txt"), "\n".join(L) + "\n")


def write_home(src, stats):
	L = ["# Heaps documentation", "",
		"Unified documentation of the [Heaps](https://heaps.io) game engine and of its libraries, for humans and AI assistants.", ""]
	g = guides()
	if g:
		L += ["## Guides", "", "| Guide | |", "|---|---|"]
		for f, title, summary in g:
			L.append("| [%s](guides/%s) | %s |" % (title, f, summary))
		L.append("")
	L += ["## API reference", "", "| Library | Types | Reference | HTML (dox) | Dependencies | Sources |", "|---|---:|---|---|---|---|"]
	for repo, n in stats:
		L.append("| **%s** | %d | [Markdown](api/%s/README.md) | [dox](html/%s/index.html) | [map](deps/%s/DEPENDENCIES.md) | [GitHub](https://github.com/%s/tree/%s) |"
			% (repo["name"], n, repo["id"], repo["id"], repo["id"], repo["github"], repo["branch"]))
	L += ["", "### What each library does", ""]
	for repo, _ in stats:
		L.append("- **%s**: %s" % (repo["name"], intro_text(src, repo, "README.md")))
	L += ["", "## For AI assistants", "",
		"- [llms.txt](llms.txt): index of the documentation ([llmstxt.org](https://llmstxt.org) format), with one index per library under `llms/`.",
		"- `llms/<library>-full.txt`: all the API pages of a library in one file.",
		"- Every page of this site is also available as Markdown: replace `.html` with `.md` in the URL.",
		"", "## How it is built", "",
		"The doc comments live in the sources of each library. Each repository generates its own reference (`tools/docgen/build-api.sh`); this portal assembles them, links the types across libraries and publishes the site (`tools/build.py`, run by GitHub Actions).", ""]
	write(os.path.join(CONTENT, "README.md"), "\n".join(L))


# ------------------------------------------------------------------ render
CSS = """
:root{--bg:#fff;--fg:#1f2328;--muted:#59636e;--border:#d1d9e0;--code:#f6f8fa;--link:#0969da;--accent:#f6f8fa}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--fg:#e6edf3;--muted:#9198a1;--border:#3d444d;--code:#151b23;--link:#4493f8;--accent:#151b23}}
:root[data-theme="dark"]{--bg:#0d1117;--fg:#e6edf3;--muted:#9198a1;--border:#3d444d;--code:#151b23;--link:#4493f8;--accent:#151b23}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:2;background:var(--accent);border-bottom:1px solid var(--border)}
header .in{max-width:1100px;margin:0 auto;padding:8px 16px;display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center}
header .brand{font-weight:600;color:var(--fg)}
header nav{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:14px}
#q{margin-left:auto;min-width:220px;flex:1 1 220px;max-width:360px;padding:6px 10px;border:1px solid var(--border);border-radius:6px;background:var(--bg);color:var(--fg)}
#res{position:absolute;right:16px;top:100%;width:min(560px,calc(100vw - 32px));max-height:70vh;overflow:auto;background:var(--bg);border:1px solid var(--border);border-radius:6px;display:none;box-shadow:0 8px 24px rgba(0,0,0,.2)}
#res a{display:block;padding:6px 10px;border-bottom:1px solid var(--border);color:var(--fg)}#res a:hover,#res a.sel{background:var(--code);text-decoration:none}
#res b{color:var(--link);font-weight:600}#res span{display:block;font-size:13px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
main{max-width:1100px;margin:0 auto;padding:16px 16px 64px;overflow-wrap:anywhere}
.crumbs{font-size:14px;color:var(--muted);margin-bottom:8px}.alt{float:right;font-size:13px}
pre{background:var(--code);padding:12px;border-radius:6px;overflow:auto;font-size:14px;line-height:1.45}
code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:90%}pre code{background:none;padding:0}
table{border-collapse:collapse;display:block;overflow:auto;max-width:100%}th,td{border:1px solid var(--border);padding:6px 10px;vertical-align:top}th{background:var(--code)}
blockquote{margin:0;padding:0 1em;color:var(--muted);border-left:4px solid var(--border)}
h1,h2,h3{line-height:1.25}h2{border-bottom:1px solid var(--border);padding-bottom:.3em}
h3{font-size:1.05em}
"""

JS = """
(function(){
var q=document.getElementById('q'),res=document.getElementById('res'),idx=null,sel=-1;
function load(cb){if(idx)return cb();fetch(ROOT+'search.json').then(function(r){return r.json()}).then(function(d){idx=d;cb()})}
function show(){var v=q.value.trim().toLowerCase();if(!v){res.style.display='none';return}
load(function(){var words=v.split(/\\s+/),out=[];for(var i=0;i<idx.length&&out.length<40;i++){var e=idx[i],n=e[0].toLowerCase(),t=(n+' '+e[1]).toLowerCase();
if(words.every(function(w){return t.indexOf(w)>=0})){var last=n.split('.').pop(),lw=words[words.length-1];
var inName=words.every(function(w){return n.indexOf(w)>=0});out.push([(last==lw?0:last.indexOf(lw)==0?2:4)+(inName?0:1),e])}}
out.sort(function(a,b){return a[0]-b[0]});
res.innerHTML=out.length?out.map(function(o){var e=o[1];return '<a href="'+ROOT+e[2]+'"><b>'+esc(e[0])+'</b><span>'+esc(e[1])+'</span></a>'}).join(''):'<a>No result</a>';
res.style.display='block';sel=-1})}
function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
q.addEventListener('input',show);q.addEventListener('focus',show);
q.addEventListener('keydown',function(e){var a=res.querySelectorAll('a[href]');if(e.key=='ArrowDown'||e.key=='ArrowUp'){sel=Math.max(0,Math.min(a.length-1,sel+(e.key=='ArrowDown'?1:-1)));a.forEach(function(x,i){x.classList.toggle('sel',i==sel)});e.preventDefault()}
else if(e.key=='Enter'&&a.length){location.href=a[Math.max(sel,0)].href}else if(e.key=='Escape'){res.style.display='none';q.blur()}});
document.addEventListener('click',function(e){if(!res.contains(e.target)&&e.target!=q)res.style.display='none'});
document.addEventListener('keydown',function(e){if(e.key=='/'&&document.activeElement!=q){q.focus();e.preventDefault()}});
})();
"""

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="{root}assets/style.css">
<link rel="alternate" type="text/markdown" href="{md}"></head>
<body><header><div class="in" style="position:relative"><a class="brand" href="{root}index.html">Heaps docs</a>
<nav>{nav}</nav><input id="q" type="search" placeholder="Search a type ( / )" autocomplete="off"><div id="res"></div></div></header>
<main><div class="crumbs">{crumbs}<a class="alt" href="{md}">Markdown</a></div>
{body}
</main><script>var ROOT="{root}";</script><script src="{root}assets/search.js"></script></body></html>
"""


def md_to_html_links(h):
	def sub(m):
		url, anchor = m.group(1), m.group(2) or ""
		if os.path.basename(url) == "README":
			url = url[:-len("README")] + "index"
		return 'href="%s.html%s"' % (url, anchor)
	return re.sub(r'href="((?![a-z]+:)[^"#]*?)\.md(#[^"]*)?"', sub, h)


def render():
	import markdown
	shutil.rmtree(SITE, ignore_errors=True)
	shutil.copytree(CONTENT, SITE, ignore=shutil.ignore_patterns("html"))
	open(os.path.join(SITE, ".nojekyll"), "w").close()
	write(os.path.join(SITE, "assets", "style.css"), CSS)
	write(os.path.join(SITE, "assets", "search.js"), JS)
	# dox sites
	if os.path.isdir(os.path.join(CONTENT, "html")):
		shutil.copytree(os.path.join(CONTENT, "html"), os.path.join(SITE, "html"))
	# search index from the llms indexes
	search = []
	for repo in REPOS:
		p = os.path.join(CONTENT, "llms", repo["id"] + ".txt")
		for l in open(p, encoding="utf-8").read().split("\n") if os.path.exists(p) else []:
			m = LLMS_ENTRY_RE.match(l)
			if m:
				url = m.group(2)[len(BASE):] if m.group(2).startswith(BASE) else m.group(2)
				search.append([m.group(1), (m.group(3) or "")[:160], url[:-3] + ".html" if url.endswith(".md") else url])
	for f, title, summary in guides():
		search.append(["Guide: " + title, summary[:160], "guides/" + f[:-3] + ".html"])
	write(os.path.join(SITE, "search.json"), json.dumps(search, separators=(",", ":")))
	md = markdown.Markdown(extensions=["fenced_code", "tables", "toc", "sane_lists"])
	count = 0
	for d, _, files in os.walk(SITE):
		if os.path.relpath(d, SITE).split(os.sep)[0] in ("html", "assets"):
			continue
		for f in files:
			if not f.endswith(".md"):
				continue
			p = os.path.join(d, f)
			r = os.path.relpath(p, SITE).replace(os.sep, "/")
			text = open(p, encoding="utf-8").read()
			md.reset()
			body = md_to_html_links(md.convert(text))
			title = next((l[2:].strip() for l in text.split("\n") if l.startswith("# ")), f[:-3]).replace("`", "")
			depth = r.count("/")
			root = "../" * depth
			nav = " ".join('<a href="%sapi/%s/index.html">%s</a>' % (root, x["id"], x["name"]) for x in REPOS)
			if os.path.isdir(os.path.join(SITE, "guides")):
				nav = '<a href="%sguides/index.html">Guides</a> ' % root + nav
			nav += ' <a href="%sllms.txt">llms.txt</a>' % root
			parts = r.split("/")[:-1]
			crumbs = '<a href="%sindex.html">Home</a>' % root
			for i, part in enumerate(parts):
				up = "../" * (len(parts) - i - 1)
				exists = os.path.exists(os.path.join(SITE, *parts[:i + 1], "README.md"))
				crumbs += ' / ' + ('<a href="%sindex.html">%s</a>' % (up, html.escape(part)) if exists else html.escape(part))
			out = p[:-3] + ".html" if f != "README.md" else os.path.join(d, "index.html")
			write(out, PAGE.format(title=html.escape(title + " · Heaps docs"), root=root, nav=nav, crumbs=crumbs, md=f, body=body))
			count += 1
	print("rendered %d pages, %d search entries" % (count, len(search)))


def copy_dox(src):
	for repo in REPOS:
		s = os.path.join(src, repo["id"], "docs", "api", "html")
		d = os.path.join(CONTENT, "html", repo["id"])
		shutil.rmtree(d, ignore_errors=True)
		if os.path.isdir(s):
			shutil.copytree(s, d)


if __name__ == "__main__":
	cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
	src = sys.argv[sys.argv.index("--src") + 1] if "--src" in sys.argv else os.path.join(ROOT, "src")
	if cmd in ("assemble", "all"):
		assemble(src)
		copy_dox(src)
	if cmd in ("render", "all"):
		render()
