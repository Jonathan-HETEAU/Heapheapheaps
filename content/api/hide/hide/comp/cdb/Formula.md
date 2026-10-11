# hide.comp.cdb.Formula

**typedef** · package [`hide.comp.cdb`](README.md) · module [`hide.comp.cdb.Formulas`](Formulas.md) · source [`hide_js/hide/comp/cdb/Formulas.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/cdb/Formulas.hx) · available on editor (js)

A CDB formula: a function of the formulas file computing a number column from a line.

## Fields

### type

```haxe
var type:String
```

The type name of the sheet (see `Formulas.getTypeName`).

### name

```haxe
var name:String
```

The function name.

### call

```haxe
var call:() -> Null<Float>
```

Computes the value from the line.
