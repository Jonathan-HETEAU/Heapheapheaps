# hxd.fs.ConvertCommand

**typedef** · package [`hxd.fs`](README.md) · module [`hxd.fs.FileConverter`](FileConverter.md) · source [`hxd/fs/FileConverter.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/fs/FileConverter.hx) · available on hl/sdl, hl/directx

The conversions of a rule, with their parameters, and the next command applied to the result.

## Fields

### then

```haxe
var ?then:Null<ConvertCommand>
```

A conversion to run on the result.

### paramsStr

```haxe
var ?paramsStr:Null<String>
```

The parameters formatted as a string, added to the output file name.

### params

```haxe
var ?params:Null<Dynamic>
```

The parameters of the conversion.

### conv

```haxe
var conv:Array<Convert>
```

The converters, the first one supporting the file is used.
