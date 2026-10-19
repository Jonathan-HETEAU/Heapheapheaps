/**
	Loads the level `res/level.prefab`, made in Hide, and shows it.
**/
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
