
*****************************
Selecting Point Cloud Objects
*****************************

This section describes the available selection operators when working with point cloud objects in *Edit Mode*.
These operators allow you to quickly select or deselect points for further editing or transformation.

.. _bpy.ops.pointcloud.select_all:

All
===

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> All`
   :Shortcut:  :kbd:`A`

Selects all points in the point cloud.


Select None
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> None`
   :Shortcut:  :kbd:`Alt-A`

Deselects all currently selected points in the point cloud.


Select Invert
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Invert`
   :Shortcut:  :kbd:`Ctrl-I`

Inverts the selection state of each point in the point cloud:

- Points that were selected become deselected.
- Points that were not selected become selected.

This operator is useful for quickly selecting the opposite subset of points in your current selection.


.. _bpy.ops.pointcloud.select_random:

Select Random
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Random`

Selects a random subset of points in the point cloud.

Seed
   The :term:`seed` value used by the pseudo-random number generator.
   Adjusting this value changes which points are randomly selected.
Probability
   A value between 0.0 and 1.0 that determines the percentage of points to be selected.
   For example, a value of 0.25 selects roughly 25% of the points.

This operator is useful for procedural modeling, scattering, or testing effects with a random distribution.
