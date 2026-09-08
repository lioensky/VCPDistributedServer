bpy.utils submodule (bpy.utils.previews)
========================================

.. module:: bpy.utils.previews

This module contains utility functions to handle custom previews.

It behaves as a high-level 'cached' previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
('icon_value' for UILayout functions).


Custom Icon Example
-------------------

.. literalinclude:: __/__/__/scripts/templates_py/ui_previews_custom_icon.py

.. function:: new()

   :return: a new preview collection.
   :rtype: :class:`ImagePreviewCollection`

.. function:: remove(pcoll)

   Remove the specified previews collection.
   
   :param pcoll: Preview collection to close.
   :type pcoll: :class:`ImagePreviewCollection`

.. class:: ImagePreviewCollection

   Dictionary-like class of previews.
   
   This is a subclass of Python's built-in dict type,
   used to store multiple image previews.
   
   .. note::
   
       - instance with :mod:`bpy.utils.previews.new`
       - keys must be ``str`` type.
       - values will be :class:`bpy.types.ImagePreview`

   .. method:: clear()

      Clear all previews.

   .. method:: close()

      Close the collection and clear all previews.

   .. method:: load(name, filepath, file_type, force_reload=False)
   
      Generate a new preview from given file path.
   
      :param name: The name (unique id) identifying the preview.
      :type name: str
      :param filepath: The file path to generate the preview from.
      :type filepath: str | bytes
      :param file_type: The type of file, needed to generate the preview.
      :type file_type: Literal['IMAGE', 'MOVIE', 'BLEND', 'FONT', 'OBJECT_IO']
      :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
      :type force_reload: bool
      :return: The Preview matching given name, or a new empty one.
      :rtype: :class:`bpy.types.ImagePreview`
      :raises KeyError: if ``name`` already exists.

   .. method:: new(name)
   
      Generate a new empty preview.
   
      :param name: The name (unique id) identifying the preview.
      :type name: str
      :return: The Preview matching given name, or a new empty one.
      :rtype: :class:`bpy.types.ImagePreview`
      :raises KeyError: if ``name`` already exists.



