# hxd.fmt.hmd.SkinSplit

**class** · package [`hxd.fmt.hmd`](README.md) · module [`hxd.fmt.hmd.Data`](Data.md) · source [`hxd/fmt/hmd/Data.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/fmt/hmd/Data.hx)

A part of a skin drawn separately, to limit the number of joints per draw call.

## Constructor

### new

```haxe
function new():Void
```

Creates a part.

## Variables

### materialIndex

```haxe
var materialIndex:Int
```

The material of the part.

### joints

```haxe
var joints:Array<Index<SkinJoint>>
```

The joints used by the part.
