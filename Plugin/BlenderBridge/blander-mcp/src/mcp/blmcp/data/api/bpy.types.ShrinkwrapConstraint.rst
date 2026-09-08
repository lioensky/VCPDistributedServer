ShrinkwrapConstraint(Constraint)
================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: ShrinkwrapConstraint(Constraint)

   Create constraint-based shrinkwrap relationship

   .. attribute:: cull_face

      Stop vertices from projecting to a face on the target when facing towards/away (default ``'OFF'``)

      - ``OFF``
        Off -- No culling.
      - ``FRONT``
        Front -- No projection when in front of the face.
      - ``BACK``
        Back -- No projection when behind the face.

      :type: Literal['OFF', 'FRONT', 'BACK']

   .. attribute:: distance

      Distance to Target (in [0, inf], default 0.0)

      :type: float

   .. attribute:: project_axis

      Axis constrain to (default ``'POS_X'``)

      :type: Literal[:ref:`rna_enum_object_axis_items`]

   .. attribute:: project_axis_space

      Space for the projection axis (default ``'WORLD'``)

      - ``WORLD``
        World Space -- The constraint is applied relative to the world coordinate system.
      - ``CUSTOM``
        Custom Space -- The constraint is applied in local space of a custom object/bone/vertex group.
      - ``POSE``
        Pose Space -- The constraint is applied in Pose Space, the object transformation is ignored.
      - ``LOCAL_WITH_PARENT``
        Local With Parent -- The constraint is applied relative to the rest pose local coordinate system of the bone, thus including the parent-induced transformation.
      - ``LOCAL``
        Local Space -- The constraint is applied relative to the local coordinate system of the object.

      :type: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']

   .. attribute:: project_limit

      Limit the distance used for projection (zero disables) (in [0, inf], default 0.0)

      :type: float

   .. attribute:: shrinkwrap_type

      Select type of shrinkwrap algorithm for target position (default ``'NEAREST_SURFACE'``)

      - ``NEAREST_SURFACE``
        Nearest Surface Point -- Shrink the location to the nearest target surface.
      - ``PROJECT``
        Project -- Shrink the location to the nearest target surface along a given axis.
      - ``NEAREST_VERTEX``
        Nearest Vertex -- Shrink the location to the nearest target vertex.
      - ``TARGET_PROJECT``
        Target Normal Project -- Shrink the location to the nearest target surface along the interpolated vertex normals of the target.

      :type: Literal['NEAREST_SURFACE', 'PROJECT', 'NEAREST_VERTEX', 'TARGET_PROJECT']

   .. attribute:: target

      Target Mesh object

      :type: :class:`Object` | None

   .. attribute:: track_axis

      Axis that is aligned to the normal (default ``'TRACK_X'``)

      :type: Literal['TRACK_X', 'TRACK_Y', 'TRACK_Z', 'TRACK_NEGATIVE_X', 'TRACK_NEGATIVE_Y', 'TRACK_NEGATIVE_Z']

   .. attribute:: use_invert_cull

      When projecting in the opposite direction invert the face cull mode (default False)

      :type: bool

   .. attribute:: use_project_opposite

      Project in both specified and opposite directions (default False)

      :type: bool

   .. attribute:: use_track_normal

      Align the specified axis to the surface normal (default False)

      :type: bool

   .. attribute:: wrap_mode

      Select how to constrain the object to the target surface (default ``'ON_SURFACE'``)

      :type: Literal[:ref:`rna_enum_modifier_shrinkwrap_mode_items`]

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
   - :class:`Constraint.name`
   - :class:`Constraint.type`
   - :class:`Constraint.is_override_data`
   - :class:`Constraint.owner_space`
   - :class:`Constraint.target_space`
   - :class:`Constraint.space_object`
   - :class:`Constraint.space_subtarget`
   - :class:`Constraint.mute`
   - :class:`Constraint.enabled`
   - :class:`Constraint.show_expanded`
   - :class:`Constraint.is_valid`
   - :class:`Constraint.active`
   - :class:`Constraint.influence`
   - :class:`Constraint.error_location`
   - :class:`Constraint.error_rotation`

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
   - :class:`Constraint.bl_rna_get_subclass`
   - :class:`Constraint.bl_rna_get_subclass_py`

