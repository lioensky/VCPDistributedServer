Speaker(ID)
===========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Speaker(ID)

   Speaker data-block for 3D audio speaker objects

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: attenuation

      How strong the distance affects volume, depending on distance model (in [0, inf], default 1.0)

      :type: float

   .. attribute:: cone_angle_inner

      Angle of the inner cone, in degrees, inside the cone the volume is 100% (in [0, 360], default 360.0)

      :type: float

   .. attribute:: cone_angle_outer

      Angle of the outer cone, in degrees, outside this cone the volume is the outer cone volume, between inner and outer cone the volume is interpolated (in [0, 360], default 360.0)

      :type: float

   .. attribute:: cone_volume_outer

      Volume outside the outer cone (in [0, 1], default 1.0)

      :type: float

   .. attribute:: distance_max

      Maximum distance for volume calculation, no matter how far away the object is (in [0, inf], default 3.40282e+38)

      :type: float

   .. attribute:: distance_reference

      Reference distance at which volume is 100% (in [0, inf], default 1.0)

      :type: float

   .. attribute:: muted

      Mute the speaker (default False)

      :type: bool

   .. attribute:: pitch

      Playback pitch of the sound (in [0.1, 10], default 1.0)

      :type: float

   .. attribute:: sound

      Sound data-block used by this speaker

      :type: :class:`Sound` | None

   .. attribute:: volume

      How loud the sound is (in [0, 1], default 1.0)

      :type: float

   .. attribute:: volume_max

      Maximum volume, no matter how near the object is (in [0, 1], default 1.0)

      :type: float

   .. attribute:: volume_min

      Minimum volume, no matter how far away the object is (in [0, 1], default 0.0)

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

   - :mod:`bpy.context.speaker`
   - :class:`BlendData.speakers`
   - :class:`BlendDataSpeakers.new`
   - :class:`BlendDataSpeakers.remove`

