bpy_prop
========

.. currentmodule:: bpy.types

.. class:: bpy_prop

   built-in base class for all property classes.

   .. method:: as_bytes()
   
      Returns this string property as a byte rather than a Python string.
   
      :return: The string as bytes.
      :rtype: bytes


   .. method:: path_from_id()
   
      Returns the data path from the ID to this property (string).
   
      :return: The path from :class:`bpy.types.bpy_struct.id_data` to this property.
      :rtype: str


   .. method:: path_from_module()
   
      Returns the full data path to this struct (as a string) from the bpy module.
   
      :return: The full path to the data.
      :rtype: str
   
      :raises ValueError:
         if the input data cannot be converted into a full data path.
   
         .. note:: Even if all input data is correct, this function might
            error out because Blender cannot derive a valid path.
            The incomplete path will be printed in the error message.


   .. method:: update()
   
      Execute the properties update callback.
   
      .. note::
         This is called when assigning a property,
         however in rare cases it's useful to call explicitly.


   .. attribute:: data

      The data this property is using, *type* :class:`bpy.types.bpy_struct`


   .. attribute:: id_data

      The :class:`bpy.types.ID` object this data-block is from or None, (not available for all data types) (readonly)
      
      :type: :class:`bpy.types.ID`


   .. attribute:: rna_type

      The property type for introspection.


