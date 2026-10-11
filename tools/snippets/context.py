"""The context assumed by the code examples, for tools/snippets/check.py.

ENVS: compilation environments (libraries, base class, fields available to every example).
CONTEXT: per example, keyed by "<repo>/<path> :: <first line of the example>":
  env      the environment (default: DEFAULT_ENV of the repository)
  mode     "body" (statements, default), "members" (class members), "module" (type declarations),
           "split" (type declarations followed by statements),
           "members-body" (class members, then statements from the `split` marker line)
  implements  interface implemented by the Snippet class
  split    see "members-body"
  wrap     module code with a `{code}` placeholder for the example (instead of mode)
  imports  module imports
  module   extra type declarations
  members  extra fields of the Snippet class
  locals   statements before the example (declarations of the variables it uses)
  hxml     extra compiler arguments
  skip     reason not to compile it
"""

HEAPS_MEMBERS = """
	var obj : h3d.scene.Object;
	var mesh : h3d.scene.Mesh;
	var prim : h3d.prim.Primitive;
	var cache : h3d.prim.ModelCache;
	var mask : h3d.scene.Mesh;
	var ctx : h3d.scene.RenderContext;
	var texture : h3d.mat.Texture;
	var source : h3d.mat.Texture;
	var destination : h3d.mat.Texture;
	var output : h3d.mat.Texture;
	var floats : hxd.FloatBuffer;
	var myObj : h2d.Object;
	var myTextureInstance : h3d.mat.Texture;
	var tile : h2d.Tile;
	var console : h2d.Console;
"""

ENVS = {
	"heaps": {
		"hxml": ["-lib heaps", "-js", "x.js"],
		"base": "hxd.App",
		"members": HEAPS_MEMBERS,
	},
	"heaps-sys": {
		"hxml": ["-lib heaps", "-lib hlsdl", "-hl", "x.hl"],
	},
	"hxbit": {
		"hxml": ["-lib hxbit", "-js", "x.js"],
	},
	"hrt": {
		"hxml": ["-lib heaps", "-lib castle", "-lib hscript", "-lib hlsdl", "-D hscriptPos", "-D hide", "-cp $SRC/hide", "-hl", "x.hl"],
		"base": "hxd.App",
	},
	"hide": {
		"hxml": ["-lib heaps", "-lib hxnodejs", "-lib hscript", "-lib castle", "-lib hx3compat", "-lib domkit", "-lib hashlink",
			"-D js-classic", "-D js-unflatten", "-D hscriptPos", "-D multidriver", "-D editor", "-D no-deprecation-warnings",
			"-D manual_sync_pad", "-D hide", "-cp $SRC/hide", "-cp $SRC/hide/hide_js", "-cp $SRC/hide/hide_js/libs", "-js", "x.js"],
	},
}

DEFAULT_ENV = {"heaps": "heaps", "hxbit": "hxbit", "domkit": "heaps", "hlsteam": "heaps", "hide": "hrt"}

CONTEXT = {
	"heaps/h2d/Console.hx :: function addItem(id:Int, ?amount:Int) {": {
		"locals": "var player : Dynamic = null; function findItemById(id:Int) return { name : \"item\" };",
	},
	"heaps/h2d/filter/Shader.hx :: class InvertColorShader extends h3d.shader.ScreenShader {": {"mode": "split"},
	"heaps/h3d/pass/ScreenFx.hx :: var fx = new h3d.pass.ScreenFx(new MyScreenShader());": {
		"module": "class MyScreenShader extends h3d.shader.ScreenShader { static var SRC = { @param var texture : Sampler2D; function fragment() { pixelColor = texture.get(calculatedUV); } } }",
	},
	"heaps/h3d/pass/Shadows.hx :: light.shadows.mode = Dynamic;": {
		"locals": "var light = new h3d.scene.pbr.DirLight(s3d);",
	},
	"heaps/h3d/scene/MeshBatch.hx :: batch.begin(units.length);": {
		"locals": "var batch : h3d.scene.MeshBatch = null; var colorShader = new h3d.shader.ColorMult(); var units : Array<{ x : Float, y : Float, color : Int }> = [];",
	},
	"heaps/hxd/fs/FileConverter.hx :: // Register Convert": {
		"env": "heaps-sys", "mode": "members",
		"module": "class MyFancyConvert extends hxd.fs.Convert { public function new() { super(\"origext,otherext\", \"fancyext\"); } }",
	},
	"hxbit/README.md :: var s = new hxbit.Serializer();": {
		"module": "class User implements hxbit.Serializable { @:s public var name : String; public function new() {} }",
		"locals": "var user = new User(); var bytes : haxe.io.Bytes = null;",
	},
	"hxbit/README.md :: @:rpc(server) public function sendAction( act : String ) : Bool {": {
		"mode": "members-body", "split": "sendAction(\"test\"", "implements": "hxbit.NetworkSerializable",
	},
	"hxbit/README.md :: function teleport( t : Target ) {": {
		"mode": "members", "implements": "hxbit.NetworkSerializable",
		"module": "typedef Target = { function getPosition() : { x : Float, y : Float }; }",
		"members": "@:s var x : Float; @:s var y : Float;",
	},
	"hxbit/README.md :: @:rpc(checked)": {
		"mode": "members-body", "split": "// Usage:", "implements": "hxbit.NetworkSerializable",
		"module": "enum PurchaseResult { Success; NotFound; NotEnoughGold; }",
		"members": "var inventory : Map<Int, { price : Int }>; var player : { gold : Int, addItem : Dynamic -> Void }; function showError(r : PurchaseResult) {}",
		"locals": "var itemId = 0;",
	},
	"hxbit/hxbit/Serializer.hx :: var bytes = new hxbit.Serializer().serialize(obj);": {
		"module": "class MyClass implements hxbit.Serializable { public function new() {} }",
		"locals": "var obj = new MyClass();",
	},
	"hide/README.md :: // HideImports.hx": {"skip": "imports the classes of the user's own project"},
	"hide/README.md :: class MyPrefab extends hrt.prefab.Object3D {": {"env": "hide"},
	"hide/README.md :: import hide.view.FileView;": {"env": "hide"},
	"hide/hrt/prefab/Prefab.hx :: static var _ = Prefab.register(\"myPrefabName\", MyPrefabClass);": {
		"wrap": "import hrt.prefab.Prefab;\nclass MyPrefabClass extends Prefab {\n{code}\n}",
	},
}
