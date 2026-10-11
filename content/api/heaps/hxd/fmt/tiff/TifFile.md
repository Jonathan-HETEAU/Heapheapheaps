# hxd.fmt.tiff.TifFile

**typedef** · package [`hxd.fmt.tiff`](README.md) · module `hxd.fmt.tiff.Data` · source [`hxd/fmt/tiff/Data.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/fmt/tiff/Data.hx)

The content of a TIFF file: its tags and its strips of data.

## Fields

### tags

```haxe
var tags:Array<{ value:TifValue, type:TifType, tag:TifTag }>
```

The tags of the image.

### data

```haxe
var data:Array<Bytes>
```

The strips of image data.
