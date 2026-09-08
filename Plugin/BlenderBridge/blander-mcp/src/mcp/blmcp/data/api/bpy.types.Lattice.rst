Lattice(ID)
===========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Lattice(ID)

   Lattice data-block defining a grid for deforming other objects

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: interpolation_type_u

      (default ``'KEY_BSPLINE'``)

      :type: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']

   .. attribute:: interpolation_type_v

      (default ``'KEY_BSPLINE'``)

      :type: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']

   .. attribute:: interpolation_type_w

      (default ``'KEY_BSPLINE'``)

      :type: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']

   .. data:: is_editmode

      True when used in editmode (default False, readonly)

      :type: bool

   .. data:: points

      Points of the lattice (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`LatticePoint`]

   .. attribute:: points_u

      Points in U direction (cannot be changed when there are shape keys) (in [1, 64], default 0)

      :type: int

   .. attribute:: points_v

      Points in V direction (cannot be changed when there are shape keys) (in [1, 64], default 0)

      :type: int

   .. attribute:: points_w

      Points in W direction (cannot be changed when there are shape keys) (in [1, 64], default 0)

      :type: int

   .. data:: shape_keys

      (readonly)

      :type: :class:`Key` | None

   .. attribute:: use_outside

      Only display and take into account the outer vertices (default False)

      :type: bool

   .. attribute:: vertex_group

      Vertex group to apply the influence of the lattice (default "", never None)

      :type: str

   .. method:: transform(matrix, *, shape_keys=False)

      Transform lattice by a matrix

      :param matrix: Matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
      :type matrix: :class:`mathutils.Matrix` | Sequence[Sequence[float]]
      :param shape_keys: Transform Shape Keys (optional)
      :type shape_keys: bool

   .. method:: update_gpu_tag()

      update_gpu_tag


   .. method:: unit_test_compare(*, lattice=None, threshold=7.1526e-06)

      unit_test_compare

      :param lattice: Lattice to compare to (optional)
      :type lattice: :class:`Lattice` | None
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

   - :mod:`bpy.context.lattice`
   - :class:`BlendData.lattices`
   - :class:`BlendDataLattices.new`
   - :class:`BlendDataLattices.remove`
   - :class:`Lattice.unit_test_compare`

