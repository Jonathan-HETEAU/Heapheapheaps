# Heapheapheaps — Heaps documentation portal

Unified documentation of the [Heaps](https://heaps.io) game engine and of its libraries (HxBit, DomKit, hlsteam, Hide), for humans and AI assistants.

- Site: https://jonathan-heteau.github.io/heapheapheaps/
- Start page (Markdown): [content/README.md](content/README.md)
- For AI assistants: [content/llms.txt](content/llms.txt) ([llmstxt.org](https://llmstxt.org) format)

## Layout

| Path | Content |
|---|---|
| `sources.json` | The documented repositories (GitHub repository and branch) |
| `guides/` | Hand-written guides (Markdown) |
| `content/` | Generated Markdown: API reference per library (`api/<lib>/`), dependency maps (`deps/<lib>/`), `llms.txt` indexes (`llms/`) |
| `tools/build.py` | Assembles `content/` from the repositories and renders the HTML site in `site/` |
| `.github/workflows/pages.yml` | Rebuilds and publishes the site on push and every night |

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
- `python3 tools/snippets/check.py --src src` type checks every ```` ```haxe ```` example of the doc comments and READMEs of the libraries, in the context described in `tools/snippets/context.py`.
