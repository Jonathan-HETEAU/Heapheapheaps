# hxd.Interactive

**interface** · package [`hxd`](README.md) · module [`hxd.SceneEvents`](SceneEvents.md) · source [`hxd/SceneEvents.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxd/SceneEvents.hx)

Implemented by: [`h2d.Interactive`](../h2d/Interactive.md), [`h3d.scene.Interactive`](../h3d/scene/Interactive.md)

An object which can receive events from `SceneEvents`, such as [`h2d.Interactive`](../h2d/Interactive.md) and [`h3d.scene.Interactive`](../h3d/scene/Interactive.md).

## Variables

### propagateEvents

```haxe
var propagateEvents:Bool
```

If set, events are also sent to the interactives below this one.

### cursor

```haxe
var cursor(default, set):Cursor
```

The cursor displayed when the mouse is over the interactive.

## Methods

### handleEvent

```haxe
function handleEvent(e:Event):Void
```

Handles an event sent to the interactive.

### getInteractiveScene

```haxe
function getInteractiveScene():InteractiveScene
```

Returns the scene of the interactive.
