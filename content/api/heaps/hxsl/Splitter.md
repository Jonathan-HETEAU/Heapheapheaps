# hxsl.Splitter

**class** · package [`hxsl`](README.md) · source [`hxsl/Splitter.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxsl/Splitter.hx)

Splits a linked shader into its stages (vertex and fragment, or compute), with the variables each one uses.

## Constructor

### new

```haxe
function new():Void
```

Creates the pass.

## Methods

### split

```haxe
function split(s:ShaderData, isBatchShader:Bool):Array<ShaderData>
```

Returns the stages of the shader.
