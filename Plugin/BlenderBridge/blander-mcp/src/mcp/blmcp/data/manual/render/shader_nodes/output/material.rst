.. _bpy.types.ShaderNodeOutputMaterial:

********************
Material Output Node
********************

.. figure:: /images/node-types_ShaderNodeOutputMaterial.webp
   :align: right
   :alt: Material Output Node.

The *Material Output* node is used to output surface material information to a surface object.


Inputs
======

Surface
   Shading for the :doc:`surface </render/materials/components/surface>` of the object.
Volume
   Shading for the :doc:`volume </render/materials/components/volume>` inside the object.
Displacement
   Used to create bump mapping or actual subdivided :doc:`displacement </render/materials/components/displacement>`.
Thickness :guilabel:`EEVEE`
   Used to approximate the inner geometry structure of the object without heavy computation.
   This is currently used for :doc:`Subsurface Scattering </render/shader_nodes/shader/sss>`,
   :doc:`Translucent BSDF </render/shader_nodes/shader/translucent>`,
   :doc:`Refraction BSDF </render/shader_nodes/shader/refraction>`, and the nodes containing these effects.

   If no value is plugged into the output node,
   a default thickness based on the smallest dimension of the object is used.
   If a value is connected it will be used as object space thickness (i.e. scaled by object transform).
   A value of zero will disable the thickness approximation and treat the object as having only one interface.

   This output is only used by the EEVEE render engine.

   .. note::

      - The thickness is used to skip the inner part of the object.
      - Refraction will not refract objects inside the thickness distance.
      - Shadow casting object will not cast shadow within the thickness distance.

   .. tip::

      - For large or compound meshes (e.g. vegetation),
        the thickness should be set to the thickness of individual parts (e.g. leaves, grass blades).
      - Thickness can be baked to textures or custom attributes for more accurate result.

   .. seealso::

      :ref:`Thickness Mode <bpy.types.Material.thickness_mode>` -- controls how the thickness value is used.


Properties
==========

Target
   Render engine the input shaders are used for.
   By default shaders are shared between Cycles and EEVEE,
   with multiple output nodes specialized shader setups can be created for each.


Outputs
=======

This node has no outputs.
