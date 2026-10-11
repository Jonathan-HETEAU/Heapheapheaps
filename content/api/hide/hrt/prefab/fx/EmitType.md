# hrt.prefab.fx.EmitType

**enum** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.Emitter`](Emitter.md) · source [`hrt/prefab/fx/Emitter.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/Emitter.hx)

When the particles are emitted.

## Constructors

### Infinity

```haxe
Infinity
```

Continuously, at `emitRate` particles per second.

### InfinityRandom

```haxe
InfinityRandom
```

Continuously, at a rate changing randomly between `emitRateMin` and `emitRateMax` every `emitRateChangeDelay` seconds.

### Duration

```haxe
Duration
```

At `emitRate` particles per second during `emitDuration` seconds.

### Burst

```haxe
Burst
```

`burstCount` bursts of `burstParticleCount` particles, every `burstDelay` seconds.

### BurstDuration

```haxe
BurstDuration
```

Bursts of `burstParticleCount` particles every `burstDelay` seconds, during `emitDuration` seconds.
