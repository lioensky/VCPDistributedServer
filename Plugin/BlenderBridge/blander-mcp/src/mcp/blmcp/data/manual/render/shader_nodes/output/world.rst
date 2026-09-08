.. _bpy.types.ShaderNodeOutputWorld:

*****************
World Output Node
*****************

.. figure:: /images/node-types_ShaderNodeOutputWorld.webp
   :align: right
   :alt: World Node.

The *World Output* node is used to output color information to the scene's
:doc:`World </render/lights/world>`.

To access this node, change the *Shader Type* in the header of
the Shader Editor to *World*.

Inputs
======

Surface
   The appearance of the environment.
   Usually connected to a :doc:`Background </render/shader_nodes/shader/background>` shader.
Volume
   Used to add volumetric effects to the world.
   See the shaders :doc:`Principled Volume </render/shader_nodes/shader/volume_principled>`,
   :doc:`Volume Absorption </render/shader_nodes/shader/volume_absorption>`,
   and :doc:`Volume Scatter </render/shader_nodes/shader/volume_scatter>` for more information.

   .. note::

      It's not possible to have a Surface and a Volume at the same time: surfaces are assumed to be
      at an infinite distance from the camera, so they will always be fully occluded by the volume.


Properties
==========

Target
   Render engine the input shaders are used for.
   By default, shaders are shared between Cycles and EEVEE --
   with multiple output nodes, a specialized shader setup can be created for each.


Outputs
=======

This node has no outputs.
