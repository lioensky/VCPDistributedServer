BrushCapabilitiesSculpt(bpy_struct)
===================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BrushCapabilitiesSculpt(bpy_struct)

   Read-only indications of which brush operations are supported by the current sculpt tool

   .. data:: has_accumulate

      (default False, readonly)

      :type: bool

   .. data:: has_auto_smooth

      (default False, readonly)

      :type: bool

   .. data:: has_auto_smooth_pressure

      (default False, readonly)

      :type: bool

   .. data:: has_color

      (default False, readonly)

      :type: bool

   .. data:: has_direction

      (default False, readonly)

      :type: bool

   .. data:: has_dyntopo

      (default False, readonly)

      :type: bool

   .. data:: has_gravity

      (default False, readonly)

      :type: bool

   .. data:: has_hardness

      (default False, readonly)

      :type: bool

   .. data:: has_hardness_pressure

      (default False, readonly)

      :type: bool

   .. data:: has_height

      (default False, readonly)

      :type: bool

   .. data:: has_jitter

      (default False, readonly)

      :type: bool

   .. data:: has_normal_radius

      (default False, readonly)

      :type: bool

   .. data:: has_normal_weight

      (default False, readonly)

      :type: bool

   .. data:: has_persistence

      (default False, readonly)

      :type: bool

   .. data:: has_pinch_factor

      (default False, readonly)

      :type: bool

   .. data:: has_plane_depth

      (default False, readonly)

      :type: bool

   .. data:: has_plane_height

      (default False, readonly)

      :type: bool

   .. data:: has_plane_offset

      (default False, readonly)

      :type: bool

   .. data:: has_rake_factor

      (default False, readonly)

      :type: bool

   .. data:: has_random_texture_angle

      (default False, readonly)

      :type: bool

   .. data:: has_sculpt_plane

      (default False, readonly)

      :type: bool

   .. data:: has_secondary_color

      (default False, readonly)

      :type: bool

   .. data:: has_size_pressure

      (default False, readonly)

      :type: bool

   .. data:: has_smooth_stroke

      (default False, readonly)

      :type: bool

   .. data:: has_space_attenuation

      (default False, readonly)

      :type: bool

   .. data:: has_strength_pressure

      (default False, readonly)

      :type: bool

   .. data:: has_tilt

      (default False, readonly)

      :type: bool

   .. data:: has_topology_rake

      (default False, readonly)

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

   - :class:`Brush.sculpt_capabilities`

