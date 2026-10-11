# hrt.shgraph.ShaderGraphGenContext

**class** · package [`hrt.shgraph`](README.md) · module [`hrt.shgraph.ShaderGraph`](ShaderGraph.md) · source [`hrt/shgraph/ShaderGraph.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/shgraph/ShaderGraph.hx)

Generates the HXSL expression of a graph, by sorting and generating its nodes.

## Constructor

### new

```haxe
function new(graph:Graph, ?includePreviews:Bool = false):Void
```

Creates the context. `includePreviews` adds the preview outputs of the nodes.

## Methods

### initNodes

```haxe
function initNodes():Void
```

Initializes the node data.

### generate

```haxe
function generate(?genContext:NodeGenContext):hxsl.TExpr
```

Returns the expression of the graph.
