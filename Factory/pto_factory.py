# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy

from . import pto_factory_utils

class PTOFactory:
    def __init__(self):
        s = 0
        
    def CreateStructure(self, context):
        obj = context.active_object
        scene = context.scene

        factory_utils = pto_factory_utils.PTOFactoryUtils()
        spec = factory_utils.GetSpec(context)
        
        dimension = factory_utils.GetDimension(spec)
        num_of_dimension = len(dimension)

        bpy.ops.action.select_all(action="DESELECT'")
        if num_of_dimension == 3:


    def CreateAngle(self, context, spec):
        factory_utils = pto_factory_utils.PTOFactoryUtils()
        factory_utils.AddNewObject(context, factory_utils.GetSpecName())
        
        bpy.ops.object.mode_set(mode="OBJECT")
        parent_obj.select_set(False)
        parent_obj.select_set(True)
        bpy.ops.object.mode_set(mode="EDIT")
