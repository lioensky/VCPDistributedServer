VolumeRender(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: VolumeRender(bpy_struct)

   Volume object render settings

   .. attribute:: clipping

      Value under which voxels are considered empty space to optimize rendering (in [0, 1], default 0.001)

      :type: float

   .. attribute:: precision

      Specify volume data precision. Lower values reduce memory consumption at the cost of detail. (default ``'HALF'``)

      - ``FULL``
        Full -- Use 32-bit floating-point numbers for all data.
      - ``HALF``
        Half -- Use 16-bit floating-point numbers for all data.
      - ``VARIABLE``
        Variable -- Use variable bit quantization.

      :type: Literal['FULL', 'HALF', 'VARIABLE']

   .. attribute:: space

      Specify volume density and step size in object or world space (default ``'OBJECT'``)

      - ``OBJECT``
        Object -- Keep volume opacity and detail the same regardless of object scale.
      - ``WORLD``
        World -- Specify volume step size and density in world space.

      :type: Literal['OBJECT', 'WORLD']

   .. attribute:: step_size

      Distance between volume samples. Lower values render more detail at the cost of performance. If set to zero, the step size is automatically determined based on voxel size. (in [0, inf], default 0.0)

      :type: float

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

   - :class:`Volume.render`

