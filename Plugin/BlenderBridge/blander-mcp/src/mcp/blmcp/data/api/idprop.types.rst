ID Property Access (idprop.types)
=================================

.. module:: idprop.types

.. class:: IDPropertyArray

   An array of values with a fixed type, supporting indexing and slicing.

   .. method:: to_list()
   
      Return the array as a list.
   
      :return: The array as a list.
      :rtype: list[int] | list[float] | list[bool]


   .. attribute:: typecode

      The type of the data in the array {'f': float (32-bit), 'd': double (64-bit), 'i': int, 'b': bool}. Both 'f' and 'd' use Python's :class:`float` type but differ in storage precision.




.. class:: IDPropertyGroup

   A dictionary-like group of ID properties, supporting key access, iteration, and membership testing.

   .. method:: clear()
   
      Clear all members from this group.


   .. method:: get(key, default=None)
   
      Return the value for key, if it exists, else default.
   
      :param key: The key to look up.
      :type key: str
      :param default: Value to return if *key* is not found.
      :type default: Any
      :return: The value for the key, or *default* if not found.
      :rtype: Any


   .. method:: items()
   
      Return a view of the items in the group, behaves like dictionary method items.
   
      :return: A view of the items.
      :rtype: :class:`IDPropertyGroupViewItems`


   .. method:: keys()
   
      Return a view of the keys in the group.
   
      :return: A view of the keys.
      :rtype: :class:`IDPropertyGroupViewKeys`


   .. method:: pop(key, default)
   
      Remove an item from the group, returning a Python representation.
   
      :raises KeyError: When the item doesn't exist and no *default* is given.
   
      :param key: Name of item to remove.
      :type key: str
      :param default: Value to return when *key* isn't found (optional, a :exc:`KeyError` is raised when omitted and the key is not found).
      :type default: Any
      :return: A Python representation of the removed item, or *default*.
      :rtype: Any


   .. method:: to_dict()
   
      Return a purely Python version of the group.
   
      :return: A dictionary representation of the group.
      :rtype: dict[str, Any]


   .. method:: update(other)
   
      Update key-value pairs from *other*, overwriting existing keys.
   
      .. note::
   
         Unlike :meth:`dict.update`, keyword arguments are not supported.
   
      :param other: Updates the values in the group with this.
      :type other: :class:`IDPropertyGroup` | dict[str, Any]


   .. method:: values()
   
      Return the values associated with this group.
   
      :return: A view of the values.
      :rtype: :class:`IDPropertyGroupViewValues`


   .. attribute:: name

      The name of this Group.




.. class:: IDPropertyGroupIterItems

   Iterator over :class:`IDPropertyGroup` items (key/value pairs).



.. class:: IDPropertyGroupIterKeys

   Iterator over :class:`IDPropertyGroup` keys.



.. class:: IDPropertyGroupIterValues

   Iterator over :class:`IDPropertyGroup` values.



.. class:: IDPropertyGroupViewItems

   A view of :class:`IDPropertyGroup` items as key/value pairs (supports ``len()``, ``in``, iteration, and ``reversed()``).



.. class:: IDPropertyGroupViewKeys

   A view of :class:`IDPropertyGroup` keys (supports ``len()``, ``in``, iteration, and ``reversed()``).



.. class:: IDPropertyGroupViewValues

   A view of :class:`IDPropertyGroup` values (supports ``len()``, ``in``, iteration, and ``reversed()``).



