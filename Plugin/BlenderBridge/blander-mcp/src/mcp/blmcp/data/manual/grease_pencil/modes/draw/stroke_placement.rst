.. _bpy.types.ToolSettings.gpencil_stroke_placement_view3d:

****************
Stroke Placement
****************

.. reference::

   :Mode:      Draw Mode
   :Header:    :menuselection:`Stroke Placement`

.. figure:: /images/grease-pencil_modes_draw_stroke-placement_selector.png
   :align: right

   Stroke Placement pop-over.

The Stroke Placement selector helps to select the location in which strokes are drawn.

.. note::

   The Stroke Placement selection only affects new strokes and does not affect the existing ones.

:Origin: Strokes are placed at Grease Pencil object origin.
:3D Cursor: Strokes are placed at 3D cursor.
:Surface: Strokes will stick on mesh surfaces.

   .. _bpy.types.ToolSettings.gpencil_surface_offset:

   Offset
      Distance from the mesh surface to place the new strokes.

   .. _bpy.types.ToolSettings.use_gpencil_project_only_selected:

   Project Onto Selected
      Only project the strokes onto selected objects.

:Stroke:
   Strokes will stick on other strokes.

   .. _bpy.types.ToolSettings.gpencil_stroke_snap_mode:

   Target
      :All Points:
         All the points of the new stroke sticks to other strokes.
      :End Points:
         Only the start and end points of the new stroke sticks to other strokes.
      :First Point:
         Only the start point of the new stroke sticks to other strokes.

.. list-table:: Stroke using different Stroke Placements.

   * - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_origin.png
          :width: 200px

          Origin.

     - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_3D-cursor.png
          :width: 200px

          3D Cursor.

     - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_surface.png
          :width: 200px

          Surface.

     - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_stroke.png
          :width: 200px

          Stroke.
