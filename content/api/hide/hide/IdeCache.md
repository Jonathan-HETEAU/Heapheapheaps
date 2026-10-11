# hide.IdeCache

**class** · package [`hide`](README.md) · module [`hide.Ide`](Ide.md) · source [`hide_js/hide/Ide.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/Ide.hx) · available on editor (js)

A cache of the IDE stored in the engine resource cache.

## Constructor

### new

```haxe
function new():Void
```

Creates an empty cache.

## Variables

### getTextureCache

```haxe
var getTextureCache:Map<String, h3d.mat.Texture>
```

The textures loaded by `Ide.getTexture`, by full path.
