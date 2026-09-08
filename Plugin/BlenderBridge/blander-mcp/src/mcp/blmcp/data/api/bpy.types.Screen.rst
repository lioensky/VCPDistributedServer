Screen(ID)
==========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Screen(ID)

   Screen data-block, defining the layout of areas in a window

   .. data:: areas

      Areas the screen is subdivided into (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Area`]

   .. data:: is_animation_playing

      Animation playback is active (default False, readonly)

      :type: bool

   .. data:: is_scrubbing

      True when the user is scrubbing through time (default False, readonly)

      :type: bool

   .. data:: is_temporary

      (default False, readonly)

      :type: bool

   .. data:: show_fullscreen

      An area is maximized, filling this screen (default False, readonly)

      :type: bool

   .. attribute:: show_statusbar

      Show status bar (default True)

      :type: bool

   .. attribute:: use_follow

      Follow current frame in editors (default False)

      :type: bool

   .. attribute:: use_play_3d_editors

      (default False)

      :type: bool

   .. attribute:: use_play_animation_editors

      (default False)

      :type: bool

   .. attribute:: use_play_clip_editors

      (default False)

      :type: bool

   .. attribute:: use_play_image_editors

      (default False)

      :type: bool

   .. attribute:: use_play_node_editors

      (default False)

      :type: bool

   .. attribute:: use_play_properties_editors

      (default False)

      :type: bool

   .. attribute:: use_play_sequence_editors

      (default False)

      :type: bool

   .. attribute:: use_play_spreadsheet_editors

      (default False)

      :type: bool

   .. attribute:: use_play_top_left_3d_editor

      (default False)

      :type: bool

   .. method:: statusbar_info()

      statusbar_info

      :return: Status Bar Info, (never None)
      :rtype: str

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

   - :class:`BlendData.screens`
   - :class:`Context.screen`
   - :class:`Window.screen`
   - :class:`WorkSpace.screens`

