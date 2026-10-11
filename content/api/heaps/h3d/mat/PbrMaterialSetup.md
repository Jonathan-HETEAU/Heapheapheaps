# h3d.mat.PbrMaterialSetup

**class** · package [`h3d.mat`](README.md) · source [`h3d/mat/PbrMaterialSetup.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/mat/PbrMaterialSetup.hx)

Extends: [`h3d.mat.MaterialSetup`](MaterialSetup.md)

The material setup of the physically based rendering: it creates `PbrMaterial` materials, the
[`h3d.scene.pbr.Renderer`](../scene/pbr/Renderer.md) renderer and the [`h3d.scene.pbr.LightSystem`](../scene/pbr/LightSystem.md).

Call `set()` before creating the scene (for instance in the `main` function, before creating the [`hxd.App`](../../hxd/App.md)).
On WebGL 1, the default renderer is used instead.

## Constructor

### new

```haxe
function new(?name:String = "PBR"):Void
```

Creates the setup. `name` is used to store the material properties (see `MaterialDatabase`).

## Static methods

### set

```haxe
static function set():Void
```

Sets a `PbrMaterialSetup` as `MaterialSetup.current`.

## Methods

### createRenderer

```haxe
override function createRenderer():h3d.scene.Renderer
```

### createLightSystem

```haxe
override function createLightSystem():h3d.scene.pbr.LightSystem
```

### createMaterial

```haxe
override function createMaterial():Material
```

### gloss

```haxe
function gloss():Bool
```

Tells that this setup uses glossiness. Always `true`.

## Inherited members

- from [`h3d.mat.MaterialSetup`](MaterialSetup.md): `name`, `displayName`, `createRenderer`, `createLightSystem`, `createMaterial`, `getDefaults`, `loadProps`, `loadMaterialProps`, `saveMaterialProps`, `customMeshInit`
