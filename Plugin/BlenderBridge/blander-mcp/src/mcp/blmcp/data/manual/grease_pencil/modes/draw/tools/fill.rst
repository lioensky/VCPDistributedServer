.. _tool-grease-pencil-draw-fill:

*********
Fill Tool
*********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Fill`

The Fill tool is used to automatically fill closed strokes areas.

The Fill tool uses any of the Grease Pencil *Fill* draw mode brushes.
Activating a brush from an asset shelf or brush selector will also activate this tool for convenience.


Tool Settings
=============

Brush Asset
-----------

The asset selector can be used to open a pop-up asset browser to select the active brush asset for the tool.

See :ref:`brush-management-utility-operators` for more information.


Brush Settings
--------------

You can also configure the brush main settings exposed on the Tool Settings for convenience.

.. _bpy.types.BrushGpencilSettings.fill_direction:

Direction :kbd:`Ctrl`
   The portion of area to fill.

   :Normal:
      Fills the area inside the shape under the cursor.
   :Inverted:
      When clicking outside the drawing, fills all shapes touching the area under the cursor.

.. _bpy.types.BrushGpencilSettings.fill_factor:

Precision
   Multiplier for fill boundary accuracy.
   Higher values are more accurate but slower.

.. _bpy.types.BrushGpencilSettings.dilate:

Dilate/Contract
   Size in pixels to expand or shrink the fill area from the strokes boundary.

Thickness
   The thickness radius of the boundary stroke in pixels.


Advanced
^^^^^^^^

.. _bpy.types.BrushGpencilSettings.fill_draw_mode:

Boundary
   Sets the type of fill boundary limits calculation to perform.

   :All:    Use the thickness of the strokes and the editing lines together.
   :Strokes: Use only the thickness of the strokes (ignore edit lines).
   :Edit Lines:   Use only the edit lines (ignore strokes).

   .. _bpy.types.BrushGpencilSettings.show_fill_boundary:

   Show Lines (eye icon)
      Toggle show auxiliary lines to see the fill boundary.

.. _bpy.types.BrushGpencilSettings.fill_layer_mode:

Layers
   Determines which :doc:`Layers </grease_pencil/properties/layers>` are used for boundary strokes.

   :Visible: Calculates boundaries based on all visible layers.
   :Active:  Calculates boundaries based on the active layer.
   :Layer Above: Calculates boundaries based on the layer above the active layer.
   :Layer Below: Calculates boundaries based on the layer below the active layer.
   :All Above: Calculates boundaries based on all layers above the active layer.
   :All Below: Calculates boundaries based on all layers below the active layer.

.. _bpy.types.BrushGpencilSettings.fill_simplify_level:

Simplify
   Number of simplify steps to apply to the boundary line.
   Higher values reduce the accuracy of the final filled area.

.. _bpy.types.BrushGpencilSettings.show_fill:
.. _bpy.types.BrushGpencilSettings.fill_threshold:

Ignore Transparent
   When enabled, strokes with transparency does not take into account on fill boundary calculations.

   The value slider controls the threshold to consider a material transparent.

.. _bpy.types.BrushGpencilSettings.use_fill_limit:

Limit to Viewport
   When enabled, fill only visible areas in the viewport.

.. _bpy.types.BrushGpencilSettings.use_auto_remove_fill_guides:

Auto-Remove Fill Guides
   When enabled, after creating a fill, automatically remove the fill guide strokes.

Gap Closure
"""""""""""

Gap closure lines are automatic temporarily lines that help to close gaps on the strokes.

.. _bpy.types.BrushGpencilSettings.extend_stroke_factor:

Size
   Control the Size of the line extension or the circumference to use to calculate the lines that will close the gaps.

.. _bpy.types.BrushGpencilSettings.fill_extend_mode:

Mode :kbd:`S`
   Sets the type of Gap closure method to use.

   :Radius: Uses the Radius of circumference of opened nearest points to calculate a line that close the gap.
   :Extend: Extends the opened strokes to close gaps.

.. _bpy.types.BrushGpencilSettings.show_fill_extend:

Visual Aids
   Toggle show closure lines helper.

.. _bpy.types.BrushGpencilSettings.use_collide_strokes:

Strokes Collision :kbd:`D`
   Check if extend lines collide with strokes, stopping the extension if a collision is detected.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Fill tool uses *Fill Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Filling Areas
-------------

Click :kbd:`LMB` in a closed stroke area. The tool will automatically calculate
the boundary and create a new closed stroke filled with the material selected.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_example-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_example-02.png
          :width: 200px

          Use the fill tool to leak materials on closed areas.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_example-03.png
          :width: 200px

          Final filled drawing.


Fill Guides
-----------

If you have a large gap in an area that you want fill,
you can add fill guides manually, a temporary auxiliary lines for closing open shapes.
To create a fill guide stroke use :kbd:`Alt-LMB` and draw a line to close the desired area.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_boundary-strokes-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_boundary-strokes-02.png
          :width: 200px

          Add fill guide to close open areas (red lines).

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_boundary-strokes-03.png
          :width: 200px

          Use the Fill tool to leak material on the new closed area.

When you are satisfied with the fill result you can delete the fill guide using
the *Clean Up* tool in the :doc:`Grease Pencil Menu </grease_pencil/modes/edit/grease_pencil_menu>` in Edit Mode.


Automatic Gap Closure
---------------------

A more automatic way to close gaps in an area that you want fill is using temporarily helper lines.
There are two method to use "Radius" or "Extend"

*Radius* use temporary auxiliary lines calculated from the radius of nearby open points to close open shapes.
Set the size more than zero to control the circle size over opened points
(the circle will disappear when the line close the gap).
Click over the area you want to be filled and change the length of the strokes using
:kbd:`PageUp` :kbd:`PageDown` or :kbd:`Wheel`.
When you are satisfied with the length and you are sure the temporarily strokes cross each other,
click again to fill the area.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_radius-02.png
          :width: 200px

          Use Radius mode to close open areas (Red circles and cyan lines).

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_radius-03.png
          :width: 200px

          Use Fill Tool to leak material on the new closed area.

*Extend* use temporary auxiliary lines extending the actual strokes ends for closing open shapes.
Set the size more than zero to use the extended lines, click over the area you want to be filled
and change the length of the strokes using :kbd:`PageUp`/:kbd:`PageDown`, :kbd:`Wheel` or a pen's :kbd:`MMB`.
When you are satisfied with the length and you are sure the temporarily strokes cross each other,
click again to fill the area.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-02.png
          :width: 200px

          Use Extend mode to close open areas (cyan lines).

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-03.png
          :width: 200px

          Use Fill Tool to leak material on the new closed area.


.. Switch to Draw Tool
.. -------------------

.. Use :kbd:`Ctrl-LMB` to change temporary to the active draw tool.
.. For example to manually cover small areas difficult to reach for the Fill tool.
.. See :doc:`Draw Tool </grease_pencil/modes/draw/tools/draw>` for more information.
