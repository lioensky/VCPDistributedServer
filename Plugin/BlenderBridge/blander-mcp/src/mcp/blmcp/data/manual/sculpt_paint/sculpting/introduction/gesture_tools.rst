*************
Gesture Tools
*************

Separate from brushes and filters, Sculpt mode also has a set of tools that perform actions to a drawn
selection area. These tools are similar to the selection tools (e.g. :ref:`box selection <tool-select-box>`
and :ref:`lasso selection <tool-select-lasso>` in other areas of Blender).

These tools do not provide a selection of elements that are then modified, they directly modify the underlying
mesh.


.. _gesture-tool-box:

Box Gestures
============

Dragging creates a rectangular area defined by where :kbd:`LMB` was pressed and where :kbd:`LMB` is released.


Controls
--------

Move :kbd:`Spacebar`
   Hold to reposition the selection area.


.. _gesture-tool-lasso:

Lasso Gestures
==============

Dragging creates a freeform area that follows the cursor defined by where :kbd:`LMB` was pressed and where :kbd:`LMB`
is released.


Controls
--------

Move :kbd:`Spacebar`
   Hold to reposition the selection area.


Tool Settings
-------------

Stabilize Stroke
   Helps to reduce jitter of the strokes while drawing by delaying and correcting the location of points.

   Radius
      Minimum distance from the last point before the stroke continues.
   Factor
      A smooth factor, where higher values result in smoother strokes
      but the drawing sensation feels as if you were pulling the stroke.


.. _gesture-tool-line:

Line Gestures
=============

Dragging creates a line. The resulting action acts upon everything on the highlighted side of the line. The area acted
upon is extended in both directions of the viewport.


Controls
--------

Flip :kbd:`F`
   Toggles the side of the line that the tool affects.
Snap :kbd:`Ctrl`
   Hold to constrain the rotation of the line to user-specified intervals. Defaults to 5 degree increments,
   customizable via the Snapping menu indicated by the magnet icon in the header.
Move :kbd:`Spacebar`
   Hold to reposition the line.


Tool Settings
-------------

Limit to Segment
   The affected area will not extend the length of the drawn line.
   This helps defining a smaller area instead of extending the line infinitely long.


.. _gesture-tool-polyline:

Polyline Gestures
=================

Clicking places a point in the viewport. Each time :kbd:`LMB` is pressed, a new point of the polygon is created.
Pressing :kbd:`LMB` on the starting point, pressing :kbd:`LMB` twice,
or pressing :kbd:`Return` closes the selection area.


Controls
--------

Move :kbd:`Spacebar`
   Hold to reposition the selection area.
