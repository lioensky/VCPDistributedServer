
************
Line Project
************

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Line Project`

This tool flattens the geometry along a plane determined by the camera view and a drawn line.
The region of the mesh being flattened is visualized by the side of the line that is shaded.

.. list-table::

   * - .. figure:: /images/sculpt-paint_sculpting_tools_line-project_before.png

          Before Line Project.

     - .. figure:: /images/sculpt-paint_sculpting_tools_line-project_after.png

          After Line Project.


Usage
=====

Use the tool by:

#. Orient the 3D Viewport to define the direction in depth.
#. :kbd:`LMB` and hold while moving the cursor to define direction of the line projection.
#. Adjust the operation with extra *Controls* shortcuts.
#. Release :kbd:`LMB` to confirm.


Controls
========

Flip :kbd:`F`
   Changes the side of the line that the tool projects geometry.
Snap :kbd:`Ctrl`
   Constrains the rotation of the line to 15 degree intervals.
Move :kbd:`Ctrl-Spacebar`
   Reposition the line.


Tool Settings
=============

Limit to Segment
   The affected area will not extend the length of the drawn line.
   This helps defining a smaller area instead of extending the line infinitely long
