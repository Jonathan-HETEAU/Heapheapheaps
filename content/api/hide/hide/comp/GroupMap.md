# hide.comp.GroupMap

**typedef** · package [`hide.comp`](README.md) · module [`hide.comp.PropsEditor`](PropsEditor.md) · source [`hide_js/hide/comp/PropsEditor.hx`](https://github.com/Jonathan-HETEAU/hide/blob/ccr-01f70725-tatboj/hide_js/hide/comp/PropsEditor.hx) · available on editor (js)

The field groups of a properties editor, by name, with their copy and paste functions.

Alias for: `Map<String, { serialize:() -> Dynamic, pasteFn:(refresh:Bool, undo:hide.ui.UndoHistory, data:Dynamic) -> Void, fields:Array<PropsField> }>`
