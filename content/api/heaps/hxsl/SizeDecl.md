# hxsl.SizeDecl

**enum** · package [`hxsl`](README.md) · module `hxsl.Ast` · source [`hxsl/Ast.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxsl/Ast.hx)

The size of an array: a constant, or a constant variable.

## Constructors

### SConst

```haxe
SConst(v:Int)
```

A constant size.

### SVar

```haxe
SVar(v:TVar)
```

The size given by a constant variable.
