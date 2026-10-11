# h3d.shader.BufferKind

**enum abstract** · package [`h3d.shader`](README.md) · module [`h3d.shader.Buffers`](Buffers.md) · source [`h3d/shader/Buffers.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/shader/Buffers.hx)

The kinds of shader data uploaded to the GPU.

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `Globals` | `0` | The global values (camera, time...), uploaded once per shader. |
| `Params` | `1` | The parameters of the shaders of an object. |
| `Textures` | `2` | The textures of the shaders of an object. |
| `Buffers` | `3` | The buffers of the shaders of an object. |
