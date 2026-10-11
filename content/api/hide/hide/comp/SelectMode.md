# hide.comp.SelectMode

**enum** · package [`hide.comp`](README.md) · module [`hide.comp.SceneEditor`](SceneEditor.md) · source [`hide_js/hide/comp/SceneEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/SceneEditor.hx) · available on editor (js)

How a selection updates the tree and the undo history.

## Constructors

### Default

```haxe
Default
```

Update tree, add undo command

### NoHistory

```haxe
NoHistory
```

Update tree only

### NoTree

```haxe
NoTree
```

Add undo but don't update tree

### Nothing

```haxe
Nothing
```

Don't refresh tree and don't undo command
