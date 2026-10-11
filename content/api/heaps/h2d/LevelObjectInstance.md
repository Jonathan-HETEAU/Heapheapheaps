# h2d.LevelObjectInstance

**class** · package [`h2d`](README.md) · module [`h2d.CdbLevel`](CdbLevel.md) · source [`h2d/CdbLevel.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h2d/CdbLevel.hx)

[CastleDB](http://castledb.org) integration; A part of `CdbLevel` decoder.

## Constructor

### new

```haxe
function new():Void
```

Creates an instance.

## Variables

### x

```haxe
var x:Int
```

The X position of the object in the level, in pixels.

### y

```haxe
var y:Int
```

The Y position of the object in the level, in pixels.

### rot

```haxe
var rot:Int
```

The rotation of the object, in quarter turns.

### flip

```haxe
var flip:Bool
```

Tells if the object is flipped horizontally.

### obj

```haxe
var obj:LevelObject
```

The object of the tileset.
