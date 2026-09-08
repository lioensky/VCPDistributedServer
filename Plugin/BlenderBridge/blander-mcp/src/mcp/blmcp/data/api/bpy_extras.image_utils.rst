bpy_extras submodule (bpy_extras.image_utils)
=============================================

.. module:: bpy_extras.image_utils

.. function:: load_image(imagepath, dirname='', place_holder=False, recursive=False, ncase_cmp=True, convert_callback=None, verbose=False, relpath=None, check_existing=False, force_reload=False)

   Return an image from the file path with options to search multiple paths
   and return a placeholder if it's not found.
   
   :param imagepath: The image filename
      If a path precedes it, this will be searched as well.
   :type imagepath: str
   :param dirname: is the directory where the image may be located - any file at
      the end will be ignored.
   :type dirname: str
   :param place_holder: if True a new place holder image will be created.
      this is useful so later you can relink the image to its original data.
   :type place_holder: bool
   :param recursive: If True, directories will be recursively searched.
      Be careful with this if you have files in your root directory because
      it may take a long time.
   :type recursive: bool
   :param ncase_cmp: on non windows systems, find the correct case for the file.
   :type ncase_cmp: bool
   :param convert_callback: a function that takes an existing path and returns
      a new one. Use this when loading image formats blender may not support,
      the CONVERT_CALLBACK can take the path for a GIF (for example),
      convert it to a PNG and return the PNG's path.
      For formats blender can read, simply return the path that is given.
   :type convert_callback: Callable[[str], str] | None
   :param verbose: If True, print extra information when searching for the image.
   :type verbose: bool
   :param relpath: If not None, make the file relative to this path.
   :type relpath: str | None
   :param check_existing: If true,
      returns already loaded image data-block if possible
      (based on file path).
   :type check_existing: bool
   :param force_reload: If true,
      force reloading of image (only useful when ``check_existing``
      is also enabled).
   :type force_reload: bool
   :return: an image or None
   :rtype: :class:`bpy.types.Image` | None

