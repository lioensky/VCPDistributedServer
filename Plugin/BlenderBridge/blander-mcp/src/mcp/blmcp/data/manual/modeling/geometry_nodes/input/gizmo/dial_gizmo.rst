.. index:: Geometry Nodes; Dial Gizmo
.. _bpy.types.GeometryNodeGizmoDial:

**********
Dial Gizmo
**********

.. figure:: /images/node-types_GeometryNodeGizmoDial.png
   :align: right
   :alt: Dial Gizmo Node.

The *Dial Gizmo* node is ideal for creating gizmos that control angles.

.. figure:: /images/node-types_GeometryNodeGizmoDial_viewport.png
   :align: right
   :alt: The gizmo in the viewport.

Inputs
======

Value
   Special gizmo value socket.
   Everything that linked into this socket will be modified when the gizmo is rotated.
Position
   Position of the gizmo in the local space of the object.
Up
   Up or normal direction of the gizmo in the viewport.
Screen Space
   If enabled, the gizmo will always have the same size in the viewport independent of the zoom level.
   This affects the meaning of the radius input.
Radius
   In screen space mode, this is a factor on top of the default radius.
   Otherwise, this is the radius of the gizmo in Blender units.


Properties
==========

Color
   Controls which theme color is used for this gizmo.


Outputs
=======

Transform
   Should be joined into the geometry that is controlled by this gizmo.
