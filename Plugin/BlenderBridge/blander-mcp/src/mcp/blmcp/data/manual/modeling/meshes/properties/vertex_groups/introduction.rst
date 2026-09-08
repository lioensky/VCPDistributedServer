
************
Introduction
************

.. figure:: /images/modeling_meshes_properties_vertex-groups_introduction_panel.png
   :align: right

   The Vertex Groups panel.

Vertex groups are primarily used to tag vertices that belong to specific parts of a mesh or :term:`Lattice` object.
For example, they can represent the legs of a chair, the hinges of a door, or the arms, hands, and head of a
character.

Each vertex group can store a weight value for each vertex it includes. These weights are in the range of 0 to 1 and
are used by many operators, tools, and modifiers, which is why vertex groups are sometimes also referred to as "weight
groups".

Usage
=====


Vertex groups can be created manually or generated automatically. They are most commonly used for armature-based
deformation (also called *skinning*), but they are also used in many other areas of Blender, such as:

- Shape keys
- Modifiers
- Particle systems
- Physics simulations

.. seealso::

   :doc:`Skinning Mesh Objects </animation/armatures/skinning/introduction>`

.. note::

   Vertex groups are only available for mesh and lattice objects.
