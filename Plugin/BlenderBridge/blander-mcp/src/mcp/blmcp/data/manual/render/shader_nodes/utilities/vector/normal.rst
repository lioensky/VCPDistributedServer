.. _bpy.types.ShaderNodeNormal:

***********
Normal Node
***********

.. figure:: /images/node-types_ShaderNodeNormal.webp
   :align: right
   :alt: Normal Node.

The Normal node generates a normal vector and a dot product.


Inputs
======

Normal
   Normal vector input.


Properties
==========

Normal Direction
   To manually set a fixed normal direction vector.
   :kbd:`LMB` click and drag on the sphere to set the direction of the normal.
   Holding :kbd:`Ctrl` while dragging snaps to 45 degree rotation increments.


Outputs
=======

Normal
   Normal vector output.
Dot
   Dot product output. The dot product is a scalar value.

   - If two normals are pointing in the same direction the dot product is 1.
   - If they are perpendicular the dot product is zero (0).
   - If they are antiparallel (facing directly away from each other) the dot product is -1.
