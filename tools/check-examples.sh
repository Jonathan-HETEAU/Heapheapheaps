#!/bin/sh
# Compiles the examples of the guides (guides/examples/*/build-*.hxml, and the Hide plugins
# */hide-plugin.hxml) against the local libraries.
# Needs Haxe and the documented libraries as haxelib (dev) libraries.
set -e
cd "$(dirname "$0")/../guides/examples"
fail=0
for hxml in */build-*.hxml */hide-plugin.hxml; do
	[ -f "$hxml" ] || continue
	dir=$(dirname "$hxml")
	if (cd "$dir" && haxe "$(basename "$hxml")" >/dev/null 2>&1); then echo "ok   $hxml"; else echo "FAIL $hxml"; fail=1; fi
done
exit $fail
