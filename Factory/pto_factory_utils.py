# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy

class PTOFactoryUtils:
    def GetSpec(self, context, StructureType):

        context.scene.

    def GetSpecByType(self, context, StructureType):
        structType = context.scene.StructureType
        if structType == "Angle":
            return context.scene.SpecsAngle
        elif structType == "Channel":
            return context.scene.SpecsChannel
        elif structType == "FlatBar":
            return context.scene.SpecsFlatBar
        elif structType == "IBeam":
            return context.scene.SpecsIBeam
        elif structType == "H":
            return context.scene.SpecsH
    
    def GetSpecByName(self, context, name):