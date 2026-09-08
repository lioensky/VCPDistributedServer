.. index:: Geometry Nodes; Align Rotation to Vector
.. _bpy.types.FunctionNodeAlignRotationToVector:

*****************************
Align Rotation to Vector Node
*****************************

.. figure:: /images/node-types_FunctionNodeAlignRotationToVector.webp
   :align: center
   :alt: Align Rotation to Vector node.

The *Align Rotation to Vector* node rotates an Euler rotation into the given direction.


Inputs
======

Rotation
   The :term:`Euler` rotation to align.

   .. important::

      This input has to be a rotation input. Be careful not to connect a direction vector
      like the :doc:`normal </modeling/geometry_nodes/geometry/read/normal>`.

Factor
   Determines how much the points are rotated towards the vector.
   Zero effectively disables the node and one means that the points are aligned with the vector perfectly.

Vector
   The direction vector that points should be rotated to.
   The vector is in the local space of the object that is being modified.
   When it is all zeros for a point, it is not rotated at all.


Properties
==========

Axis
   Local axis of the object that is to be rotated towards the vector input.

Pivot
   The local axis to rotate around.

   :Auto:
      The best rotation angle is computed automatically.
      This minimizes the angle of rotation.
   :X, Y, Z:
      Rotate around a specific local axis.


Outputs
=======

Rotation
   The rotated Euler rotation.
