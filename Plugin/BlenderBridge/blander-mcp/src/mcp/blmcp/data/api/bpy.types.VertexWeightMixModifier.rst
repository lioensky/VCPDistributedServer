VertexWeightMixModifier(Modifier)
=================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: VertexWeightMixModifier(Modifier)

   Mix the weights of two vertex groups

   .. attribute:: default_weight_a

      Default weight a vertex will have if it is not in the first A vgroup (in [0, 1], default 0.0)

      :type: float

   .. attribute:: default_weight_b

      Default weight a vertex will have if it is not in the second B vgroup (in [0, 1], default 0.0)

      :type: float

   .. attribute:: invert_mask_vertex_group

      Invert vertex group mask influence (default False)

      :type: bool

   .. attribute:: invert_vertex_group_a

      Invert the influence of vertex group A (default False)

      :type: bool

   .. attribute:: invert_vertex_group_b

      Invert the influence of vertex group B (default False)

      :type: bool

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

   .. attribute:: mix_mode

      How weights from vgroup B affect weights of vgroup A (default ``'SET'``)

      - ``SET``
        Replace -- Replace VGroup A's weights by VGroup B's ones.
      - ``ADD``
        Add -- Add VGroup B's weights to VGroup A's ones.
      - ``SUB``
        Subtract -- Subtract VGroup B's weights from VGroup A's ones.
      - ``MUL``
        Multiply -- Multiply VGroup A's weights by VGroup B's ones.
      - ``DIV``
        Divide -- Divide VGroup A's weights by VGroup B's ones.
      - ``DIF``
        Difference -- Difference between VGroup A's and VGroup B's weights.
      - ``AVG``
        Average -- Average value of VGroup A's and VGroup B's weights.
      - ``MIN``
        Minimum -- Minimum of VGroup A's and VGroup B's weights.
      - ``MAX``
        Maximum -- Maximum of VGroup A's and VGroup B's weights.

      :type: Literal['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'DIF', 'AVG', 'MIN', 'MAX']

   .. attribute:: mix_set

      Which vertices should be affected (default ``'AND'``)

      - ``ALL``
        All -- Affect all vertices (might add some to VGroup A).
      - ``A``
        VGroup A -- Affect vertices in VGroup A.
      - ``B``
        VGroup B -- Affect vertices in VGroup B (might add some to VGroup A).
      - ``OR``
        VGroup A or B -- Affect vertices in at least one of both VGroups (might add some to VGroup A).
      - ``AND``
        VGroup A and B -- Affect vertices in both groups.

      :type: Literal['ALL', 'A', 'B', 'OR', 'AND']

   .. attribute:: normalize

      Normalize the resulting weights (otherwise they are only clamped within 0.0 to 1.0 range) (default False)

      :type: bool

   .. attribute:: vertex_group_a

      First vertex group name (default "", never None)

      :type: str

   .. attribute:: vertex_group_b

      Second vertex group name (default "", never None)

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

