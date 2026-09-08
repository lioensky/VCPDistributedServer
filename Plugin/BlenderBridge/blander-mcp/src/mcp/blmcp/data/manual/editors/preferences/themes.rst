.. _bpy.types.Theme:

******
Themes
******

The *Themes* section allows you to customize interface appearance and colors.

.. figure:: /images/editors_preferences_section_themes.webp

The colors for each editor can be set separately by simply selecting the editor you wish to
change in the multi-choice list at the left, and adjusting colors as required.
Notice that changes appear in real-time on your screen. In addition, details such as the dot size
in the *3D Viewport* or the *Graph Editor* can also be changed.


Preset Management
=================

Theme Presets
   Select the Theme from a list of predefined Themes.

.. _bpy.ops.wm.interface_theme_preset_add:

:bl-icon:`add` Add Theme
   Adds a custom theme to the preset list.

.. _bpy.ops.wm.interface_theme_preset_remove:

:bl-icon:`remove` Remove Theme
   Removes a custom theme from the preset list.

.. _bpy.ops.wm.interface_theme_preset_save:

:bl-icon:`file_tick` Save Theme
   Save a custom theme in the preset list.

   This will save the theme to an XML file in the ``./scripts/presets/interface_theme/`` subdirectory of one of
   the :doc:`configuration directories </advanced/blender_directory_layout>`.

.. _bpy.ops.preferences.theme_install:

Install
   Load and apply a Blender XML theme file and add it to the list of theme presets.

.. _bpy.ops.preferences.reset_default_theme:

Reset
   Reset to the default theme colors.

Blender comes bundled with a small selection of themes.

.. figure:: /images/editors_preferences_themes_example.png

   This is an example of the theme *Blender Light*.
