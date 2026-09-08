BooleanModifier(Modifier)
=========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: BooleanModifier(Modifier)

   Boolean operations modifier

   .. attribute:: collection

      Use mesh objects in this collection for Boolean operation

      :type: :class:`Collection` | None

   .. attribute:: debug_options

      Debugging options, only when started with '-d' (default set())

      :type: set[Literal['SEPARATE', 'NO_DISSOLVE', 'NO_CONNECT_REGIONS']]

   .. attribute:: double_threshold

      Threshold for checking overlapping geometry (in [0, 1], default 1e-06)

      :type: float

   .. attribute:: material_mode

      Method for setting materials on the new faces (default ``'INDEX'``)

      - ``INDEX``
        Index Based -- Set the material on new faces based on the order of the material slot lists. If a material does not exist on the modifier object, the face will use the same material slot or the first if the object does not have enough slots..
      - ``TRANSFER``
        Transfer -- Transfer materials from non-empty slots to the result mesh, adding new materials as necessary. For empty slots, fall back to using the same material index as the operand mesh..

      :type: Literal['INDEX', 'TRANSFER']

   .. attribute:: object

      Mesh object to use for Boolean operation

      :type: :class:`Object` | None

   .. attribute:: operand_type

      (default ``'OBJECT'``)

      - ``OBJECT``
        Object -- Use a mesh object as the operand for the Boolean operation.
      - ``COLLECTION``
        Collection -- Use a collection of mesh objects as the operand for the Boolean operation.

      :type: Literal['OBJECT', 'COLLECTION']

   .. attribute:: operation

      (default ``'DIFFERENCE'``)

      - ``INTERSECT``
        Intersect -- Keep the part of the mesh that is common between all operands.
      - ``UNION``
        Union -- Combine meshes in an additive way.
      - ``DIFFERENCE``
        Difference -- Combine meshes in a subtractive way.

      :type: Literal['INTERSECT', 'UNION', 'DIFFERENCE']

   .. attribute:: solver

      Method for calculating booleans (default ``'EXACT'``)

      - ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      - ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      - ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.

      :type: Literal['FLOAT', 'EXACT', 'MANIFOLD']

   .. attribute:: use_hole_tolerant

      Better results when there are holes (slower) (default False)

      :type: bool

   .. attribute:: use_self

      Allow self-intersection in operands (default False)

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

