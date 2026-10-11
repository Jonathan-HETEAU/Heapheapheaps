# h3d.parts.GpuSortMode

**enum** · package [`h3d.parts`](README.md) · module [`h3d.parts.GpuParticles`](GpuParticles.md) · source [`h3d/parts/GpuParticles.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/parts/GpuParticles.hx)

How the particles of a `GpuPartGroup` are sorted.

## Constructors

### None

```haxe
None
```

Particles are not sorted.

### Dynamic

```haxe
Dynamic
```

Particles are sorted back-to-front every frame based on their current position.
