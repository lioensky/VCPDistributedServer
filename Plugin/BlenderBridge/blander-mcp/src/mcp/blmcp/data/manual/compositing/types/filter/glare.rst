.. index:: Compositor Nodes; Glare
.. _bpy.types.CompositorNodeGlare:

**********
Glare Node
**********

.. figure:: /images/node-types_CompositorNodeGlare.webp
   :align: right
   :alt: Glare Node.

The *Glare Node* enhances bright areas of an image by adding effects such as lens flares, bloom, and fog glow.
It simulates the way light interacts with lenses, creating realistic or artistic highlights and reflections.


Inputs
======

Image
   Standard color input.

Glare Type
   Defines the type of glare effect applied to the image.

   :Bloom:
      Simulates the soft glow around bright areas due to light scattering in eyes and camera lenses.
   :Ghosts:
      Creates multiple overlapping glare artifacts resembling lens reflections or a hazy glow.
   :Streaks:
      Produces bright streaks radiating from highlights, commonly used to simulate lens flares.
   :Fog Glow:
      Simulates the soft glow around bright areas due to light scattering in eyes and camera lenses.
      This glare is a more physically accurate version of *Bloom*, creating a softer,
      more realistic glow at the cost of increased computation time.
   :Simple Star:
      Similar to *Streaks*, but produces a simpler star-shaped glare effect.
   :Sun Beams:
      Simulates the effect of bright light getting scattered in a medium
      `(Crepuscular Rays) <https://en.wikipedia.org/wiki/Crepuscular_rays>`__.
      This phenomenon can be created by renderers, but full volumetric lighting is
      a rather arduous approach and takes a long time to render.
   :Kernel:
      Applies a custom convolution filter using a :doc:`kernel </compositing/image_kernels>`
      defined either numerically or from an image.
      This mode allows the creation of user-defined glare or diffusion effects
      by specifying the shape and intensity distribution of the kernel.

Quality
   Controls the resolution at which the glare effect is processed.
   This can be helpful to save render times while only doing preview renders.

   :High: Full-resolution processing for best quality.
   :Medium: Uses a lower resolution to reduce computation time.
   :Low: Fastest processing but with lower detail.


Highlights
----------

Threshold
   Defines the minimum luminance required for an area to contribute to the glare effect.
   Lower values include more areas, while higher values restrict glare to the brightest regions.

Smoothness
   Controls how gradually pixels transition into the glare effect.
   Higher values create a smoother highlight extraction.


Clamp
^^^^^

Clamp bright highlights defined by the *Maximum* input.

This can help create a more consistent looking bloom effect when there is a large variations in luminance.

Maximum
   Clamps the intensity of the highlights to this value.


Adjust
------

Strength
   Adjusts the overall intensity of the glare effect.
   Values greater than 1 boost the luminance of the glare,
   while values less than 1 blends the glare with the original image.

Saturation
   Modifies the color saturation of the glare effect.

Tint
   Tints the glare effect, allowing for colored highlights.


Glare
-----

Size :guilabel:`Bloom` :guilabel:`Fog Glow` :guilabel:`Sun Beams`
   Defines the relative spread of the effect across the image.
   A value of 1 makes the effect cover the full image, while 0.5 restricts it to half, and so on.

Streaks :guilabel:`Streaks`
   The number of streaks radiating from highlights.

Streaks Angle :guilabel:`Streaks`
   The angle that the first streak makes with the horizontal axis.

Iterations :guilabel:`Ghosts` :guilabel:`Streaks` :guilabel:`Simple Star`
   The number of ghosts for *Ghost* glare or the quality and
   spread of glare for *Streaks* and *Simple Star* glare types.

Color Modulation :guilabel:`Ghosts` :guilabel:`Streaks`
   Introduces subtle color variations, simulating chromatic dispersion effects.

Fade :guilabel:`Streaks` :guilabel:`Simple Star`
   The fade-out intensity of the streaks.

Diagonal :guilabel:`Simple Star`
   Rotates the *Simple Star* streaks by 45° for an alternate pattern.

Sun Position :guilabel:`Sun Beams`
   Source point of the rays as a factor of the image dimensions.

Jitter :guilabel:`Sun Beams`
   The amount of jitter to introduce while computing rays,
   higher jitter can be faster but can produce grainy or noisy results.

Kernel Data Type :guilabel:`Kernel`
   Determines how the kernel is defined:

   :Float: A numeric kernel defined by the *Kernel* input socket.
   :Color: A full color image used as the kernel, allowing for more complex filtering patterns

Kernel :guilabel:`Kernel`
   When the *Float* type is selected, this input defines the numeric
   :doc:`kernel </compositing/image_kernels>` values.
   When the *Color* type is selected, an image input can be connected
   to provide a grayscale or color-based convolution kernel.


Outputs
=======

Image
   The final image with the generated glare added.

Glare
   The generated glare effect isolated from the input image.
   Useful for further compositing or adjustments.

Highlights
   The extracted bright areas used to generate the glare effect.
   Can be used to fine-tune the glare or as a base for custom effects.


Gizmos
======

The *Glare* node provides an interactive gizmo in the Node Editor.
To use it, enable :ref:`Active Node Gizmo <bpy.types.SpaceNodeEditor.show_gizmo_active_node>` and
select the *Glare* node.

For the *Sun Beams* type, a cross-shaped gizmo appears in the image preview to set the *Sun Position*.


Examples
========

Sun Beams
---------

Usually, the first step is to define the area from which rays are cast.
Any diffuse reflected light from surfaces is not going to contribute to such scattering in the real world,
so should be excluded from the input data.
Possible ways to achieve this are:

- Entirely separate image as a light source.
- Brightness/contrast tweaking to leave only the brightest areas.
- Muting shadow and midtone colors, which is a bit more flexible.
- Masking for ultimate control.

After generating the sun beams from such a light source image they can then be overlaid on the original image.
Usually, a simple "Add" Mix node is sufficient,
and physically correct because the scattered light adds to the final result.

.. figure:: /images/compositing_types_filter_sun-beams_example.jpg
   :width: 400px
