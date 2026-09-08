RemeshModifier(Modifier)
========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: RemeshModifier(Modifier)

   Generate a new surface with regular topology that follows the shape of the input mesh

   .. attribute:: adaptivity

      Reduces the final face count by simplifying geometry where detail is not needed, generating triangles. A value greater than 0 disables Fix Poles. (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: mode

      (default ``'VOXEL'``)

      - ``BLOCKS``
        Blocks -- Output a blocky surface with no smoothing.
      - ``SMOOTH``
        Smooth -- Output a smooth surface with no sharp-features detection.
      - ``SHARP``
        Sharp -- Output a surface that reproduces sharp edges and corners from the input mesh.
      - ``VOXEL``
        Voxel -- Output a mesh corresponding to the volume of the original mesh.

      :type: Literal['BLOCKS', 'SMOOTH', 'SHARP', 'VOXEL']

   .. attribute:: octree_depth

      Resolution of the octree; higher values give finer details (in [1, 24], default 4)

      :type: int

   .. attribute:: scale

      The ratio of the largest dimension of the model over the size of the grid (in [0, 0.99], default 0.9)

      :type: float

   .. attribute:: sharpness

      Tolerance for outliers; lower values filter noise while higher values will reproduce edges closer to the input (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: threshold

      If removing disconnected pieces, minimum size of components to preserve as a ratio of the number of polygons in the largest component (in [0, 1], default 1.0)

      :type: float

   .. attribute:: use_remove_disconnected

      (default True)

      :type: bool

   .. attribute:: use_smooth_shade

      Output faces with smooth shading rather than flat shaded (default False)

      :type: bool

   .. attribute:: voxel_size

      Size of the voxel in object space used for volume evaluation. Lower values preserve finer details. (in [0, inf], default 0.1)

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

