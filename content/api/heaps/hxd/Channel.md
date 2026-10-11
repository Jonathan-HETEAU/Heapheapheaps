# hxd.Channel

**enum abstract** · package [`hxd`](README.md) · module [`hxd.Pixels`](Pixels.md) · source [`hxd/Pixels.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/Pixels.hx)

A color channel.

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `R` | `0` | The red channel. |
| `G` | `1` | The green channel. |
| `B` | `2` | The blue channel. |
| `A` | `3` | The alpha channel. |

## Static methods

### fromInt

```haxe
static inline function fromInt(v:Int):Channel
```

Returns the channel of the given index.

## Methods

### toInt

```haxe
inline function toInt():Int
```

Returns the index of the channel.
