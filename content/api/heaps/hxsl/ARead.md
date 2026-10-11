# hxsl.ARead

**enum** · package [`hxsl`](README.md) · module [`hxsl.Flatten`](Flatten.md) · source [`hxsl/Flatten.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxsl/Flatten.hx)

How a flattened variable is read: at a fixed position, or at an offset computed at runtime (array access).

## Constructors

### AIndex

```haxe
AIndex(a:hxsl._Flatten.Alloc)
```

At the position of the allocation.

### AOffset

```haxe
AOffset(a:hxsl._Flatten.Alloc, stride:Int, delta:TExpr)
```

At the position of the allocation plus `delta`, computed at runtime; `stride` is the size of an element, in `vec4`.
