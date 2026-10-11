# hrt.prefab.LightShadows

**typedef** · package [`hrt.prefab`](README.md) · module [`hrt.prefab.Light`](Light.md) · source [`hrt/prefab/Light.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/Light.hx)

The shadows of a light.

## Fields

### size

```haxe
var size:Int
```

The size of the shadow map, in pixels.

### samplingMode

```haxe
var samplingMode:ShadowSamplingMode
```

How the shadow map is sampled.

### radius

```haxe
var radius:Float
```

The blur radius.

### quality

```haxe
var quality:Float
```

The blur quality.

### mode

```haxe
var mode:h3d.pass.RenderMode
```

The rendering mode: none, dynamic, static (baked) or mixed.

### bias

```haxe
var bias:Float
```

The depth bias.
