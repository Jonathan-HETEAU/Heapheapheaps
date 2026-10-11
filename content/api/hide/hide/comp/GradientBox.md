# hide.comp.GradientBox

**class** · package [`hide.comp`](README.md) · module [`hide.comp.GradientEditor`](GradientEditor.md) · source [`hide_js/hide/comp/GradientEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/GradientEditor.hx) · available on editor (js)

Extends: [`hide.comp.Component`](Component.md)

Displays a gradient. Opens a gradient editor on click.

## Constructor

### new

```haxe
function new(?parent:Null<hide.Element>, ?root:Null<hide.Element>):Void
```

Creates a gradient box. `root` is replaced by the box.

## Variables

### value

```haxe
var value(get, set):hrt.impl.GradientData
```

The gradient.

## Methods

### onChange

```haxe
dynamic function onChange(isDragging:Bool):Void
```

Called when the gradient changes. `isDragging` is true during a drag.

## Inherited members

- from [`hide.comp.Component`](Component.md): `componentName`, `element`, `saveDisplayKey`, `remove`
