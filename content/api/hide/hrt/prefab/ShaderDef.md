# hrt.prefab.ShaderDef

**typedef** · package [`hrt.prefab`](README.md) · module [`hrt.prefab.Cache`](Cache.md) · source [`hrt/prefab/Cache.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hrt/prefab/Cache.hx)

A shader loaded by `ContextShared.loadShader`, with the initial values of its parameters.

## Fields

### shader

```haxe
var shader:hxsl.SharedShader
```

The shader.

### inits

```haxe
var inits:Array<{ variable:hxsl.TVar, value:Dynamic }>
```

The initial values of the parameters.
