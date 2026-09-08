.. index:: Geometry Nodes; Curves to Grease Pencil
.. _bpy.types.GeometryNodeCurvesToGreasePencil:

****************************
Curves to Grease Pencil Node
****************************

.. figure:: /images/node-types_GeometryNodeCurvesToGreasePencil.png
   :align: right
   :alt: Curves to Grease Pencil node.

The *Curves to Grease Pencil* node Converts top-level curve instances into Grease Pencil layers

Inputs
======

Curves
   Either plain curves or curve instances.

Selection
    Either a curve or instance selection.

Instances as Layers
    Create a separate layer for each instance. If instances are used, realized curve geometry will be
    ignored. Layer names will use the instance geometry name. If real curve geometry is used, a single
    layer is created with the input geometry's name.


Outputs
=======

Grease Pencil
   Standard Grease Pencil geometry.


Examples
========

.. figure:: /images/node-types_curves_to_grease_pencil_set_radius_example.jpeg

   This example shows how to use the *Curves to Grease Pencil* node to create a Grease Pencil layer from a curve.

   The *Set Curve Radius* node is used to set the radius of the Grease Pencil strokes.

