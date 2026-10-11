# hxd.tools.ConvexHull

**class** · package [`hxd.tools`](README.md) · module [`hxd.tools.VHACD`](VHACD.md) · source [`hxd/tools/VHACD.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/tools/VHACD.hx) · available on hl/sdl, hl/directx

A convex hull computed by V-HACD.

## Constructor

### new

```haxe
function new():Void
```

Creates an empty hull.

## Variables

### points

```haxe
var points:hl.Bytes
```

The points (3 doubles each).

### triangles

```haxe
var triangles:hl.Bytes
```

The triangle indexes (3 ints each).

### pointCount

```haxe
var pointCount:Int
```

The number of points.

### triangleCount

```haxe
var triangleCount:Int
```

The number of triangles.

### volume

```haxe
var volume:Float
```

The volume of the hull.

### centerX

```haxe
var centerX:Float
```

The X coordinate of the center of the hull.

### centerY

```haxe
var centerY:Float
```

The Y coordinate of the center of the hull.

### centerZ

```haxe
var centerZ:Float
```

The Z coordinate of the center of the hull.

### meshId

```haxe
var meshId:Int
```

The identifier of the hull.

### boundsMinX

```haxe
var boundsMinX:Float
```

The minimum X of the bounds.

### boundsMinY

```haxe
var boundsMinY:Float
```

The minimum Y of the bounds.

### boundsMinZ

```haxe
var boundsMinZ:Float
```

The minimum Z of the bounds.

### boundsMaxX

```haxe
var boundsMaxX:Float
```

The maximum X of the bounds.

### boundsMaxY

```haxe
var boundsMaxY:Float
```

The maximum Y of the bounds.

### boundsMaxZ

```haxe
var boundsMaxZ:Float
```

The maximum Z of the bounds.
