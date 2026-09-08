ArrayModifier(Modifier)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ArrayModifier(Modifier)

   Array duplication modifier

   .. attribute:: constant_offset_displace

      Value for the distance between arrayed items (array of 3 items, in [-inf, inf], default (1.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: count

      Number of duplicates to make (in [1, inf], default 2)

      :type: int

   .. attribute:: curve

      Curve object to fit array length to

      :type: :class:`Object` | None

   .. attribute:: end_cap

      Mesh object to use as an end cap

      :type: :class:`Object` | None

   .. attribute:: fit_length

      Length to fit array within (in [0, inf], default 0.0)

      :type: float

   .. attribute:: fit_type

      Array length calculation method (default ``'FIXED_COUNT'``)

      - ``FIXED_COUNT``
        Fixed Count -- Duplicate the object a certain number of times.
      - ``FIT_LENGTH``
        Fit Length -- Duplicate the object as many times as fits in a certain length.
      - ``FIT_CURVE``
        Fit Curve -- Fit the duplicated objects to a curve.

      :type: Literal['FIXED_COUNT', 'FIT_LENGTH', 'FIT_CURVE']

   .. attribute:: merge_threshold

      Limit below which to merge vertices (in [0, inf], default 0.01)

      :type: float

   .. attribute:: offset_object

      Use the location and rotation of another object to determine the distance and rotational change between arrayed items

      :type: :class:`Object` | None

   .. attribute:: offset_u

      Amount to offset array UVs on the U axis (in [-1, 1], default 0.0)

      :type: float

   .. attribute:: offset_v

      Amount to offset array UVs on the V axis (in [-1, 1], default 0.0)

      :type: float

   .. attribute:: relative_offset_displace

      The size of the geometry will determine the distance between arrayed items (array of 3 items, in [-inf, inf], default (1.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: start_cap

      Mesh object to use as a start cap

      :type: :class:`Object` | None

   .. attribute:: use_constant_offset

      Add a constant offset (default False)

      :type: bool

   .. attribute:: use_merge_vertices

      Merge vertices in adjacent duplicates (default False)

      :type: bool

   .. attribute:: use_merge_vertices_cap

      Merge vertices in first and last duplicates (default False)

      :type: bool

   .. attribute:: use_object_offset

      Add another object's transformation to the total offset (default False)

      :type: bool

   .. attribute:: use_relative_offset

      Add an offset relative to the object's bounding box (default True)

      :type: bool

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
   - :class:`Modifier.name`
   - :class:`Modifier.type`
   - :class:`Modifier.show_viewport`
   - :class:`Modifier.show_render`
   - :class:`Modifier.show_in_editmode`
   - :class:`Modifier.show_on_cage`
   - :class:`Modifier.show_expanded`
   - :class:`Modifier.is_active`
   - :class:`Modifier.use_pin_to_last`
   - :class:`Modifier.is_override_data`
   - :class:`Modifier.use_apply_on_spline`
   - :class:`Modifier.execution_time`
   - :class:`Modifier.persistent_uid`

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
   - :class:`Modifier.bl_rna_get_subclass`
   - :class:`Modifier.bl_rna_get_subclass_py`

