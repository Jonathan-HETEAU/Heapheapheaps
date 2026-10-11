# hide.comp.cdb.ValidationFunction

**typedef** · package [`hide.comp.cdb`](README.md) · module [`hide.comp.cdb.Formulas`](Formulas.md) · source [`hide_js/hide/comp/cdb/Formulas.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/cdb/Formulas.hx) · available on editor (js)

A line validation function of the formulas file: a function whose name starts with `validate`.

## Fields

### type

```haxe
var type:String
```

The type name of the sheet.

### name

```haxe
var name:String
```

The function name.

### call

```haxe
var call:() -> ValidationResult
```

Validates a line.
