
************
Introduction
************

A Surface is a smooth sheet that's defined by a set of control points.
It's an extension of a :doc:`Curve </modeling/curves/introduction>`,
which is a smooth line.

.. figure:: /images/modeling_surfaces_introduction_nurbs-surface.png

   Surface in Edit Mode.

The control points are arranged in a grid with yellow lines indicating
the rows (U direction) and pink lines the columns (V direction).
The surface can be open or closed (cyclic) in either or both directions,
which allows the creation of, say, a cylinder or a sphere.

A Surface can be converted to a mesh using the menu item
:menuselection:`Object --> Convert --> Mesh` or the context menu item
:menuselection:`Convert To --> Mesh`.
