GreasePencilTimeModifierSegment(bpy_struct)
===========================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilTimeModifierSegment(bpy_struct)

   Configuration for a single dash segment

   .. attribute:: name

      Name of the dash segment (default "", never None)

      :type: str

   .. attribute:: segment_end

      Last frame of the segment (in [0, 32767], default 2)

      :type: int

   .. attribute:: segment_mode

      (default ``'NORMAL'``)

      - ``NORMAL``
        Regular -- Apply offset in usual animation direction.
      - ``REVERSE``
        Reverse -- Apply offset in reverse animation direction.
      - ``PINGPONG``
        Ping Pong -- Loop back and forth.

      :type: Literal['NORMAL', 'REVERSE', 'PINGPONG']

   .. attribute:: segment_repeat

      Number of cycle repeats (in [1, 32767], default 1)

      :type: int

   .. attribute:: segment_start

      First frame of the segment (in [0, 32767], default 1)

      :type: int

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

   - :class:`GreasePencilTimeModifier.segments`

