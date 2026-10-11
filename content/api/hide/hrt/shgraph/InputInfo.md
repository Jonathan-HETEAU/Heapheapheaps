# hrt.shgraph.InputInfo

**typedef** · package [`hrt.shgraph`](README.md) · module [`hrt.shgraph.ShaderNode`](ShaderNode.md) · source [`hrt/shgraph/ShaderNode.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/shgraph/ShaderNode.hx)

An input of a node.

## Fields

### type

```haxe
var type:SgType
```

The type.

### name

```haxe
var name:String
```

The name.

### inlineEditable

```haxe
var ?inlineEditable:Null<Bool>
```

Tells if the default value can be edited on the node.

### def

```haxe
var def:ShaderDefInput
```

The default value when not connected.
