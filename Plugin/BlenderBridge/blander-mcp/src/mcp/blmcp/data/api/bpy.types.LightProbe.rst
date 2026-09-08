LightProbe(ID)
==============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

subclasses --- 
:class:`LightProbePlane`, :class:`LightProbeSphere`, :class:`LightProbeVolume`

.. class:: LightProbe(ID)

   Light Probe data-block for lighting capture objects

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: clip_start

      Probe clip start, below which objects will not appear in reflections (in [1e-06, inf], default 0.8)

      :type: float

   .. attribute:: data_display_size

      Viewport display size of the sampled data (in [0, inf], default 0.1)

      :type: float

   .. attribute:: influence_distance

      Influence distance of the probe (in [0, inf], default 2.5)

      :type: float

   .. attribute:: invert_visibility_collection

      Invert visibility collection (Deprecated) (default False)

      :type: bool

   .. attribute:: show_clip

      Show the clipping distances in the 3D view (default False)

      :type: bool

   .. attribute:: show_data

      Deprecated, use use_data_display instead (default False)

      :type: bool

   .. attribute:: show_influence

      Show the influence volume in the 3D view (default True)

      :type: bool

   .. data:: type

      Type of light probe (default ``'SPHERE'``, readonly)

      - ``SPHERE``
        Sphere -- Light probe that captures precise lighting from all directions at a single point in space.
      - ``PLANE``
        Plane -- Light probe that captures incoming light from a single direction on a plane.
      - ``VOLUME``
        Volume -- Light probe that captures low frequency lighting inside a volume.

      :type: Literal['SPHERE', 'PLANE', 'VOLUME']

   .. attribute:: use_data_display

      Display sampled data in the viewport to debug captured light (default False)

      :type: bool

   .. attribute:: visibility_bleed_bias

      Bias for reducing light-bleed on variance shadow maps (Deprecated) (in [0, 1], default 0.0)

      :type: float

   .. attribute:: visibility_blur

      Filter size of the visibility blur (Deprecated) (in [0, 1], default 0.2)

      :type: float

   .. attribute:: visibility_buffer_bias

      Bias for reducing self shadowing (Deprecated) (in [0.001, 9999], default 1.0)

      :type: float

   .. attribute:: visibility_collection

      Restrict objects visible for this probe (Deprecated)

      :type: :class:`Collection` | None

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :mod:`bpy.context.lightprobe`
   - :class:`BlendData.lightprobes`
   - :class:`BlendDataProbes.new`
   - :class:`BlendDataProbes.remove`

