bl_info = {
    "name": "SketchBridge",
    "author": "Chuong + OpenAI",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D",
    "description": "SketchUp Bridge",
    "category": "Import-Export",
}

import bpy

from .logger import log


class SKETCHBRIDGE_OT_Test(
    bpy.types.Operator
):

    bl_idname = "sketchbridge.test"

    bl_label = "Test Bridge"

    def execute(
        self,
        context
    ):

        log("Bridge Loaded Successfully")

        self.report(
            {'INFO'},
            "SketchBridge OK"
        )

        return {'FINISHED'}


classes = (
    SKETCHBRIDGE_OT_Test,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    log("Addon Registered")


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    log("Addon Unregistered")