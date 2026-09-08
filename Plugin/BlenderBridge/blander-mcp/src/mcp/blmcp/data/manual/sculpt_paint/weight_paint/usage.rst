
*******************
Using Vertex Groups
*******************

.. _weight-painting-bones:

Vertex Groups for Bones
=======================

This is one of the main uses of weight painting. While you can have Blender
generate the weights automatically (see the
:doc:`skinning section </animation/armatures/skinning/index>`),
you may want to tweak them or even create them from scratch,
especially around joints.

The process is as follows:

#. Select the armature and bring it into *Pose Mode* by pressing :kbd:`Ctrl-Tab`.
#. Make sure that :menuselection:`Edit --> Lock Object Modes` is unchecked
   in the topbar.
#. Select the mesh and bring it into *Weight Paint Mode*.
#. Make sure that *Bone Selection* is checked in the 3D Viewport's header.
#. Select a bone using :kbd:`Alt-LMB` (or :kbd:`Shift-Ctrl-LMB`).
   This will activate the bone's vertex group and display its current weights on the mesh.
#. Paint weights for the bone using :kbd:`LMB`.

.. note::

   You can only select one bone at a time in this mode.

.. tip::

   The bones are likely embedded inside the mesh, making them invisible and
   unselectable. To get around this, you can enable :ref:`In Front <bpy.types.Object.show>`
   for the armature.

If a bone doesn't have a vertex group yet when you start painting,
Blender will create one automatically.

If you have a symmetrical mesh and a symmetrical armature, you can use
:ref:`Mirror Vertex Groups <bpy.types.Mesh.use_mirror_vertex_groups>`
to automatically create vertex groups and weights for the other side.


Vertex Groups for Particles
===========================

.. figure:: /images/sculpt-paint_weight-paint_usage_particles.png
   :width: 320px

   Weight painted particle emission.

By selecting vertex groups in the :doc:`Vertex Groups </physics/particles/emitter/vertex_groups>`
panel of a :doc:`particle system </physics/particles/introduction>`'s properties,
you can have different particle densities, hair lengths etc. across different areas of the mesh.
