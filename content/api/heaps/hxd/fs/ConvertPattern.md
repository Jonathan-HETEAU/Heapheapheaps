# hxd.fs.ConvertPattern

**enum** · package [`hxd.fs`](README.md) · module [`hxd.fs.FileConverter`](FileConverter.md) · source [`hxd/fs/FileConverter.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/fs/FileConverter.hx) · available on hl/sdl, hl/directx

The files matched by a conversion rule, from the key of the `fs.convert` entry.

## Constructors

### Filename

```haxe
Filename(name:String)
```

A file name.

### Regexp

```haxe
Regexp(r:EReg)
```

A regular expression on the file name or path (keys starting with `^`).

### Ext

```haxe
Ext(e:String)
```

A file extension.

### Exts

```haxe
Exts(e:Array<String>)
```

A list of extensions (keys such as `png,jpg`).

### Wildcard

```haxe
Wildcard
```

All files (the `*` key).
