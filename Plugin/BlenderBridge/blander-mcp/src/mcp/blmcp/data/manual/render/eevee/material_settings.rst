*********
Materials
*********

.. seealso::

   While EEVEE shares the same material node system as Cycles, not all features are supported.
   See :ref:`Shader nodes limitations <eevee-limitations-materials>`.


.. _eevee-materials-thickness:

Thickness
=========

.. reference::

   :Panel:     :menuselection:`Properties --> Material --> Thickness`

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


Material Settings
=================

.. reference::

   :Panel:     :menuselection:`Properties --> Material --> Settings`

Pass Index
   Index number for the *Material Index* :doc:`render pass </render/layers/passes>`.
   This can be used to give a mask to a material which then can be read with
   the :doc:`ID Mask Node </compositing/types/mask/id_mask>` in the Compositor.

   .. note::

      :doc:`Volume Objects </modeling/volumes/introduction>` do not support the pass index.


Surface
=======

.. _bpy.types.Material.use_backface_culling:

Backface Culling
   Backface Culling hides the back side of faces.
   This option should be turned on whenever it is possible, as it has an impact on performance.

   Camera
      Use back face culling to hide the back side of the face.

   Shadow
      Use back face culling when casting shadows.

   Light Probe Volume
      Use back face culling when baking :doc:`Light Probe Volumes </render/eevee/light_probes/volume>`.
      Additionally helps rejecting capture point inside the object to avoid light leaking

.. _bpy.types.Material.displacement_method:

Displacement
   Controls how the displacement output from the shader node tree is used.

   :Bump Only:
      Use Bump Mapping to simulated the appearance of displacement.
      This only modifies the shading normal of the object. Vertex position is not affected.
   :Displacement Only:
      This mode is not supported and falls back to *Displacement and Bump*.
   :Displacement and Bump:
      Combination of true displacement and bump mapping for finer details.
      Vertex position is modified.

   .. note::

      This type of displacement is not precomputed. It has a performance impact multiplied by the
      render sample count. However, the evaluation is much faster than doing it using geometry
      nodes or a displacement modifier.

   .. note::

      Displacing flat shaded geometry will split adjacent faces.
      This can be worked around by passing the vertex normals as a custom attribute.

.. _bpy.types.Material.max_vertex_displacement:

Max Distance
   The maximum distance a vertex can be displaced when using true displacement.
   Displacements over this threshold may cause visibility issues.
   These visibility issues can be observed when the object is out of view at the edge of screen
   with parts being displaced inside the view. The object would then disappear because of camera culling.
   This can also produce missing shadow updates where the displaced geometry is.

.. _bpy.types.Material.use_transparent_shadow:

Transparent shadows
   Use transparent shadows for this material if it contains a Transparent BSDF.
   Disabling will render faster but not give accurate shadows.

.. _bpy.types.Material.surface_render_method:

Render Method
   Controls the blending and the compatibility with certain features.

   :Dithered:
      Allows for grayscale hashed transparency, and compatible with render passes and raytracing.
      Also know as deferred rendering.

      When using *Dithered* render method, the materials are rendered in layers.
      Each layer can only transmit (e.g. refract) light emitted from previous layers.
      If no intersection with the layers below exists, the transmissive BSDFs will fallback to light probes.

      .. _bpy.types.Material.use_raytrace_refraction:

      Raytraced Transmission
         Use raytracing to determine transmitted color instead of using only light probes.
         This prevents the surface from contributing to the lighting of surfaces not using this setting.

   :Blended:
      Allows the colored transparency, but incompatible with render passes and raytracing.
      Also known as forward rendering.

      .. admonition:: Sorting Problem
         :class: important

         When using *Blended* render method, the order in which the color blending
         happens is important as it can change the final output color.
         EEVEE does not support per-fragment (pixel) sorting or per-triangle sorting.
         Only per-object sorting is available and is automatically done on all
         transparent surfaces based on object origin.
         Opaque surfaces (i.e. that have no transparency)
         will still have correct sorting regardless of the render method.

         .. tip::

            Face order can be adjusted in edit mode by using
            :doc:`sort element </modeling/meshes/editing/mesh/sort_elements>` or using a
            :doc:`geometry node </modeling/geometry_nodes/geometry/operations/sort_elements>`.

      .. note::

         Per-object sorting has a performance cost and having thousands of
         objects in a scene will greatly degrade performance.

.. _bpy.types.Material.use_transparency_overlap:

Transparency Overlap
   If enabled, all transparent fragments will be rendered.
   If disabled, only the front-most surface fragments will be rendered.
   This option can be disabled to fix sorting issues caused by blending order.
   Only available for the *Blended* render method.

.. _bpy.types.Material.thickness_mode:

Thickness
   Determines what model to use to approximate the object geometry.

   :Sphere:
      Approximate the object as a sphere whose diameter is equal to the thickness defined by the node tree.
      This is more suited to objects with rounder edges (e.g. a monkey head), and is perfectly suited to spheres.
   :Slab:
      Approximate the object as an infinite slab of thickness defined by the node tree.
      This is more suited to very flat or thin objects (e.g. glass panels, grass blades).

.. _bpy.types.Material.use_thickness_from_shadow:

From Shadow
   Use the shadow maps from shadow casting lights to refine the thickness defined by the material node tree.
   This takes the minimum thickness between the shadow map and the material node tree value.
   This is useful for objects where pre-computation is difficult (e.g. complex meshes), impossible
   (e.g. procedural geometry with displacement) or just impractical.
   However, this will have a performance impact that scale with the number of render samples.


Volume
======

.. _bpy.types.Material.volume_intersection_method:

Intersection
   Determines which inner part of the mesh will produce volumetric effect.

   :Fast:
      Each face is considered as a medium interface. Gives correct results for manifold geometry
      that contains no inner part.
   :Accurate:
      Faces are considered as medium interface only when they have different consecutive facing.
      Gives correct results as long as the max ray depth is not exceeded. Has significant memory
      overhead compared to the fast method.
