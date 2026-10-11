# h3d.parts.GpuPart

**class** · package [`h3d.parts`](README.md) · module [`h3d.parts.GpuParticles`](GpuParticles.md) · source [`h3d/parts/GpuParticles.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/parts/GpuParticles.hx)

The initial state of a particle of a `GpuPartGroup`, computed on the CPU and uploaded once.
The particle is then animated on the GPU.

## Constructor

### new

```haxe
function new():Void
```

Creates a particle.

## Variables

### index

```haxe
var index:Int
```

The index of the particle.

### x

```haxe
var x:Float
```

The current X position (see `updatePos`).

### y

```haxe
var y:Float
```

The current Y position.

### z

```haxe
var z:Float
```

The current Z position.

### w

```haxe
var w:Float
```

The distance used for sorting.

### sx

```haxe
var sx:Float
```

The initial X position.

### sy

```haxe
var sy:Float
```

The initial Y position.

### sz

```haxe
var sz:Float
```

The initial Z position.

### vx

```haxe
var vx:Float
```

The X velocity.

### vy

```haxe
var vy:Float
```

The Y velocity.

### vz

```haxe
var vz:Float
```

The Z velocity.

### time

```haxe
var time:Float
```

The time offset of the particle in its life cycle.

### life

```haxe
var life:Float
```

The life duration of the particles, in seconds.

### initX

```haxe
var initX:Float
```

The initial X offset of the quad (size and rotation).

### initY

```haxe
var initY:Float
```

The initial Y offset of the quad.

### deltaX

```haxe
var deltaX:Float
```

The X variation of the quad offset over time (size increase and rotation).

### deltaY

```haxe
var deltaY:Float
```

The Y variation of the quad offset over time.

### next

```haxe
var next:GpuPart
```

The next particle of the list.

## Methods

### updatePos

```haxe
function updatePos(time:Float, gravity:Float):Void
```

Computes the CPU position at `time` (used for sorting and bounds).
