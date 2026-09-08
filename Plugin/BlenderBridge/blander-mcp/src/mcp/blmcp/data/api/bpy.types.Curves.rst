Curves(ID)
==========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Curves(ID)

   Hair data-block for hair curves

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. data:: attributes

      Geometry attributes (default None, readonly)

      :type: :class:`AttributeGroupCurves`\ [:class:`Attribute`]

   .. data:: color_attributes

      Geometry color attributes (default None, readonly)

      :type: :class:`AttributeGroupCurves`\ [:class:`Attribute`]

   .. data:: curve_offset_data

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`IntAttributeValue`]

   .. data:: curves

      All curves in the data-block (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`CurveSlice`]

   .. data:: materials

      (default None, readonly)

      :type: :class:`IDMaterials`\ [:class:`Material`]

   .. data:: normals

      The curve normal value at each of the curve's control points (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`FloatVectorValueReadOnly`]

   .. data:: points

      Control points of all curves (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`CurvePoint`]

   .. data:: position_data

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`FloatVectorAttributeValue`]

   .. attribute:: selection_domain

      (default ``'POINT'``)

      :type: Literal[:ref:`rna_enum_attribute_curves_domain_items`]

   .. attribute:: surface

      Mesh object that the curves can be attached to

      :type: :class:`Object` | None

   .. attribute:: surface_collision_distance

      Distance to keep the curves away from the surface (in [1.192e-07, inf], default 0.005)

      :type: float

   .. attribute:: surface_uv_map

      The name of the attribute on the surface mesh used to define the attachment of each curve (default "", never None)

      :type: str

   .. attribute:: use_mirror_x

      Enable symmetry in the X axis (default False)

      :type: bool

   .. attribute:: use_mirror_y

      Enable symmetry in the Y axis (default False)

      :type: bool

   .. attribute:: use_mirror_z

      Enable symmetry in the Z axis (default False)

      :type: bool

   .. attribute:: use_sculpt_collision

      Enable collision with the surface while sculpting (default False)

      :type: bool

   .. method:: add_curves(sizes)

      add_curves

      :param sizes: Sizes, The number of points in each curve (array of 1 items, in [0, inf])
      :type sizes: Sequence[int]

   .. method:: remove_curves(*, indices=(0,))

      Remove all curves. If indices are provided, remove only the curves with the given indices.

      :param indices: Indices, The indices of the curves to remove (array of 1 items, in [0, inf], optional)
      :type indices: Sequence[int]

   .. method:: resize_curves(sizes, *, indices=(0,))

      Resize all existing curves. If indices are provided, resize only the curves with the given indices. If the new size for a curve is smaller, the curve is trimmed. If the new size for a curve is larger, the new end values are default initialized.

      :param sizes: Sizes, The number of points in each curve (array of 1 items, in [1, inf])
      :type sizes: Sequence[int]
      :param indices: Indices, The indices of the curves to resize (array of 1 items, in [0, inf], optional)
      :type indices: Sequence[int]

   .. method:: reorder_curves(new_indices)

      Reorder the curves by the new indices.

      :param new_indices: New indices, The new index for each of the curves (array of 1 items, in [0, inf])
      :type new_indices: Sequence[int]

   .. method:: set_types(*, type='CATMULL_ROM', indices=(0,))

      Set the curve type. If indices are provided, set only the types with the given curve indices.

      :param type: Type, (optional)
      :type type: Literal[:ref:`rna_enum_curves_type_items`]
      :param indices: Indices, The indices of the curves to resize (array of 1 items, in [0, inf], optional)
      :type indices: Sequence[int]

   .. method:: unit_test_compare(*, curves=None, threshold=7.1526e-06)

      unit_test_compare

      :param curves: Curves to compare to (optional)
      :type curves: :class:`Curves` | None
      :param threshold: Threshold, Comparison tolerance threshold (in [0, inf], optional)
      :type threshold: float
      :return: Return value, String description of result of comparison (never None)
      :rtype: str

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :mod:`bpy.context.curves`
   - :class:`BlendData.hair_curves`
   - :class:`BlendDataHairCurves.new`
   - :class:`BlendDataHairCurves.remove`
   - :class:`Curves.unit_test_compare`

