# domkit.BytesMap

**abstract** · package [`domkit`](README.md) · module [`domkit.CssStyle`](CssStyle.md) · source [`domkit/CssStyle.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/CssStyle.hx) · available on hl

Type parameters: `<T>`

A map with bytes keys, used by the style cache on HashLink.

Underlying type: `Map<Int, BytesCell<domkit.BytesMap.T>>`

## Methods

### get

```haxe
inline function get(bytes:hl.Bytes, len:Int):Null<domkit.BytesMap.T>
```

Returns the value of the first `len` bytes, or `null`.

### set

```haxe
inline function set(bytes:hl.Bytes, len:Int, value:domkit.BytesMap.T):Void
```

Sets the value of the first `len` bytes.
