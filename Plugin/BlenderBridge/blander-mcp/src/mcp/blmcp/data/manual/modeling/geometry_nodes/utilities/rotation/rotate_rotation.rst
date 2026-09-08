.. index:: Geometry Nodes; Rotate Rotation
.. _bpy.types.FunctionNodeRotateRotation:

********************
Rotate Rotation Node
********************

.. figure:: /images/node-types_FunctionNodeRotateRotation.webp
   :align: right
   :alt: Rotate Euler node.

The *Rotate Rotation* node applies an additional rotation to a given one.

To rotate an :term:`Euler Rotation`, first use the
:doc:`/modeling/geometry_nodes/utilities/rotation/euler_to_rotation`.


Inputs
======

Rotation
   The starting rotation.

Rotate By
   The additional rotation.


Properties
==========

Space
   :Global: Rotate in :term:`Global Space`.
   :Local: Rotate in :term:`Local Space`.


Outputs
=======

Rotation
   The resulting rotation.
