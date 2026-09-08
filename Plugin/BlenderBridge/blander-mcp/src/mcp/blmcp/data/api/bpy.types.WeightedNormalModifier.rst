WeightedNormalModifier(Modifier)
================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: WeightedNormalModifier(Modifier)


   .. attribute:: invert_vertex_group

      Invert vertex group influence (default False)

      :type: bool

   .. attribute:: keep_sharp

      Keep sharp edges as computed for default custom normals, instead of setting a single weighted normal for each vertex (default False)

      :type: bool

   .. attribute:: mode

      Weighted vertex normal mode to use (default ``'FACE_AREA'``)

      - ``FACE_AREA``
        Face Area -- Generate face area weighted normals.
      - ``CORNER_ANGLE``
        Corner Angle -- Generate corner angle weighted normals.
      - ``FACE_AREA_WITH_ANGLE``
        Face Area & Angle -- Generated normals weighted by both face area and angle.

      :type: Literal['FACE_AREA', 'CORNER_ANGLE', 'FACE_AREA_WITH_ANGLE']

   .. attribute:: thresh

      Threshold value for different weights to be considered equal (in [0, 10], default 0.01)

      :type: float

   .. attribute:: use_face_influence

      Use influence of face for weighting (default False)

      :type: bool

   .. attribute:: vertex_group

      Vertex group name for modifying the selected areas (default "", never None)

      :type: str

   .. attribute:: weight

      Corrective factor applied to faces' weights, 50 is neutral, lower values increase weight of weak faces, higher values increase weight of strong faces (in [1, 100], default 50)

      :type: int

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

