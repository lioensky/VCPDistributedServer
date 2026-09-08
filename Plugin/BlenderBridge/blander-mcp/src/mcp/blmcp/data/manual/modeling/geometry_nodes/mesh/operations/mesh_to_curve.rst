.. index:: Geometry Nodes; Mesh to Curve
.. _bpy.types.GeometryNodeMeshToCurve:

******************
Mesh to Curve Node
******************

.. figure:: /images/node-types_GeometryNodeMeshToCurve.webp
   :align: right
   :alt: Mesh to Curve node.

The *Mesh to Curve* node converts a mesh into one or more curve splines.

Two different conversion modes are supported, depending on the desired output:

- **Edges**: Turns each string of connected mesh edges into a poly spline.
  Whenever two or more edge strings intersect, they will be split into separate splines.
- **Faces**: Creates a cyclic spline from each mesh face. This mode is generally much faster than *Edges*,
  as it parallelizes easily and can share face and corner attributes without needing to copy them.

Loose vertices are ignored -- they will not be turned into single-point splines.

Attributes, both named and unnamed ones, are transferred to the resulting splines.
If there is a ``radius`` attribute, it will be applied as such,
although you may find it more convenient to use the
:doc:`/modeling/geometry_nodes/curve/write/set_curve_radius` for this.


Inputs
======

Mesh
   Standard mesh input.

Selection
   A field input evaluated on the edge domain to determine whether each edge will be included in the result.

   .. tip::

      Using this input is more efficient than deleting parts of the geometry before or after the conversion.


Properties
==========

Mode
   Determines how the mesh is converted to curves:

   :Edges: Converts connected edge chains into poly splines.
   :Faces: Converts each face into a cyclic spline.

Outputs
=======

Curve
   Generated curve.
