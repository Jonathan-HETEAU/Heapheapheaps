# hrt.impl.RemotePrefabActionKind

**enum abstract** · package [`hrt.impl`](README.md) · module [`hrt.impl.RemoteConsole`](RemoteConsole.md) · source [`hrt/impl/RemoteConsole.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/impl/RemoteConsole.hx)

The kind of a remote prefab message.

Underlying type: `String`

## Values

| Name | Value | Description |
|---|---|---|
| `Open` | `"Open"` | Game -> Hide: requests to open the prefab data contained in `data`. |
| `Update` | `"Update"` | Hide -> Game: updates the prefab opened in the game with the new `data`. |
