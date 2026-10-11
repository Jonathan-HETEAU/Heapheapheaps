# hxd.fs.AsyncReadState

**enum abstract** · package [`hxd.fs`](README.md) · module [`hxd.fs.AsyncRead`](AsyncRead.md) · source [`hxd/fs/AsyncRead.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/fs/AsyncRead.hx)

The state of an `AsyncRead`.

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `Pending` | `0` | Waiting to be read. |
| `Reading` | `1` | Being read. |
| `Done` | `2` | Read, and the callback was called. |
| `Cancelled` | `3` | Cancelled with `AsyncRead.cancel`. |
