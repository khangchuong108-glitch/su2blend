import bpy

from .panel import SU2BLEND_PT_main_panel


CLASSES = (
    SU2BLEND_PT_main_panel,
)


def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)