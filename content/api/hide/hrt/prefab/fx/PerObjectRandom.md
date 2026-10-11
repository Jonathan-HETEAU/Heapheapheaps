# hrt.prefab.fx.PerObjectRandom

**class** · package [`hrt.prefab.fx`](README.md) · module [`hrt.prefab.fx.Swarm`](Swarm.md) · source [`hrt/prefab/fx/Swarm.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/fx/Swarm.hx)

Extends: [`hxsl.Shader`](../../../../heaps/hxsl/Shader.md)

Gives a random value per object of a `Swarm`.

## Constructor

### new

```haxe
function new():Void
```

## Variables

### randomParam

```haxe
var randomParam(get, set):Float
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
