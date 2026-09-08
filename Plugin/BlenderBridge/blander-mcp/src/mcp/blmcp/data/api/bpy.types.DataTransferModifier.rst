DataTransferModifier(Modifier)
==============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: DataTransferModifier(Modifier)

   Modifier transferring some data from a source mesh

   .. attribute:: data_types_edges

      Which edge data layers to transfer (default set())

      - ``SHARP_EDGE``
        Sharp -- Transfer sharp mark.
      - ``SEAM``
        UV Seam -- Transfer UV seam mark.
      - ``CREASE``
        Crease -- Transfer subdivision crease values.
      - ``BEVEL_WEIGHT_EDGE``
        Bevel Weight -- Transfer bevel weights.
      - ``FREESTYLE_EDGE``
        Freestyle -- Transfer Freestyle edge mark.

      :type: set[Literal['SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE']]

   .. attribute:: data_types_loops

      Which face corner data layers to transfer (default set())

      - ``CUSTOM_NORMAL``
        Custom Normals -- Transfer custom normals.
      - ``COLOR_CORNER``
        Colors -- Transfer color attributes.
      - ``UV``
        UVs -- Transfer UV layers.

      :type: set[Literal['CUSTOM_NORMAL', 'COLOR_CORNER', 'UV']]

   .. attribute:: data_types_polys

      Which face data layers to transfer (default set())

      - ``SMOOTH``
        Smooth -- Transfer flat/smooth mark.
      - ``FREESTYLE_FACE``
        Freestyle Mark -- Transfer Freestyle face mark.

      :type: set[Literal['SMOOTH', 'FREESTYLE_FACE']]

   .. attribute:: data_types_verts

      Which vertex data layers to transfer (default set())

      - ``VGROUP_WEIGHTS``
        Vertex Groups -- Transfer active or all vertex groups.
      - ``BEVEL_WEIGHT_VERT``
        Bevel Weight -- Transfer bevel weights.
      - ``COLOR_VERTEX``
        Colors -- Transfer color attributes.

      :type: set[Literal['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'COLOR_VERTEX']]

   .. attribute:: edge_mapping

      Method used to map source edges to destination ones (default ``'NEAREST'``)

      :type: Literal[:ref:`rna_enum_dt_method_edge_items`]

   .. attribute:: invert_vertex_group

      Invert vertex group influence (default False)

      :type: bool

   .. attribute:: islands_precision

      Factor controlling precision of islands handling (typically, 0.1 should be enough, higher values can make things really slow) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: layers_uv_select_dst

      How to match source and destination layers (default ``'NAME'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_dst_items`]

   .. attribute:: layers_uv_select_src

      Which layers to transfer, in case of multi-layers types (default ``'ALL'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_src_items`]

   .. attribute:: layers_vcol_loop_select_dst

      How to match source and destination layers (default ``'NAME'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_dst_items`]

   .. attribute:: layers_vcol_loop_select_src

      Which layers to transfer, in case of multi-layers types (default ``'ALL'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_src_items`]

   .. attribute:: layers_vcol_vert_select_dst

      How to match source and destination layers (default ``'NAME'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_dst_items`]

   .. attribute:: layers_vcol_vert_select_src

      Which layers to transfer, in case of multi-layers types (default ``'ALL'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_src_items`]

   .. attribute:: layers_vgroup_select_dst

      How to match source and destination layers (default ``'NAME'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_dst_items`]

   .. attribute:: layers_vgroup_select_src

      Which layers to transfer, in case of multi-layers types (default ``'ALL'``)

      :type: Literal[:ref:`rna_enum_dt_layers_select_src_items`]

   .. attribute:: loop_mapping

      Method used to map source faces' corners to destination ones (default ``'NEAREST_POLYNOR'``)

      :type: Literal[:ref:`rna_enum_dt_method_loop_items`]

   .. attribute:: max_distance

      Maximum allowed distance between source and destination element, for non-topology mappings (in [0, inf], default 1.0)

      :type: float

   .. attribute:: mix_factor

      Factor to use when applying data to destination (exact behavior depends on mix mode, multiplied with weights from vertex group when defined) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: mix_mode

      How to affect destination elements with source values (default ``'REPLACE'``)

      :type: Literal[:ref:`rna_enum_dt_mix_mode_items`]

   .. attribute:: object

      Object to transfer data from

      :type: :class:`Object` | None

   .. attribute:: poly_mapping

      Method used to map source faces to destination ones (default ``'NEAREST'``)

      :type: Literal[:ref:`rna_enum_dt_method_poly_items`]

   .. attribute:: ray_radius

      'Width' of rays (especially useful when raycasting against vertices or edges) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: use_edge_data

      Enable edge data transfer (default False)

      :type: bool

   .. attribute:: use_loop_data

      Enable face corner data transfer (default False)

      :type: bool

   .. attribute:: use_max_distance

      Source elements must be closer than given distance from destination one (default False)

      :type: bool

   .. attribute:: use_object_transform

      Evaluate source and destination meshes in global space (default True)

      :type: bool

   .. attribute:: use_poly_data

      Enable face data transfer (default False)

      :type: bool

   .. attribute:: use_vert_data

      Enable vertex data transfer (default False)

      :type: bool

   .. attribute:: vert_mapping

      Method used to map source vertices to destination ones (default ``'NEAREST'``)

      :type: Literal[:ref:`rna_enum_dt_method_vertex_items`]

   .. attribute:: vertex_group

      Vertex group name for selecting the affected areas (default "", never None)

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

