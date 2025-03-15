# © pto8913 2025 Blender Foundation
# License: GPL-2.0-or-later

import bpy
import json

bl_info = {
    "name" : "pto8913",
    "author" : "pto8913",
    "description" : "Blender like CAD",
    "blender" : (4, 3, 1),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

from . import pto_ui
from Factory import pto_factory_utils

if "bpy" in locals():
    import importlib
    if "pto_ui" in locals():
        importlib.reload(pto_ui)

def register():
    bpy.types.Scene.StructureTypes = []
    bpy.types.Scene.SpecsAngle = {}
    bpy.types.Scene.SpecsChannel = {}
    bpy.types.Scene.SpecsFlatBar = {}
    bpy.types.Scene.SpecsIBeam = {}
    bpy.types.Scene.SpecsH = {}

    with open("Factory/specs.json", encoding="utf-8") as f:
        specs = json.load(f)

        factory_utils = pto_factory_utils.PTOFactoryUtils()
        
        for name in specs:
            bpy.types.Scene.StructureTypes.append({name, name, name})
            for spec in specs[name]:
                factory_utils.GetSpecListByType(name)[spec["name"]] = [spec["tooltip"], spec["desc"]]

    bpy.types.Scene.pto_factory_expanded = bpy.props.BoolProperty()

    pto_ui.register()

def unregister():
    pto_ui.unregister()