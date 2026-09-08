
************
Median Point
************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Location:  :menuselection:`Header --> Transform Pivot Point --> Median Point` (:bl-icon:`pivot_median`)
   :Shortcut:  :kbd:`Period`

Places the pivot point at the averaged-out position of the selected items.


In Object Mode
==============

In Object Mode, the Median Point is the averaged-out position of the
:doc:`origins </scene_layout/object/origin>` of the selected objects.
The shape and size of the objects is not taken into account.

Origins can be chosen freely and can even lie outside their object's
geometry, so that the Median Point is not always what you might expect.

.. _fig-view3d-median-point-object-mode:

.. figure:: /images/editors_3dview_controls_pivot-point_median-point_object-mode.png
   :align: center

   Median points in Object Mode.


In Edit Mode
============

In Edit Mode, the Median Point is the averaged-out position of the
selected vertices. This means that the pivot point will shift towards
the area with the densest geometry.

In the example below, the pivot point lies perfectly in the middle
if both cubes have the same number of vertices, but heavily leans towards
the side if one cube is subdivided -- even though both cubes still
have the same size.

.. _fig-view3d-median-point-edit-mode:

.. figure:: /images/editors_3dview_controls_pivot-point_median-point_edit-mode.png
   :align: center

   Median points in Edit Mode.
