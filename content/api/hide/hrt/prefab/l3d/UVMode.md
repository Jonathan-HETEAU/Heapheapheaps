# hrt.prefab.l3d.UVMode

**enum** · package [`hrt.prefab.l3d`](README.md) · module [`hrt.prefab.l3d.Trails`](Trails.md) · source [`hrt/prefab/l3d/Trails.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/l3d/Trails.hx)

How the texture coordinate U goes along the trails.

## Constructors

### EStretch

```haxe
EStretch
```

Stretched between the head (`u = 0`) and the tail (`u = 1`).

### ETileFixed

```haxe
ETileFixed
```

Tiled along the trail, the texture staying fixed in world space.

### ETileFollow

```haxe
ETileFollow
```

Tiled along the trail, the texture following the head (`u = 0` at the head).

### ELifetime

```haxe
ELifetime
```

The life of the point.
