.. _bpy.types.Bone.use_deform:

******
Deform
******

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Bone --> Deform`

.. figure:: /images/animation_armatures_bones_properties_deform_panel.png

   The Deform panel.

In this panel you can set deformation options for each bone.

Toggling the checkbox in the panel header off,
prevents the bone from deforming the geometry at all,
overriding any weights that it might have been assigned before; it mutes its influence.

It also excludes the active bone in the automatic weight calculation when the mesh is
parented to the armature using the *Armature Deform* tool with the *With Automatic Weights* option.


.. _armature-bones-envelope:

Envelope
========

.. figure:: /images/animation_armatures_bones_structure_envelope-edit-mode.png
   :align: right
   :figwidth: 180px

   Bone influence areas for envelopes method.

Envelopes is the most general skinning method. It works with all available object types for
skinning (meshes, lattices, curves, surfaces and texts).
It is based on proximity between bones and their geometry,
each bone having two different areas of influence,
shown in the *Envelope* visualization:

- The inside area, materialized by the "solid" part of the bone, and controlled by both root and tip radius.
- The outside area, materialized by the lighter part around the bone,
  and controlled by the *Distance* setting.

.. container:: lead

   .. clear

.. seealso::

   The :doc:`editing pages </animation/armatures/bones/editing/transform>` for how to edit these properties.

.. _bpy.types.Bone.envelope_distance:

Envelope Distance
   The Distance defines a volume which is the range within the bone
   has an influence on vertices of the deformed object.
   The geometry is less and less affected by the bone as it goes away by following a quadratic decay.

   .. figure:: /images/animation_armatures_bones_properties_deform_envelope-distance.png

      Single bone with various envelope sizes.

.. _bpy.types.Bone.envelope_weight:

Envelope Weight
   A bone property, that controls the global influence of the bone over the deformed object,
   when using the envelopes method.

   It is only useful for the parts of geometry that are "shared",
   influenced by more than one bone (generally, at the joints...) -- a bone with a high weight will
   have more influence on the result than one with a low weight...
   Note that when set to 0.0, it has the same effect as disabling the *Deform* option.

.. _bpy.types.Bone.use_envelope_multiply:

Envelope Multiply
   This option controls how the two deforming methods interact, when they are both enabled.
   By default, when they are both active, all vertices belonging to at least one vertex group are only deformed
   through the vertex groups method. The other "orphan" vertices being handled by the envelopes one.
   When you enable this option, the "deformation influence" that this bone would have on a vertex
   (based from its envelope settings) is multiplied with this vertex's weight in the corresponding vertex group.
   In other words, the vertex groups method is further "weighted" by the envelopes method.

.. _bpy.types.Bone.head_radius:
.. _bpy.types.Bone.tail_radius:

Radius Head, Tail
   Set the radius for the head and the tail of envelope bones.
   Inside this volume, the geometry if fully affected by the bone.

   .. figure:: /images/animation_armatures_bones_properties_deform_envelope-radius.png

      Three Armature Bones all using Envelope Weight.

      The 1st with a default radius value, the two others with differing Tail and Head radius values.
