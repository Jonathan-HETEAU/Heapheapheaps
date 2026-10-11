# hide.comp.HideSceneEditorAPI

**class** · package [`hide.comp`](README.md) · module [`hide.comp.SceneEditor`](SceneEditor.md) · source [`hide_js/hide/comp/SceneEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/SceneEditor.hx) · available on editor (js)

Implements: [`hrt.prefab.SceneEditorAPI`](../../hrt/prefab/SceneEditorAPI.md)

The [`hrt.prefab.SceneEditorAPI`](../../hrt/prefab/SceneEditorAPI.md) of a `SceneEditor`.

## Constructor

### new

```haxe
function new(parent:SceneEditor):Void
```

Creates the API.

## Methods

### getRootPrefab

```haxe
function getRootPrefab():hrt.prefab.Prefab
```

Returns the edited prefab.

### selectPrefabs

```haxe
function selectPrefabs(prefabs:Array<hrt.prefab.Prefab>):Void
```

Selects prefabs.

### focusObjects

```haxe
function focusObjects(objects:Array<h3d.scene.Object>):Void
```

Moves the camera to show the objects.
