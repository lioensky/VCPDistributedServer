.. _bpy.types.GPencilSculptSettings.lock_axis:

*************
Drawing Plane
*************

.. reference::

   :Mode:      Draw Mode and Sculpt Mode
   :Header:    :menuselection:`Drawing Plane`

.. figure:: /images/grease-pencil_modes_draw_drawing-planes_selector.png
   :align: right

   Drawing Planes pop-over.

The Drawing Planes selector helps to select the plane in which strokes are drawn.

To see which plane you are using when drawing strokes,
you can enable *Canvas* in :ref:`Viewport Overlays <3dview-overlay-grease-pencil>`.
See :doc:`Viewport Display </interface/controls/templates/curve>` to know more about Canvas settings.

.. note::

   The Drawing Plane only affects new strokes and does not affect existing strokes.

:View: Strokes are drawn with the current 3D Viewport orientation.
:Front (X-Z): Strokes are drawn on the plane determined by the XZ axes (front view).
:Side (Y-Z): Strokes are drawn on the plane determined by the YZ axes (side view).
:Top (X-Y): Strokes are drawn on the plane determined by the XY axes (top view).
:Cursor: Strokes are drawn with the current 3D cursor orientation.

.. list-table:: Stroke using different Drawing Planes with Canvas overlay activated.

   * - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_front.png
          :width: 200px

          Front.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_side.png
          :width: 200px

          Side.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_top.png
          :width: 200px

          Top.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_view.png
          :width: 200px

          View.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_cursor.png
          :width: 200px

          Cursor.
