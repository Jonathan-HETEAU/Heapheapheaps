# hrt.prefab.fx.SwarmObject

**class** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.Swarm`](Swarm.md) · source [`hrt/prefab/fx/Swarm.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/Swarm.hx)

Extends: [`h3d.scene.Object`](../../../../heaps/h3d/scene/Object.md)

The object of a `Swarm`: simulates the objects at 15 steps per second and renders them (with a [`h3d.scene.MeshBatch`](../../../../heaps/h3d/scene/MeshBatch.md)).

## Constructor

### new

```haxe
function new(?parent:h3d.scene.Object, prefab:Swarm):Void
```

Creates the object.

## Variables

### prefab

```haxe
var prefab:Swarm
```

The prefab.

### elements

```haxe
var elements:Array<SwarmElement>
```

The objects of the swarm.

### lastPos

```haxe
var lastPos:h3d.Vector
```

The position of the swarm at the previous step.

### facingAngle

```haxe
var facingAngle:Float
```

The current facing angle, in radians (`autoTrackRotation`).

### targetAngle

```haxe
var targetAngle:Float
```

The facing angle toward the movement, in radians (`autoTrackRotation`).

### batch

```haxe
var batch:h3d.scene.MeshBatch
```

The mesh batch rendering the objects.

### swarmElementTemplate

```haxe
var swarmElementTemplate:hrt.prefab.Object3D
```

The prefab of the object mesh (a small box if `null`).

### customAnims

```haxe
var customAnims:Array<CustomAnimation>
```

The shader animations.

### shader

```haxe
var shader:PerObjectRandom
```

The shader giving the random value per object.

### debugViz _(editor (js) only)_

```haxe
var debugViz:h3d.scene.Graphics
```

The display of the targets (editor only).

## Methods

### init

```haxe
function init():Void
```

Creates the mesh batch from the template, with the materials and shaders of the prefab.
