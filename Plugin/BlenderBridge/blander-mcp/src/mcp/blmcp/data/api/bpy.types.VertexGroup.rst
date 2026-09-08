VertexGroup(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: VertexGroup(bpy_struct)

   Group of vertices, used for armature deform and other purposes

   .. data:: index

      Index number of the vertex group (in [0, inf], default 0, readonly)

      :type: int

   .. attribute:: lock_weight

      Maintain the relative weights for the group (default False)

      :type: bool

   .. attribute:: name

      Vertex group name (default "", never None)

      :type: str

   .. method:: add(index, weight, type)

      Add vertices to the group

      :param index: List of indices (array of 1 items, in [-inf, inf])
      :type index: Sequence[int]
      :param weight: Vertex weight (in [0, 1])
      :type weight: float
      :param type: Vertex assign mode

         - ``REPLACE``
           Replace -- Replace.
         - ``ADD``
           Add -- Add.
         - ``SUBTRACT``
           Subtract -- Subtract.
      :type type: Literal['REPLACE', 'ADD', 'SUBTRACT']

   .. method:: remove(index)

      Remove vertices from the group

      :param index: List of indices (array of 1 items, in [-inf, inf])
      :type index: Sequence[int]

   .. method:: weight(index)

      Get a vertex weight from the group

      :param index: Index, The index of the vertex (in [0, inf])
      :type index: int
      :return: Vertex weight (in [0, 1])
      :rtype: float

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`Object.vertex_groups`
   - :class:`VertexGroups.active`
   - :class:`VertexGroups.new`
   - :class:`VertexGroups.remove`

