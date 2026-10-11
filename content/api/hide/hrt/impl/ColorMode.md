# hrt.impl.ColorMode

**typedef** · package [`hrt.impl`](README.md) · module [`hrt.impl.ColorSpace`](ColorSpace.md) · source [`hrt/impl/ColorSpace.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/impl/ColorSpace.hx)

A color space, with its conversions.

## Fields

### valueToARGB

```haxe
var valueToARGB:(value:h3d.Vector4, outColor:Color) -> Color
```

Converts a value of the color space to a color.

### name

```haxe
var name:String
```

The name.

### ARGBToValue

```haxe
var ARGBToValue:(color:Color, outVector:h3d.Vector4) -> h3d.Vector4
```

Converts a color to a value of the color space.
