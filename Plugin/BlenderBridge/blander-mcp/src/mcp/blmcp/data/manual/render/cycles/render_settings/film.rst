
****
Film
****

.. reference::

   :Panel:     :menuselection:`Render --> Film`

.. _bpy.types.CyclesRenderSettings.film_exposure:

Exposure
   This can be used to change the brightness of an image.
   Different than the *Exposure* option found in the :ref:`Color management <render-post-color-management>` panel,
   this exposure option works *on the data* while the Color management exposure is on the *view transform*.


Pixel Filter
============

Due to limited resolution of images and computer screens, pixel filters are needed to avoid :term:`Aliasing`.
This is achieved by slightly blurring the image to soften edges.

.. _bpy.types.CyclesRenderSettings.pixel_filter_type:

Type
   Pixel Filtering algorithm to use.

   :Box: No filter.
   :Gaussian: Smooth filter.
   :Blackman-Harris: Default filter with a better balance between smoothness and detail preservation.

.. _bpy.types.CyclesRenderSettings.filter_width:

Width
   Lower values give more crisp renders, higher values are softer and reduce aliasing.


.. _bpy.types.RenderSettings.film_transparent:

Transparent
===========

Render the background transparent, for compositing the image over another background after rendering.

.. _bpy.types.CyclesRenderSettings.film_transparent_glass:

Transparent Glass
   Render transmissive surfaces as transparent, for compositing glass over another background.

.. _bpy.types.CyclesRenderSettings.film_transparent_roughness:

Roughness Threshold
   For transparent glass, keep surfaces with roughness above the threshold opaque.
