# hrt.prefab.fx.EmitterMacros

**class** · package [`hrt.prefab.fx`](README.md) · source [`hrt/prefab/fx/EmitterMacros.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/EmitterMacros.hx)

Builds the parameters of `Emitter` from their `@:param` and `@:instParam` metadata.

## Static methods

### param _(runtime (hl) only)_

```haxe
static function param(e:Dynamic):Dynamic
```

Returns the value of the parameter `e` (a field name), with its random variation if any.
