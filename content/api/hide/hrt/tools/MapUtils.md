# hrt.tools.MapUtils

**class** · package [`hrt.tools`](README.md) · source [`hrt/tools/MapUtils.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/tools/MapUtils.hx)

Map helpers.

## Static methods

### getOrPut _(runtime (hl) only)_

```haxe
static function getOrPut(map:Map<getOrPut.K, getOrPut.V>, key:getOrPut.K, def:getOrPut.V):Dynamic
```

Returns `map[key]` if key if present, else evaluate `def` and puts the result into `map[key]`, then retunrs `map[key]`
