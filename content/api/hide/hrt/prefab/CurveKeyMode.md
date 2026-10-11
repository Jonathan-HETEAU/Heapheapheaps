# hrt.prefab.CurveKeyMode

**enum abstract** · package [`hrt.prefab`](README.md) · module [`hrt.prefab.Curve`](Curve.md) · source [`hrt/prefab/Curve.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/Curve.hx)

How a curve is interpolated around a key.

Underlying type: `Int`

## Values

| Name | Value | Description |
|---|---|---|
| `Aligned` | `0` | Bezier interpolation, with aligned handles. |
| `Free` | `1` | Bezier interpolation, with independent handles. |
| `Linear` | `2` | Linear interpolation. |
| `Constant` | `3` | The value of the key until the next key. |
