# hide.comp.RefreshFlag

**enum** · package [`hide.comp`](README.md) · module [`hide.comp.FancyTree`](FancyTree.md) · source [`hide_js/hide/comp/FancyTree.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/FancyTree.hx) · available on editor (js)

What a tree refresh must update.

## Constructors

### Flat

```haxe
Flat
```

Rebuilds the list of the shown items.

### Search

```haxe
Search
```

Applies the search filter again (implies `Flat`).

### FocusCurrent

```haxe
FocusCurrent
```

Scrolls to the current item.

### RegenHeader

```haxe
RegenHeader
```

Regenerates the name and icon of the items.
