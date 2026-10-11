# domkit.CssSheetElement

**typedef** · package [`domkit`](README.md) · module [`domkit.CssParser`](CssParser.md) · source [`domkit/CssParser.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/CssParser.hx)

A CSS rule: its selectors, properties, transitions and nested rules.

## Fields

### transitions

```haxe
var ?transitions:Null<Array<Transition>>
```

The transitions.

### subRules

```haxe
var ?subRules:Null<CssSheet>
```

The nested rules, when not expanded (see `CssParser.expandSubRules`).

### style

```haxe
var style:Array<CssRule>
```

The properties.

### classes

```haxe
var classes:Array<CssClass>
```

The selectors (separated by commas).
