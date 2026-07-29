import bpy


class SU2BLEND_OT_reload_bridge(bpy.types.Operator):
    """Reload Bridge"""

    bl_idname = "su2blend.reload_bridge"
    bl_label = "Reload Bridge"

    def execute(self, context):

        self.report(
            {'INFO'},
            "Reload complete."
        )

        return {'FINISHED'}