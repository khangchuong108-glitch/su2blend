import bpy
from ..utils.bridge_manager import bridge


class SU2BLEND_OT_connect_bridge(bpy.types.Operator):
    """Connect Bridge"""

    bl_idname = "su2blend.connect_bridge"
    bl_label = "Connect Bridge"

    def execute(self, context):

        bridge.create()

        self.report(
            {'INFO'},
            "Bridge folder is ready."
        )

        return {'FINISHED'}