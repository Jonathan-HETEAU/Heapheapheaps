# Heaps documentation

Unified documentation of the [Heaps](https://heaps.io) game engine and of its libraries, for humans and AI assistants.

## Guides

| Guide | |
|---|---|
| [Getting started](guides/01-getting-started.md) | Install Heaps, write a first application, compile it for the browser (WebGL) and for HashLink, and understand its life cycle. |
| [Using Hide, the Heaps editor](guides/02-hide.md) | Build and run Hide, make a level with it, load the level in a Heaps game, and add your own prefab types to the editor. · [Français](guides/fr/02-hide.md) |

## API reference

| Library | Types | Reference | HTML (dox) | Dependencies | Sources |
|---|---:|---|---|---|---|
| **Heaps** | 990 | [Markdown](api/heaps/README.md) | [dox](html/heaps/index.html) | [map](deps/heaps/DEPENDENCIES.md) | [GitHub](https://github.com/Jonathan-HETEAU/heaps/tree/ccr-01f70725-tatboj) |
| **HxBit** | 54 | [Markdown](api/hxbit/README.md) | [dox](html/hxbit/index.html) | [map](deps/hxbit/DEPENDENCIES.md) | [GitHub](https://github.com/Jonathan-HETEAU/hxbit/tree/ccr-01f70725-tatboj) |
| **DomKit** | 53 | [Markdown](api/domkit/README.md) | [dox](html/domkit/index.html) | [map](deps/domkit/DEPENDENCIES.md) | [GitHub](https://github.com/Jonathan-HETEAU/domkit/tree/ccr-01f70725-tatboj) |
| **hlsteam** | 75 | [Markdown](api/hlsteam/README.md) | [dox](html/hlsteam/index.html) | [map](deps/hlsteam/DEPENDENCIES.md) | [GitHub](https://github.com/Jonathan-HETEAU/hlsteam/tree/ccr-01f70725-tatboj) |
| **Hide** | 1069 | [Markdown](api/hide/README.md) | [dox](html/hide/index.html) | [map](deps/hide/DEPENDENCIES.md) | [GitHub](https://github.com/Jonathan-HETEAU/hide/tree/ccr-01f70725-tatboj) |

### What each library does

- **Heaps**: Heaps is a cross-platform 2D/3D game engine written in Haxe (targets: HashLink with SDL/OpenGL or DirectX, and JavaScript/WebGL). Packages: `h2d` (2D scene graph), `h3d` (3D engine, GPU abstraction), `hxd` (resources, input, system, sound), `hxsl` (Haxe shader language).
- **HxBit**: HxBit is a binary serialization and network synchronization library for Haxe: classes implementing `hxbit.Serializable` get macro-generated, strictly typed serialization code; `hxbit.NetworkSerializable` objects are replicated by a `hxbit.NetworkHost` (property sync and RPCs). The README explains the concepts: [README.md](https://github.com/Jonathan-HETEAU/hxbit/blob/ccr-01f70725-tatboj/README.md).
- **DomKit**: DomKit is a strictly typed UI framework for Haxe based on components and CSS: components are declared with an XML-like markup (`static var SRC = <comp>...</comp>`) compiled by macros, and styled with CSS properties checked at compile time. It is used by Heaps (`h2d.domkit`): see https://heaps.io/documentation/domkit.html.
- **hlsteam**: hlsteam is a Haxe wrapper of the Steamworks API for HashLink (native library `steam.hdll`): initialization and callbacks (`steam.Api`), achievements, stats and leaderboards, cloud files, Workshop (UGC), friends, lobbies and matchmaking, networking, game servers, timeline and Steam Input controllers. See the README for the setup.
- **Hide**: Hide (Heaps IDE) is the editor of the Heaps engine. `hrt` is its runtime, used by the games: prefabs (3D levels, FX, materials, render props...), shader graphs, animation graphs and texture graphs. `hide` is the editor itself (JS/nw.js and HashLink versions): views, property editors, CastleDB editor and editing tools of the prefabs.

## For AI assistants

- [llms.txt](llms.txt): index of the documentation ([llmstxt.org](https://llmstxt.org) format), with one index per library under `llms/`.
- `llms/<library>-full.txt`: all the API pages of a library in one file.
- Every page of this site is also available as Markdown: replace `.html` with `.md` in the URL.

## How it is built

The doc comments live in the sources of each library. Each repository generates its own reference (`tools/docgen/build-api.sh`); this portal assembles them, links the types across libraries and publishes the site (`tools/build.py`, run by GitHub Actions).
