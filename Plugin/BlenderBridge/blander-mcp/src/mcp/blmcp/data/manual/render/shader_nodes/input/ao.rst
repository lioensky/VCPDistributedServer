.. _bpy.types.ShaderNodeAmbientOcclusion:

**********************
Ambient Occlusion Node
**********************

.. figure:: /images/node-types_ShaderNodeAmbientOcclusion.webp
   :align: right
   :alt: Ambient Occlusion node.

The *Ambient Occlusion* node computes how much the hemisphere above the shading point is occluded.
This can be used for procedural texturing, for example to add weathering effects to corners only.

For Cycles, this is an expensive shader and can slow down render significantly.
If render time is a concern, using Pointiness from the Geometry node or baking Ambient Occlusion will result
in faster renders.

.. note::

   :guilabel:`Cycles Only`
    The Ambient Occlusion node will not produce a valid result when:
     - The object is either a :ref:`Caustic caster <bpy.types.CyclesObjectSettings.is_caustics_caster>`
       or :ref:`Caustic receiver <bpy.types.CyclesObjectSettings.is_caustics_receiver>` while the scene
       contains an active :ref:`Caustic caster <bpy.types.CyclesObjectSettings.is_caustics_caster>`,
       :ref:`Caustic receiver <bpy.types.CyclesObjectSettings.is_caustics_receiver>`, and
       :ref:`Shadow Caustic Light <bpy.types.CyclesLightSettings.is_caustics_light>`.
     - :doc:`/render/cycles/osl/index` is active while using the OptiX rendering backend.

.. seealso::

   The :ref:`bpy.types.ViewLayer.use_pass_ambient_occlusion` pass gives occlusion factors
   across the whole render for use in compositing.

Inputs
======

Color
   Tint for AO output color.
Distance
   Distance up to which other objects are considered to occlude the shading point.
Normal
   Normal used for ambient occlusion; if nothing is connected the default shading normal is used.


Properties
==========

Samples
   Number of samples to use for ray-traced ambient occlusion sampling.
   Keep as low as possible for optimal performance.
Inside
   Detect convex rather than concave shapes, by computing occlusion inside mesh.
Only Local :guilabel:`Cycles Only`
   Only detect occlusion from the object itself, and not others.


Outputs
=======

Color
   Ambient occlusion with color tint.
AO
   Ambient occlusion factor without color tint.


Example
=======

.. figure:: /images/render_shader-nodes_input_ao_example.jpg

   White AO shader.
