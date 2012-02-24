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

""" This script imports timeline markers from file."""

def read_markers(context, filepath): # , z_up, rot_ord, sensor_width, sensor_height):

    scene = context.scene
    markers = scene.timeline_markers

    # read the file
    filehandle = open(filepath, 'r')

    currentline = filehandle.readline().rstrip('\r\n')
    
    # iterate through the files lines
    while currentline:
        marker = markers.new(currentline)
        marker.frame = int(filehandle.readline().rstrip('\r\n'))
        currentline = filehandle.readline().rstrip('\r\n')
        
    filehandle.close()

    return {"FINISHED"}
