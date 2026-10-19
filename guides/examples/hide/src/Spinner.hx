/**
	A prefab of the game: a colored cube that turns on itself.

	The fields with `@:s` are saved in the prefab file. In Hide, `edit` shows them in the
	properties panel; in the game, `makeObject` creates the 3D object and `updateInstance` applies
	the fields to it.
**/
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
