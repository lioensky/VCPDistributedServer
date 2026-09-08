
***********
UV Overlays
***********

.. figure:: /images/editors_uv_overlays.png
   :align: right

   The Overlays pop-over.

In the header, there is a button to turn off all overlays for the UV Editor.
This option also toggles the visibility of :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
tile information.

The drop-down button opens a pop-over with more detailed settings.
The following categories are available:


Guides
======

.. _bpy.types.SpaceImageOverlay.show_grid_background:

Grid
   Show the grid.

.. _bpy.types.SpaceUVEditor.show_grid_over_image:

Over Image
   Show the grid on top of the image rather than behind it.

.. _bpy.types.SpaceUVEditor.grid_shape_source:

Grid Shape Source
   How the row and column counts are determined.

   :Dynamic: The grid starts at 8×8 cells that are automatically subdivided further as you zoom in.
   :Fixed: The row and column counts are fixed and can be configured manually.
   :Pixel: Each grid cell matches one image pixel.

.. _bpy.types.SpaceUVEditor.custom_grid_subdivisions:

Fixed Subdivisions X, Y
   Number of columns/rows in the grid.

.. _bpy.types.SpaceUVEditor.tile_grid_shape:

Tiles X, Y
   The number of :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
   tile grids to display in each cardinal direction.


UV Editing
==========

.. _bpy.types.SpaceUVEditor.display_stretch_type:
.. _bpy.types.SpaceUVEditor.show_stretch:

Display Stretch
   Show how much of a shape difference there is between UV space and 3D space.
   Blue means low distortion, red means high.
   You can choose whether to display the distortion based on *Angle* or *Area*.


Geometry
========

.. _bpy.types.SpaceUVEditor.show_uv:

Display UVs
   Show the active UV map as an overlay in the UV Editor.

   .. _bpy.types.SpaceUVEditor.uv_face_opacity:

   Faces
      Adjust the opacity of face fill colors in UV overlays.

   .. _bpy.types.SpaceUVEditor.uv_edge_opacity:

   Edges
      Adjust the opacity of edge colors in UV overlays.

.. _bpy.types.SpaceUVEditor.uv_opacity:

UV Opacity :guilabel:`Edit Mode`
   Opacity of edges and faces.

.. _bpy.types.SpaceUVEditor.edge_display_type:

Display As :guilabel:`Edit Mode`
   Control how edges are shown.

   :Outline: Display edges in gray with a black outline.
   :Dash: Display edges as dashed black-gray lines.
   :Black: Display edges in black.
   :White: Display edges in white.

.. _bpy.types.SpaceUVEditor.show_modified_edges:

Modified Edges :guilabel:`Edit Mode`
   Additionally show the edges as they look after applying modifiers (in gray).

.. _bpy.types.SpaceUVEditor.show_faces:

Faces :guilabel:`Edit Mode`
   Display faces over the image.


Image
=====

Show Metadata
   Display metadata about the selected Render Result. See the Output tab's
   :doc:`/render/output/properties/metadata` panel to change what metadata to include.
