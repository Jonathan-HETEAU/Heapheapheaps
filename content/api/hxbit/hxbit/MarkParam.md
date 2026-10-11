# hxbit.MarkParam

**abstract** · package [`hxbit`](README.md) · module [`hxbit.Serializable`](Serializable.md) · source [`hxbit/Serializable.hx`](https://github.com/Jonathan-HETEAU/hxbit/blob/ccr-01f70725-tatboj/hxbit/Serializable.hx)

The visibility groups of the objects, by UID, used when marking the references visible from a client (`null` for all the references).

Underlying type: [`hxbit.UIDMap`](UIDMap.md)

Implicit casts from: `UIDMap<Int>`

## Methods

### get

```haxe
inline function get(v:NetworkSerializable):Null<Int>
```

Returns the visibility groups of the object (`-1` for all groups).
