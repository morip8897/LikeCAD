# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy

class PTOFactoryUtils:
    def AddNewObject(self, context, name):
        new_obj = bpy.data.objects.new(name, None)
        context.scene.objects.link(new_obj)
        return new_obj

    def GetSpecListByType(self, context, StructureType) -> dict:
        if StructureType == "Angle":
            return context.scene.SpecsAngle
        elif StructureType == "Channel":
            return context.scene.SpecsChannel
        elif StructureType == "FlatBar":
            return context.scene.SpecsFlatBar
        elif StructureType == "IBeam":
            return context.scene.SpecsIBeam
        elif StructureType == "H":
            return context.scene.SpecsH
        
    # Get active structure name
    def GetActiveStructName(self, context, StructureType):
        if StructureType == "Angle":
            return context.scene.StructAngle
        elif StructureType == "Channel":
            return context.scene.StructChannel
        elif StructureType == "FlatBar":
            return context.scene.StructFlatBar
        elif StructureType == "IBeam":
            return context.scene.StructIBeam
        elif StructureType == "H":
            return context.scene.StructH

    def GetSpec(self, context):
        structure_type = context.scene.StructureType
        spec_dict = self.GetSpecListByType(context, structure_type)
        active_struct_name = self.GetActiveStructName(context, structure_type)
        for name, descs in spec_dict.items():
            if name == active_struct_name:
                return [name, *descs]
        
        print("""
            Critical Error.
            spec is not exist.  
            Please report to pto8913project@gmail.com
        """)
        return None
    
    def GetDimension(self, spec):
        return self.GetSpecName(spec).split("_")[1]
    
    def GetSpecName(self, spec):
        return spec[0]
        
    def GetSpecTooltip(self, spec):
        return spec[1]

    def GetSpecDesc(self, spec):
        return spec[2]