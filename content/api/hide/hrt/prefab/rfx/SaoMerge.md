# hrt.prefab.rfx.SaoMerge

**class** · package [`hrt.prefab.rfx`](README.md) · module [`hrt.prefab.rfx.Sao`](Sao.md) · source [`hrt/prefab/rfx/Sao.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/rfx/Sao.hx)

Extends: [`h3d.shader.ScreenShader`](../../../../heaps/h3d/shader/ScreenShader.md)

Combines the screen space occlusion with the material occlusion.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### blendMode

```haxe
var blendMode(get, set):Int
```

### screenOcclusion

```haxe
var screenOcclusion(get, set):hxsl.Texture
```

### materialOcclusionIntensity

```haxe
var materialOcclusionIntensity(get, set):Float
```

### materialOcclusion

```haxe
var materialOcclusion(get, set):hxsl.TextureChannel
```

### materialOcclusionChannel

```haxe
var materialOcclusionChannel(get, set):hxsl.Channel
```

## Methods

### updateConstants

```haxe
override function updateConstants(globals:hxsl.Globals):Void
```

### getParamValue

```haxe
override function getParamValue(index:Int):Dynamic
```

### getParamFloatValue

```haxe
override function getParamFloatValue(index:Int):Float
```

### writeParam

```haxe
override function writeParam(index:Int, type:hxsl.Type, out:hxsl.ShaderParamBuffer, pos:Int):Void
```

### clone

```haxe
override function clone():hxsl.Shader
```
