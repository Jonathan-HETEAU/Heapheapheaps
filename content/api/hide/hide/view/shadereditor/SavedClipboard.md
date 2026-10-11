# hide.view.shadereditor.SavedClipboard

**typedef** · package [`hide.view.shadereditor`](README.md) · module [`hide.view.shadereditor.ShaderEditor`](ShaderEditor.md) · source [`hide_js/hide/view/shadereditor/ShaderEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/view/shadereditor/ShaderEditor.hx) · available on editor (js)

The nodes and edges copied to the clipboard.

## Fields

### nodes

```haxe
var nodes:Array<{ props:Dynamic, pos:h2d.col.Point, nodeType:Class<hrt.shgraph.ShaderNode> }>
```

The copied nodes.

### edges

```haxe
var edges:Array<{ toInputId:Int, toIdx:Int, fromOutputId:Int, fromIdx:Int }>
```

The edges between the copied nodes, by index in `nodes`.
