# hxsl.BatchInstanceParams

**class** · package [`hxsl`](README.md) · module [`hxsl.Cache`](Cache.md) · source [`hxsl/Cache.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxsl/Cache.hx)

The parameters forced to be stored per instance in a batch shader, by shader name.

## Constructor

### new

```haxe
function new(forcedPerInstance:Array<{ shader:String, params:Array<String> }>):Void
```

Creates the parameters.

## Methods

### getSignature

```haxe
function getSignature():String
```

Returns a string identifying the parameters.
