# steam.helpers.MacroHelper

**class** · package [`steam.helpers`](README.md) · source [`steam/helpers/MacroHelper.hx`](https://github.com/Jonathan-HETEAU/hlsteam/blob/ccr-01f70725-tatboj/steam/helpers/MacroHelper.hx)

Macros used by the `steam` package.

## Static methods

### buildMap

```haxe
static function buildMap(typePath:Dynamic, invert:Dynamic, ?exclude:Dynamic):Dynamic
```

* Builds a map from static uppercase inline variables in an abstract type.
*
* @param   invert  Use the field value as the key and the name as the value
