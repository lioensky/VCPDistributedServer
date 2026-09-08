Theme(bpy_struct)
=================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Theme(bpy_struct)

   User interface styling and color settings

   .. data:: bone_color_sets

      (default None, readonly, never None)

      :type: :class:`bpy_prop_collection`\ [:class:`ThemeBoneColorSet`]

   .. data:: clip_editor

      (readonly, never None)

      :type: :class:`ThemeClipEditor`

   .. data:: collection_color

      (default None, readonly, never None)

      :type: :class:`bpy_prop_collection`\ [:class:`ThemeCollectionColor`]

   .. data:: common

      Theme properties shared by different editors (readonly, never None)

      :type: :class:`ThemeCommon`

   .. data:: console

      (readonly, never None)

      :type: :class:`ThemeConsole`

   .. data:: dopesheet_editor

      (readonly, never None)

      :type: :class:`ThemeDopeSheet`

   .. data:: file_browser

      (readonly, never None)

      :type: :class:`ThemeFileBrowser`

   .. attribute:: filepath

      The path to the preset loaded into this theme (if any) (default "", never None)

      :type: str

   .. data:: graph_editor

      (readonly, never None)

      :type: :class:`ThemeGraphEditor`

   .. data:: image_editor

      (readonly, never None)

      :type: :class:`ThemeImageEditor`

   .. data:: info

      (readonly, never None)

      :type: :class:`ThemeInfo`

   .. attribute:: name

      Name of the theme (default "", never None)

      :type: str

   .. data:: nla_editor

      (readonly, never None)

      :type: :class:`ThemeNLAEditor`

   .. data:: node_editor

      (readonly, never None)

      :type: :class:`ThemeNodeEditor`

   .. data:: outliner

      (readonly, never None)

      :type: :class:`ThemeOutliner`

   .. data:: preferences

      (readonly, never None)

      :type: :class:`ThemePreferences`

   .. data:: properties

      (readonly, never None)

      :type: :class:`ThemeProperties`

   .. data:: regions

      Theme properties for common editor regions (readonly, never None)

      :type: :class:`ThemeRegions`

   .. data:: sequence_editor

      (readonly, never None)

      :type: :class:`ThemeSequenceEditor`

   .. data:: spreadsheet

      (readonly, never None)

      :type: :class:`ThemeSpreadsheet`

   .. data:: statusbar

      (readonly, never None)

      :type: :class:`ThemeStatusBar`

   .. data:: strip_color

      (default None, readonly, never None)

      :type: :class:`bpy_prop_collection`\ [:class:`ThemeStripColor`]

   .. data:: text_editor

      (readonly, never None)

      :type: :class:`ThemeTextEditor`

   .. attribute:: theme_area

      (default ``'USER_INTERFACE'``)

      :type: Literal['USER_INTERFACE', 'STYLE', 'REGIONS', 'COMMON', 'VIEW_3D', 'DOPESHEET_EDITOR', 'FILE_BROWSER', 'GRAPH_EDITOR', 'IMAGE_EDITOR', 'INFO', 'CLIP_EDITOR', 'NODE_EDITOR', 'NLA_EDITOR', 'OUTLINER', 'PREFERENCES', 'PROPERTIES', 'CONSOLE', 'SPREADSHEET', 'STATUSBAR', 'TEXT_EDITOR', 'TOPBAR', 'SEQUENCE_EDITOR', 'BONE_COLOR_SETS']

   .. data:: topbar

      (readonly, never None)

      :type: :class:`ThemeTopBar`

   .. data:: user_interface

      (readonly, never None)

      :type: :class:`ThemeUserInterface`

   .. data:: view_3d

      (readonly, never None)

      :type: :class:`ThemeView3D`

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

   - :class:`Preferences.themes`

