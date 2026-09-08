.. index:: Compositor Nodes; Chromatic Aberration

*************************
Chromatic Aberration Node
*************************

.. figure:: /images/node-types_CompositorNodeChromaticAberration.webp
   :align: right
   :alt: Chromatic Aberration Node.

The *Chromatic Aberration* node simulates the dispersion of light caused by a camera lens,
where different wavelengths (colors) of light are refracted by slightly different amounts.
This effect produces subtle color fringing near edges or high-contrast transitions
and can be used for both realistic lens simulation and stylistic distortion effects.

It can also be combined with other post-processing effects such as
:doc:`Vignette </compositing/types/camera_lens_effects/vignette>` or
:doc:`Lens Distortion </compositing/types/transform/lens_distortion>`
to create convincing camera imperfections.


Inputs
======

Image
   Standard color input image.

Type
   Defines the method used to generate the chromatic aberration effect.

   :Offset:
      Offsets individual color channels along the X or Y axis.
      A simple and fast way to create horizontal or vertical color fringing.
   :Scale:
      Scales each color channel differently from the image center,
      creating a radial dispersion effect.
   :Directional Blur:
      Blurs color channels along a specific direction to simulate motion-like chromatic smearing.
   :Lens Dispersion:
      Simulates wavelength-dependent refraction through a lens,
      creating realistic radial rainbow edges near the image borders.

Axis :guilabel:`Offset`
   Determines the axis along which channel offsets occur.

   :Vertical:
      Applies offsets vertically.
   :Horizontal:
      Applies offsets horizontally.

Factor
   Controls the intensity of the aberration.
   Higher values increase the separation between color channels and make the effect more visible.

Center :guilabel:`Directional Blur`
   The pivot point around which directional transformations occur.
   Defined in normalized coordinates (0.0-1.0 across the image).

Samples :guilabel:`Directional Blur`
   Sets the number of samples used to compute the directional blur.
   More samples produce a smoother result but increase computation time.
   The number of samples is *2ⁿ*, growing exponentially with this input.

Fit :guilabel:`Lens Dispersion`
   Scales the resulting image to fit entirely within the frame,
   avoiding empty borders caused by radial dispersion.


Outputs
=======

Image
   The resulting image with chromatic aberration applied.
