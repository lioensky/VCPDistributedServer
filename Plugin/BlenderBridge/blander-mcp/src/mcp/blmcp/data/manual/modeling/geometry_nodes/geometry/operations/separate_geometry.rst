.. index:: Geometry Nodes; Separate Geometry
.. _bpy.types.GeometryNodeSeparateGeometry:

**********************
Separate Geometry Node
**********************

.. figure:: /images/node-types_GeometryNodeSeparateGeometry.webp
   :align: right
   :alt: Separate Geometry node.

The *Separate Geometry* node produces two geometry outputs. Based on the *Selection* input,
the input geometry is split between the two outputs.

.. tip::

   This node can be combined with the :doc:`/modeling/geometry_nodes/utilities/math/compare`
   for a more precise control of which parts are separated to a given output geometry.


Inputs
======

Geometry
   Standard Geometry input.

Selection
   Boolean field used to calculate which output each part of the geometry will go to.
   Parts in the selection will move to the *Selection* output.
   Parts not in the selection will move to the *Inverted* output.


Properties
==========

Domain
   The domain on which the selection field is evaluated.

   :Point:
      The selection is on the points, control points, and vertices of the geometry.
   :Edge:
      The selection is on the edges of the mesh component. The other components
      are not modified.
   :Faces:
      The selection is on the faces of the mesh component. The other components
      are not modified.
   :Spline:
      The selection is on the splines in the curve component. For each spline, it
      is either entirely in the selection or not at all. The other components are not
      modified.

   .. note::

      When selecting a domain that doesn't modify all components, the unmodified
      components will appear in both outputs.


Outputs
=======

Selection
   The parts of the geometry in the selection.

Inverted
   The parts of the geometry not in the selection.
