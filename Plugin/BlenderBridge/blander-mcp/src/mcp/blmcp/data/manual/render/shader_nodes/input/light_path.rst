.. _bpy.types.ShaderNodeLightPath:

***************
Light Path Node
***************

.. figure:: /images/node-types_ShaderNodeLightPath.webp
   :align: right
   :alt: Light Path Node.

The *Light Path* node is used to find out for which kind of incoming ray the shader is being executed;
particularly useful for non-physically-based tricks. More information about the meaning of each type
is in the :doc:`Light Paths </render/cycles/render_settings/light_paths>` documentation.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Is Camera Ray
   1.0 if shading is executed for a camera ray, otherwise 0.0.
Is Shadow Ray
   1.0 if shading is executed for a shadow ray, otherwise 0.0.
Is Diffuse Ray
   1.0 if shading is executed for a diffuse ray, otherwise 0.0.
Is Glossy Ray
   1.0 if shading is executed for a glossy ray, otherwise 0.0.
Is Singular Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a singular ray, otherwise 0.0.
Is Reflection Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a reflection ray, otherwise 0.0.
Is Transmission Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a transmission ray, otherwise 0.0.
Is Volume Scatter Ray :guilabel:`Cycles Only`
   1.0 if shading is executed for a volume scatter ray, otherwise 0.0.
Ray Length :guilabel:`Cycles Only`
   Distance traveled by the light ray from the last bounce or camera.
Ray Depth
   Number of times the ray has been reflected or transmitted on interaction with a surface.

   .. note::

      Passing through a
      :ref:`transparent <render-cycles-light-paths-transparency>`
      shader does not count as a normal "bounce".

Diffuse Depth :guilabel:`Cycles Only`
   Number of times the ray has gone through diffuse reflection or transmission.
Glossy Depth :guilabel:`Cycles Only`
   Number of times the ray has gone through glossy reflection or transmission.
Transparent Depth :guilabel:`Cycles Only`
   Number of times the ray has gone through a transparent surface.
Transmission Depth :guilabel:`Cycles Only`
   Number of times the ray has gone through a transmissive surface.
   A typical use case is to avoid black spots in the render (caused by rays hitting
   the bounce limit) by switching from a transmissive to a diffuse shader past a
   certain point. See :doc:`/render/shader_nodes/shader/mix`.
Portal Depth: :guilabel:`Cycles Only`
   Number of times the ray has passed through a :doc:`/render/shader_nodes/shader/ray_portal`.

EEVEE Support
=============

EEVEE has no real concept of rays, but in order to ease the workflow between Cycles and EEVEE,
some of the outputs are supported in particular cases.

- *Is Camera*: Supported.
- *Is Shadow*: Supported.
- *Is Diffuse*: Supported.
- *Is Glossy*: Supported.
- *Is Singular*: Not supported. Same as *Is Glossy*.
- *Is Reflection*: Not supported. Same as *Is Glossy*.
- *Is Transmission*: Not supported. Same as *Is Glossy*.
- *Ray Length*: Distance from the camera to the shading point.
- *Ray Depth*: Indicates the current bounce when baking the light cache.
- *Diffuse Depth*: Same as Ray Depth but only when baking diffuse light.
- *Glossy Depth*: Same as Ray Depth but only when baking specular light.
- *Transparent Depth*: Not supported. Defaults to 0.
- *Transmission Depth*: Not supported. Same as *Glossy Depth*.

.. note::

   *Is Glossy* does not work with Screen Space Reflections/Refractions
   but does work with reflection planes (whether used with SSR or not).
