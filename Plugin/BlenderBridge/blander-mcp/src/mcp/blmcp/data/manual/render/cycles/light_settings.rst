
***********************
Light Settings (Cycles)
***********************

.. reference::

   :Panel:     :menuselection:`Properties --> Object Data`
               and :menuselection:`Shader Editor --> Sidebar --> Options`

Next to lighting from the background and any object with an emission shader,
lights are another way to add light into the scene.
The difference is that they are not directly visible in the rendered image,
and can be more easily managed as objects of their own type.


Light
=====

:doc:`Light settings </render/lights/light_object>` for all renderers.

Beam Shape
----------

.. _bpy.types.AreaLight.spread:

Spread :guilabel:`Area Lights`
   How wide the emitted light fans out controlling how diffused the area light is.
   Larger values create soft shadows while smaller values create sharper light
   simulating a `gridded softbox <https://en.wikipedia.org/wiki/Softbox>`__.

   .. figure:: /images/render_lights_light-object-area-spread.png

      Example of Spread at different angles.


Settings
========

.. _bpy.types.CyclesLightSettings.max_bounces:

Max Bounces
   Maximum number of times light from the light is allowed to :term:`Bounce <Light Bounces>`.
   Limited by :ref:`scene-wide bounce settings <bpy.types.CyclesRenderSettings.max_bounces>`.

Cast Shadow
   By disabling this option, light from lights will not be blocked by objects in between.
   This can speed up rendering by not having to trace rays to the light source.

.. _bpy.types.CyclesLightSettings.use_multiple_importance_sampling:

Multiple Importance Sample
   By default lights use only direct light sampling. For area lights and sharp glossy reflections, however,
   this can be noisy,
   and enabling this option will enable indirect light sampling to be used in addition to reduce noise.

.. _bpy.types.CyclesLightSettings.is_caustics_light:

Shadow Caustics
   Mark a light as a refractive caustic caster. This setting can be used in conjunction with the
   :ref:`Cast and Receive caustics object settings <bpy.types.CyclesObjectSettings.is_caustics_caster>`
   to selectively speed up refractive caustic rendering of select objects.

.. _render-cycles-lights-area-portals:

Portals :guilabel:`Area Lights`
   Area lights can also function as light portals to help sample the environment light,
   and significantly reduce noise in interior scenes.
   Note that rendering with portals is usually slower, but as it converges more quickly, less samples are required.

   Light portals work by enabling the *Portal* option, and placing areas lights in
   windows, door openings, and any place where light will enter the interior.

   In outdoor scenes most rays do not bounce much and just fly off into the sky and therefore,
   light portals are not helpful for outdoor scenes.

   .. figure:: /images/render_cycles_light-settings_portals2.jpg
   .. figure:: /images/render_cycles_light-settings_portals.jpg

      White Room model by Jay Hardy.


.. _cycles-light-nodes:

Nodes
=====

In Cycles, lights can be fully defined using shader nodes.
This allows creating complex, physically based light behavior that goes beyond
the basic light settings.

.. note::

   The basic :doc:`Light settings </render/lights/light_object>`
   are applied on top of the light output node.

Light shader nodes are edited in the :doc:`Shader Editor </render/shader_nodes/index>`
when the editor is set to *Light* context and a light object is selected.


Emission Shader
---------------

Light objects use an :doc:`Emission </render/shader_nodes/shader/emission>` shader
to define their output.

The *Emission* shader controls:

- **Color**: The spectral color of the emitted light.
- **Strength**: The intensity of the emitted light.

The output of the *Emission* shader must be connected to the
:doc:`Light Output </render/shader_nodes/output/light>` node.


Using Shader Nodes
------------------

By default, lights use a simple node setup consisting of an *Emission* shader
connected directly to the *Light Output*.

More advanced setups can be created using additional shader and utility nodes, for example:

- Mixing multiple *Emission* shaders to create layered light colors.
- Using :doc:`Texture </render/shader_nodes/textures/index>` nodes to vary light color
  or intensity across the light surface.
- Driving light intensity or color using math nodes or animation.

This makes it possible to create effects such as patterned lights, animated flicker,
or lights that change color based on time or other inputs.


Light Output
------------

The :doc:`Light Output </render/shader_nodes/output/light>` node defines the final
shader used by the light object.
Only shader nodes connected to this output affect the light's appearance in Cycles.


Limitations
-----------

- Shader-based light definitions are only supported in **Cycles**.
  EEVEE uses simplified light models and ignores light shader node trees.
- Only *Emission*-based shading contributes to lighting.
  Other shader types (such as *BSDF* shaders) have no effect when used on lights.

Using shader nodes for lights provides fine-grained control and enables procedural
lighting workflows that are not possible with standard light settings alone.
