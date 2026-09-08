.. index:: Geometry Nodes; Instance Rotation
.. _bpy.types.GeometryNodeInputInstanceRotation:

**********************
Instance Rotation Node
**********************

.. figure:: /images/node-types_GeometryNodeInputInstanceRotation.webp
   :align: right
   :alt: Instance Rotation node.

The *Instance Rotation* outputs the XYZ :term:`Euler` rotation of each top-level instance in the
local space of the modifier object.

The :doc:`/modeling/geometry_nodes/instances` page contains more information about geometry instances.

.. note::

   Though rotations are often displayed in units of degrees in the spreadsheet or node editor,
   they are stored internally in radians, so this node outputs radians.

Inputs
======

This node has no inputs.


Outputs
=======

Rotation
   Vector that indicates the rotation of each top-level instance in radians.
