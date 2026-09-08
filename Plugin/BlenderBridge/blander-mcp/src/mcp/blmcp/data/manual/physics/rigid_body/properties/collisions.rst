
**********
Collisions
**********

.. reference::

   :Panel:     :menuselection:`Physics --> Rigid Body --> Collisions`

.. figure:: /images/physics_rigid-body_properties_collisions_panel.png

   Rigid Body Collisions panel.

.. _bpy.types.RigidBodyObject.collision_shape:

Shape
   Determines the collision shape of the object;
   these can be broken into two categories: primitive shapes and mesh based shapes.

   Primitive shapes (*Box*, *Sphere*, *Capsule*, *Cylinder*, and *Cone*)
   are best in terms of memory and performance but do not
   necessarily reflect the actual shape of the object.
   The size of the shape is calculated based on the object's bounding box.
   The center of gravity is always in the geometric center of the shape.
   Primitive shapes can be shown in the 3D Viewport by enabling
   :ref:`Extras Overlay <bpy.types.View3DOverlay.show_extras>`.

   Mesh based shapes (*Convex Hull* and *Mesh*) are calculated based on the geometry of the object
   so they are a better representation of the object.
   The center of gravity for these shapes is the object origin.

   :Box:
      Box-like shapes (e.g. cubes), including planes (e.g. ground planes).
      The size per axis is calculated from the bounding box.
   :Sphere:
      Sphere-like shapes. The radius is the largest axis of the bounding box.
   :Capsule:
      This points up the Z axis.
   :Cylinder:
      This points up the Z axis.
      The height is taken from the Z axis, while the radius is the larger of the X or Y axes.
   :Cone:
      This points up the Z axis.
      The height is taken from the Z axis, while the radius is the larger of the X or Y axes.
   :Convex Hull:
      A mesh-like surface encompassing (e.g. shrink-wrapped over) all vertices (best results with fewer vertices).
      A convex approximation of the object, which has good performance and stability.
   :Mesh:
      :term:`Mesh` consisting of triangles only, allowing for more detailed interactions than convex hulls.
      Allows simulating concave objects, but is rather slow and unstable.
   :Compound Parent:
      Takes the collision shapes from the object's :doc:`children </scene_layout/object/editing/parent>`
      and combines them. This makes it possible to create concave shapes from primitive shapes.
      This usually results in a faster simulation than the *Mesh* collision shape
      while also being generally more stable.

.. _bpy.types.RigidBodyObject.mesh_source:

Source
   Source of the mesh used to create the collision shape.

   :Base:
      The base mesh of the object.
   :Deform:
      Includes any deformations added to the mesh (shape keys, deform modifiers).
   :Final:
      Includes all deformations and modifiers.

.. _bpy.types.RigidBodyObject.use_deform:

Deforming
   Mesh shapes can deform during simulation.


Surface Response
================

.. _bpy.types.RigidBodyObject.friction:

Friction
   Resistance of object to movement. Specifies how much velocity is lost when objects collide with each other.

.. _bpy.types.RigidBodyObject.restitution:

Bounciness
   Tendency of object to bounce after colliding with another (0 to 1) (rigid to perfectly elastic).
   Specifies how much objects can bounce after collisions.


Sensitivity
===========

The collision margin is used to improve the performance and stability of rigid bodies.
Depending on the shape, it behaves differently: some shapes embed it,
while others have a visible gap around them.

The margin is *embedded* for these shapes:

- Sphere
- Box
- Capsule
- Cylinder
- Convex Hull: Only allows for uniform scale when embedded.

The margin is *not embedded* for these shapes:

- Cone
- Active Triangle Mesh
- Passive Triangle Mesh: Can be set to 0 most of the time.

.. _bpy.types.RigidBodyObject.collision_margin:

Margin
   Threshold of distance near the surface where collisions are still considered (best results when nonzero).


.. _bpy.types.RigidBodyObject.collision_collections:

Collections
===========

Allows rigid body collisions allocate on different groups (maximum 20).
