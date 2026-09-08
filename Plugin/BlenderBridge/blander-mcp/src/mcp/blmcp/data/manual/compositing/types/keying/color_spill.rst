.. index:: Compositor Nodes; Color Spill
.. _bpy.types.CompositorNodeColorSpill:

****************
Color Spill Node
****************

.. figure:: /images/node-types_CompositorNodeColorSpill.webp
   :align: right
   :alt: Color Spill Node.

The *Color Spill* node is used to suppress unwanted color casts—typically green or blue;
caused by light reflecting from a chroma key (green or blue screen) onto the subject.

This "spill" is common in compositing workflows and can give a subject an unnatural colored tint.
The node reduces the influence of the selected color channel,
removing the excess and restoring a more natural appearance.


Inputs
======

Image
   The input RGBA image to be processed.

Factor
   Blend factor for how strongly the node affects the image.
   A value of 1.0 fully applies the effect; lower values blend with the original.

Spill Channel
   Selects which channel to reduce:

   :R: Suppress red spill.
   :G: Suppress green spill (common for green screens).
   :B: Suppress blue spill (common for blue screens).

Limit Method
   Chooses the method for spill reduction:

   :Simple: Compares the *Limiting Channel* channel to the others and reduces it if it is higher.
   :Average: Uses the average of the other two channels to set the limit for the despill channel.

Limit Channel :guilabel:`Simple`
   When using the *Simple* algorithm, you can choose which channel(s) to use as a reference for limiting:

   :R: Use red as the reference.
   :G: Use green as the reference.
   :B: Use blue as the reference.

Limit Strength
   Specifies the limiting strength of the limit channel.


Spill Strength
--------------

If enabled, the spill strength for each color channel can be specified.
If disabled, the spill channel will have a unit scale, while other channels will be zero.

Strength
   Specifics the spilling strength of each color channel.


Outputs
=======

Image
   The image with the corrected channels.


Example
=======

Results with the nodes applied to an image from
the `Mango Open Movie <https://mango.blender.org/>`__.

.. list-table::

   * - .. figure:: /images/compositing_types_matte_color-spill_example-before.jpg

          Before: green border and green reflections.

     - .. figure:: /images/compositing_types_matte_color-spill_example-after.jpg

          After: no unwanted green.
