
************
Stanford PLY
************

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Stanford (.ply)`

Use the operator to import ASCII or binary PLY-files, you can select multiple files at once.
For exporting, you can choose to enable or disable the modifiers during the export
and you can choose which data you want to export (UV textures, Color Attributes, ...).


.. _bpy.ops.wm.ply_import:

Import
======

General
-------

Scale
   Value by which to scale the imported objects in relation to the world's origin.
Scene Unit
   Apply current scene's unit (as defined by unit scale) to imported data.
Forward Axis, Up Axis
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Options
-------

Merge Vertices
   Attempts to combine co-located vertices where possible.
Import Vertex Colors
   The color space that the color data in the ply-file was saved in.

   :None: Does not import vertex color data.
   :sRGB: Vertex colors in the file are in sRGB :term:`Color Space`
   :Linear: Vertex colors in the file are in Linear :term:`Color Space`


.. _bpy.ops.wm.ply_export:

Export
======

General
-------

Format: ASCII
   Formats the file using the simple a ASCII format.
   This option might be helpful if the program that
   will later import the file does not support the binary file format.
Include: Selected Only
   Only selected objects are exported.
   Instanced objects, for example collections that are instanced in the scene,
   are considered 'selected' when their instancer is selected.
Scale
   Value by which to scale the exported objects in relation to the world's origin.
Forward Axis, Up Axis
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry
--------

UV Coordinates
   Write out the active UV layers coordinates from Blender.
Vertex Normals
   Write out Blender's face and vertex normals (depending on the faces smooth setting).

   Mostly this isn't needed since most applications will calculate their
   own normals but to match Blender's normal map textures you will need to write these too.
Vertex Colors
   The color space that the color data in the ply-file was saved in.

   :None: Does not import vertex color data.
   :sRGB: Vertex colors in the file are in sRGB :term:`Color Space`
   :Linear: Vertex colors in the file are in Linear :term:`Color Space`
Triangulated Mesh
   All :term:`N-gons <N-gon>` with four or more vertices will be triangulated.
   Meshes in the scene will not be affected.
   Behaves like :doc:`/modeling/modifiers/generate/triangulate` with the following settings:

   - N-gon Method: "Beauty"
   - Quad-method: "Shortest Diagonal"
   - Min vertices: 4
Apply Modifiers
   Export objects using the evaluated mesh, meaning the resulting mesh after all
   :doc:`Modifiers </modeling/modifiers/index>` have been calculated.
