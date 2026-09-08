MeshCacheModifier(Modifier)
===========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: MeshCacheModifier(Modifier)

   Cache Mesh

   .. attribute:: cache_format

      (default ``'MDD'``)

      :type: Literal['MDD', 'PC2']

   .. attribute:: deform_mode

      (default ``'OVERWRITE'``)

      - ``OVERWRITE``
        Overwrite -- Replace vertex coordinates with cached values.
      - ``INTEGRATE``
        Integrate -- Integrate deformation from this modifier's input with the mesh-cache coordinates (useful for shape keys).

      :type: Literal['OVERWRITE', 'INTEGRATE']

   .. attribute:: eval_factor

      Evaluation time in seconds (in [0, 1], default 0.0)

      :type: float

   .. attribute:: eval_frame

      The frame to evaluate (starting at 0) (in [0, 1.04857e+06], default 0.0)

      :type: float

   .. attribute:: eval_time

      Evaluation time in seconds (in [0, inf], default 0.0)

      :type: float

   .. attribute:: factor

      Influence of the deformation (in [0, 1], default 1.0)

      :type: float

   .. attribute:: filepath

      Path to external displacements file (default "", never None, blend relative ``//`` prefix supported)

      :type: str

   .. attribute:: flip_axis

      (array of 3 items, default (False, False, False))

      :type: :class:`bpy_prop_array`\ [bool]

   .. attribute:: forward_axis

      (default ``'POS_Y'``)

      :type: Literal[:ref:`rna_enum_object_axis_items`]

   .. attribute:: frame_scale

      Evaluation time in seconds (in [0, 100], default 1.0)

      :type: float

   .. attribute:: frame_start

      Add this to the start frame (in [-1.04857e+06, 1.04857e+06], default 0.0)

      :type: float

   .. attribute:: interpolation

      (default ``'LINEAR'``)

      :type: Literal['NONE', 'LINEAR']

   .. attribute:: invert_vertex_group

      Invert vertex group influence (default False)

      :type: bool

   .. attribute:: play_mode

      (default ``'SCENE'``)

      - ``SCENE``
        Scene -- Use the time from the scene.
      - ``CUSTOM``
        Custom -- Use the modifier's own time evaluation.

      :type: Literal['SCENE', 'CUSTOM']

   .. attribute:: time_mode

      Method to control playback time (default ``'FRAME'``)

      - ``FRAME``
        Frame -- Control playback using a frame-number (ignoring time FPS and start frame from the file).
      - ``TIME``
        Time -- Control playback using time in seconds.
      - ``FACTOR``
        Factor -- Control playback using a value between 0 and 1.

      :type: Literal['FRAME', 'TIME', 'FACTOR']

   .. attribute:: up_axis

      (default ``'POS_Z'``)

      :type: Literal[:ref:`rna_enum_object_axis_items`]

   .. attribute:: vertex_group

      Name of the Vertex Group which determines the influence of the modifier per point (default "", never None)

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

