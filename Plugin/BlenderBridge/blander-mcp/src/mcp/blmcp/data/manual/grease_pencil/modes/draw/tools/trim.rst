.. _tool-grease-pencil-draw-trim:

*********
Trim Tool
*********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Trim`

The Trim tool delete points in between intersecting strokes.


Tool Settings
=============

Flat Caps
   Mark newly created :ref:`End Caps <bpy.ops.grease_pencil.caps_set>` as *Flat*.

.. _bpy.types.GPencilSculptSettings.intersection_threshold:

Threshold
   Determine the threshold for stroke intersections.


Usage
=====

Draw a dotted line around the strokes you want to trim.
After releasing the mouse button all the points on the selected strokes
will be deleted until another intersecting stroke is found.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_cutter_example-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_cutter_example-02.png
          :width: 200px

          Lasso Selecting the strokes to be trimmed.

     - .. figure:: /images/grease-pencil_modes_draw_tools_cutter_example-03.png
          :width: 200px

          Final result.
