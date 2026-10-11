# h3d.mat.PbrCullingMode

**enum abstract** · package [`h3d.mat`](README.md) · module [`h3d.mat.PbrMaterial`](PbrMaterial.md) · source [`h3d/mat/PbrMaterial.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/mat/PbrMaterial.hx)

The face culling of a `PbrMaterial` (see `h3d.mat.Data.Face`).

Underlying type: `String`

## Values

| Name | Value | Description |
|---|---|---|
| `None` | `"None"` | No culling: both faces are drawn. |
| `Back` | `"Back"` | Back faces are culled. |
| `Front` | `"Front"` | Front faces are culled. |
| `Both` | `"Both"` | Both faces are culled: nothing is drawn. |
