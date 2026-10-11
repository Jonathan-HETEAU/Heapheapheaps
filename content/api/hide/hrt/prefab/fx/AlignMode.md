# hrt.prefab.fx.AlignMode

**enum** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.Emitter`](Emitter.md) · source [`hrt/prefab/fx/Emitter.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/Emitter.hx)

How the particles are oriented.

## Constructors

### None

```haxe
None
```

Not sorted.

### Screen

```haxe
Screen
```

Facing the screen.

### Axis

```haxe
Axis
```

Facing the screen, rotating around the locked axis (`alignLockAxis`).

### Speed

```haxe
Speed
```

Along their speed.

### ScreenSpeed

```haxe
ScreenSpeed
```

Facing the screen, oriented along their speed projected on the screen.

### AxisSpeed

```haxe
AxisSpeed
```

Along their speed, rotating around it to face the screen.
