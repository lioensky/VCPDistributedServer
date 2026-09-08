.. index:: Geometry Nodes; Named Layer Selection
.. _bpy.types.GeometryNodeInputNamedLayerSelection:

**************************
Named Layer Selection Node
**************************

.. figure:: /images/node-types_GeometryNodeInputNamedLayerSelection.webp
   :align: right
   :alt: Named Layer Selection Node.

The *Named Layer Selection* node outputs a Boolean field whose index value is true
for :doc:`Grease Pencil layers </grease_pencil/properties/layers>` whose name matches a string input.

.. note::

   - The specified layer must already exist in the object.
   - If no matching layer is found, the selection will be false for all elements.


Inputs
======

Name
   The name of the Grease Pencil layer to match.


Outputs
=======

Selection
   A Boolean field for which the index for layers
   whose name matches the input string will be true; all others are false.
