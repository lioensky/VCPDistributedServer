gpu_extras submodule (gpu_extras.batch)
=======================================

.. module:: gpu_extras.batch

.. function:: batch_for_shader(shader, type, content, *, indices=None)

   Return a batch already configured and compatible with the shader.
   
   :param shader: shader for which a compatible format will be computed.
   :type shader: :class:`gpu.types.GPUShader`
   :param type: The primitive type of batch geometry.
   :type type: Literal['POINTS', 'LINES', 'TRIS', 'LINE_STRIP', 'TRI_STRIP', 'LINES_ADJ', 'TRIS_ADJ', 'LINE_STRIP_ADJ']
   :param content: Maps the name of the shader attribute with the data to fill the vertex buffer.
      For the dictionary values see documentation for :class:`gpu.types.GPUVertBuf.attr_fill` data argument.
   :type content: dict[str, Buffer | Sequence[float] | Sequence[int] | Sequence[Sequence[float]] | Sequence[Sequence[int]]]
   :return: compatible batch
   :rtype: :class:`gpu.types.GPUBatch`

