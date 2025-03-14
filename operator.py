# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy

from LikeCAD.Factory import pto_factory

class PTO_OT_CreateStructure(bpy.types.Operator):
    bl_idname = "object.pto_create_struct"
    bl_label = "Create Structure"
    bl_description = "create structure from StructureType"

    def execute(self, context):
        factory = pto_factory.PTOFactory()
        return factory.CreateStructure(context)
        