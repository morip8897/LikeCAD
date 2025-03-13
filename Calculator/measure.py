# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy

from .. import pto_utils

class PTO_Measure:
    def makeSpec(self, context):
        parent_obj = context.active_object

        bpy.ops.object.mode_set(mode="OBJECT")
        parent_obj.select_set(False)
        parent_obj.select_set(True)
        bpy.ops.object.mode_set(mode="EDIT")

        prev_vert_co = None
        result_distances = set() 
        for vert in parent_obj.data.vertices:
            if vert.select == True:
                if prev_vert_co == None:
                    prev_vert_co = vert.co
                else:
                    result_distances.append(
                        round(pto_utils.PTO_Utils.distanceTo(prev_vert_co, vert.co))
                    )
                    prev_vert_co = vert.co
        
        bpy.ops.object.mode_set(mode="OBJECT")
        current_mode = parent_obj.mode

        bpy.ops.object.text_add(
            radius=bpy.types.Scene.MeasureSize, 
            enter_editmode=False, 
            align='WORLD', 
            location=(0, 0, 0), 
            scale=(1, 1, 1)
        )
        text_obj = context.active_object

        text_obj.select = True
        parent_obj.select = True

        bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

