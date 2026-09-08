
**********
Point Menu
**********

.. _bpy.ops.grease_pencil.extrude_move:

Extrude
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Extrude`
   :Tool:      :menuselection:`Toolbar --> Extrude`
   :Shortcut:  :kbd:`E`

Extrudes points by duplicating the selected points, which then can be moved.
The new points stay connected with the original points of the edit line.

.. note::

   Since Grease Pencil strokes can only have one start an end point,
   a new stroke will be created when extrude intermediate points in the strokes.


.. _bpy.ops.grease_pencil.stroke_smooth:

Smooth
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Smooth`

Softens strokes by reducing the differences in the locations of the points along the line,
while trying to maintain similar values that make the line fluid and smoother.

Iterations
   The number of times to repeat the procedure.
Factor
   The amount of the smoothness to apply.
Smooth Endpoints
   Smooths the stroke's endpoints.
Keep Shape
   Preserves the strokes shape.
Position
   When enabled, the operator affect the points location.
Radius
   When enabled, the operator affect the points thickness.
Opacity
   When enabled, the operator affect the points strength (alpha).


Vertex Groups
=============

Operators for working with vertex groups.


.. _bpy.ops.grease_pencil.set_handle_type:

Set Handle Type
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Set Handle Type`
   :Shortcut:  :kbd:`V`

Sets the handle type for the points on the Bézier curve that are in the selection.

Type
   The handle type to switch to.

   :Auto:
      This handle has a completely automatic length and direction
      which is set by Blender to ensure the smoothest result.
      These handles convert to *Align* handles when moved.
   :Vector:
      Both parts of a handle always point to the previous handle or the next handle which allows
      you to create curves or sections thereof made of straight lines or with sharp corners.
      Vector handles convert to *Free* handles when moved.
   :Align:
      These handles always lie in a straight line,
      and give a continuous curve without sharp angles.
   :Free:
      The handles are independent of each other.
   :Toggle Free/Align:
      Replaces Free handles with Align, and all Align with Free handles.


.. _bpy.ops.grease_pencil.set_corner_type:

Set Corner Type
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Set Corner Type`

Sets how corners between strokes or segments are shaped when using stroke
thickness or fills. This affects how the stroke geometry joins at sharp angles.

Corner Type
   Defines the style of the corner for the selected points.

   :Round: Smoothly rounds the corner, creating a curved transition between segments.
   :Flat: Cuts the corner flat, creating a beveled join.
   :Sharp: Keeps the corner pointed, preserving the original angle between segments.

Miter Cut Angle
   Specifies the angle threshold (in degrees) for flattening sharp corners.
   Any corner sharper than this angle will be cut flat when *Corner Type* is set to *Flat* or *Round*.
