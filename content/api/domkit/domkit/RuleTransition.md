# domkit.RuleTransition

**class** · package [`domkit`](README.md) · module [`domkit.CssStyle`](CssStyle.md) · source [`domkit/CssStyle.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/CssStyle.hx)

A transition set by a `Rule`.

## Constructor

### new

```haxe
function new(p:Property, time:Float, curve:Curve):Void
```

Creates the transition.

## Variables

### p

```haxe
var p:Property
```

The property.

### time

```haxe
var time:Float
```

The duration, in seconds.

### curve

```haxe
var curve:Curve
```

The easing curve.

### next

```haxe
var next:RuleTransition
```

The next transition applied to the object (temporary list).
