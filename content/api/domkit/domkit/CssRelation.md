# domkit.CssRelation

**enum abstract** · package [`domkit`](README.md) · module [`domkit.CssParser`](CssParser.md) · source [`domkit/CssParser.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/CssParser.hx)

The relation between a selector and its parent selector.

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `None` | `0` | A descendant (`a b`). |
| `ImmediateChildren` | `1` | A direct child (`a > b`). |
| `SubRule` | `2` | The same object, in a nested rule (`&.b`). |
