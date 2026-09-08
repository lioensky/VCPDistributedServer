CameraStereoData(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CameraStereoData(bpy_struct)

   Stereoscopy settings for a Camera data-block

   .. attribute:: convergence_distance

      The converge point for the stereo cameras (often the distance between a projector and the projection screen) (in [1e-05, inf], default 1.95)

      :type: float

   .. attribute:: convergence_mode

      (default ``'OFFAXIS'``)

      - ``OFFAXIS``
        Off-Axis -- Off-axis frustums converging in a plane.
      - ``PARALLEL``
        Parallel -- Parallel cameras with no convergence.
      - ``TOE``
        Toe-in -- Rotated cameras, looking at the same point at the convergence distance.

      :type: Literal['OFFAXIS', 'PARALLEL', 'TOE']

   .. attribute:: interocular_distance

      Set the distance between the eyes - the stereo plane distance / 30 should be fine (in [0, inf], default 0.065)

      :type: float

   .. attribute:: pivot

      (default ``'LEFT'``)

      :type: Literal['LEFT', 'RIGHT', 'CENTER']

   .. attribute:: pole_merge_angle_from

      Angle at which interocular distance starts to fade to 0 (in [0, 1.5708], default 1.0472)

      :type: float

   .. attribute:: pole_merge_angle_to

      Angle at which interocular distance is 0 (in [0, 1.5708], default 1.309)

      :type: float

   .. attribute:: use_pole_merge

      Fade interocular distance to 0 after the given cutoff angle (default False)

      :type: bool

   .. attribute:: use_spherical_stereo

      Render every pixel rotating the camera around the middle of the interocular distance (default False)

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

   - :class:`Camera.stereo`

