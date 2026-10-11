# hrt.shader.WireframeOverlayShader

**class** · package [`hrt.shader`](README.md) · module [`hrt.shader.WireframeOverlay`](WireframeOverlay.md) · source [`hrt/shader/WireframeOverlay.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/shader/WireframeOverlay.hx)

Extends: [`hxsl.Shader`](../../../heaps/hxsl/Shader.md)

Draws the mesh slightly inflated, in a flat color.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### color

```haxe
var color(get, set):hxsl.Vec
```

### alpha

```haxe
var alpha(get, set):Float
```

### thickness

```haxe
var thickness(get, set):Float
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
