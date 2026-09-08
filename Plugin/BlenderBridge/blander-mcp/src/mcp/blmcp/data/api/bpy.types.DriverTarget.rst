DriverTarget(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DriverTarget(bpy_struct)

   Source of input values for driver variables

   .. attribute:: bone_target

      Name of PoseBone to use as target (default "", never None)

      :type: str

   .. attribute:: context_property

      Type of a context-dependent data-block to access property from (default ``'ACTIVE_SCENE'``)

      - ``ACTIVE_SCENE``
        Active Scene -- Currently evaluating scene.
      - ``ACTIVE_VIEW_LAYER``
        Active View Layer -- Currently evaluating view layer.

      :type: Literal['ACTIVE_SCENE', 'ACTIVE_VIEW_LAYER']

   .. attribute:: data_path

      RNA Path (from ID-block) to property used (default "", never None)

      :type: str

   .. attribute:: fallback_value

      The value to use if the data path cannot be resolved (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: id

      ID-block that the specific property used can be found from (id_type property must be set first)

      :type: :class:`ID` | None

   .. attribute:: id_type

      Type of ID-block that can be used (default ``'OBJECT'``)

      :type: Literal[:ref:`rna_enum_id_type_items`]

   .. data:: is_fallback_used

      Indicates that the most recent variable evaluation used the fallback value (default False, readonly)

      :type: bool

   .. attribute:: rotation_mode

      Mode for calculating rotation channel values (default ``'AUTO'``)

      :type: Literal[:ref:`rna_enum_driver_target_rotation_mode_items`]

   .. attribute:: transform_space

      Space in which transforms are used (default ``'WORLD_SPACE'``)

      - ``WORLD_SPACE``
        World Space -- Transforms include effects of parenting/restpose and constraints.
      - ``TRANSFORM_SPACE``
        Transform Space -- Transforms don't include parenting/restpose or constraints.
      - ``LOCAL_SPACE``
        Local Space -- Transforms include effects of constraints but not parenting/restpose.

      :type: Literal['WORLD_SPACE', 'TRANSFORM_SPACE', 'LOCAL_SPACE']

   .. attribute:: transform_type

      Driver variable type (default ``'LOC_X'``)

      :type: Literal['LOC_X', 'LOC_Y', 'LOC_Z', 'ROT_X', 'ROT_Y', 'ROT_Z', 'ROT_W', 'SCALE_X', 'SCALE_Y', 'SCALE_Z', 'SCALE_AVG']

   .. attribute:: use_fallback_value

      Use the fallback value if the data path cannot be resolved, instead of failing to evaluate the driver (default False)

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

   - :class:`DriverVariable.targets`

