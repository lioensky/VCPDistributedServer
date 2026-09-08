.. index:: Geometry Nodes; Set Instance Transform
.. _bpy.types.GeometryNodeSetInstanceTransform:

***************************
Set Instance Transform Node
***************************

.. figure:: /images/node-types_GeometryNodeSetInstanceTransform.webp
   :align: right
   :alt: Set Instance Transform node.

The *Set Instance Transform* node :term:`Transforms <Transform>` geometry instances
using a :term:`Transformation Matrix`.

The :doc:`/modeling/geometry_nodes/instances` page contains more information about geometry instances.


Inputs
======

Instances
   Standard geometry input.

Selection
   Boolean field used to determine if an instance will be rotated.

Transform
   The transformation matrix to translate, rotate, and scale individual instances.


Outputs
=======

Instances
   Standard geometry output.
