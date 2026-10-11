# hrt.prefab.fx.Particle2DInstance

**class** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.Emitter2D`](Emitter2D.md) · source [`hrt/prefab/fx/Emitter2D.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/Emitter2D.hx)

Extends: [`h2d.BatchElement`](../../../../heaps/h2d/BatchElement.md)

A particle of an `Emitter2DObject`.

## Constructor

### new

```haxe
function new(t:h2d.Tile, e:Emitter2DObject):Void
```

Creates a particle of the emitter `e`.

## Variables

### emitter

```haxe
var emitter:Emitter2DObject
```

The emitter.

### idx

```haxe
var idx:Int
```

The index of the particle, for its random values.

### lifeTime

```haxe
var lifeTime:Float
```

The lifetime, in seconds.

### curLifeTime

```haxe
var curLifeTime:Float
```

The age, in seconds.

## Methods

### remove

```haxe
override function remove():Void
```
