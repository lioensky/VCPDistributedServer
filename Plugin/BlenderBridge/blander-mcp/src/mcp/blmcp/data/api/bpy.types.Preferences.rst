Preferences(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Preferences(bpy_struct)

   Global preferences

   .. attribute:: active_section

      Preferences (default ``'INTERFACE'``)

      :type: Literal[:ref:`rna_enum_preference_section_items`]

   .. data:: addons

      (default None, readonly)

      :type: :class:`Addons`\ [:class:`Addon`]

   .. attribute:: app_template

      (default "", never None)

      :type: str

   .. data:: apps

      Preferences that work only for apps (readonly, never None)

      :type: :class:`PreferencesApps`

   .. data:: autoexec_paths

      (default None, readonly)

      :type: :class:`PathCompareCollection`\ [:class:`PathCompare`]

   .. data:: edit

      Settings for interacting with Blender data (readonly, never None)

      :type: :class:`PreferencesEdit`

   .. data:: experimental

      Settings for features that are still early in their development stage (readonly, never None)

      :type: :class:`PreferencesExperimental`

   .. data:: extensions

      Settings for extensions (readonly, never None)

      :type: :class:`PreferencesExtensions`

   .. data:: filepaths

      Default paths for external files (readonly, never None)

      :type: :class:`PreferencesFilePaths`

   .. data:: inputs

      Settings for input devices (readonly, never None)

      :type: :class:`PreferencesInput`

   .. attribute:: is_dirty

      Preferences have changed (default False)

      :type: bool

   .. data:: keymap

      Shortcut setup for keyboards and other input devices (readonly, never None)

      :type: :class:`PreferencesKeymap`

   .. attribute:: show_hidden_ids

      Show data-blocks with dot-prefixed names in search menus (default False)

      :type: bool

   .. data:: studio_lights

      (default None, readonly)

      :type: :class:`StudioLights`\ [:class:`StudioLight`]

   .. data:: system

      Graphics driver and operating system settings (readonly, never None)

      :type: :class:`PreferencesSystem`

   .. data:: themes

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Theme`]

   .. data:: ui_styles

      (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`ThemeStyle`]

   .. attribute:: use_preferences_save

      Save preferences on exit when modified (unless factory settings have been loaded) (default True)

      :type: bool

   .. attribute:: use_recent_searches

      Sort the recently searched items at the top (default True)

      :type: bool

   .. data:: version

      Version of Blender the userpref.blend was saved with (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: view

      Preferences related to viewing data (readonly, never None)

      :type: :class:`PreferencesView`

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

   - :class:`Context.preferences`

