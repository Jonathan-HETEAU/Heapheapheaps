# steam.data.ControllerActionSet

**typedef** · package [`steam.data`](README.md) · module [`steam.data.ControllerConfig`](ControllerConfig.md) · source [`steam/data/ControllerConfig.hx`](https://github.com/Jonathan-HETEAU/hlsteam/blob/ccr-01f70725-tatboj/steam/data/ControllerConfig.hx)

An action set: the actions available in a context of the game (menu, gameplay...).

## Fields

### stickPadGyro

```haxe
var stickPadGyro:Array<StickPadGyroAction>
```

The stick, pad or gyro actions.

### name

```haxe
var name:String
```

The name of the action set.

### localizationKey

```haxe
var localizationKey:String
```

The localization key of its title.

### button

```haxe
var button:Array<ButtonAction>
```

The digital actions.

### analogTrigger

```haxe
var analogTrigger:Array<AnalogTriggerAction>
```

The analog trigger actions.
