# domkit.Curve

**class** · package [`domkit`](README.md) · module [`domkit.CssParser`](CssParser.md) · source [`domkit/CssParser.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/CssParser.hx)

Subclasses: [`domkit.BezierCurve`](BezierCurve.md)

An easing curve: linear.

## Constructor

### new

```haxe
function new():Void
```

Creates the curve.

## Methods

### interpolate

```haxe
function interpolate(v:Float):Float
```

Returns the progress of the value at the time `v` (from `0` to `1`).
