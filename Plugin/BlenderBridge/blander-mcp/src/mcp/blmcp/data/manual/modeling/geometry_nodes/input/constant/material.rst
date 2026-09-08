.. index:: Geometry Nodes; Material
.. _bpy.types.GeometryNodeInputMaterial:

*************
Material Node
*************

.. figure:: /images/node-types_GeometryNodeInputMaterial.webp
   :align: right
   :width: 300px
   :alt: Material Input Node.

The *Material* input node outputs a single material. It can be connected to other material sockets
to make using the same material name in multiple places more convenient.

.. tip::

   The Material node can also be added by dragging and dropping a material data-block into the node editor.
   This will add the node and select the dropped material in the :ref:`ui-data-block`.


Inputs
======

This node has no inputs.


Properties
==========

- Material


Output
======

Material
   A reference to the selected material.
