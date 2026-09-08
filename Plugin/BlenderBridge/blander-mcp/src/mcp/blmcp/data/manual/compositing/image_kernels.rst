
*************
Image Kernels
*************

An *image kernel* is a small matrix of numeric values used to process an image by applying a
mathematical operation known as *convolution*.
Each value in the kernel defines how much neighboring pixels contribute to the output pixel's value.

Kernels are a fundamental concept in image processing and are used to perform operations such as
blurring, sharpening, and edge detection.
They determine how pixel neighborhoods are weighted and combined to produce new image details.


Concept
=======

When an image is convolved with a kernel, the kernel is centered over each pixel in the image.
Each pixel in the neighborhood is multiplied by the corresponding kernel value, and the results
are summed to form the output pixel color.
The process repeats for every pixel in the image.

The kernel values can be positive, negative, or fractional,
and their pattern determines the effect produced.


Common Examples
===============

Below are a few common kernels and their uses:

Blur
----

A simple blur can be achieved with evenly weighted positive values.
For example, a 3x3 average blur kernel:

::

   1/9  1/9  1/9
   1/9  1/9  1/9
   1/9  1/9  1/9

This softens the image by averaging neighboring pixels.


Sharpen
-------

A sharpening kernel enhances contrast at edges by emphasizing differences
between the center pixel and its neighbors:

::

    0  -1   0
   -1   5  -1
    0  -1   0


Edge Detection
--------------

Edge detection kernels highlight transitions in brightness by measuring differences between
adjacent pixels.
For example, the *Laplacian* kernel:

::

    0  -1   0
   -1   4  -1
    0  -1   0

Or the *Sobel* kernel (horizontal edges):

::

   -1  -2  -1
    0   0   0
    1   2   1


Normalization
=============

Often, kernels are normalized so that the sum of all values equals 1.
This prevents overall brightening or darkening of the image.
For example, dividing each element of a blur kernel by the total sum of all values ensures
consistent brightness after convolution.


Creating a Kernel in the Compositor
===================================

Kernels can be created directly inside the compositor using Blender's existing nodes,
without the need for an external image.

This approach is useful for designing procedural or parameterized filters, blurs,
and glare patterns that can be modified interactively.


#. **Start with a Constant Image**
   Use an :doc:`Image Node </compositing/types/input/image>` set to a small resolution,
   such as 9x9 or 15x15 pixels.
   Alternatively, generate a solid color using a :doc:`RGB </compositing/types/input/constant/rgb>` node.
#. **Shape the Kernel**
   Modify the pixel values to define the kernel weights:

   - Use the :doc:`Ellipse Mask </compositing/types/mask/ellipse_mask>` or
     :doc:`Blur </compositing/types/filter/blur/blur>` nodes to create soft, circular falloffs.
   - Combine multiple masks with :doc:`Mix </compositing/types/color/mix_color>` nodes to form
     complex or directional shapes (for example, a star or streak pattern).

   Scale the overall strength using a :doc:`Math </compositing/types/utilities/math/math>` node
   in *Multiply* mode, or normalize the kernel values by dividing by their total sum.
#. **Feed into the Convolve Node**
   Connect the resulting procedural image to the *Kernel* input of the
   :doc:`Convolve Node </compositing/types/filter/convolve>`.
   The pattern and brightness of this image directly control the convolution effect.


Tips
----

- Small images (under 20x20 pixels) produce efficient, responsive kernels.
- Use *Normalize Kernel* in the *Convolve* node to maintain brightness balance automatically.
- Animated masks or procedural noise patterns can be used to create dynamic or flickering filter effects.
- Kernels with positive and negative values can be used to emphasize edges or textures.
