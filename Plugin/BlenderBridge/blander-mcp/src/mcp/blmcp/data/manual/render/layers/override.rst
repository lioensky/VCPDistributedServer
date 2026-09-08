
*******************
View Layer Override
*******************

.. reference::

   :Panel:     :menuselection:`Properties --> View Layer --> Override`

View Layer overrides allow selectively replacing certain scene-level settings for a specific view layer.
This is useful for rendering multiple versions of a scene, for example, with different materials, lighting,
or sampling settings, without modifying the original scene data.

Overrides are applied only when rendering the specific view layer and do not affect the scene globally.

.. _bpy.types.ViewLayer.material_override:

Material Override
   Replaces all materials used in the view layer with a single material.
   This is often used for clay renders or lighting passes where the original material data is not needed.

   .. tip::

      Use a neutral diffuse material for previewing lighting or form without distractions from textures or shaders.

.. _bpy.types.ViewLayer.world_override:

World Override
   Replaces the scene's world settings (such as background color or HDRI lighting) for the current view layer.

   This can be used to render different lighting conditions
   or to isolate objects against a flat background for compositing.

.. _bpy.types.ViewLayer.samples:

Samples
   Allows the view layer to use a different number of samples than the main scene.
   This is controlled by the :ref:`Layer Samples <bpy.types.CyclesRenderSettings.use_layer_samples>`
   when using the Cycles renderer. When using EEVEE, the *Samples* override is always used.

   Lowering the number of samples for background or utility passes can speed up render times,
   while still using higher samples for beauty passes.
