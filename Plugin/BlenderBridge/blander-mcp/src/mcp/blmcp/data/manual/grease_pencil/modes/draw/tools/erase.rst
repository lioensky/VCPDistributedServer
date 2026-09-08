.. _tool-grease-pencil-draw-erase:

**********
Erase Tool
**********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Brush`

The Erase tool erases already drawn strokes.

The Erase tool uses any of the Grease Pencil *Erase* draw mode brushes.
Activating a brush from an asset shelf or brush selector will also activate this tool for convenience.


Tool Settings
=============

Brush Asset
-----------

The asset selector can be used to open a pop-up asset browser to select the active brush asset for the tool.

See :ref:`brush-management-utility-operators` for more information.


Brush Settings
--------------

Radius
   The radius of the brush in pixels.

   :kbd:`F` allows you to change the brush size interactively by dragging the pointer or
   by typing a number then confirm.

   :bl-icon:`stylus_pressure` (Size Pressure)
      Adjusts the radius based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.

Strength
   Control how much will affect the eraser has on the stroke transparency (alpha).

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the pointer and then :kbd:`LMB`.
   You can also enter the size numerically.

   :bl-icon:`stylus_pressure` (Strength Pressure)
      Adjusts the strength based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.

.. _bpy.types.BrushGpencilSettings.eraser_mode:

Mode
   Determines how the erase tool behaves.

   :Dissolve:
      To simulate a raster type eraser, this eraser type
      affects the strength and thickness of the strokes before actually delete a point.
   :Point: Delete one point at a time.
   :Stroke: Delete an entire stroke.


Cursor
^^^^^^

The cursor can be disabled by toggling the checkbox in the *Cursor* pop-over menu.


Usage
=====

Selecting a Brush
-----------------

In the Tool Settings select the brush to use with the tool.
The Erase tool uses :ref:`Erase Brush <grease_pencil-draw-brushes-erase>` types (soft, point and stroke).


Dissolve Erasing
----------------

- Select an erase brush of type Soft/Hard.
- Adjust brush settings.
- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-02.png
          :width: 200px

          The eraser affect the transparency of the strokes.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-03.png
          :width: 200px

          Final result.


Point Erasing
-------------

- Select an erase brush of type Point.
- Adjust brush settings.
- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-02.png
          :width: 200px

          The eraser delete one point at a time.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-03.png
          :width: 200px

          Final result.


Stroke Erasing
--------------

- Select an erase brush of type Stroke.
- Adjust brush settings.
- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-02.png
          :width: 200px

          The eraser delete one stroke at a time.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-03.png
          :width: 200px

          Final result.
