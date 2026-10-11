# steam.ServerMode

**enum abstract** · package [`steam`](README.md) · module [`steam.GameServer`](GameServer.md) · source [`steam/GameServer.hx`](https://github.com/Jonathan-HETEAU/hlsteam/blob/ccr-01f70725-tatboj/steam/GameServer.hx)

The authentication mode of a game server (Steamworks `EServerMode`).

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `NoAuthentification` | `1` | No authentication of the users. |
| `Authentification` | `2` | The users are authenticated by Steam. |
| `AuthentificationAndSecure` | `3` | The users are authenticated, and the server is VAC secured. |
