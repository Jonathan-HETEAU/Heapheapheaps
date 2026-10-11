# hxd.res.FontBuildOptions

**typedef** · package [`hxd.res`](README.md) · module [`hxd.res.FontBuilder`](FontBuilder.md) · source [`hxd/res/FontBuilder.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/res/FontBuilder.hx)

Options for `FontBuilder.getFont`.

## Fields

### kerning

```haxe
var ?kerning:Null<Bool>
```

Enables kerning (currently unused).

### chars

```haxe
var ?chars:Null<String>
```

The characters to include in the font (default `hxd.Charset.DEFAULT_CHARS`).

### antiAliasing

```haxe
var ?antiAliasing:Null<Bool>
```

Enables anti-aliasing (default `true`).
