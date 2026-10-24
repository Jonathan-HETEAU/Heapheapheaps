# Heaps skills for Claude Code

Skills that make Claude Code effective on games made with [Heaps](https://heaps.io) (Haxe) and
its libraries. Each one holds what was learned and checked on real projects: commands, versions
that work together, pitfalls and their fixes, and tested code to start from.

| Skill | Use |
|---|---|
| [heaps-setup](skills/heaps-setup/SKILL.md) | Install Haxe, the libraries and HashLink in compatible versions; create a project (`scripts/new-project.sh`: 2D, 3D, DomKit); build and run for the web and HashLink; fix build errors |
| [heaps-docs](skills/heaps-docs/SKILL.md) | Look up any type of Heaps, HxBit, DomKit, hlsteam and Hide (`scripts/lookup.sh`), find the Heaps sample of a feature |
| [heaps-game](skills/heaps-game/SKILL.md) | Structure and practices of a Heaps game; two complete small games to start from: `assets/skeleton` (turn by turn: title menu, levels, pause, options, save, sounds, keyboard and gamepad, tested rules) and `assets/shooter` (real time: analog movement, fire, particles, best score) |
| [heaps-domkit](skills/heaps-domkit/SKILL.md) | Menus and HUDs with DomKit components and CSS; `references/components.md`: every component and property; `assets/example` |
| [heaps-hide](skills/heaps-hide/SKILL.md) | The Hide editor: build it, load its levels in the game, add your own prefab types with a plugin |
| [heaps-hxbit](skills/heaps-hxbit/SKILL.md) | Versioned binary saves and networking with HxBit |
| [heaps-hlsteam](skills/heaps-hlsteam/SKILL.md) | Steam (achievements, stats, leaderboards, cloud) with hlsteam; `assets/Steam.hx`, safe without Steam |
| [heaps-browser-test](skills/heaps-browser-test/SKILL.md) | Run the web build in headless Chromium: keyboard, mouse and gamepad inputs, screenshots, motion, errors (`scripts/run.js`) |

Install: see the [README of the repository](../../README.md#claude-code-skills). In a session,
the skills are also callable by name: `/heaps:heaps-setup`, `/heaps:heaps-browser-test`...
(or `/heaps-setup`... when copied into a repository's `.claude/skills/`).

The code of the skills (scripts, skeleton, examples) is checked with Haxe 4.3, Heaps, DomKit,
HxBit, hlsteam and Hide from git (October 2026), for JavaScript and HashLink.
