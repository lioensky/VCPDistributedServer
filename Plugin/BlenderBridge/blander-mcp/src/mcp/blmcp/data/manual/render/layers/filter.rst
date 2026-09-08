
******
Filter
******

These options control which types of data are included in the final render for the current view layer.

.. _bpy.types.ViewLayer.use_sky:

Include
   Environment :guilabel:`Cycles`, :guilabel:`EEVEE`
      Disables rendering the *Environment* render pass in the final render.

   .. _bpy.types.ViewLayer.use_solid:

   Surfaces :guilabel:`Cycles`, :guilabel:`EEVEE`
      Disables rendering object materials in the final render.

   .. _bpy.types.ViewLayer.use_strand:

   Curves :guilabel:`Cycles`, :guilabel:`EEVEE`
      Disables rendering curve strands in the final render.

   .. _bpy.types.ViewLayer.use_volumes:

   Volume :guilabel:`Cycles`, :guilabel:`EEVEE`
      Disables rendering :doc:`Volumes </modeling/volumes/index>` in the final render.

   .. _bpy.types.ViewLayer.use_grease_pencil:

   Grease Pencil :guilabel:`Cycles`, :guilabel:`EEVEE`
      Render Grease Pencil objects on current layer

.. _bpy.types.ViewLayer.use_motion_blur:

Use
   Motion Blur :guilabel:`Cycles`, :guilabel:`EEVEE`
      Render motion blur for current layer,
      if enabled in the :ref:`Render Settings <bpy.types.RenderSettings.use_motion_blur>`.
