*************
Custom Camera
*************

In addition to the built-in camera types (Perspective, Orthographic and Panoramic cameras),
Cycles also supports implementing custom cameras using
`Open Shading Language <https://github.com/AcademySoftwareFoundation/OpenShadingLanguage>`__ (OSL).

Custom cameras are implemented as OSL shaders. A camera shader receives a sensor position
as its input and outputs the corresponding ray's position, direction and throughput.

OSL for shading and custom cameras are independent, so the latter can be used even when OSL shading
is disabled.

Using Custom Cameras
====================

In order to use a custom camera, set the :ref:`lens type <camera-lens-type>` to Custom.

This enables the selection of a text data-block or external file, similar to the
:ref:`Script node <bpy.types.ShaderNodeScript>` in shaders.

If the selected camera shader has parameters, they will be displayed below the Lens panel.

Writing Camera Shaders
======================

Inputs
------

The primary input to the camera shader is the sensor position. This is provided by the function
``camera_shader_raster_position()``, which returns a point whose X and Y components store the
position within the image in the range of 0-1.

In order to support random sampling in the shader, a pair of random numbers is provided by
``camera_shader_random_sample()``, which returns a vector containing random numbers in its
X and Y components. For the particular case of sampling the aperture, it's better
to use the ``cam:aperture_position`` attribute (see below) to be compatible with Blender's usual
aperture options.

Outputs
-------

The shader is expected to output three variables:
  - ``position``, a variable of type ``point`` which contains the origin of the generated ray.
  - ``direction``, a variable of type ``vector`` which contains the normalized direction of the generated ray.
  - ``throughput``, a variable of type ``color`` which contains the throughput of the ray - a weighting factor

that can be used to dim or tint the resulting color seen by the camera.

Both ``position`` and ``direction`` are in camera coordinates, where the origin is the position of
the camera itself, the positive Z axis is the view direction, and the positive Y axis is up.

If ``throughput`` is black, the resulting ray is skipped. This can be used to e.g. indicate
invalid rays for panoramic mappings.

Attributes
----------

Since camera shaders are not shaders in the traditional sense, many of OSL's features such as closures
or geometry-related attributes are not available.

Instead, the following camera-specific attributes are available through ``getattribute()``:

``cam:sensor_size``
   Size of the camera sensor in millimeters, as set in the
   :ref:`Camera properties <bpy.types.Camera.sensor_fit>`.
``cam:image_resolution``
   Resolution of the rendered image.
``cam:focal_distance``
   Focal distance of the camera in millimeters, as set in the
   :ref:`Depth of Field properties <bpy.types.CameraDOFSettings>`.
``cam:aperture_aspect_ratio``
   Aspect ratio of the camera aperture, as set in the
   :ref:`Depth of Field properties <bpy.types.CameraDOFSettings>`.
``cam:aperture_size``
   Size of the camera aperture, as set in the
   :ref:`Depth of Field properties <bpy.types.CameraDOFSettings>`.
``cam:aperture_position``
   A random position on the aperture, taking into account its size, shape and aspect ratio as set
   in the :ref:`Depth of Field properties <bpy.types.CameraDOFSettings>`. Note that this uses the
   same random numbers as provided by `camera_shader_random_sample()`, so avoid using both as it
   would lead to correlation issues.

Derivatives
-----------

For some features such as the Wireframe node, Cycles needs derivatives of the ray origin and
direction with respect to image X and Y coordinates.

By default, OSL auto-differentiation will be used to compute these. For advanced cases where you
can compute the derivatives more accurately or efficiently, you can make your shader output four
additional variables named ``dPdx``, ``dPdy``, ``dDdx`` and ``dDdy``. If any of these are present, their
values will be used instead. Note that you can not mix both options - either all or none must be
explicitly provided.

Parameters
----------

Shaders can define additional input parameters. These will be exposed to the user in the Camera
properties panel, under the Lens options.

To further control how they are presented, the following OSL metadata can be used:

``[[ string help = "This is a parameter" ]]``
  Description of the parameter, shown in the tooltip.
``[[ float sensitivity = 0.25 ]]``
  How far to increment/decrement the parameter when dragging/clicking.
``[[ int digits = 2 ]]``
  How many digits are displayed for numerical parameters.
``[[ float min = -5, float max = 5 ]]``
  What range the property can take on.
``[[ int slider = 1, float slidermin = -4, float slidermax = 4 ]]``
  Display the property as a slider with the given range.
``[[ string widget = "boolean" ]]``
  Display the ```int``` property as a checkbox, resulting in values 0 or 1.

An Example
----------

This is a very basic shader implementing a perspective camera:

.. code-block:: c

  shader perspective_camera(
      float focal_length = 90.0 [[ float sensitivity = 0.2, float min = 0 ]],
      output point position = 0.0,
      output vector direction = 0.0,
      output color throughput = 1.0) {
    vector sensor_size;
    getattribute("cam:sensor_size", sensor_size);

    point Pcam = camera_shader_raster_position() - point(0.5);
    Pcam *= sensor_size / focal_length;
    direction = normalize(vector(Pcam.x, Pcam.y, 1.0));
  }

More examples can be found in :menuselection:`Text Editor --> Templates --> Open Shading Language`.

Limitations
===========

.. important::

   Custom cameras are not supported with GPU rendering unless using the OptiX backend.

Some features in Cycles, in particular the Vector pass and Window texture coordinates, require
inverse mappings from rays to image coordinates. This is not yet supported with custom cameras.
