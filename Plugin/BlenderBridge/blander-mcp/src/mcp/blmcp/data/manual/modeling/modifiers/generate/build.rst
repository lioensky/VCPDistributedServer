.. index:: Modeling Modifiers; Build Modifier
.. _bpy.types.BuildModifier:

**************
Build Modifier
**************

The *Build* modifier causes the faces of the mesh object to appear or disappear one after the other over time.

By default, faces appear in the order in which they are stored in memory (by default, the order of creation).
The face/vertex order can be altered in Edit Mode by using :ref:`Sort Mesh Elements <mesh-edit-sort-elements>`.


Options
=======

.. figure:: /images/modeling_modifiers_generate_build_panel.png
   :align: right
   :width: 300px

   The Build modifier.

Start Frame
   The start frame of the building process.

Length
   The number of frames over which to rebuild the object.

Reversed
   The modifier will operate in reverse, essentially allowing it to be used as a "deconstruction" effect.
   This is useful for making a set of instancing objects gradually disappear.


Randomize
---------

Randomizes the order in which the faces are built.

Seed
   The random seed.
   Changing this value gives a different "random" order when *Randomize* is checked.
   This order is always the same for a given seed/mesh set.


Example
=======

The Build modifier can be used to make a large number of items to progressively appear,
without resorting to animating the visibility of each one by one. Examples of this include
a mesh containing vertices only, which is used as
an :doc:`Instancing Vertex emitter </scene_layout/object/properties/instancing/verts>`,
and has the Build modifier on it. Such a setup is a workaround/technique for being able to art-direct
a semi-random layout of a collection of objects (e.g. leaves/balls forming a carpet).
This can be preferable to particles e.g. due to undesirable distribution of items leaving random gaps
and overlapping in other places.

.. peertube:: 2b0eadea-17ac-4c08-90ec-fc603d7effa4
