# hrt.prefab.fx.CustomAnimation

**class** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.BaseFX`](BaseFX.md) · source [`hrt/prefab/fx/BaseFX.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/BaseFX.hx)

Extends: [`hrt.prefab.fx.Evaluator`](Evaluator.md)

Subclasses: [`hrt.prefab.fx.RendererFXAnimation`](RendererFXAnimation.md), [`hrt.prefab.fx.ScreenShaderGraphFXAnimation`](ScreenShaderGraphFXAnimation.md), [`hrt.prefab.fx.ShaderAnimation`](ShaderAnimation.md)

Animates custom properties with curves in an FX.

## Constructor

### new

```haxe
function new(?randValues:Array<Float>, ?stride:Int):Void
```

## Variables

### finishSync

```haxe
var finishSync:Bool
```

This animation will need to keep being updated if setTime was called once

### startedPlaying

```haxe
var startedPlaying:Bool
```

Tells if `setTime` was called since the last reset.

## Methods

### setTime

```haxe
function setTime(time:Float):Void
```

Applies the values at `time`. Must be overridden.

## Inherited members

- from [`hrt.prefab.fx.Evaluator`](Evaluator.md): `parameters`, `setAllParameters`, `getFast`, `getFloat`, `getSum`, `getVector`, `getFastVec`, `getVector2`
