.. _tool-grease-pencil-draw-curve:

**********
Curve Tool
**********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Curve`

The Curve tool create complex Bézier style curves using any of the *Draw* type brushes..


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
      When enabled, the stroke use a curve profile to control the thickness along the curve.

.. list-table:: Different thickness profile samples.

   * - .. figure:: /images/grease-pencil_modes_draw_tools_curve_thickness-profile-01.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tools_curve_thickness-profile-02.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tools_curve_thickness-profile-03.png
          :width: 200px


Brush Asset
-----------

Picks the brush asset used by the tool.

See :doc:`/grease_pencil/modes/draw/tool_settings/brushes` for more information.

See :doc:`/grease_pencil/modes/draw/brushes/draw` for a detailed list of all draw brushes and their options.


Brush Settings
--------------

Parameters to control to look of the stroke.

See :doc:`/grease_pencil/modes/draw/brushes/draw` for details.


Color
-----

Settings to determine the color of strokes.

See :doc:`/grease_pencil/modes/draw/tool_settings/color`


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Curve tool uses *Draw Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Creating Curves
---------------

#. Click (:kbd:`LMB` or the :kbd:`Pen` tip) and drag the start point.
#. Release on the desired end point.
#. After releasing you can tweak the curve using two cyan Bézier like manipulators.
#. Then confirm (:kbd:`Return`/:kbd:`MMB`) or cancel (:kbd:`Esc`/:kbd:`RMB`).

While dragging you can hold :kbd:`Shift` to use only one manipulator to tweak the curve (like the Arc tool),
use :kbd:`Alt` to create the arc from a center point.

:kbd:`NumpadPlus` and :kbd:`NumpadMinus` or using the mouse :kbd:`Wheel` will increase
or decrease the amount of points in the final curve.

:kbd:`F` will adjust the line thickness and :kbd:`Shift-F` will adjust the opacity of the strokes.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_curve_example-01.png
          :width: 200px

          click and dragging the start point.

     - .. figure:: /images/grease-pencil_modes_draw_tools_curve_example-02.png
          :width: 200px

          Tweaking curve with the manipulators.

     - .. figure:: /images/grease-pencil_modes_draw_tools_curve_example-03.png
          :width: 200px

          The curve after confirming.


Extruding
---------

Before confirming you can use :kbd:`E` to extrude the end point of the curve
to generate multiple connected curves.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_curve_extrude-01.png
          :width: 200px

          End point extruding.

     - .. figure:: /images/grease-pencil_modes_draw_tools_curve_extrude-02.png
          :width: 200px

          Tweaking the last curve with the manipulators.

     - .. figure:: /images/grease-pencil_modes_draw_tools_curve_extrude-03.png
          :width: 200px

          The connected curves after confirming.
