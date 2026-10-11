# hide.view.settings.Categorie

**class** · package [`hide.view.settings`](README.md) · module [`hide.view.settings.Settings`](Settings.md) · source [`hide_js/hide/view/settings/Settings.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/view/settings/Settings.hx) · available on editor (js)

A category of a settings view.

## Constructor

### new

```haxe
function new(name:String):Void
```

Creates a category.

## Variables

### name

```haxe
var name:String
```

The name.

### element

```haxe
var element:hide.Element
```

The element of the settings of the category.

## Methods

### add

```haxe
function add(settingsName:String, editElement:hide.Element, value:Dynamic, ?onChange:() -> Void):Void
```

Adds a setting with its edit element. `onChange` is called with the new value.
