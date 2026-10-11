# h3d.impl.AllocStats

**typedef** · package [`h3d.impl`](README.md) · module [`h3d.impl.MemoryManager`](MemoryManager.md) · source [`h3d/impl/MemoryManager.hx`](https://github.com/Jonathan-HETEAU/heaps/blob/ccr-01f70725-tatboj/h3d/impl/MemoryManager.hx)

The allocations made from the same code position (see `MemoryManager.allocStats`).

## Fields

### tex

```haxe
var tex:Bool
```

Tells if the allocations are textures (or buffers).

### stacks

```haxe
var stacks:Array<StackStats>
```

The allocations, by call stack.

### size

```haxe
var size:Float
```

The memory size in bytes.

### position

```haxe
var position:String
```

The code position.

### count

```haxe
var count:Int
```

The number of allocations.
