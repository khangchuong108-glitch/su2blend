bl_info = {
    "name": "SU2Blend",
    "author": "Chuong + OpenAI",
    "version": (0, 1, 0),
    "blender": (5, 2, 0),
    "location": "View3D > Sidebar",
    "description": "SketchUp to Blender Bridge",
    "category": "Import-Export",
}

from .logger import log
from .operators import register as register_operators
from .operators import unregister as unregister_operators
from .ui import register as register_ui
from .ui import unregister as unregister_ui


def register():

    register_operators()
    register_ui()

    log.info("SU2Blend Loaded")


def unregister():

    unregister_ui()
    unregister_operators()

    log.info("SU2Blend Unloaded")