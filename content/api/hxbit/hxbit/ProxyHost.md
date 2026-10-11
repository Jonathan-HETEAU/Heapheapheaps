# hxbit.ProxyHost

**interface** · package [`hxbit`](README.md) · module [`hxbit.NetworkSerializable`](NetworkSerializable.md) · source [`hxbit/NetworkSerializable.hx`](https://github.com/Jonathan-HETEAU/hxbit/blob/ccr-01f70725-tatboj/hxbit/NetworkSerializable.hx)

Subclasses: [`hxbit.NetworkSerializable`](NetworkSerializable.md)

Implemented by: [`hxbit.BaseProxy`](BaseProxy.md)

An object notified when a value it contains is modified: a `NetworkSerializable`, or a proxy containing other proxies.

## Methods

### networkSetBitCond

```haxe
function networkSetBitCond(bit:Int):Void
```

Marks the property `bit` as changed, if its send conditions (`@:increment`, `@:condSend`) allow it.
