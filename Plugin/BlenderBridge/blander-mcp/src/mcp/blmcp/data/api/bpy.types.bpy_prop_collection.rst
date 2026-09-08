bpy_prop_collection
===================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`

.. class:: bpy_prop_collection(bpy_prop)

   built-in class used for all collections.

   .. method:: find(key)
   
      Returns the index of a key in a collection or -1 when not found
      (matches Python's string find function of the same name).
   
      :param key: The identifier for the collection member.
      :type key: str
      :return: index of the key.
      :rtype: int


   .. method:: foreach_get(attr, seq)
   
      This is a function to give fast access to attributes within a collection.


      Only works for 'basic type' properties (bool, int and float)!
      Multi-dimensional arrays (like array of vectors) will be flattened into seq.

      .. literalinclude:: ./examples/bpy.types.bpy_prop_collection.foreach_get.0.py
         :lines: 5-


   .. method:: foreach_set(attr, seq)
   
      This is a function to give fast access to attributes within a collection.


      Only works for 'basic type' properties (bool, int and float)!
      seq must be uni-dimensional, multi-dimensional arrays (like array of vectors) will be re-created from it.

      .. literalinclude:: ./examples/bpy.types.bpy_prop_collection.foreach_set.0.py
         :lines: 5-


   .. method:: get(key, default=None)
   
      Returns the value of the item assigned to key or default when not found
      (matches Python's dictionary function of the same name).
   
      :param key: The identifier for the collection member.
      :type key: str
      :param default: Optional argument for the value to return if
         *key* is not found.
      :type default: Any
      :return: The collection member or default.
      :rtype: :class:`bpy_struct`


   .. method:: items()
   
      Return the identifiers of collection members
      (matching Python's dict.items() functionality).
   
      :return: (key, value) pairs for each member of this collection.
      :rtype: list[tuple[str, :class:`bpy.types.bpy_struct`]]


   .. method:: keys()
   
      Return the identifiers of collection members
      (matching Python's dict.keys() functionality).
   
      :return: the identifiers for each member of this collection.
      :rtype: list[str]


   .. method:: values()
   
      Return the values of collection
      (matching Python's dict.values() functionality).
   
      :return: The members of this collection.
      :rtype: list[:class:`bpy.types.bpy_struct` | None]


