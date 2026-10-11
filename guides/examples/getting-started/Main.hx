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
