# hrt.prefab.rfx.SharpenShader

**class** · package [`hrt.prefab.rfx`](README.md) · module [`hrt.prefab.rfx.Sharpen`](Sharpen.md) · source [`hrt/prefab/rfx/Sharpen.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/rfx/Sharpen.hx)

Extends: [`h3d.shader.ScreenShader`](../../../../heaps/h3d/shader/ScreenShader.md)

Sharpens the screen.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### source

```haxe
var source(get, set):hxsl.Texture
```

### intensity

```haxe
var intensity(get, set):Float
```

### resolution

```haxe
var resolution(get, set):hxsl.Vec
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
