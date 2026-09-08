
******
Curves
******

Transform
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Transform`

A curves objects can be edited by transforming the locations of control points.

Move, Rotate, Scale
   Like other elements in Blender, control points can be moved, rotated, or scaled as described in
   :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>`.
To Sphere, Shear, Bend, Push/Pull
   The transform tools are described in
   the :doc:`Transformations </modeling/meshes/editing/mesh/transform/index>` sections.


.. _modeling-curves-radius:

Radius
------

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Radius`
   :Menu:      :menuselection:`Curves --> Transform --> Radius`
   :Shortcut:  :kbd:`Alt-S`

The Radius allows you to directly control the width of the extrusion along the "spinal" curve.
The radius will be interpolated from point to point (you can check it with the normals).
The *Radius* of the points is set using the *Radius* transform tool. Or in the Sidebar *Transform* panel.

.. figure:: /images/modeling_curves_editing_curve_extrude-radius.png
   :align: center
   :width: 50%

   One control point radius set to zero.


Mirror
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

The *Mirror* tool is also available, behaving exactly as with
:doc:`mesh vertices </modeling/meshes/editing/mesh/mirror>`.


Snap
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Snap`
   :Shortcut:  :kbd:`Shift-S`

:doc:`Mesh snapping </editors/3dview/controls/snapping>` also works with curve components.
Both control points and their handles will be affected by snapping,
except for within itself (other components of the active curve).
Snapping works with 2D curves but points will be constrained to the local XY axes.


.. _bpy.ops.curves.duplicate_move:

Duplicate
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Duplicate`
   :Shortcut:  :kbd:`Shift-D`

This operator duplicates the selected control points,
along with the curve segments implicitly selected (if any).
.. If only a handle is selected, the full point will be duplicated too.
The copy is selected so you can move it to another place.


.. _bpy.ops.curves.extrude_move:

Extrude Curve and Move
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Extrude Curve and Move`
   :Shortcut:  :kbd:`E`

Extrudes points by duplicating the selected points, which then can be moved,
and connecting those points back to the original curve creating a continuous curve.


.. _bpy.ops.curves.attribute_set:

Set Attribute
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Set Attribute`

Opens a pop-up window showing the name of the :term:`active` :term:`attribute`
as well as the value of that attribute for the selected points
From there, you assign a new value to a selected attribute across all selected points.

This operator is useful for uniformly setting attribute values.


.. _bpy.ops.curves.curve_type_set:

Set Curve Type
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Set Curve Type`
   :Shortcut:  :kbd:`V`

Converts splines in a curve object between Bézier, NURBS, Poly, and Catmull Rom types.
This is a basic conversion, meaning Blender does not preserve the exact shape or the number of control points.
For example, converting a NURBS spline to a Bézier spline maps each group of three NURBS control points
to a single Bézier control point with two handles.

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


Toggle Cyclic
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Toggle Cyclic`
   :Shortcut:  :kbd:`Alt-C`

Toggles between an open curve and closed curve (Cyclic).
Only curves with at least one selected control point will be closed/open.
The shape of the closing segment is based on the start and end handles for Bézier curves,
and as usual on adjacent control points for NURBS.
The only time a handle is adjusted after closing is if the handle is an *Auto* one.
Fig. :ref:`fig-curves-editing-open-close` is the same Bézier curve open and closed.

This action only works on the original starting control point or the last control point added.
Deleting a segment(s) does not change how the action applies;
it still operates only on the starting and last control points. This means that
:kbd:`Alt-C` may actually join two curves instead of closing a single curve!
Remember that when a 2D curve is closed, it creates a renderable flat face.

.. _fig-curves-editing-open-close:

.. figure:: /images/modeling_curves_editing_curve_open-closed-cyclic.png

   Open and Closed curves.


.. _bpy.ops.curves.separate:

Separate
========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Separate`
   :Shortcut:  :kbd:`P`

Separates the selected curve geometry into their own curve object.


.. _bpy.ops.curves.delete:

Delete
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Curves --> Delete`
   :Shortcut:  :kbd:`X`

The Delete operator can remove Control Points or Segments.
Deleting can be used to make curves shorter or simplify
segments by deleting control points in the mid section of a segment.


.. _bpy.ops.curves.split:

Split
=====

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Y`

The *Split* operator separates the selected portion of a curve from the rest,
creating a new, independent curve segment.
This curve can then be moved or altered without affecting the other curve.

- If a segment of the curve is selected, it will be split off
  as a new curve that can be moved or edited independently.
- If only a single control point is selected, it will be duplicated as a loose control point,
  while the original remains attached to the rest of the curve.
