.. index:: Compositor Nodes; Tone Map
.. _bpy.types.CompositorNodeTonemap:

*************
Tone Map Node
*************

.. figure:: /images/node-types_CompositorNodeTonemap.webp
   :align: right
   :alt: Tone Map Node.

Tone mapping is used to map high dynamic range colors into a more limited dynamic
range supported by the display, while preserving the appearance as much as possible.

This is a legacy node. It is recommended to use view transforms in the
color management settings instead, and output linear high dynamic range images
from the compositor instead of low dynamic range.


Inputs
======

Image
   :abbr:`HDR (High Dynamic Range)` image.
Type
   Algorithm used for tone mapping:

   :Rh Simple:
      A simplified Reinhard tone mapping operator that uses the image's average luminance.
      Suitable for quick and general-purpose tone mapping.
   :R/D Photoreceptor:
      A more complex algorithm modeling human photoreceptor response,
      allowing finer adjustments in adaptation, contrast, and color correction.
Intensity :guilabel:`R/D Photoreceptor`
   If less than zero, darkens image; otherwise, makes it brighter.
Contrast :guilabel:`R/D Photoreceptor`
   Set to 0 to use estimate from input image.
Light Adaptation :guilabel:`R/D Photoreceptor`
   If 0, global; if 1, based on pixel intensity.
Chromatic Adaptation :guilabel:`R/D Photoreceptor`
   If 0, same for all channels; if 1, each independent.
Key :guilabel:`Rh Simple`
   The value the average luminance is mapped to.
Balance :guilabel:`Rh Simple`
   Normally always 1, but can be used as an extra control to alter the brightness curve.
Gamma :guilabel:`Rh Simple`
   If not used, set to 1.


Outputs
=======

Image
   :abbr:`LDR (Low Dynamic Range)` image.
