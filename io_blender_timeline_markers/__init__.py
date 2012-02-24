# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "Blender Timeline Marker Format (.bmf)",
    "author": "Troy James Sobotka",
    "version": (1,0,1),
    "blender": (2, 6, 2),
    "location": "Timeline Marker > Marker Import / Export",
    "description": "Import/Export Blender Timeline Markers",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}


# To support reload properly, try to access a package var,
# if it's there, reload everything
if "bpy" in locals():
    import imp
    if "import_timeline_markers" in locals():
        imp.reload(import_timeline_markers)
    if "export_timeline_markers" in locals():
        imp.reload(export_timeline_markers)


import bpy
from bpy.types import Operator, Menu
from bpy_extras.io_utils import ImportHelper, ExportHelper
from bpy.props import (StringProperty,
                       BoolProperty,
                       EnumProperty,
                       FloatProperty)

class ImportMarkers(Operator, ImportHelper):
    '''Import Blender timeline markers from file. '''
    bl_idname = "marker.import"
    bl_label = "Import Blender timeline markers from file"

    filename_ext = ".bmf"

    filter_glob = StringProperty(default="*.bmf", options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from . import import_timeline_markers
        return import_timeline_markers.read_markers(context,
                                          self.filepath)

class ExportMarkers(Operator, ExportHelper):
    '''Export Blender timeline markers to file. '''
    bl_idname = "marker.export"
    bl_label = "Export Blender timeline markers to file"

    filename_ext = ".bmf"
    filter_glob = StringProperty(default="*.bmf", options={'HIDDEN'})

    selected_only = BoolProperty(
            name="Selected only",
            description="Export selected markers only",
            default=False)

    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        from . import export_timeline_markers
        return export_timeline_markers.save_markers(context,
                                          self.filepath,
                                          self.selected_only)

class MT_ImportExportMarkers(Menu):
    bl_label = "Marker Import / Export"

    def draw(self, context):
        self.layout.operator(ImportMarkers.bl_idname, text="Import Blender BMF (.bmf)")
        self.layout.operator(ExportMarkers.bl_idname, text="Export Blender BMF (.bmf)")

def menu_importexport(self, context):
    self.layout.menu("MT_ImportExportMarkers")

def register():
    bpy.utils.register_class(ImportMarkers)
    bpy.utils.register_class(ExportMarkers)
    bpy.utils.register_class(MT_ImportExportMarkers)
    bpy.types.TIME_MT_marker.append(menu_importexport)

def unregister():
    bpy.utils.unregister_class(ImportMarkers)
    bpy.utils.unregister_class(ExportMarkers)
    bpy.utils.unregister_class(MT_ImportExportMarkers)
    bpy.types.TIME_MT_marker.remove(menu_importexport)

if __name__ == "__main__":
    register()
