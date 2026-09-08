GreasePencilShrinkwrapModifier(Modifier)
========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilShrinkwrapModifier(Modifier)

   Shrink wrapping modifier to shrink wrap an object to a target

   .. attribute:: auxiliary_target

      Additional mesh target to shrink to

      :type: :class:`Object` | None

   .. attribute:: cull_face

      Stop vertices from projecting to a face on the target when facing towards/away (default ``'OFF'``)

      :type: Literal[:ref:`rna_enum_shrinkwrap_face_cull_items`]

   .. attribute:: invert_layer_filter

      Invert layer filter (default False)

      :type: bool

   .. attribute:: invert_layer_pass_filter

      Invert layer pass filter (default False)

      :type: bool

   .. attribute:: invert_material_filter

      Invert material filter (default False)

      :type: bool

   .. attribute:: invert_material_pass_filter

      Invert material pass filter (default False)

      :type: bool

   .. attribute:: invert_vertex_group

      Invert vertex group weights (default False)

      :type: bool

   .. attribute:: layer_pass_filter

      Layer pass filter (in [0, 100], default 0)

      :type: int

   .. attribute:: material_filter

      Material used for filtering

      :type: :class:`Material` | None

   .. attribute:: material_pass_filter

      Material pass (in [0, 100], default 0)

      :type: int

   .. attribute:: offset

      Distance to keep from the target (in [-inf, inf], default 0.05)

      :type: float

   .. attribute:: open_influence_panel

      (default False)

      :type: bool

   .. attribute:: project_limit

      Limit the distance used for projection (zero disables) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: smooth_factor

      Amount of smoothing to apply (in [0, 1], default 0.05)

      :type: float

   .. attribute:: smooth_step

      Number of times to apply smooth (high numbers can reduce FPS) (in [1, 10], default 1)

      :type: int

   .. attribute:: subsurf_levels

      Number of subdivisions that must be performed before extracting vertices' positions and normals (in [0, 6], default 0)

      :type: int

   .. attribute:: target

      Mesh target to shrink to

      :type: :class:`Object` | None

   .. attribute:: tree_node_filter

      Layer name (default "", never None)

      :type: str

   .. attribute:: use_invert_cull

      When projecting in the negative direction invert the face cull mode (default False)

      :type: bool

   .. attribute:: use_layer_group_filter

      Filter by layer group name (default False)

      :type: bool

   .. attribute:: use_layer_pass_filter

      Use layer pass filter (default False)

      :type: bool

   .. attribute:: use_material_pass_filter

      Use material pass filter (default False)

      :type: bool

   .. attribute:: use_negative_direction

      Allow vertices to move in the negative direction of axis (default False)

      :type: bool

   .. attribute:: use_positive_direction

      Allow vertices to move in the positive direction of axis (default True)

      :type: bool

   .. attribute:: use_project_x

      (default False)

      :type: bool

   .. attribute:: use_project_y

      (default False)

      :type: bool

   .. attribute:: use_project_z

      (default False)

      :type: bool

   .. attribute:: vertex_group_name

      Vertex group name for modulating the deform (default "", never None)

      :type: str

   .. attribute:: wrap_method

      (default ``'NEAREST_SURFACEPOINT'``)

      :type: Literal[:ref:`rna_enum_shrinkwrap_type_items`]

   .. attribute:: wrap_mode

      Select how vertices are constrained to the target surface (default ``'ON_SURFACE'``)

      :type: Literal[:ref:`rna_enum_modifier_shrinkwrap_mode_items`]

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

