# hrt.prefab.l3d.SplineUV

**class** · package [`hrt.prefab.l3d`](README.md) · module [`hrt.prefab.l3d.SplineMesh`](SplineMesh.md) · source [`hrt/prefab/l3d/SplineMesh.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/l3d/SplineMesh.hx)

Extends: [`hxsl.Shader`](../../../../heaps/hxsl/Shader.md)

Uses the texture coordinates of the spline mesh.

## Constructor

### new

```haxe
function new():Void
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
