# hide.comp.RenderPropsPopup

**class** · package [`hide.comp`](README.md) · module [`hide.comp.SceneEditor`](SceneEditor.md) · source [`hide_js/hide/comp/SceneEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/SceneEditor.hx) · available on editor (js)

Extends: [`hide.comp.Popup`](Popup.md) → [`hide.comp.Component`](Component.md)

The popup choosing the render props of the scene.

## Constructor

### new

```haxe
function new(?parent:Null<hide.Element>, view:hide.view.FileView, editor:SceneEditor, ?isSearchable:Bool = false, ?canChangeCurrRp:Bool = false):Void
```

Creates the popup.

## Methods

### onSearchChanged

```haxe
override function onSearchChanged(searchBar:hide.Element):Void
```

## Inherited members

- from [`hide.comp.Popup`](Popup.md): `anchor`, `offsetX`, `offsetY`, `position`, `wasCancelled`, `open`, `onScroll`, `onSearchChanged`, `close`, `onClose`, `canCloseOnClickOutside`, `onShouldCloseOnClick`
- from [`hide.comp.Component`](Component.md): `componentName`, `element`, `saveDisplayKey`, `remove`
