# steam.LobbyKind

**enum abstract** · package [`steam`](README.md) · module [`steam.Matchmaking`](Matchmaking.md) · source [`steam/Matchmaking.hx`](https://github.com/Jonathan-HETEAU/hlsteam/blob/ccr-01f70725-tatboj/steam/Matchmaking.hx)

The visibility of a lobby (Steamworks `ELobbyType`).

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `Private` | `0` | Only way to join the lobby is to invite to someone else |
| `FriendsOnly` | `1` | Shows for friends or invitees, but not in lobby list |
| `Public` | `2` | Visible for friends and in lobby list |
| `Invisible` | `3` | Returned by search, but not visible to other friends |
