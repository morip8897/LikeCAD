# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy
from bpy.props import (
    FloatProperty, IntProperty
)

class PTO_PT_Object(bpy.types.Panel):
    bl_idname = "PTO_PT_Object"
    bl_label = "Object"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pto"

    bpy.types.Scene.MeasureSize = IntProperty(
        name = "MeasureSize",
        min = 1,
        soft_min = 1,
        default = 15,
    )