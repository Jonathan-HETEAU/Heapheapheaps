# domkit.SetAttributeResult

**enum** · package [`domkit`](README.md) · module [`domkit.Properties`](Properties.md) · source [`domkit/Properties.hx`](https://github.com/Jonathan-HETEAU/domkit/blob/ccr-01f70725-tatboj/domkit/Properties.hx)

The result of `Properties.setAttribute`.

## Constructors

### Ok

```haxe
Ok
```

The value was applied.

### Unknown

```haxe
Unknown
```

The property is unknown.

### Unsupported

```haxe
Unsupported
```

The component doesn't support the property.

### InvalidValue

```haxe
InvalidValue(?msg:String)
```

The value is invalid for the property.
