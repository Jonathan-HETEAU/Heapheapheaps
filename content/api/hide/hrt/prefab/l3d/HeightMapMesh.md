# hrt.prefab.l3d.HeightMapMesh

**class** · package [`hrt.prefab.l3d`](README.md) · module [`hrt.prefab.l3d.HeightMap`](HeightMap.md) · source [`hrt/prefab/l3d/HeightMap.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/l3d/HeightMap.hx)

Extends: [`h3d.scene.Object`](../../../../heaps/h3d/scene/Object.md)

The object of a `HeightMap`: shows the tiles visible by the camera, created on demand.

## Constructor

### new

```haxe
function new(hmap:HeightMap, ?parent:h3d.scene.Object):Void
```

Creates the object.

## Methods

### onTileReady

```haxe
dynamic function onTileReady(t:HeightMapTile):Void
```

Called when a tile mesh is created.

### isAssetFiltered

```haxe
dynamic function isAssetFiltered(obj:h3d.scene.WorldModel, pos:h3d.Matrix):Bool
```

Tells if a world model should be filtered out. Returns `false` by default.

### initTile

```haxe
function initTile(t:HeightMapTile):Void
```

Creates the mesh of a tile.

### init

```haxe
function init():Void
```

Creates the grids from the height texture size and the quality.
