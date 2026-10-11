# hide.comp.Shape

**enum** · package [`hide.comp`](README.md) · module [`hide.comp.ShapeEditor`](ShapeEditor.md) · source [`hide_js/hide/comp/ShapeEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/ShapeEditor.hx) · available on editor (js)

A collision shape edited by the `ShapeEditor`. The center and rotation are relative to the parent.

## Constructors

### Box

```haxe
Box(center:h3d.col.Point, rotation:h3d.Vector, sizeX:Float, sizeY:Float, sizeZ:Float)
```

A box.

### Sphere

```haxe
Sphere(center:h3d.col.Point, radius:Float)
```

A sphere.

### Capsule

```haxe
Capsule(center:h3d.col.Point, rotation:h3d.Vector, radius:Float, height:Float)
```

A capsule.

### Cylinder

```haxe
Cylinder(center:h3d.col.Point, rotation:h3d.Vector, radius:Float, height:Float)
```

A cylinder.
