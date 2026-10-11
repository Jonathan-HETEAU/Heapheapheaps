# Getting started

> Install Heaps, write a first application, compile it for the browser (WebGL) and for HashLink, and understand its life cycle.

![The application of this guide](img/getting-started.png)

## Install

Heaps is a Haxe library. You need:

- [Haxe](https://haxe.org/download/) 4.3 or later.
- To run on desktop: [HashLink](https://hashlink.haxe.org), the Haxe virtual machine (`hl` command).
- To run in the browser: nothing more, any browser supporting WebGL.

Then install the libraries from haxelib:

```sh
haxelib install heaps
haxelib install hlsdl      # HashLink with SDL (OpenGL), Windows, Linux and macOS
haxelib install hldx       # optional: HashLink with DirectX, Windows only
```

## A first application

An application extends [`hxd.App`](../api/heaps/hxd/App.md). The `App` creates the window, the engine, a 2D scene `s2d` and a 3D scene `s3d`, then calls your functions:

```haxe
class Main extends hxd.App {

	var logo : h2d.Bitmap;
	var label : h2d.Text;

	override function init() {
		// a bitmap from the res/hxlogo.png resource, centered on its pivot
		var tile = hxd.Res.hxlogo.toTile().center();
		logo = new h2d.Bitmap(tile, s2d);

		// a text with the default font
		label = new h2d.Text(hxd.res.DefaultFont.get(), s2d);
		label.text = "Hello Heaps!";
		label.setScale(2);
		label.setPosition(20, 20);

		onResize();
	}

	override function onResize() {
		// keep the logo at the center of the window
		logo.setPosition(s2d.width / 2, s2d.height / 2);
	}

	override function update(dt : Float) {
		// dt is the elapsed time in seconds since the last frame
		logo.rotation += dt;
	}

	static function main() {
		// embed the files of res/ in the program, available as hxd.Res.*
		hxd.Res.initEmbed();
		new Main();
	}
}
```

Put an image named `hxlogo.png` in a `res` directory next to `Main.hx`. The full project is in [examples/getting-started](examples/getting-started/Main.hx).

## Compile and run

### In the browser (WebGL)

`build-js.hxml`:

```hxml
-cp .
-lib heaps
-main Main
-js main.js
```

Run `haxe build-js.hxml`, then open an `index.html` holding a canvas with the id `webgl` (Heaps draws in it):

```html
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Hello Heaps</title>
<style>html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; } #webgl { width: 100%; height: 100%; }</style>
</head>
<body>
<canvas id="webgl"></canvas>
<script src="main.js"></script>
</body>
</html>
```

Serve the directory with a local web server (for example `python3 -m http.server`) rather than opening the file directly.

### With HashLink

`build-hl.hxml`:

```hxml
-cp .
-lib heaps
-lib hlsdl
-main Main
-hl main.hl
```

Run `haxe build-hl.hxml`, then `hl main.hl`. Replace `-lib hlsdl` with `-lib hldx` to use DirectX on Windows.

## The life cycle of an application

`new Main()` sets everything up, then Heaps calls the functions of your `App`:

| Function | When |
|---|---|
| `loadAssets(onLoaded)` | Once, first. Override it to load assets asynchronously, and call `onLoaded` when done. By default it calls `onLoaded` at once. |
| `init()` | Once, after `loadAssets`. Create your scene here. |
| `update(dt)` | Every frame, before rendering. `dt` is the elapsed time in seconds ([`hxd.Timer.dt`](../api/heaps/hxd/Timer.md), smoothed). |
| `onResize()` | When the window is resized. `s2d.width` and `s2d.height` give the new size. |

After `update`, the engine renders `s3d` then `s2d` over it. `hxd.Timer.tmod` gives the same time as a frame ratio (`1` at 60 FPS) if you prefer to count in frames.

## Resources

The files of the `res` directory are available, typed, as `hxd.Res.<path>`: `res/hxlogo.png` is `hxd.Res.hxlogo`, `res/ui/font.fnt` is `hxd.Res.ui.font`. A typo is a compilation error. Call one of these before using them:

| Call | Resources come from | Use |
|---|---|---|
| `hxd.Res.initEmbed()` | the program itself | all platforms, the simplest |
| `hxd.Res.initLocal()` | the `res` directory on disk, with hot reloading | desktop development |
| `hxd.Res.initPak()` | a `.pak` archive built by `hxd.fmt.pak.Build` | desktop release |

Use `-D resourcesPath=dir` to use another directory than `res`. See [`hxd.Res`](../api/heaps/hxd/Res.md) and [`hxd.res.Loader`](../api/heaps/hxd/res/Loader.md).

## Next steps

- The [`h2d` package](../api/heaps/h2d/README.md): the 2D scene graph (`h2d.Object`, `h2d.Bitmap`, `h2d.Text`, `h2d.Graphics`, `h2d.Interactive`...).
- The [`h3d.scene` package](../api/heaps/h3d/scene/README.md): the 3D scene graph.
- The samples of the Heaps repository (`samples/`): `haxe gen.hxml` creates a project per sample.
