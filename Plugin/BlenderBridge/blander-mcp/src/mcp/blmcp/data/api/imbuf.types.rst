Image Buffer Types (imbuf.types)
================================

.. module:: imbuf.types

This module provides access to image buffer types.

.. note::

   Image buffer is also the structure used by :class:`bpy.types.Image`
   ID type to store and manipulate image data at runtime.

.. class:: ImBuf


   .. method:: copy()
   
      Return a copy of the image.
   
      :return: A copy of the image.
      :rtype: :class:`ImBuf`


   .. method:: crop(min, max)
   
      Crop the image in-place.
   
      :param min: Minimum pixel coordinates (X, Y), inclusive.
      :type min: tuple[int, int]
      :param max: Maximum pixel coordinates (X, Y), inclusive.
      :type max: tuple[int, int]


   .. method:: free()
   
      Clear image data immediately (causing an error on re-use).


   .. method:: resize(size, *, method='FAST')
   
      Resize the image in-place.
   
      :param size: New size.
      :type size: tuple[int, int]
      :param method: Method of resizing ('FAST', 'BILINEAR').
      :type method: str


   .. attribute:: channels

      Number of color channels.
      
      :type: int


   .. attribute:: filepath

      Filepath associated with this image.
      
      :type: str


   .. attribute:: planes

      Number of bits per pixel.
      
      :type: int


   .. attribute:: ppm

      Pixels per meter.
      
      :type: tuple[float, float]


   .. attribute:: size

      Size of the image in pixels.
      
      :type: tuple[int, int]




