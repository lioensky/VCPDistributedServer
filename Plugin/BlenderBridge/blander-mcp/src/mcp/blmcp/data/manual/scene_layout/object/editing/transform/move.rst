.. _bpy.ops.transform.translate:

****
Move
****

.. reference::

   :Mode:      Object Mode, Edit Mode, and Pose Mode
   :Menu:      :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Move`
   :Shortcut:  :kbd:`G`

In Object Mode, the move option lets you move objects.
Translation means changing location of objects. It also lets you move any elements
that make up the object within the 3D space of the active 3D Viewport.

Pressing :kbd:`G` activates "Move" transformation mode. The selected object
or element then moves freely according to the mouse pointer's location and camera.
To confirm the action, press :kbd:`LMB`.
While moving items, the amount of change along the X, Y, and Z axis is displayed in the header of the 3D Viewport.

.. figure:: /images/scene-layout_object_editing_transform_move_display-values.png

   Translation Display.

.. tip::

   Moving an object in Object Mode changes the object's origin.
   Moving the object's vertices/edges/faces in Edit Mode does not change the object's origin.

.. seealso::

   Using a combination of shortcuts gives you more control over your transformation.
   See :doc:`Transform Control </scene_layout/object/editing/transform/control/index>`.


Options
=======

Move X, Y, Z
   The amount to move the selection on the respected axis.

Orientation
   Aligns the transformation axes to a specified orientation constraint.
   See :doc:`Transform Orientations </editors/3dview/controls/orientation>` for more information.

Proportional Editing
   The extruded face will affect nearby geometry.
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>` for a full reference.
