GreasePencilOffsetModifier(Modifier)
====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilOffsetModifier(Modifier)


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

   .. attribute:: location

      Values for change location (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: material_filter

      Material used for filtering

      :type: :class:`Material` | None

   .. attribute:: material_pass_filter

      Material pass (in [0, 100], default 0)

      :type: int

   .. attribute:: offset_mode

      (default ``'RANDOM'``)

      - ``RANDOM``
        Random -- Randomize stroke offset.
      - ``LAYER``
        Layer -- Offset layers by the same factor.
      - ``STROKE``
        Stroke -- Offset strokes by the same factor based on stroke draw order.
      - ``MATERIAL``
        Material -- Offset materials by the same factor.

      :type: Literal['RANDOM', 'LAYER', 'STROKE', 'MATERIAL']

   .. attribute:: open_general_panel

      (default False)

      :type: bool

   .. attribute:: open_influence_panel

      (default False)

      :type: bool

   .. attribute:: rotation

      Values for changes in rotation (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Euler`

   .. attribute:: scale

      Values for changes in scale (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: seed

      Random seed (in [0, inf], default 0)

      :type: int

   .. attribute:: stroke_location

      Value for changes in location (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: stroke_rotation

      Value for changes in rotation (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Euler`

   .. attribute:: stroke_scale

      Value for changes in scale (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: stroke_start_offset

      Offset starting point (in [0, inf], default 0)

      :type: int

   .. attribute:: stroke_step

      Number of elements that will be grouped (in [1, 500], default 1)

      :type: int

   .. attribute:: tree_node_filter

      Layer name (default "", never None)

      :type: str

   .. attribute:: use_layer_group_filter

      Filter by layer group name (default False)

      :type: bool

   .. attribute:: use_layer_pass_filter

      Use layer pass filter (default False)

      :type: bool

   .. attribute:: use_material_pass_filter

      Use material pass filter (default False)

      :type: bool

   .. attribute:: use_uniform_random_scale

      Use the same random seed for each scale axis for a uniform scale (default False)

      :type: bool

   .. attribute:: vertex_group_name

      Vertex group name for modulating the deform (default "", never None)

      :type: str

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

