
*****
Shape
*****

.. reference::

   :Panel:     :menuselection:`Physics --> Cloth --> Shape`

.. figure:: /images/physics_cloth_settings_shape_pinning.png

   Cloth Shape.

.. _bpy.types.ClothSettings.vertex_group_mass:

Pin Group
   Vertex group to use for pinning.

   The shape of the cloth can be controlled by pinning cloth to
   a :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/index>`.
   There are several ways of doing this including
   :doc:`Weight Painting </sculpt_paint/weight_paint/index>` areas you want to pin.
   The weight of each vertex in the group controls how strongly it is pinned.

.. _bpy.types.ClothSettings.pin_stiffness:

Stiffness
   Target position stiffness.

.. _bpy.types.ClothSettings.use_sewing_springs:

Sewing
   Another method of restraining cloth similar to pinning is sewing springs.
   Sewing springs are virtual springs that pull vertices in one part of
   a cloth mesh toward vertices in another part of the cloth mesh.
   This is different from pinning which binds vertices of the cloth mesh in place or to another object.
   A clasp on a cloak could be created with a sewing spring.
   The spring could pull two corners of a cloak about a character's neck.
   This could result in a more realistic simulation than pinning the cloak to
   the character's neck since the cloak would be free to slide about the character's neck and shoulders.

   Sewing springs are created by adding extra edges to a cloth mesh that are not included in any faces.
   They should connect vertices in the mesh that should be pulled together.
   For example the corners of a cloak.

.. _bpy.types.ClothSettings.sewing_force_max:

Max Sewing Force
   Maximum force that can be applied by sewing springs. Zero means unbounded, but it is not
   recommended to leave the field at zero in most cases, as it can cause instability due to
   extreme forces in the initial frames where the ends of the sewing springs are far apart.

.. _bpy.types.ClothSettings.shrink_min:

Shrinking Factor
   Factor by which to shrink the cloth, specifying a negative value controls the amount for the cloth to grow.

.. _bpy.types.ClothSettings.use_dynamic_mesh:

Dynamic Mesh
   Allows animating the rest shape of cloth using shape keys or
   modifiers (e.g. an Armature modifier or any deformation modifier) placed above the Cloth modifier.
   When it is enabled, the rest shape is recalculated every frame, allowing unpinned
   cloth to squash and stretch following the character with the help of shape keys or modifiers, but
   otherwise move freely under control of the physics simulation.

   Normally cloth uses the state of the object in the first frame to compute
   the natural rest shape of the cloth, and keeps that constant throughout the simulation.
   This is reasonable for fully realistic scenes, but does not quite work for clothing
   on cartoon style characters that use a lot of squash and stretch.

.. _bpy.types.ClothSettings.rest_shape_key:

Rest Shape Key
   Allows starting the cloth simulation using a specific
   :doc:`Shape Key </animation/shape_keys/index>` as the rest state,
   instead of the shape that results from evaluating shape keys and preceding modifiers
   in the regular way. This option is mutually exclusive with *Dynamic Mesh*.

   This can be used to start the simulation with the cloth in a pre-draped state without
   applying that shape as a plastic deformation that relaxes all springs as a side effect.

   This property is only visible if the mesh has shape keys.
