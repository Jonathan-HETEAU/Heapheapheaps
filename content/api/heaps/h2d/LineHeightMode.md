# h2d.LineHeightMode

**enum** · package [`h2d`](README.md) · module [`h2d.HtmlText`](HtmlText.md) · source [`h2d/HtmlText.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h2d/HtmlText.hx)

The `HtmlText` line height calculation rules.

## Constructors

### Accurate

```haxe
Accurate
```

Accurate line height calculations. Each line will adjust it's height according to it's contents.

### TextOnly

```haxe
TextOnly
```

Only text adjusts line heights, and `<img>` tags do not affect it (partial legacy behavior).

### Constant

```haxe
Constant
```

Legacy line height mode. When used, line heights remain constant based on `Text.font` variable.
