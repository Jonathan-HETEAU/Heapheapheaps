#!/bin/sh
# Copies the skills of this plugin into a game repository: <repo>/.claude/skills/heaps-*.
#
#   install-skills.sh <game repository>
#
# Claude Code loads the skills of a repository's .claude/skills/ everywhere, cloud sessions
# included (which do not install plugins). Commit the copied folders in the game repository; run
# the script again to update them.
set -e
[ -d "$1" ] || { echo "usage: $0 <game repository>" >&2; exit 2; }
src=$(cd "$(dirname "$0")/skills" && pwd)
mkdir -p "$1/.claude/skills"
for d in "$src"/*/; do
	name=$(basename "$d")
	rm -rf "$1/.claude/skills/$name"
	cp -r "$d" "$1/.claude/skills/$name"
	echo "installed $name"
done
