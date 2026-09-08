.. index:: Compositor Nodes; Switch View
.. _bpy.types.CompositorNodeSwitchView:

****************
Switch View Node
****************

.. figure:: /images/node-types_CompositorNodeSwitchView.webp
   :align: right
   :alt: Switch View Node.

The *Switch View* node combines the *views* (left and right) into a single stereo 3D output.
This can be useful if for example, you need to treat the view as separate images by combining each of the views.

.. container:: lead

   .. clear

.. seealso::

   :doc:`The multi-view workflow </render/output/properties/stereoscopy/index>`.


Inputs
======

Left
   Left-eye image input.
Right
   Right-eye image input.


Outputs
=======

Image
   Stereo 3D image output.


Example
=======

.. figure:: /images/render_output_properties_stereoscopy_usage_compositor.png

   Render result, left and right views.

The views to render are defined in the current scene views,
in a similar way as you define the composite output resolution in the current scene render panel,
regardless of the Image nodes resolutions or Render Layers from different scenes.
