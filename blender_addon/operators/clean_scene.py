import bpy

from ..logger import log


class SU2BLEND_OT_clean_scene(bpy.types.Operator):
    """Delete imported Bridge collection"""

    bl_idname = "su2blend.clean_scene"
    bl_label = "Clean Scene"

    def execute(self, context):

        log.info("Clean Scene button pressed")

        self.report(
            {'INFO'},
            "Clean Scene chưa được cài."
        )

        return {'FINISHED'}