# Using Hide, the Heaps editor

> Build and run Hide, make a level with it, load the level in a Heaps game, and add your own prefab types to the editor.

*[Version française](fr/02-hide.md)*

![The level of this guide, loaded in the game](img/hide-level.png)

The example of this guide is in [`examples/hide`](https://github.com/Jonathan-HETEAU/Heapheapheaps/tree/main/guides/examples/hide): a small project with its `res/` folder, a level made of Hide prefabs, a prefab type of the game (`Spinner`) and the game that loads the level.

## What Hide is

Hide (Heaps IDE) is the editor Shiro Games use for their games. It works on the files of the `res/` folder of a game: you open the project, Hide shows its resources, and each kind of file opens in its own editor.

| Files | Editor | In the game |
|---|---|---|
| `.prefab` | Scene editor: a tree of objects (models, lights, boxes, your own types...) | [`hrt.prefab.Prefab`](../api/hide/hrt/prefab/Prefab.md) |
| `.l3d` | Same scene editor, for whole 3D levels (terrain, baked lighting...) | `hrt.prefab.Prefab` |
| `.fx`, `.fx2d` | Visual effects on a timeline: emitters, curves, animated properties | [`hrt.prefab.fx.FX`](../api/hide/hrt/prefab/fx/FX.md) |
| `.shgraph` | Shader graph: a shader made of connected nodes | [`hrt.shgraph.ShaderGraph`](../api/hide/hrt/shgraph/ShaderGraph.md) |
| `.matlib`, `.rp` | Material library, render profile | `hrt.prefab.Prefab` |
| `.fbx`, `.hmd` | Model viewer: animations, materials | `hxd.res.Model` |
| images, `.wav`, `.mp3`, `.ogg` | Image viewer, sound player | `hxd.res.Image`, `hxd.res.Sound` |
| `data.cdb` (Database menu) | [CastleDB](https://castledb.org) tables: the data of the game | `cdb` |

Hide has two parts:

- **the editor** (`hide` package), a JavaScript application running in [NW.js](https://nwjs.io);
- **the runtime** (`hrt` package), which the game uses with `-lib hide` to load what the editor made.

Most of these files are **prefabs**: a tree of typed nodes, saved as JSON. Each node has a type (`"box"`, `"light"`, `"model"`...) that is a Haxe class registered under that name, and the fields of the class marked `@:s`. The editor creates and edits the tree, and the game rebuilds the same objects from it.

## Build and run Hide

Hide is built from its sources with the same libraries as the game. Install them from git, as the [README of Hide](https://github.com/HeapsIO/hide#compiling-from-source) says:

```sh
haxelib git format https://github.com/HaxeFoundation/format
haxelib git heaps https://github.com/HeapsIO/heaps
haxelib git castle https://github.com/ncannasse/castle
haxelib git hxbit https://github.com/ncannasse/hxbit
haxelib git hscript https://github.com/HaxeFoundation/hscript
haxelib git hxnodejs https://github.com/HaxeFoundation/hxnodejs
haxelib git domkit https://github.com/HeapsIO/domkit
haxelib git hx3compat https://github.com/HaxeFoundation/hx3compat
haxelib git hashlink https://github.com/HaxeFoundation/hashlink master other/haxelib/
```

Then clone Hide, register it as a library for your games, and build the editor:

```sh
git clone https://github.com/HeapsIO/hide
haxelib dev hide hide
cd hide
haxe hide.hxml          # creates bin/hide.js
```

Hide runs in **NW.js**: download the NW.js **SDK** from [nwjs.io](https://nwjs.io) and copy it into `bin/nwjs`. Then:

- Windows: run `bin/hide.cmd`.
- Linux: from the `bin` folder, run `nwjs/nw .`
- macOS: copy all the files of `bin` into `bin/nwjs.app/Contents/Resources/app.nw`, then open the NW.js application.

Hide and the game must use the same Heaps: if `haxe hide.hxml` fails, update the libraries from git.

## Open a project

A Hide project is the folder that contains the `res/` folder of the game. Use **Project > Open...** and choose that folder (choosing `res/` itself also works: Hide goes up one folder). The last projects are in **Project > Recently opened**.

Hide reads its settings from `bin/defaultProps.json`, then from your user settings, then from `res/props.json` in the project, each one overriding the previous ones; a `props.json` in a subfolder applies to the files of that folder. The plugins of the game are declared in `res/props.json` (see [Your own prefab types](#your-own-prefab-types)), a JSON file edited like any other. **Settings > User settings** edits your preferences, and **Settings > Project settings** lists the `props.json` files of the project and edits their material libraries, render props and conversion settings. The CastleDB database of the project is `res/data.cdb` (setting `cdb.databaseFile`), opened from the **Database** menu.

## The interface

- **File browser** (**View > File Browser**): the files of `res/`. Double-click opens a file in a tab; right-click on a folder, **New ...** creates a file (directory, prefab, FX, shader graph, particles...).
- **Scene editor** (`.prefab`, `.l3d`, `.fx`): the 3D view, the tree of the prefab beside it, and the properties of the selected node. Right-click in the tree, **New...**, adds a node, grouped by kind (**3D**, **2D**...).
- **Tabs**: several files open at once; **Layout** saves the arrangement of the panels.

Moving in the 3D view:

| Action | Mouse and keys |
|---|---|
| Look around | Hold the right button and move the mouse |
| Fly | While holding the right button: Z Q S D or the arrows (W also goes forward); A and E roll the view, Shift + A / E go up and down |
| Change the flying speed | Mouse wheel while holding the right button |
| Drag the ground | Hold the middle button (or Alt + left button) |
| Frame the selection | F |

Main shortcuts of the scene editor (all of them are in `bin/defaultProps.json`, keys `key.*`, and can be changed in the settings):

| Key | Action | Key | Action |
|---|---|---|---|
| W | Move gizmo | Ctrl+S | Save |
| E | Rotate gizmo | Ctrl+Z / Ctrl+Y | Undo / redo |
| R | Scale gizmo | Ctrl+D | Duplicate in place |
| X | Snap on / off | Delete | Delete |
| G | Grid on / off | F2 | Rename |
| H / Ctrl+H | Hide / show all | Ctrl+G | Group the selection |
| I | Isolate the selection | Backspace | Select the parent |

## Make a level

1. In the file browser, right-click on `res`, **New ...**, **Prefab**, and name it `level`: Hide creates `res/level.prefab` and opens it.
2. Right-click in the tree, **New...**, **3D**, **Light**. In its properties, set **Kind** to **Directional**, and turn it with the rotation fields so that it lights the scene from above.
3. **New...**, **3D**, **Box**: rename it `ground` (F2), and give it a scale of 12 × 12 × 0.2 and a Z of -1 in the **Position** group.
4. Save with Ctrl+S.

The file is the JSON of the tree. Only the fields that differ from their default value are written:

```json
{
	"type": "prefab",
	"children": [
		{
			"type": "light",
			"name": "sun",
			"rotationY": 50,
			"rotationZ": 30,
			"kind": "Directional",
			"power": 0.8
		},
		{
			"type": "box",
			"name": "ground",
			"z": -1,
			"scaleX": 12,
			"scaleY": 12,
			"scaleZ": 0.2
		}
	]
}
```

The [`level.prefab`](examples/hide/res/level.prefab) of the example also has two `spinner` nodes, a type of the game: see [Your own prefab types](#your-own-prefab-types).

## Load the level in the game

The game uses the runtime of Hide with `-lib hide`. With it, `hxd.Res` gives a [`hrt.prefab.Resource`](../api/hide/hrt/prefab/Resource.md) for each `.prefab`, `.fx` or `.l3d` file.

```haxe
class Main extends hxd.App {

	var root : h3d.scene.Object;
	var level : hrt.prefab.Prefab;

	override function init() {
		engine.backgroundColor = 0x203040;
		s3d.camera.pos.set(9, -12, 8);
		s3d.camera.target.set(0, 0, 0);

		root = new h3d.scene.Object(s3d);
		load();

		// Saving the level in Hide reloads it in the running game (with hxd.Res.initLocal).
		hxd.Res.level.watch(load);
	}

	function load() {
		root.removeChildren();
		// load() reads the file (once, then cached); make() creates its objects under root.
		level = hxd.Res.level.load().make(root);

		// The prefab tree: find a prefab by class, or all of them.
		for( s in level.findAll(Spinner) )
			trace('${s.name}: ${s.speed} turns per second');
	}

	static function main() {
		#if hl
		hxd.res.Resource.LIVE_UPDATE = true;
		hxd.Res.initLocal(); // the res/ files from the disk: they can change while the game runs
		#else
		hxd.Res.initEmbed(); // the res/ files embedded in the program
		#end
		new Main();
	}
}
```

- `load()` returns the prefab of the file, a template: it is read once and kept in cache.
- `make(parent)` creates the objects of the tree under `parent` (an `h3d.scene.Object` or an `h2d.Object`) and returns the instance.
- `find(Class)`, `findAll(Class)` and `getOpt(Class, name)` search the tree of the instance. An [`Object3D`](../api/hide/hrt/prefab/Object3D.md) prefab gives its 3D object with `local3d`.
- `watch(callback)` is called when the file changes: on HashLink with `hxd.Res.initLocal()`, the level is rebuilt each time it is saved in Hide.

The prefab types used by the files must be **compiled into the game**: a type registers itself when its class is compiled, and Haxe only compiles the classes the code uses. List them in the `.hxml`:

```hxml
-cp src
-lib heaps
-lib hide
-main Main
# The Hide prefab types used by the levels: each one registers itself when compiled.
hrt.prefab.Light
hrt.prefab.l3d.Box
-js main.js
```

A node whose type is not compiled is loaded as an [`hrt.prefab.Unknown`](../api/hide/hrt/prefab/Unknown.md) prefab, without error and without object: if a part of a level is missing in the game, check this list first. On HashLink, `--macro include("hrt.prefab")` compiles all of them; on the web it fails, because some of them only exist on desktop.

## Your own prefab types

A game adds its own node types by extending a prefab class. This one is a colored cube that turns on itself:

```haxe
class Spinner extends hrt.prefab.Object3D {

	/** Turns per second. **/
	@:s public var speed : Float = 0.5;

	/** Color of the cube, as 0xRRGGBB. **/
	@:s public var color : Int = 0xFF8000;

	override function makeObject( parent3d : h3d.scene.Object ) : h3d.scene.Object {
		return new SpinnerMesh(parent3d);
	}

	override function updateInstance( ?propName : String ) {
		super.updateInstance(propName);
		var mesh = cast(local3d, SpinnerMesh);
		mesh.speed = speed;
		mesh.material.color.setColor(color);
	}

	#if editor
	// Hide only: the name and icon in the "New..." menu, and the properties panel.
	override function getHideProps() : hide.prefab.HideProps {
		return { icon : "refresh", name : "Spinner" };
	}

	override function edit( ctx : hide.prefab.EditContext ) {
		super.edit(ctx); // position, rotation, scale
		var props = new hide.Element('
			<div class="group" name="Spinner">
				<dl>
					<dt>Speed</dt><dd><input type="range" min="0" max="4" field="speed"/></dd>
					<dt>Color</dt><dd><input type="color" field="color"/></dd>
				</dl>
			</div>
		');
		ctx.properties.add(props, this, function(propName) ctx.onChange(this, propName));
	}
	#end

	// "spinner" is the type written in the prefab files.
	static var _ = hrt.prefab.Prefab.register("spinner", Spinner);
}

/** The cube of a `Spinner`, turning around its Z axis. **/
class SpinnerMesh extends h3d.scene.Mesh {

	public var speed = 0.;

	public function new( parent ) {
		// The cube shared by all the meshes, 1 unit wide and centered.
		super(h3d.prim.Cube.defaultUnitCube(), null, parent);
	}

	override function sync( ctx : h3d.scene.RenderContext ) {
		super.sync(ctx);
		rotate(0, 0, speed * Math.PI * 2 * ctx.elapsedTime);
	}
}
```

- `@:s` fields are saved in the file (when they differ from their default value) and loaded back.
- `makeObject` creates the 3D object, `updateInstance` applies the fields to it: the editor calls it again each time a property changes.
- `register("spinner", Spinner)` gives the type its name in the files.
- The `#if editor` part only exists in Hide: `getHideProps` names the type in the **New...** menu, `edit` builds the properties panel. `field="speed"` binds an input to the `speed` field, and `ctx.onChange` updates the scene.

The game knows `Spinner` because it uses it. **Hide** knows it through a **plugin**: the classes of the game compiled for the editor. List them in a module:

```haxe
// HideImports.hx: the classes of the game that Hide must know.
import Spinner;
```

compile them with `hide.Plugin.init()`:

```hxml
# hide-plugin.hxml
-cp src
-lib hide
-lib hxnodejs
-lib domkit
-lib castle
--macro hide.Plugin.init()
-js hide-plugin.js
-dce no
HideImports
```

and declare the plugin in `res/props.json` (its path is relative to `res/`):

```json
{
	"plugins": ["../hide-plugin.js"]
}
```

After `haxe hide-plugin.hxml`, reopen the project in Hide (or press Ctrl+F5 to reload the editor): **New...**, **3D**, **Spinner** adds a cube, and its speed and color appear in the properties. Rebuild the plugin each time the prefab classes change.

## The example

[`examples/hide`](https://github.com/Jonathan-HETEAU/Heapheapheaps/tree/main/guides/examples/hide) puts it all together. It is also a Hide project: open its folder with **Project > Open...** after building the plugin.

```sh
cd examples/hide
haxe hide-plugin.hxml   # the plugin, for Hide
haxe build-js.hxml      # the game for the browser: open index.html through a local server
haxe build-hl.hxml      # the game for HashLink: hl main.hl, reloads the level when it is saved
```

## Troubleshooting

| Problem | Cause |
|---|---|
| A node of the level is missing in the game, without error | Its type is not compiled into the game: add its class to the `.hxml`. |
| A type of the game is missing from **New...** in Hide | The plugin is not built, not declared in `res/props.json`, or not reloaded. |
| `Please add -lib domkit` when building the plugin | Add `-lib domkit` to `hide-plugin.hxml`. |
| `You cannot access the sys package while targeting js` | `include("hrt.prefab")` on the web: list the needed types instead. |
| `haxe hide.hxml` fails | Hide needs the same, recent, versions of Heaps and its libraries: update them from git. |
