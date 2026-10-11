# hrt.prefab.l3d.CameraSyncObject

**class** · package [`hrt.prefab.l3d`](README.md) · module [`hrt.prefab.l3d.Camera`](Camera.md) · source [`hrt/prefab/l3d/Camera.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/l3d/Camera.hx)

Extends: [`h3d.scene.Object`](../../../../heaps/h3d/scene/Object.md)

The object of a `Camera`: applies its field of view and planes to the scene camera when enabled.

## Constructor

### new

```haxe
function new(?parent:h3d.scene.Object):Void
```

## Variables

### enable

```haxe
var enable:Bool
```

Applies the properties to the scene camera at each sync.

### fovY

```haxe
var fovY:Float
```

The vertical field of view, in degrees.

### zFar

```haxe
var zFar:Float
```

The far plane.

### zNear

```haxe
var zNear:Float
```

The near plane.
