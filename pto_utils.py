# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy
import math

class PTO_Utils:
    def __init__(self):
        self.object = None

    def getChildren(self, context):
        self.object = context.object

        if not self.object:
            print("""
                Fail get children.
                Please select any object.
            """)
            return None

        current_mode = self.object.mode

        if current_mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")

        return self.object.children_recursive
    
    def selectChildren(self, context):
        children = self.getChildren(context)

        if children == None:
            return False

        for child in children:
            child.select = True

        return True
    
    def getLength(self, context):
        targets = bpy.context.selected_objects

    def distanceTo(self, x, y):
        return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2)
