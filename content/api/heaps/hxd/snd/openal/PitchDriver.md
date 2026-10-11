# hxd.snd.openal.PitchDriver

**class** · package [`hxd.snd.openal`](README.md) · source [`hxd/snd/openal/PitchDriver.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/snd/openal/PitchDriver.hx) · available on hl/sdl, hl/directx

Extends: [`hxd.snd.EffectDriver`](../EffectDriver.md)

Implements [`hxd.snd.effect.Pitch`](../effect/Pitch.md) with the OpenAL source pitch.

## Constructor

### new

```haxe
function new():Void
```

## Methods

### apply

```haxe
override function apply(e:hxd.snd.effect.Pitch, source:SourceHandle):Void
```

### unbind

```haxe
override function unbind(e:hxd.snd.effect.Pitch, source:SourceHandle):Void
```

## Inherited members

- from [`hxd.snd.EffectDriver`](../EffectDriver.md): `acquire`, `release`, `update`, `bind`, `apply`, `unbind`
