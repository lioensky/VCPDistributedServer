.. index:: Modeling Modifiers; Explode Modifier
.. _bpy.types.ExplodeModifier:

****************
Explode Modifier
****************

The *Explode* modifier is used to alter the mesh geometry by moving/rotating its faces in a way
that roughly tracks particles emitted by that object, making it look as if the mesh is being exploded
(broken apart and pushed outward).

For this modifier to have any visible effect, there needs to be a particle system on its object.
That particle system will control how the mesh is exploded.

Both the number of emitted particles and number of faces determine how granular the *Explode* modifier is.
More of each faces and particles will mean more individual pieces.

Here is a
`demo video <https://archive.blender.org/wiki/2015/index.php/File:Manual_-_Explode_Modifier_-_Exploding_Cube_
-_2.5.ogg/>`__
showing a cube with a particle system and *Explode* modifier.
(`blend-file <https://archive.blender.org/wiki/2015/index.php/File:Manual_-_Explode_Modifier_-_Exploding_Cube_
-_2.5.blend>`__).

.. note::

   The *Explode* modifier must come after the *Particle System* one in the :ref:`modifier stack <modifier-stack>`,
   in order for the former to get required data from the later.


Options
=======

.. figure:: /images/modeling_modifiers_physics_explode_panel.png
   :align: right
   :width: 300px

   The Explode modifier, with a Particle System above it.

Particle UV
   If set, the U value of the coordinates in that :term:`UV Map` will be overwritten
   with the age of the particle attached to the matching mesh face
   (in proportion, from 0 for not yet born particles, to 1 for dead ones).

   The V value is set to a constant 0.5 value.

   You can for example vary the color of a fragment (face) during the explosion phase,
   by using a texture with a color gradient along its *U* axis.

Show
   Unborn
      Show faces when their attached particles are unborn.
   Alive
      Show faces when their attached particles are alive.
   Dead
      Show faces when their attached particles are dead.

Cut Edges
   Split the mesh in pieces based on location of emitted particles, instead of using existing faces.
   This will typically results in a splitting that appears more random.

Size
   Scale each face using the size of its attached particle, once that particle is alive.

Vertex Group
   Vertices in this group may not be affected by the *Explode* modifier.
   Vertices with full weight are not affected at all,
   while vertices with less weight have a higher chance of being affected.

   Vertices with null weight will be treated like those which do not belong to the group at all,
   and explode normally.

   :bl-icon:`arrow_leftright` Invert
      Inverts the influence of the selected vertex group, meaning that the group
      now represents vertices that will not be deformed by the modifier.

      The setting reverses the weight values of the group.

Protect
   Clean vertex group edges. Depending on the weights assigned to that vertex group,
   either completely protect those faces from being affected by the *Explode* modifier
   (which would happen if the faces had a weight value of 1),
   or completely remove protection from those faces
   (which would happen if the faces had a weight value of 0).

Refresh
   Refresh data in the *Explode* modifier.


Known Limitations
=================

Dynamic Vertex Weights
----------------------

This modifier uses the initial vertex weights.
Modifiers that dynamically change weights will not influence the explosion as these values are only used once.

.. Ref #77654
