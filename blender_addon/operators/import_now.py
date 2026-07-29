import bpy

from ..logger import log


class SU2BLEND_OT_import_now(bpy.types.Operator):
    """Import model from Bridge folder"""

    bl_idname = "su2blend.import_now"
    bl_label = "Import Now"
    bl_options = {'REGISTER'}

    def execute(self, context):

        log.info("Import button pressed")

        self.report(
            {'INFO'},
            "Import engine chưa được cài."
        )

        return {'FINISHED'}