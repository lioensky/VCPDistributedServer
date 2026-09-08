WorkSpace(ID)
=============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: WorkSpace(ID)

   Workspace data-block, defining the working environment for the user

   .. attribute:: active_addon

      Active Add-on in the Workspace Add-ons filter (in [-inf, inf], default 0)

      :type: int

   .. attribute:: asset_library_reference

      Active asset library to show in the UI, not used by the Asset Browser (which has its own active asset library) (default ``'ALL'``)

      - ``ALL``
        All Libraries -- Show assets from all of the listed asset libraries.
      - ``LOCAL``
        Current File -- Show the assets currently available in this Blender session.
      - ``ESSENTIALS``
        Essentials -- Show the basic building blocks and utilities coming with Blender.
      - ``CUSTOM``
        Custom -- Show assets from the asset libraries configured in the Preferences.

      :type: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']

   .. attribute:: object_mode

      Switch to this object mode when activating the workspace (default ``'OBJECT'``)

      :type: Literal[:ref:`rna_enum_workspace_object_mode_items`]

   .. data:: owner_ids

      (default None, readonly)

      :type: :class:`wmOwnerIDs`\ [:class:`wmOwnerID`]

   .. data:: screens

      Screen layouts of a workspace (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Screen`]

   .. attribute:: sequencer_scene

      :type: :class:`Scene` | None

   .. data:: tools

      (default None, readonly)

      :type: :class:`wmTools`\ [:class:`WorkSpaceTool`]

   .. attribute:: use_filter_by_owner

      Filter the UI by tags (default False)

      :type: bool

   .. attribute:: use_pin_scene

      Remember the last used scene for the workspace and switch to it whenever this workspace is activated again (default False)

      :type: bool

   .. attribute:: use_scene_time_sync

      Set the active scene and time based on the current scene strip (default False)

      :type: bool

   .. classmethod:: status_text_set_internal(text)

      Set the status bar text, typically key shortcuts for modal operators

      :param text: Text, New string for the status bar, None clears the text
      :type text: str

   .. method:: status_text_set(text)

      Set the status text or None to clear,
      When text is a function, this will be called with the (header, context) arguments.

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

   - :class:`BlendData.workspaces`
   - :class:`Context.workspace`
   - :class:`Window.workspace`

