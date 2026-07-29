import bpy


class SU2BLEND_OT_import_bridge(bpy.types.Operator):
    """Import Bridge"""

    bl_idname = "su2blend.import_bridge"
    bl_label = "Import Bridge"

    def execute(self, context):

        self.report(
            {'INFO'},
            "Bridge importer coming soon."
        )

        return {'FINISHED'}