.. index:: Geometry Nodes; Scale Elements
.. _bpy.types.GeometryNodeScaleElements:

*******************
Scale Elements Node
*******************

.. figure:: /images/node-types_GeometryNodeScaleElements.webp
   :align: right
   :alt: Scale Elements node.

Scales the selected faces or edges, letting you specify a scaling factor and pivot point for each one.
Connected faces/edges are scaled together using their average factor and pivot point.


Inputs
======

Geometry
   Standard geometry input.

Selection
   Boolean field indicating which elements to scale.

Scale
   The scaling factor for each element.

Center
   The pivot point for each element.

Axis :guilabel:`Single Axis Mode Only`
   Axis along which to scale each element. This vector is normalized internally, so the length does not matter.

Scale Mode
   :Uniform: Scale elements by the same factor in every direction.
   :Single Axis: Scale elements in a single direction defined by the *Axis* input.


Properties
==========

Domain
   The element type to transform.

   :Face: Scale faces.
   :Edge: Scale edges.


Output
======

Geometry
   Standard geometry output.


Examples
========

.. figure:: /images/modeling_geometry-nodes_flip-faces_extrude.png
   :align: right

The node is useful when combined with the :doc:`/modeling/geometry_nodes/mesh/operations/extrude_mesh`,
especially in *Individual* mode where connected faces aren't extruded together.
