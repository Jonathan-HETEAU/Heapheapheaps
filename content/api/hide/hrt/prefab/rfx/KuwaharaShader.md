# hrt.prefab.rfx.KuwaharaShader

**class** · package [`hrt.prefab.rfx`](README.md) · module [`hrt.prefab.rfx.KuwaharaFilter`](KuwaharaFilter.md) · source [`hrt/prefab/rfx/KuwaharaFilter.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/rfx/KuwaharaFilter.hx)

Extends: [`hrt.shader.PbrShader`](../../shader/PbrShader.md) → [`h3d.shader.ScreenShader`](../../../../heaps/h3d/shader/ScreenShader.md)

Applies a Kuwahara filter (painting effect), depending on the distance.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### startDist

```haxe
var startDist(get, set):Float
```

### endDist

```haxe
var endDist(get, set):Float
```

### startOpacity

```haxe
var startOpacity(get, set):Float
```

### endOpacity

```haxe
var endOpacity(get, set):Float
```

### scaledRadius

```haxe
var scaledRadius(get, set):Int
```

### texture

```haxe
var texture(get, set):hxsl.Texture
```

### FETCH_OPTIM_2x2

```haxe
var FETCH_OPTIM_2x2(get, set):Bool
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

## Inherited members

- from [`hrt.shader.PbrShader`](../../shader/PbrShader.md): `updateConstants`, `getParamValue`, `getParamFloatValue`, `writeParam`, `clone`
