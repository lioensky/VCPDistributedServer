.. _tool-grease-pencil-draw-box:

********
Box Tool
********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Box`

The Box tool create rectangular shapes.


Tool Settings
=============

You can configure the brush main settings exposed on the Tool Settings for convenience.
For the draw brushes configuration and settings see:
:doc:`Draw Brush </grease_pencil/modes/draw/brushes/draw>`.

Subdivisions
   The number of stroke points between each stroke edge.

Thickness Profile
   Use a :doc:`curve widget </interface/controls/templates/curve>` to define the stroke thickness
   from the start (left) to end (right) of the stroke.

   Use Curve
      When enabled, the stroke use a curve profile to control the thickness along the line.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Box tool uses *Draw Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Creating Boxes
--------------

#. Click (:kbd:`LMB` or the :kbd:`Pen` tip) and drag the start point.
#. Release on the desired end point.
#. After releasing you can move the start and end point by clicking and dragging on the yellow manipulators.
#. Then confirm (:kbd:`Return`/:kbd:`MMB`) or cancel (:kbd:`Esc`/:kbd:`RMB`).

While dragging you can use :kbd:`Shift` to make a perfect square
or use :kbd:`Alt` to create the box from a center point.

:kbd:`NumpadPlus` and :kbd:`NumpadMinus` or using the mouse :kbd:`Wheel`
will increase or decrease the amount of points in the final box.

:kbd:`F` will adjust the line thickness and :kbd:`Shift-F` will adjust the opacity of the strokes.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_box_example-01.png
          :width: 200px

          click and dragging the start point.

     - .. figure:: /images/grease-pencil_modes_draw_tools_box_example-02.png
          :width: 200px

          Moving start and end points with manipulators.

     - .. figure:: /images/grease-pencil_modes_draw_tools_box_example-03.png
          :width: 200px

          The box after confirming.
