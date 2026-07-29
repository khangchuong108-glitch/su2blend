import bpy

from .import_now import SU2BLEND_OT_import_now
from .clean_scene import SU2BLEND_OT_clean_scene
from .connect_bridge import SU2BLEND_OT_connect_bridge
from .reload_bridge import SU2BLEND_OT_reload_bridge
from .import_bridge import SU2BLEND_OT_import_bridge


CLASSES = (
    SU2BLEND_OT_import_now,
    SU2BLEND_OT_clean_scene,
    SU2BLEND_OT_connect_bridge,
    SU2BLEND_OT_reload_bridge,
    SU2BLEND_OT_import_bridge,
)


def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)