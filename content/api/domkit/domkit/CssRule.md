# domkit.CssRule

**typedef** · package [`domkit`](README.md) · module [`domkit.CssParser`](CssParser.md) · source [`domkit/CssParser.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/CssParser.hx)

A property set by a CSS rule, with its position in the source.

## Fields

### vmin

```haxe
var vmin:Int
```

The start position of the value.

### value

```haxe
var value:CssValue
```

The value.

### pmin

```haxe
var pmin:Int
```

The start position of the property name.

### pmax

```haxe
var pmax:Int
```

The end position of the value.

### p

```haxe
var p:Property
```

The property.

### file

```haxe
var file:String
```

The CSS file, or `null`.
