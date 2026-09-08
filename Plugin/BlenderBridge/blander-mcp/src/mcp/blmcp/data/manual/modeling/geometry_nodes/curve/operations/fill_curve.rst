.. index:: Geometry Nodes; Fill Curve
.. _bpy.types.GeometryNodeFillCurve:

***************
Fill Curve Node
***************

.. figure:: /images/node-types_GeometryNodeFillCurve.webp
   :align: right
   :alt: Fill Curve node.

The *Fill Curve* node generates a mesh using the constrained Delaunay triangulation algorithm
with the curves as boundaries. The mesh is only generated flat with a local Z of 0.


Inputs
======

Curve
   Standard geometry input with a curve component.

Group ID
   Value used to group curves together.
   Curves with different Group ID are treated separately.

Mode
   The type of geometry the output consists of.

   :Triangles: The output is made up of triangles.
   :N-gons: The output is made up of n-gons.


Outputs
=======

Mesh
   The filled-in curves.


Examples
========

Customized triangulation
------------------------

One or many "single point spline" can be used to customize the triangulation of the filled-in curves.

.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_example_0.png
   :align: center

   This is the default behavior of the *Fill Curve* node applied to the star primitive.


.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_example_1.png
   :align: center

   Here, a single curve point is joined to the star primitive to customize the triangulation.

.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_example_2.png
   :align: center

   Here, 300 single curve point are joined to the star primitive to customize the triangulation.

Group ID
--------

The following figures display diverse application of the Group ID.

.. The following example were made with some nodes "hidden" to illustrate the amount of mesh islands
.. and avoid Z fighting.
.. Mesh Island Index -> Set Position (as z offset)
.. Mesh Island Index -> Map Range (Mesh island count as input max) -> Color Ramp (distributed from left)
.. Colors Used : 5ABD9E, 85BD50, DDB72C, D26072

.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_group-id_0.png
   :align: center
   :alt:

   Here, the 4 curves share the same Group ID, resulting in 1 mesh island (default behavior).

.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_group-id_1.png
   :align: center

   Here, the 4 curves have different Group ID, resulting in 4 mesh islands.

.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_group-id_2.png
   :align: center

   Here, the 4 curves are seperated into two groups based on their positions, resulting in 2 mesh islands.
