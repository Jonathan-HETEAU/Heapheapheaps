# h3d.IDrawable

**interface** · package [`h3d`](README.md) · source [`h3d/IDrawable.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/IDrawable.hx)

Implemented by: [`h2d.Scene`](../h2d/Scene.md), [`h3d.scene.Scene`](scene/Scene.md), [`hxd.App`](../hxd/App.md)

Something which can be rendered by the engine, such as a [`h3d.scene.Scene`](scene/Scene.md) or a [`h2d.Scene`](../h2d/Scene.md) (see [`hxd.App`](../hxd/App.md)).

## Methods

### render

```haxe
function render(engine:Engine):Void
```

Renders the content to the current render target.
