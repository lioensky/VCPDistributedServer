VertexWeightEditModifier(Modifier)
==================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: VertexWeightEditModifier(Modifier)

   Edit the weights of vertices in a group

   .. attribute:: add_threshold

      Lower (inclusive) bound for a vertex's weight to be added to the vgroup (in [-1000, 1000], default 0.01)

      :type: float

   .. attribute:: default_weight

      Default weight a vertex will have if it is not in the vgroup (in [0, 1], default 0.0)

      :type: float

   .. attribute:: falloff_type

      How weights are mapped to their new values (default ``'LINEAR'``)

      - ``LINEAR``
        Linear -- Null action.
      - ``CURVE``
        Custom Curve.
      - ``SHARP``
        Sharp.
      - ``SMOOTH``
        Smooth.
      - ``ROOT``
        Root.
      - ``ICON_SPHERECURVE``
        Sphere.
      - ``RANDOM``
        Random.
      - ``STEP``
        Median Step -- Map all values below 0.5 to 0.0, and all others to 1.0.

      :type: Literal['LINEAR', 'CURVE', 'SHARP', 'SMOOTH', 'ROOT', 'ICON_SPHERECURVE', 'RANDOM', 'STEP']

   .. attribute:: invert_falloff

      Invert the resulting falloff weight (default False)

      :type: bool

   .. attribute:: invert_mask_vertex_group

      Invert vertex group mask influence (default False)

      :type: bool

   .. data:: map_curve

      Custom mapping curve (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: mask_constant

      Global influence of current modifications on vgroup (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: mask_tex_map_bone

      Which bone to take texture coordinates from (default "", never None)

      :type: str

   .. attribute:: mask_tex_map_object

      Which object to take texture coordinates from

      :type: :class:`Object` | None

   .. attribute:: mask_tex_mapping

      Which texture coordinates to use for mapping (default ``'LOCAL'``)

      - ``LOCAL``
        Local -- Use local generated coordinates.
      - ``GLOBAL``
        Global -- Use global coordinates.
      - ``OBJECT``
        Object -- Use local generated coordinates of another object.
      - ``UV``
        UV -- Use coordinates from a UV layer.

      :type: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']

   .. attribute:: mask_tex_use_channel

      Which texture channel to use for masking (default ``'INT'``)

      :type: Literal['INT', 'RED', 'GREEN', 'BLUE', 'HUE', 'SAT', 'VAL', 'ALPHA']

   .. attribute:: mask_tex_uv_layer

      UV map name (default "", never None)

      :type: str

   .. attribute:: mask_texture

      Masking texture

      :type: :class:`Texture` | None

   .. attribute:: mask_vertex_group

      Masking vertex group name (default "", never None)

      :type: str

   .. attribute:: normalize

      Normalize the resulting weights (otherwise they are only clamped within 0.0 to 1.0 range) (default False)

      :type: bool

   .. attribute:: remove_threshold

      Upper (inclusive) bound for a vertex's weight to be removed from the vgroup (in [-1000, 1000], default 0.01)

      :type: float

   .. attribute:: use_add

      Add vertices with weight over threshold to vgroup (default False)

      :type: bool

   .. attribute:: use_remove

      Remove vertices with weight below threshold from vgroup (default False)

      :type: bool

   .. attribute:: vertex_group

      Vertex group name (default "", never None)

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

