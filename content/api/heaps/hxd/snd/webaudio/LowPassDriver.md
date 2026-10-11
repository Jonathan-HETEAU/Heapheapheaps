# hxd.snd.webaudio.LowPassDriver

**class** · package [`hxd.snd.webaudio`](README.md) · source [`hxd/snd/webaudio/LowPassDriver.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/snd/webaudio/LowPassDriver.hx) · available on js

Extends: [`hxd.snd.EffectDriver`](../EffectDriver.md)

Implements [`hxd.snd.effect.LowPass`](../effect/LowPass.md) with a Web Audio biquad filter.

## Constructor

### new

```haxe
function new():Void
```

Creates the effect driver.

## Methods

### bind

```haxe
override function bind(e:hxd.snd.effect.LowPass, source:SourceHandle):Void
```

### apply

```haxe
override function apply(e:hxd.snd.effect.LowPass, source:SourceHandle):Void
```

### unbind

```haxe
override function unbind(e:hxd.snd.effect.LowPass, source:SourceHandle):Void
```

## Inherited members

- from [`hxd.snd.EffectDriver`](../EffectDriver.md): `acquire`, `release`, `update`, `bind`, `apply`, `unbind`
