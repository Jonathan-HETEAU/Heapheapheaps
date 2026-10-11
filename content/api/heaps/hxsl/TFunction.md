# hxsl.TFunction

**typedef** · package [`hxsl`](README.md) · module `hxsl.Ast` · source [`hxsl/Ast.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/hxsl/Ast.hx)

A typed shader function.

## Fields

### ret

```haxe
var ret:Type
```

The return type.

### ref

```haxe
var ref:TVar
```

The variable referencing the function.

### kind

```haxe
var kind:FunctionKind
```

The kind of the function.

### expr

```haxe
var expr:TExpr
```

The body of the function.

### args

```haxe
var args:Array<TVar>
```

The arguments of the function.
