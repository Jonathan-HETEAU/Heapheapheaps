# hrt.prefab.l3d.MeshSprayObject

**class** · package [`hrt.prefab.l3d`](README.md) · module [`hrt.prefab.l3d.MeshSpray`](MeshSpray.md) · source [`hrt/prefab/l3d/MeshSpray.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/l3d/MeshSpray.hx)

Extends: [`hrt.prefab.l3d.SprayObject`](SprayObject.md) → [`h3d.scene.Object`](../../../../heaps/h3d/scene/Object.md)

The object of a `MeshSpray`: renders the meshes with mesh batches.

## Constructor

### new

```haxe
function new(spray:Spray, ?parent:h3d.scene.Object):Void
```

## Variables

### batches

```haxe
var batches:Array<h3d.scene.MeshBatch>
```

The mesh batches.

### batchesMap

```haxe
var batchesMap:Map<Int, Map<String, BatchData>>
```

The batches by cell (see `split`) and model path.

### editChildren _(editor (js) only)_

```haxe
var editChildren:Bool
```

Shows the children as objects, to edit them (editor only).

## Methods

### getMaterials _(editor (js) only)_

```haxe
override function getMaterials(?arr:Array<h3d.mat.Material>, ?recursive:Bool = true):Null<Array<h3d.mat.Material>>
```

### redraw _(editor (js) only)_

```haxe
override function redraw(?updateShaders:Bool = false):Void
```

## Inherited members

- from [`hrt.prefab.l3d.SprayObject`](SprayObject.md): `redraw`
