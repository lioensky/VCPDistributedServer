.. _bpy.ops.object.track_set:

*****
Track
*****

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Object --> Track`

These tools add a tracking constraint to the selected objects;
the target object of the constraint will be the active object, which won't have a constraint added.

- :doc:`Damped Track Constraint </animation/constraints/tracking/damped_track>`
- :doc:`Track To Constraint </animation/constraints/tracking/track_to>`
- :doc:`Lock Track Constraint </animation/constraints/tracking/locked_track>`


.. _bpy.ops.object.track_clear:

Clear Track
===========

Removes all Damped Track, Track To and Lock Track Constraints from the selected objects.


Clear and Keep Transformation (Clear Track)
===========================================

Removes all Track Constraint from the selected objects, while keeping the final transform caused by them.
