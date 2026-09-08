ScrewModifier(Modifier)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: ScrewModifier(Modifier)

   Revolve edges

   .. attribute:: angle

      Angle of revolution (in [-inf, inf], default 6.28319)

      :type: float

   .. attribute:: axis

      Screw axis (default ``'Z'``)

      :type: Literal[:ref:`rna_enum_axis_xyz_items`]

   .. attribute:: iterations

      Number of times to apply the screw operation (in [1, 10000], default 1)

      :type: int

   .. attribute:: merge_threshold

      Limit below which to merge vertices (in [0, inf], default 0.01)

      :type: float

   .. attribute:: object

      Object to define the screw axis

      :type: :class:`Object` | None

   .. attribute:: render_steps

      Number of steps in the revolution (in [1, 10000], default 16)

      :type: int

   .. attribute:: screw_offset

      Offset the revolution along its axis (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: steps

      Number of steps in the revolution (in [1, 10000], default 16)

      :type: int

   .. attribute:: use_merge_vertices

      Merge adjacent vertices (screw offset must be zero) (default False)

      :type: bool

   .. attribute:: use_normal_calculate

      Calculate the order of edges (needed for meshes, but not curves) (default False)

      :type: bool

   .. attribute:: use_normal_flip

      Flip normals of lathed faces (default False)

      :type: bool

   .. attribute:: use_object_screw_offset

      Use the distance between the objects to make a screw (default False)

      :type: bool

   .. attribute:: use_smooth_shade

      Output faces with smooth shading rather than flat shaded (default True)

      :type: bool

   .. attribute:: use_stretch_u

      Stretch the U coordinates between 0 and 1 when UVs are present (default False)

      :type: bool

   .. attribute:: use_stretch_v

      Stretch the V coordinates between 0 and 1 when UVs are present (default False)

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

