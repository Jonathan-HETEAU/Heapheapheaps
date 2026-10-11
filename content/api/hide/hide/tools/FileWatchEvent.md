# hide.tools.FileWatchEvent

**typedef** · package [`hide.tools`](README.md) · module [`hide.tools.FileWatcher`](FileWatcher.md) · source [`hide/tools/FileWatcher.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide/tools/FileWatcher.hx) · available on editor (js)

A watch of a file.

## Fields

### path

```haxe
var path:String
```

The absolute path watched.

### ignoreCheck

```haxe
var ?ignoreCheck:Null<String>
```

The signature of the content whose change is ignored.

### fun

```haxe
var fun:() -> Void
```

Called when the file changes.

### element

```haxe
var element:hide.HTMLElement
```

The element the watch belongs to: the watch is removed when it leaves the document.

### checkDel

```haxe
var checkDel:Bool
```

Also calls `fun` when the file is deleted.
