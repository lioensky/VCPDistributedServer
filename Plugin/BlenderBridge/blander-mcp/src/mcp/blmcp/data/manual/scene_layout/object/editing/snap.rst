.. _bpy.ops.view3d.snap:

****
Snap
****

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Menu:      :menuselection:`Object/Object type --> Snap`
   :Shortcut:  :kbd:`Shift-S`

The *Snap* menu (also available from the 3D header in both *Object Mode* and *Edit Mode*
:menuselection:`Object --> Snap` and :menuselection:`Mesh --> Snap`).
This menu provides a number of options to move the cursor or your selection to a defined point
(the cursor, selection or the grid).

Selection to Grid
   Snaps the currently selected object(s) to the nearest grid point.
Selection to Cursor
   Moves each one of the currently selected object(s) to the cursor location.
   Optionally, the selection can be rotated to match the cursor.
Selection to Cursor (Offset)
   Places the selection at the position of the 3D cursor.
   If there are multiple objects selected, they are not moved individually at the cursor position;
   instead, they are centered around the 3D cursor, maintaining their relative distances.
Selection to Active
   Moves the selection to the origin of the active object.

Cursor to Selected
   Places the cursor to the center of the current selection, unless see below.
Cursor to World Origin
   Places the cursor to the origin of the world (location 0, 0, 0).
Cursor to Grid
   Places the cursor to the nearest grid point.
Cursor to Active
   Places the cursor to the origin of the *active* (last selected) object.

The *Cursor to Selected* option is also affected by the current :ref:`pivot-point-index`. For example:

- With the *Bounding Box Center* pivot point active,
  the *Cursor to Selected* option will snap the 3D cursor to
  the center of the bounding box surrounding the objects' origins.
- When the *Median Point* pivot point is selected,
  *Cursor to Selected* will snap the 3D cursor to
  the :doc:`median </editors/3dview/controls/pivot_point/median_point>` of the object
  origins.
