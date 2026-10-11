# hxd.BufferMapping

**abstract** · package [`hxd`](README.md) · module [`hxd.BufferFormat`](BufferFormat.md) · source [`hxd/BufferFormat.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/BufferFormat.hx)

The location of a shader input in the buffers of a mesh: the index of the buffer, the byte offset in a vertex, and the precision.

Underlying type: `Int`

## Static variables

### bufferIndex

```haxe
static var bufferIndex(get, null):Int
```

The index of the buffer containing the input.

### offset

```haxe
static var offset(get, null):Int
```

The offset of the input in a vertex, in bytes.

### precision

```haxe
static var precision(get, null):Precision
```

The storage precision of the input.
