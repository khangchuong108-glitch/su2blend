import bpy

from ..constants import PANEL_CATEGORY


class SU2BLEND_PT_main_panel(bpy.types.Panel):
    bl_label = "SU2Blend"
    bl_idname = "SU2BLEND_PT_main_panel"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = PANEL_CATEGORY

    def draw(self, context):

        layout = self.layout

        box = layout.box()

        # Title
        box.label(text="SketchUp Bridge", icon='HOME')

        box.separator()

        # Bridge Status
        box.label(
            text="Bridge Status : Disconnected",
            icon='ERROR'
        )

        # Bridge Folder
        box.label(
            text="Folder : Not Selected",
            icon='FILE_FOLDER'
        )

        box.separator()

        # Connect
        box.operator(
            "su2blend.connect_bridge",
            text="Connect",
            icon='LINKED'
        )

        box.separator()

        # Import
        box.operator(
            "su2blend.import_bridge",
            text="Import",
            icon='IMPORT'
        )

        # Reload
        box.operator(
            "su2blend.reload_bridge",
            text="Reload",
            icon='FILE_REFRESH'
        )

        # Clean
        box.operator(
            "su2blend.clean_scene",
            text="Clean",
            icon='TRASH'
        )