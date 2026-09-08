.. _bpy.ops.object.*clear:

*****
Clear
*****

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Clear --> Location / Scale / Rotation / Origin`
   :Shortcut:  :kbd:`Alt-G`, :kbd:`Alt-S`, :kbd:`Alt-R`

Clearing transforms resets the transform values.
The objects location and rotation values are set to 0, and the scale to 1.

Clear Location :kbd:`Alt-G`
   Clear (reset) the location of the selection.
   This will move the selection back to the coordinates (0, 0, 0).
Clear Scale :kbd:`Alt-S`
   Clear (reset) the scale of the selection.
   This will change the scale to (1, 1, 1).
Clear Rotation :kbd:`Alt-R`
   Clear (reset) the rotation of the selection.
   This will set the rotation of the selection to 0 degrees in each plane.

.. _bpy.ops.object.origin_clear:

Clear Origin
   Clears (resets) the offset of the child objects origin from
   the :doc:`Parent </scene_layout/object/editing/parent>`.
   This will cause child objects to move to the origin of the parent.
   The relationship between the parent and child is not affected,
   you can confirm the relationship is still intact by using the *Outliner* to
   verify that the child object is still parented.


Options
=======

Clear Delta
   Clear the :ref:`delta transform <bpy.types.Object.delta>` in addition to clearing the primary transforms.
   (Appears in the :ref:`bpy.ops.screen.redo_last` panel.)
