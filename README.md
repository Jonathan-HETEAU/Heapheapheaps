# Heapheapheaps — Heaps documentation portal

Unified documentation of the [Heaps](https://heaps.io) game engine and of its libraries (HxBit, DomKit, hlsteam, Hide), for humans and AI assistants.

- Site: https://jonathan-heteau.github.io/heapheapheaps/
- Start page (Markdown): [content/README.md](content/README.md)
- For AI assistants: [content/llms.txt](content/llms.txt) ([llmstxt.org](https://llmstxt.org) format)

## Claude Code skills

The plugin `heaps` ([plugins/heaps](plugins/heaps/README.md)) gives Claude Code the practical
knowledge of this stack: setting up and creating a project, looking up the API, structuring a
game, DomKit UI, Hide, HxBit, hlsteam, and checking a build in a headless browser.

```text
/plugin marketplace add Jonathan-HETEAU/Heapheapheaps
/plugin install heaps@heapheapheaps
```

or in one step (Claude Code 2.1.275 or later): `/plugin install heaps --marketplace Jonathan-HETEAU/Heapheapheaps`.

Cloud sessions (Claude Code on the web) do not install plugins: copy the skills into the game
repository instead, and commit them:

```sh
plugins/heaps/install-skills.sh <game repository>    # -> <game repository>/.claude/skills/heaps-*
```

## Layout

| Path | Content |
|---|---|
| `sources.json` | The documented repositories (GitHub repository and branch) |
| `guides/` | Hand-written guides (Markdown); `guides/<lang>/` holds their translations, under the same file names |
| `content/` | Generated Markdown: API reference per library (`api/<lib>/`), dependency maps (`deps/<lib>/`), `llms.txt` indexes (`llms/`) |
| `tools/build.py` | Assembles `content/` from the repositories and renders the HTML site in `site/` |
| `.github/workflows/pages.yml` | Rebuilds and publishes the site on push and every night |
| `.claude-plugin/marketplace.json`, `plugins/heaps/` | The Claude Code plugin and its skills |

The doc comments live in the sources of each library: each repository generates its own reference with `tools/docgen/build-api.sh`, and this portal assembles them.

## Build locally

```sh
pip install markdown==3.7
# clone each repository of sources.json into src/<id> (on its branch), then:
python3 tools/build.py all --src src
python3 -m http.server -d site
```

Checking the examples (needs Haxe and the libraries as haxelib dev libraries):

- `tools/check-examples.sh` compiles the examples of the guides (`guides/examples/`).
- `tools/check-skills.sh [--run]` compiles the code of the Claude Code skills (new projects, game skeleton, DomKit example, Steam wrapper) for JS and HashLink; `--run` also plays the web builds in headless Chromium.
- `python3 tools/snippets/check.py --src src` type checks every ```` ```haxe ```` example of the doc comments and READMEs of the libraries, in the context described in `tools/snippets/context.py`.
