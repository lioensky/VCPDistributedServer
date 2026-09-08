
***************
Post Processing
***************

.. reference::

   :Panel:     :menuselection:`Properties --> Output --> Post Processing`

The Post Processing panel is used to control different options used to process your image after rendering.

.. figure:: /images/render_output_properties_post-processing_panel.png
   :align: right

   Post Processing panel.

.. _bpy.types.RenderSettings.use_compositing:

Pipeline -- Compositing
   Renders the output from the compositing node setup,
   and then applies the Composite node tree on all images,
   displaying the image inputted in the Group Output node.

.. _bpy.types.RenderSettings.use_sequencer:

Pipeline -- Sequencer
   Renders the output of the Video Sequence editor, instead of the view from the 3D scene's active camera.
   If the sequence contains Scene strips, these will also be rendered as part of the pipeline.
   If *Compositing* is also enabled, the Scene strip will be the output of the Compositor.

.. _bpy.types.RenderSettings.dither_intensity:

Dither
   Dithering is a technique for blurring pixels to prevent banding that is seen in areas of
   gradients, where stair-stepping appears between colors.
   Banding artifacts are more noticeable when gradients are longer, or less steep.
   Dithering was developed for graphics with low bit depths,
   meaning they had a limited range of possible colors.

   Dithering works by taking pixel values and comparing them with a threshold and
   neighboring pixels then does calculations to generate the appropriate color.
   Dithering creates the perceived effect of a larger color palette by creating a sort of visual color mixing.
   For example, if you take a grid and distribute red and yellow pixels evenly across it,
   the image would appear to be orange.
