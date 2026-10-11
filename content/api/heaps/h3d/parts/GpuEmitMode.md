# h3d.parts.GpuEmitMode

**enum** · package [`h3d.parts`](README.md) · module [`h3d.parts.GpuParticles`](GpuParticles.md) · source [`h3d/parts/GpuParticles.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/parts/GpuParticles.hx)

The shape the particles of a `GpuPartGroup` are emitted from.

## Constructors

### Point

```haxe
Point
```

A single Point, emit in all directions

### Cone

```haxe
Cone
```

A cone, parametrized with emitAngle and emitDistance

### VolumeBounds

```haxe
VolumeBounds
```

The GpuParticles specified volumeBounds

### ParentBounds

```haxe
ParentBounds
```

The GpuParticles parent.getBounds()

### CameraBounds

```haxe
CameraBounds
```

Same as VolumeBounds, but in Camera space, not world space.

### Disc

```haxe
Disc
```

A disc, emit in one direction
