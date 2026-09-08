.. _bpy.ops.object.align:

*************
Align Objects
*************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Transform --> Align Objects`

The Align tool is used to align multiple selected objects so they line up on a specified axis.


Options
=======

High Quality
   Uses more precise math to better determine the locations for the objects.
   In case of positive or negative bounding box alignment,
   if one or more of the selected objects have any rotation transformations
   (or delta rotation transformations), it is recommended to check *High Quality*
   so that their bounding box is calculated with precision for all three global axes.
Align Mode
   The *Align Mode* control will define what part of the objects will be aligned:

   :Centers:
      The objects centers.
   :Positive Sides/Negative Sides:
      The positive or negative sides (on the global axes) of their respective bounding boxes.
Relative To
   The *Relative To* control will let us choose to align the objects to:

   :Active: The active object.
   :Selection: The median point of the selection.
   :3D Cursor: The current position of the 3D Cursor.
   :Scene Origin: The global origin.
Align X, Y, Z
   Chooses which axis to align the selected objects on.
