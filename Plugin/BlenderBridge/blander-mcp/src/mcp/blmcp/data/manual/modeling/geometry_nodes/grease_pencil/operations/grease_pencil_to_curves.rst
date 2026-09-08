.. index:: Geometry Nodes; Grease Pencil to Curves
.. _bpy.types.GeometryNodeGreasePencilToCurves:

****************************
Grease Pencil to Curves Node
****************************

.. figure:: /images/node-types_GeometryNodeGreasePencilToCurves.png
   :align: right
   :alt: Grease Pencil to Curves node.

The *Grease Pencil to Curves* node converts each Grease Pencil layer into an instance
that contains curves.


Inputs
======

Grease Pencil
   Standard Grease Pencil geometry.

Selection
   Selects the layers to convert.

Instances as Layers
   Create a separate curve instance for every layer.

   .. tip::
      This is equivalent to a :doc:`Realize Instances </modeling/geometry_nodes/instances/realize_instances>`
      operation after creating the curve geometry instances. This can simplify some logic later on, but
      typically keeping this operation off will be much better for performance.

Outputs
=======

Curves
   Standard curves geometry.
