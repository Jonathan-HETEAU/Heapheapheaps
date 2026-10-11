# hxbit.MarkInfo

**abstract** · package [`hxbit`](README.md) · module [`hxbit.Serializable`](Serializable.md) · source [`hxbit/Serializable.hx`](https://github.com/Jonathan-HETEAU/hxbit/blob/ccr-01f70725-tatboj/hxbit/Serializable.hx)

The marking parameters of `AnySerializable.markReferences`: `set` is the bits set on the marked objects (`__mark`), `mask` the bits kept.

Underlying type: `Int`

## Static variables

### set

```haxe
static var set(get, null):Int
```

The bits set on the marked objects.

### mask

```haxe
static var mask(get, null):Int
```

The bits of `__mark` kept when marking an object.
