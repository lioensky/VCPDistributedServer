.. index:: Geometry Nodes; Curve to Mesh
.. _bpy.types.GeometryNodeCurveToMesh:

******************
Curve to Mesh Node
******************

.. figure:: /images/node-types_GeometryNodeCurveToMesh.webp
   :align: right
   :alt: The Curve to Mesh node.

The Curve to Mesh node converts all splines of a curve to a mesh.
Optionally, a profile curve can be provided to give the curve a custom shape.

The node transfers attributes to the result. Attributes that are built-in on meshes but not curves,
like ``sharp_face``, will be transferred to the correct domain as well.

.. tip::

   The output mesh has :ref:`sharp edges <geometry-nodes_builtin-attributes>` set from
   the profile curve tagged automatically. If any splines in the profile curve
   are Bézier splines and any of the control points use *Free* or *Vector* handles,
   the corresponding edges will be shaded sharp.


Inputs
======

Curve
   Standard geometry input.
   All non-curve components are ignored.

Profile Curve
   If a profile curve is provided, it will be extruded along all splines.
   Otherwise the generated mesh will just be a chain of edges.

Scale
   The scale used at each control point of the input curve to scale the profile curve.

Fill Caps
   If the profile spline is cyclic, fill the ends of the generated mesh with n-gons.
   The resulting mesh is :term:`Manifold`, the two new faces for each spline are
   simply connected to existing edges.


Outputs
=======

Mesh
   Standard geometry output.
