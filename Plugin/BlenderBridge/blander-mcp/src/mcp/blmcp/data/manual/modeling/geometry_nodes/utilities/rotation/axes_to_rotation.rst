.. index:: Geometry Nodes; Axis to Rotation
.. _bpy.types.FunctionNodeAxesToRotation:

*********************
Axes to Rotation Node
*********************

.. figure:: /images/node-types_FunctionNodeAxesToRotation.webp
    :align: right
    :alt: Axis to Rotation node.

Creates a rotation based on two axis directions.

.. tip::

   In many cases, these directions are a normal and tangent on a mesh or curve.


Inputs
======

Primary Axis
   The desired direction of the primary axis.

Secondary Axis
   The desired direction of the secondary axis. Ideally, this is orthogonal to the primary direction.


Properties
==========

Primary Axis
   The axis (X, Y or Z) that should be aligned exactly to the primary direction.

Secondary Axis
   The axis that should be aligned as closely as possible to the secondary direction.


Outputs
=======

Rotation
    The rotation that results in the given axes being aligned to the given directions.
