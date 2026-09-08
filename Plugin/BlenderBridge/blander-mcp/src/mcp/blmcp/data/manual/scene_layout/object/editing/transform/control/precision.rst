
*********
Precision
*********

.. reference::

   :Mode:      Object and Edit Modes
   :Shortcut:  :kbd:`Ctrl` and/or :kbd:`Shift`

Holding :kbd:`Ctrl` during a transform operation (such as move, rotate or scale)
will toggle :doc:`Transform Snapping </editors/3dview/controls/snapping>`.
When using :ref:`Increment Snap <bpy.types.ToolSettings.snap_elements_base>`
this allows the transformation to be performed in discrete amounts.

Holding :kbd:`Shift` during a transform operation will transform
the object at 1/10th the speed, allowing much finer control.

The magnitude of the transformation can be viewed in the 3D Viewport header.
Releasing :kbd:`Ctrl` or :kbd:`Shift` during the transformation will cause
the movement to revert back to its normal mode of operation.

.. note::

   The snapping behaviors described on this page **only** apply
   when :ref:`Increment Snap <bpy.types.ToolSettings.snap_elements_base>` is selected.

.. tip::

   It is possible to enable both snapping and precision mode,
   simply hold :kbd:`Ctrl` and :kbd:`Shift`. This has the following effects:

   Move
      Changes in 0.1 unit increments, regardless of zoom level.
   Rotation
      Changes in 1 unit increments.
   Scale
      Changes in 0.01 unit increments.


Usage
=====

With Hotkeys
------------

Press :kbd:`G`, :kbd:`R` or :kbd:`S` and then hold either :kbd:`Ctrl`,
:kbd:`Shift` or :kbd:`Shift-Ctrl`.


With the Transform Gizmo
------------------------

Select the gizmo handle then while moving the mouse hold :kbd:`Ctrl`, :kbd:`Shift` or :kbd:`Shift-Ctrl`
to activate precision control or snapping.

.. seealso::

   :doc:`Read more about the Transform Gizmo </editors/3dview/display/gizmo>`.

.. tip:: Combining with Other Controls

   All of the precision controls detailed on the page can be combined with
   the :doc:`Axis Locking </scene_layout/object/editing/transform/control/axis_locking>` controls and
   used with the different :doc:`Pivot Points </editors/3dview/controls/pivot_point/index>`.


Snapping
========

Move
----

.. figure:: /images/scene-layout_object_editing_transform_control_precision_units.png
   :align: right
   :width: 200px
   :figwidth: 200px

   One unit (default zoom level).

Snapping while moving objects changes the object location in 1 unit increments.
While in an :doc:`aligned view </editors/3dview/navigate/align>`,
The increment amount is changed based on the :ref:`zoom level <bpy.ops.view3d.zoom>`.
For example, at a base zoom level objects are moved in increments of 1 unit (i.e. between the two light gray lines).
Zooming in enough to see the next set of gray lines will snap in increments of 1/10 of a unit.
Zooming in further until will snap in increments of 1/100 of a unit and so on until the zoom limit is reached.
Zooming out will have the opposite effect and
cause movement to happen by increments of 10, 100 units, etc.

.. container:: lead

   .. clear


Rotation
--------

Holding :kbd:`Ctrl` will cause rotations of 5 degrees.


Scale
-----

Holding :kbd:`Ctrl` will cause size changes in increments of 0.1 units.

.. note:: Snapping Modes

   Note that when you are :ref:`Snapping To <bpy.types.ToolSettings.snap_elements_base>`
   something other than *Increment*,
   holding :kbd:`Ctrl` will cause the selection to snap to that nearest element.

   Read more about :doc:`snapping </editors/3dview/controls/snapping>`.


Precision
=========

Holding :kbd:`Shift` during transformations allows for very fine control that does not
rely on fixed increments. Rather, large movements of the mouse across
the screen only result in small transformations of the selection.

In rotation mode the selected element will be rotate in 0.01 degree increments.
