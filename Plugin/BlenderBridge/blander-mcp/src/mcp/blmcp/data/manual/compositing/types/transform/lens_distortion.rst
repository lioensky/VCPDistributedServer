.. index:: Compositor Nodes; Lens Distortion
.. _bpy.types.CompositorNodeLensdist:

********************
Lens Distortion Node
********************

.. figure:: /images/node-types_CompositorNodeLensdist.webp
   :align: right
   :alt: Lens Distortion Node.

Use this node to simulate distortions that real camera lenses produce.


Inputs
======

Image
   Standard color input.
Type
   :Radial: Radially distorts the image to create a barrel or a Pincushion distortion.
   :Horizontal: Horizontally distorts the image to create a channel/color shifting effect.
Distortion :guilabel:`Radial`
   This creates a bulging or pinching effect from the center of the image.
Dispersion
   This simulates chromatic aberrations, where different wavelengths of light refract slightly differently,
   creating a rainbow colored fringe.
Jitter
   Adds jitter to the distortion. Faster, but noisier.
Fit :guilabel:`Radial`
   Scales image so black areas are not visible. Only works for positive distortion.


Outputs
=======

Image
   Standard color output.
