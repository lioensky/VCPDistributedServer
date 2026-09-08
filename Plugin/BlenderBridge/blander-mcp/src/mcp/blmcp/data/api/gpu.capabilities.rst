GPU Capabilities Utilities (gpu.capabilities)
=============================================

.. module:: gpu.capabilities

This module provides access to the GPU capabilities.

.. function:: compute_shader_support_get()

   Are compute shaders supported.

   :return: True when supported, False when not supported.
   :rtype: bool


.. function:: extensions_get()

   Get supported extensions in the current context.

   :return: Extensions.
   :rtype: tuple[str, ...]


.. function:: hdr_support_get()

   Return whether GPU backend supports High Dynamic range for viewport.

   :return: HDR support available.
   :rtype: bool


.. function:: max_batch_indices_get()

   Get maximum number of vertex array indices.

   :return: Number of indices.
   :rtype: int


.. function:: max_batch_vertices_get()

   Get maximum number of vertex array vertices.

   :return: Number of vertices.
   :rtype: int


.. function:: max_images_get()

   Get maximum supported number of image units.

   :return: Number of image units.
   :rtype: int


.. function:: max_texture_layers_get()

   Get maximum number of layers in texture.

   :return: Number of layers.
   :rtype: int


.. function:: max_texture_size_get()

   Get estimated maximum texture size to be able to handle.

   :return: Texture size.
   :rtype: int


.. function:: max_textures_frag_get()

   Get maximum supported texture image units used for
   accessing texture maps from the fragment shader.

   :return: Texture image units.
   :rtype: int


.. function:: max_textures_geom_get()

   Get maximum supported texture image units used for
   accessing texture maps from the geometry shader.

   :return: Texture image units.
   :rtype: int


.. function:: max_textures_get()

   Get maximum supported texture image units used for
   accessing texture maps from the vertex shader and the
   fragment processor.

   :return: Texture image units.
   :rtype: int


.. function:: max_textures_vert_get()

   Get maximum supported texture image units used for
   accessing texture maps from the vertex shader.

   :return: Texture image units.
   :rtype: int


.. function:: max_uniforms_frag_get()

   Get maximum number of values held in uniform variable
   storage for a fragment shader.

   :return: Number of values.
   :rtype: int


.. function:: max_uniforms_vert_get()

   Get maximum number of values held in uniform variable
   storage for a vertex shader.

   :return: Number of values.
   :rtype: int


.. function:: max_varying_floats_get()

   Get maximum number of varying variables used by
   vertex and fragment shaders.

   :return: Number of variables.
   :rtype: int


.. function:: max_vertex_attribs_get()

   Get maximum number of vertex attributes accessible to
   a vertex shader.

   :return: Number of attributes.
   :rtype: int


.. function:: max_work_group_count_get(index)

   Get maximum number of work groups that may be dispatched to a compute shader.

   :param index: Index of the dimension.
   :type index: int
   :return: Maximum number of work groups for the queried dimension.
   :rtype: int


.. function:: max_work_group_size_get(index)

   Get maximum size of a work group that may be dispatched to a compute shader.

   :param index: Index of the dimension.
   :type index: int
   :return: Maximum size of a work group for the queried dimension.
   :rtype: int


.. function:: shader_image_load_store_support_get()

   Is image load/store supported.

   :return: True when supported, False when not supported.
   :rtype: bool


