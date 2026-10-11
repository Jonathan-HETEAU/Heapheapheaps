# hrt.prefab.fx.Desaturate

**class** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.FX`](FX.md) · source [`hrt/prefab/fx/FX.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/FX.hx)

Extends: [`h3d.shader.ScreenShader`](../../../../heaps/h3d/shader/ScreenShader.md)

Desaturates the screen.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### texture

```haxe
var texture(get, set):hxsl.Texture
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
