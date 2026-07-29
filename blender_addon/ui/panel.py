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

        box.label(text="SketchUp Bridge")

        box.operator(
            "su2blend.import_now",
            icon='IMPORT'
        )

        box.operator(
            "su2blend.clean_scene",
            icon='TRASH'
        )