
***********
Stroke Menu
***********

This page covers many of the tools in the *Strokes* menu.
These are tools that work primarily on strokes, however,
some also work with point selections.


.. _bpy.ops.grease_pencil.stroke_subdivide:

Subdivide
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Subdivide`

The *Subdivide* operator adds new control points to selected curve segments by dividing them into smaller sections.
This is useful for creating smoother transitions, preparing curves for finer adjustments,
or adding more detail for animation or modeling.

Number of Cuts
   Specifies the number of divisions for each selected segment; each cut adds one new control point per segment.
Selected Points
   When enabled, limits the effect to only the selected points within the stroke.


.. _bpy.ops.grease_pencil.stroke_subdivide_smooth:

Subdivide and Smooth
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Subdivide and Smooth`


Subdivides and smooths the strokes by inserting points between the selected points.

Number of Cuts
   The number of subdivisions to perform.
Selected Points
   When enabled, limits the effect to only the selected points within the stroke.
Iterations
   Number of times to repeat the procedure.
Factor
   The amount of the smoothness on subdivided points.
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


.. _bpy.ops.grease_pencil.stroke_simplify:

Simplify
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Simplify`

Reduces the complexity of Grease Pencil strokes by strategically removing points.
This is useful for cleaning up strokes, optimizing performance,
and preparing drawings for further editing or animation.
There are multiple modes; described below:


Fixed
-----

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Simplify -- Fixed`

Deletes alternated points in the strokes, except the start and end points.

Steps
   The number of times to repeat the procedure.


Adaptive
--------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Simplify -- Adaptive`

Uses the RDP algorithm (Ramer-Douglas-Peucker algorithm) for points deletion.
The algorithm tries to obtain a similar line shape with fewer points.

Factor
   Controls the amount of recursively simplifications applied by the algorithm.


Sample
------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Simplify -- Sample`

Recreates the stroke geometry with a predefined length between points.

Length
   The distance between points on the recreated stroke.
   Smaller values will require more points to recreate the stroke,
   while larger values will result in fewer points needed to recreate the curve.


Merge
-----

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Simplify -- Merge`

Simplifies the stroke by merging points that are closer than the specified distance.

Distance
   The maximum distance between vertices to determine which ones will be merged.


Outline
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Outline`

The *Outline* operator converts selected Grease Pencil strokes into closed perimeter shapes.
It creates new strokes around the outer boundary of the original stroke,
effectively generating a filled outline with adjustable thickness.

View
   Defines the projection method used to generate the outline:

   :View: Use the current viewport perspective as the projection plane.
   :Front: Use the X-Z axes as the projection plane (front view).
   :Side: Use the Y-Z axes as the projection plane (side view).
   :Top: Use the X-Y axes as the projection plane (top view).
   :Camera: Use the active camera's perspective as the projection plane.
Radius
   Sets the thickness of the outline on both sides of the original stroke.
   Higher values result in a wider perimeter.
Offset Factor
   Scales the stroke outline inward or outward.
   - Positive values push the perimeter outward.
   - Negative values pull it inward.
   - A value of 0 centers the perimeter on the original stroke.
Corner Subdivisions
   Number of subdivisions used to smooth corners at stroke endpoints and joints.
   Higher values result in smoother corners but increase stroke complexity.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_outline-1.png
          :width: 320px

          Original stroke.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_outline-2.png
          :width: 320px

          Stroke after applying the *Outline* operator.


.. _bpy.ops.grease_pencil.stroke_trim:

Trim
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Trim`

Trims selected stroke to first loop or intersection.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_trim-1.png
          :width: 320px

          Original stroke.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_trim-2.png
          :width: 320px

          Result of trim operation.


Join
====

.. _bpy.ops.grease_pencil.join_selection:

Join
----

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Join --> Join,`

Join two or more strokes into a single one.

Type
   :Join:
      :kbd:`Ctrl-J`
      Join selected strokes by connecting points.
   :Join and Copy:
      Join selected strokes by connecting points in a new stroke.
Leave Gaps
   When enabled, do not use geometry to connect the strokes.


Join and Copy
-------------

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Join --> Join and Copy`
   :Shortcut:  :kbd:`Shift-Ctrl-J`

Same as :ref:`bpy.ops.grease_pencil.join_selection` but *Type* defaults to *Join and Copy*.


.. _bpy.ops.grease_pencil.move_to_layer:

Move to Layer
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Move to Layer`
   :Shortcut:  :kbd:`M`

A pop-up menu to move the stroke to a different layer.
You can choose the layer to move the selected strokes to
from a list of layers of the current Grease Pencil object.
You can also add a new layer to move the selected stroke to.
When creating a new layer, there is another pop-up to type in the name of the new layer.


.. _bpy.ops.grease_pencil.stroke_material_set:

Assign Material
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Assign Material`

Changes the material linked to the selected stroke.
You can choose the name of the material to be used by the selected stroke
from a list of materials of the current Grease Pencil object.


.. _bpy.ops.grease_pencil.set_active_material:

Set as Active Material
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set as Active Material`

Sets the active object material based on the selected stroke material.


.. _bpy.ops.grease_pencil.reorder:

Arrange
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Arrange`

Change the drawing order of the strokes in the 2D layer.

Bring to Front
   Moves to the top the selected points/strokes.
Bring Forward
   Moves the selected points/strokes upper the next one in the drawing order.
Send Backward
   Moves the selected points/strokes below the previous one in the drawing order.
Send to Back
   Moves to the bottom the selected points/strokes.


.. _bpy.ops.grease_pencil.cyclical_set:

Close
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Close`
   :Shortcut:  :kbd:`F`

Close or open strokes by connecting the last and first point.

Type
   :Close All: Close all open selected strokes.
   :Open All: Open all closed selected strokes.
   :Toggle: Close or Open selected strokes as required.
Match Point Density
   Add point in the new segment to keep the same density.


Toggle Cyclic
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Toggle Cyclic`

Toggles between an open stroke and closed stroke (cyclic).

Type
   :Close All: Close all open selected strokes.
   :Open All: Open all closed selected strokes.
   :Toggle: Close or Open selected strokes as required.
Match Point Density
   Add point in the new segment to keep the same density.


.. _bpy.ops.grease_pencil.caps_set:

Set Caps
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Caps`

Toggle ending cap styles of the stroke.

Rounded
   Sets stroke start and end points to rounded (default).

Flat
   Toggle stroke start and end points caps to flat or rounded.

Toggle Start
   Toggle stroke start point cap to flat or rounded.

Toggle End
   Toggle stroke end point cap to flat or rounded.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_cap-1.png
          :width: 200px

          Stroke ending with rounded caps.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_cap-2.png
          :width: 200px

          Stroke ending with flat caps.

     - .. figure:: /images/grease-pencil_modes_edit_stroke-menu_cap-3.png
          :width: 200px

          Stroke ending with combined caps.


.. _bpy.ops.grease_pencil.stroke_switch_direction:

Switch Direction
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Switch Direction`

The *Switch Direction* operator reverses the direction of the selected Grease Pencil stroke. This means the starting
point of the stroke becomes the endpoint, and vice versa. While this operation does not alter the visual appearance
of the stroke, but affects behaviors that rely on the point order, such as the
:doc:`Build Modifier </grease_pencil/modifiers/generate/build>`.


.. _bpy.ops.grease_pencil.set_start_point:

Set Start Point
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Start Point`

Set the start point for cyclic strokes, determining the point where the stroke begins and ends when it loops.


.. _bpy.ops.grease_pencil.set_uniform_thickness:

Set Uniform Thickness
=====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Uniform Thickness`

Makes the thickness equal for the entire stroke.

Thickness
   Thickness value to use on all points of the stroke.


.. _bpy.ops.grease_pencil.set_uniform_opacity:

Set Uniform Opacity
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Uniform Opacity`

Makes the opacity equal for the entire stroke.

Opacity
   Opacity value to use on all points of the stroke.


.. _bpy.types.GPencilSculptSettings.use_scale_thickness:

Scale Thickness
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Scale Thickness`

When enabled, scales the stroke thickness during scale transformations.


.. _bpy.ops.grease_pencil.set_curve_type:

Set Curve Type
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Curve Type`
   :Shortcut:  :kbd:`V`

Sets the spline type for the splines in the stroke component that are in the selection.

Type
   Specifies the target spline type. For more details on spline types, see the
   :ref:`Spline Types <curve-spline-types>` documentation.

   :Bézier:
      Converts the spline to a Bézier type.
      - Poly splines are converted with vector handles.
      - NURBS or Catmull Rom splines are converted with automatic handles.

      .. note::

         When converting a NURBS spline to Bézier, at least six points are required.
         If the number of points is not a multiple of three, the spline will be truncated.

   :NURBS: Converts the spline to a NURBS type.
   :Poly: Converts the spline to a poly type.
   :Catmull Rom: Converts the spline to a Catmull Rom type.

Handles
   Includes handle information during the conversion process.


.. _bpy.ops.grease_pencil.set_curve_resolution:

Set Curve Resolution
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Curve Resolution`

Sets the number of points generated along each curve segment (between two handles).


.. _bpy.ops.grease_pencil.reset_uvs:

Reset UVs
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Stroke --> Set Curve Resolution`

Reset UV transformation to default values.
