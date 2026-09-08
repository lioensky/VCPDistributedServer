GPU Shader Utilities (gpu.shader)
=================================

.. module:: gpu.shader

This module provides access to GPUShader internal functions.

.. _built-in-shaders:

.. rubric:: Built-in shaders

All built-in shaders have the ``mat4 ModelViewProjectionMatrix`` uniform.

Its value must be modified using the :mod:`gpu.matrix` module.

.. important::

   Shader uniforms must be explicitly initialized to avoid retaining values from previous executions.

``FLAT_COLOR``
   :Attributes: vec3 pos, vec4 color
   :Uniforms: none
``IMAGE``
   :Attributes: vec3 pos, vec2 texCoord
   :Uniforms: sampler2D image
``IMAGE_SCENE_LINEAR_TO_REC709_SRGB``
   :Attributes: vec3 pos, vec2 texCoord
   :Uniforms: sampler2D image
   :Note: Expect texture to be in scene linear color space
``IMAGE_COLOR``
   :Attributes: vec3 pos, vec2 texCoord
   :Uniforms: sampler2D image, vec4 color
``IMAGE_COLOR_SCENE_LINEAR_TO_REC709_SRGB``
   :Attributes: vec3 pos, vec2 texCoord
   :Uniforms: sampler2D image, vec4 color
   :Note: Expect texture to be in scene linear color space
``SMOOTH_COLOR``
   :Attributes: vec3 pos, vec4 color
   :Uniforms: none
``UNIFORM_COLOR``
   :Attributes: vec3 pos
   :Uniforms: vec4 color
``POLYLINE_FLAT_COLOR``
   :Attributes: vec3 pos, vec4 color
   :Uniforms: vec2 viewportSize, float lineWidth
``POLYLINE_SMOOTH_COLOR``
   :Attributes: vec3 pos, vec4 color
   :Uniforms: vec2 viewportSize, float lineWidth
``POLYLINE_UNIFORM_COLOR``
   :Attributes: vec3 pos
   :Uniforms: vec2 viewportSize, float lineWidth, vec4 color
``POINT_FLAT_COLOR``
   :Attributes: vec3 pos, vec4 color
   :Uniforms: float size
``POINT_UNIFORM_COLOR``
   :Attributes: vec3 pos
   :Uniforms: vec4 color, float size

.. function:: create_from_info(shader_info)

   Create shader from a GPUShaderCreateInfo.

   :param shader_info: GPUShaderCreateInfo
   :type shader_info: :class:`gpu.types.GPUShaderCreateInfo`
   :return: Shader object corresponding to the given shader info.
   :rtype: :class:`gpu.types.GPUShader`


.. function:: from_builtin(shader_name, *, config='DEFAULT')

   Shaders that are embedded in the Blender internal code (see :ref:`built-in-shaders`).
   They all read the uniform ``mat4 ModelViewProjectionMatrix``,
   which can be edited by the :mod:`gpu.matrix` module.

   You can also choose a shader configuration that uses clip_planes by setting the ``CLIPPED`` value to the config parameter. Note that in this case you also need to manually set the value of ``mat4 ModelMatrix``.

   :param shader_name: One of the builtin shader names.
   :type shader_name: str
   :param config: One of these types of shader configuration:

      - ``DEFAULT``
      - ``CLIPPED``
   :type config: str
   :return: Shader object corresponding to the given name.
   :rtype: :class:`gpu.types.GPUShader`


.. function:: unbind()

   Unbind the bound shader object.


