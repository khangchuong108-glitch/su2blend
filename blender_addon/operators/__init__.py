import bpy

from .import_now import SU2BLEND_OT_import_now
from .clean_scene import SU2BLEND_OT_clean_scene


CLASSES = (
    SU2BLEND_OT_import_now,
    SU2BLEND_OT_clean_scene,
)


def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)