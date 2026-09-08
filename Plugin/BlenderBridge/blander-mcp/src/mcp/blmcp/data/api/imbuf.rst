Image Buffer (imbuf)
====================

.. module:: imbuf

This module provides access to Blender's image manipulation API.

It provides access to image buffers outside of Blender's
:class:`bpy.types.Image` data-block context.

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   imbuf.types.rst

.. function:: load(filepath)

   Load an image from a file.

   :param filepath: The filepath of the image.
   :type filepath: str | bytes
   :return: The newly loaded image.
   :rtype: :class:`ImBuf`


.. function:: load_from_buffer(buffer)

   Load an image from a buffer.

   :param buffer: A buffer containing the image data.
   :type buffer: collections.abc.Buffer
   :return: The newly loaded image.
   :rtype: :class:`ImBuf`


.. function:: new(size)

   Create a new image.

   :param size: The size of the image in pixels.
   :type size: tuple[int, int]
   :return: The newly created image.
   :rtype: :class:`ImBuf`


.. function:: write(image, *, filepath=None)

   Write an image.

   :param image: The image to write.
   :type image: :class:`ImBuf`
   :param filepath: Optional filepath of the image (fallback to the image's file path).
   :type filepath: str | bytes | None


