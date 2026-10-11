# hrt.prefab.rfx.DistortionTonemap

**class** · package [`hrt.prefab.rfx`](README.md) · module [`hrt.prefab.rfx.Distortion`](Distortion.md) · source [`hrt/prefab/rfx/Distortion.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/rfx/Distortion.hx)

Extends: [`hxsl.Shader`](../../../../heaps/hxsl/Shader.md)

Offsets the texture coordinates of the tonemapping by the distortion map.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### distortionMap

```haxe
var distortionMap(get, set):hxsl.Texture
```

### amount

```haxe
var amount(get, set):Float
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

### setParamIndexValue

```haxe
override function setParamIndexValue(index:Int, val:Dynamic):Void
```

### setParamIndexFloatValue

```haxe
override function setParamIndexFloatValue(index:Int, val:Float):Void
```

### writeParam

```haxe
override function writeParam(index:Int, type:hxsl.Type, out:hxsl.ShaderParamBuffer, pos:Int):Void
```

### clone

```haxe
override function clone():hxsl.Shader
```
