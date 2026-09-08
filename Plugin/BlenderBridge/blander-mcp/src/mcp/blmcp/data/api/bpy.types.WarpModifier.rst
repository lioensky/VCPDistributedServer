WarpModifier(Modifier)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: WarpModifier(Modifier)

   Warp modifier

   .. attribute:: bone_from

      Bone to transform from (default "", never None)

      :type: str

   .. attribute:: bone_to

      Bone defining offset (default "", never None)

      :type: str

   .. data:: falloff_curve

      Custom falloff curve (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: falloff_radius

      Radius to apply (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: falloff_type

      (default ``'SMOOTH'``)

      :type: Literal['NONE', 'CURVE', 'SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT']

   .. attribute:: invert_vertex_group

      Invert vertex group influence (default False)

      :type: bool

   .. attribute:: object_from

      Object to transform from

      :type: :class:`Object` | None

   .. attribute:: object_to

      Object to transform to

      :type: :class:`Object` | None

   .. attribute:: strength

      (in [-inf, inf], default 1.0)

      :type: float

   .. attribute:: texture

      :type: :class:`Texture` | None

   .. attribute:: texture_coords

      (default ``'LOCAL'``)

      - ``LOCAL``
        Local -- Use the local coordinate system for the texture coordinates.
      - ``GLOBAL``
        Global -- Use the global coordinate system for the texture coordinates.
      - ``OBJECT``
        Object -- Use the linked object's local coordinate system for the texture coordinates.
      - ``UV``
        UV -- Use UV coordinates for the texture coordinates.

      :type: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']

   .. attribute:: texture_coords_bone

      Bone to set the texture coordinates (default "", never None)

      :type: str

   .. attribute:: texture_coords_object

      Object to set the texture coordinates

      :type: :class:`Object` | None

   .. attribute:: use_volume_preserve

      Preserve volume when rotations are used (default False)

      :type: bool

   .. attribute:: uv_layer

      UV map name (default "", never None)

      :type: str

   .. attribute:: vertex_group

      Vertex group name for modulating the deform (default "", never None)

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

