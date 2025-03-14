# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy
from bpy.props import (
    FloatProperty, IntProperty, EnumProperty
)

from . import (
    ui_utils
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

    # ------------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------------
    bpy.types.Scene.StructureType = EnumProperty(
        name = "StructureType",
        items = StructureTypes,
        description = "Structure type for create Object."
    )

    bpy.types.Scene.AngleSpec = EnumProperty(
        name = "AngleSpec",
        items = SpecsAngle,
        description = "Structure type for create Object."
    )
    bpy.types.Scene.ChannelSpec = EnumProperty(
        name = "ChannelSpec",
        items = SpecsChannel,
        description = "Structure type for create Object."
    )
    bpy.types.Scene.FlatBarSpec = EnumProperty(
        name = "FlatBarSpec",
        items = SpecsFlatBar,
        description = "Structure type for create Object."
    )
    bpy.types.Scene.IBeamSpec = EnumProperty(
        name = "IBeamSpec",
        items = SpecsIBeam,
        description = "Structure type for create Object."
    )
    bpy.types.Scene.HSpec = EnumProperty(
        name = "HSpec",
        items = SpecsH,
        description = "Structure type for create Object."
    )

    bpy.types.Scene.StructureLength = FloatProperty(
        name = "Structure Length",
        default = 50
    )

    def draw(self, context):
        obj = context.active_object
        scene = context.scene

        layout = self.layout

        ui_utils.LayoutSection(layout, "pto_factory_expanded")
        if scene.pto_factory_expanded:
            FactoryList = layout.column()
            FactoryList.prop(scene, "StructureType")
            if scene.StructureType == "Angle":
                FactoryList.prop(scene, "AngleSpec")
            elif scene.StructureType == "Channel":
                FactoryList.prop(scene, "ChannelSpec")
            elif scene.StructureType == "FlatBar":
                FactoryList.prop(scene, "FlatBarSpec")
            elif scene.StructureType == "IBeam":
                FactoryList.prop(scene, "IBeamSpec")
            elif scene.StructureType == "H":
                FactoryList.prop(scene, "HSpec")
            FactoryList.operator("")