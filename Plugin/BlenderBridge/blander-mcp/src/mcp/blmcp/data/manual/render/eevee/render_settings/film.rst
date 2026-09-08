
****
Film
****

Filter Size
   Due to limited resolution of images and computer screens, pixel filters are needed to avoid :term:`Aliasing`.
   This is achieved by slightly blurring the image to soften edges.

   This Setting controls how much the image is softened;
   lower values give more crisp renders, higher values are softer and reduce aliasing.

Transparent
   Render the background transparent, for compositing the image over another background after rendering.

.. _bpy.types.SceneEEVEE.use_overscan:
.. _bpy.types.SceneEEVEE.overscan_size:

Overscan
   Percentage of the render size to add to the internal render buffer.
   This will have a serious impact on performance but can fix
   render glitches around the perimeter of the rendered image.
