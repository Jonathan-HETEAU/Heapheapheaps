#!/bin/sh
# Checks the code of the Claude Code skills (plugins/heaps) against the local libraries:
# the projects made by new-project.sh, the game skeleton and shooter (and their tests), the DomKit example,
# the Steam wrapper, for JavaScript and HashLink, and the docs lookup script.
# Needs Haxe and the documented libraries as haxelib (dev) libraries, plus hlsdl.
# With --run, also plays the web builds in headless Chromium (needs node and playwright).
set -e
root=$(cd "$(dirname "$0")/.." && pwd)
skills=$root/plugins/heaps/skills
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
run=no; [ "$1" = "--run" ] && run=yes
fail=0

check() { # check <label> <command...>
	label=$1; shift
	if "$@" >"$tmp/log" 2>&1; then echo "ok   $label"; else echo "FAIL $label"; sed 's/^/     /' "$tmp/log" | tail -15; fail=1; fi
}

play() { # play <label> <folder> <steps...>: the web build must load and run without error
	[ $run = yes ] || return 0
	label=$1; dir=$2; shift 2
	check "$label (browser)" node "$skills/heaps-browser-test/scripts/run.js" "$dir" --quiet "$@"
}

for v in "2d" "3d --3d" "2d-domkit --domkit" "3d-domkit --3d --domkit"; do
	set -- $v
	sh "$skills/heaps-setup/scripts/new-project.sh" "$tmp/p-$1" $2 $3 >/dev/null
	check "new-project $1 (js)" sh -c "cd '$tmp/p-$1' && haxe build-js.hxml"
	check "new-project $1 (hl)" sh -c "cd '$tmp/p-$1' && haxe build-hl.hxml"
	play "new-project $1" "$tmp/p-$1" "key ArrowRight 300"
done

cp -r "$skills/heaps-game/assets/skeleton" "$tmp/skeleton"
check "game skeleton (tests)" sh -c "cd '$tmp/skeleton' && haxe test.hxml"
check "game skeleton (js)" sh -c "cd '$tmp/skeleton' && haxe build-js.hxml"
check "game skeleton (hl)" sh -c "cd '$tmp/skeleton' && haxe build-hl.hxml"
play "game skeleton" "$tmp/skeleton" "key Enter" "key ArrowRight" "key Escape" "key Enter"

cp -r "$skills/heaps-game/assets/shooter" "$tmp/shooter"
check "shooter (tests)" sh -c "cd '$tmp/shooter' && haxe test.hxml"
check "shooter (js)" sh -c "cd '$tmp/shooter' && haxe build-js.hxml"
check "shooter (hl)" sh -c "cd '$tmp/shooter' && haxe build-hl.hxml"
play "shooter" "$tmp/shooter" "key Enter" "down Space" "down ArrowLeft" "wait 1000" "up ArrowLeft" "up Space" "key Escape"

cp -r "$skills/heaps-domkit/assets/example" "$tmp/domkit"
check "domkit example (js)" sh -c "cd '$tmp/domkit' && haxe build-js.hxml"
check "domkit example (hl)" sh -c "cd '$tmp/domkit' && haxe build-hl.hxml"
play "domkit example" "$tmp/domkit" "key ArrowDown" "key Enter"

mkdir -p "$tmp/steam/res" && echo x > "$tmp/steam/res/readme.txt"
cp "$skills/heaps-hlsteam/assets/Steam.hx" "$tmp/steam/"
cat > "$tmp/steam/Main.hx" <<'EOF'
class Main extends hxd.App {
	override function init() {
		Steam.unlock("A");
		Steam.addStat("B", 1);
		Steam.submitScore("C", 1);
		Steam.cloudWrite("d", haxe.io.Bytes.alloc(1));
		Steam.cloudRead("d");
	}
	static function main() {
		if( Steam.init() ) { hxd.Res.initEmbed(); new Main(); }
	}
}
EOF
check "Steam.hx (hl, hlsteam)" sh -c "cd '$tmp/steam' && haxe -lib heaps -lib hlsdl -lib hlsteam -main Main -hl a.hl"
check "Steam.hx (hl, no Steam)" sh -c "cd '$tmp/steam' && haxe -lib heaps -lib hlsdl -main Main -hl b.hl"
check "Steam.hx (js)" sh -c "cd '$tmp/steam' && haxe -lib heaps -main Main -js c.js"

HEAPS_DOCS_URL=$root/content HEAPS_DOCS_CACHE=$tmp/cache \
	check "lookup.sh" sh -c "sh '$skills/heaps-docs/scripts/lookup.sh' flow | grep -q h2d.Flow && sh '$skills/heaps-docs/scripts/lookup.sh' --page hxbit.Serializer | grep -q '# hxbit.Serializer'"

exit $fail
