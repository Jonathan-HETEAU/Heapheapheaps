# hrt.prefab.l3d.LocalVolumetricLightingObject

**class** · package [`hrt.prefab.l3d`](README.md) · module [`hrt.prefab.l3d.LocalVolumetricLighting`](LocalVolumetricLighting.md) · source [`hrt/prefab/l3d/LocalVolumetricLighting.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/l3d/LocalVolumetricLighting.hx)

Extends: [`h3d.scene.Object`](../../../../heaps/h3d/scene/Object.md)

The object of a `LocalVolumetricLighting`: a unit cube rendered from inside or outside.

## Constructor

### new

```haxe
function new(parent:h3d.scene.Object, localVolume:LocalVolumetricLighting):Void
```

Creates the object.

## Variables

### localVolume

```haxe
var localVolume:LocalVolumetricLighting
```

The prefab.

### bounds

```haxe
var bounds:h3d.col.OrientedBounds
```

The bounds of the volume.

### meshInside

```haxe
var meshInside:h3d.scene.Mesh
```

The mesh rendered when the camera is inside.

### meshOutside

```haxe
var meshOutside:h3d.scene.Mesh
```

The mesh rendered when the camera is outside.

### boundsDisplay

```haxe
var boundsDisplay:h3d.scene.Graphics
```

The display of the bounds, or `null`.

### shader

```haxe
var shader:LocalVolumetricShader
```

The shader.

## Methods

### refresh

```haxe
function refresh():Void
```

Applies the properties of the prefab.
