.. _splash-quick-start:

********
Defaults
********

When you start Blender for the first time or update to a new version, the interactive region of
the :doc:`Splash Screen </interface/window_system/splash>` is replaced with a few initial preferences to configure
how you interact with Blender.

.. figure:: /images/getting-started_configuration_defaults_preferences.png

   The initial preferences dialog.


.. note::

   These options can always be changed later in the :doc:`Preferences </editors/preferences/index>`.


Import Preferences From Previous Version
========================================

Selecting this option will copy preferences from an older version of Blender. Doing so will copy preferences and
startup files from the previous version of Blender and load them. This will include installed add-ons and extensions.

The preferences need to be imported from previous versions because the configuration files of each Blender version are
stored in separate folders. Refer to the :doc:`/advanced/blender_directory_layout` page for the location of these
folders.

If you would like to start fresh with the new version, continue to `Create New Preferences`_.

.. note::

   Some previous Blender add-ons and extensions may not be compatible with a new version of Blender, and choosing this
   option may lead to errors on startup.  If this occurs, the recommended first step is to try `Loading Factory
   Settings`_.


Create New Preferences
======================

Language
   The language used in the user interface. The list is broken up into categories determining how complete the
   translations are. More language preferences can be set in the
   :ref:`Translation Preferences <prefs-interface-translation>`.

Theme
   Choose between a light or dark theme for Blender. Themes can be customized more in the
   :doc:`Preferences </editors/preferences/themes>`. Additional themes can be installed by visiting the
   `Blender Extensions Platform <https://extensions.blender.org/>`__. This is optional, and will require internet
   access.

Keymap
   Presets for the default :doc:`keymap </editors/preferences/keymap>` for Blender. Note that this manual assumes that
   you use the default "Blender" keymap.

   :Blender:
      This is the default keymap. Read more about this keymap :doc:`here </interface/keymap/blender_default>`.
   :Blender 2.7x:
      This keymap is intended to match an older series of Blender versions and is designed for people upgrading who do
      not want to learn the updated keymap.
   :Industry Compatible:
      This keymap is intended to match common commercial creation software and is intended for people who use many
      different such applications. Read more about this keymap :doc:`here </interface/keymap/industry_compatible>`.

Mouse Select
   Controls which mouse button, either right or left, is used to select items in Blender. The default is for selection
   to use the left button.

Spacebar Action
   Controls the action of :kbd:`Spacebar`.
   These and other shortcuts can be modified in the :doc:`keymap preferences </editors/preferences/keymap>`.

   :Play:
      Starts/stops :doc:`animation playback </animation/index>`.
      This option is good for animation or video editing work.
   :Tools:
      Opens the Toolbar underneath the cursor to quickly change the active tool. This option is good if doing a lot of
      modeling or rigging.
   :Search:
      Opens up the :ref:`Menu Search <bpy.ops.wm.search_menu>`. This option is good for someone who is new to Blender
      and is unfamiliar with its menus and shortcuts.

Save New Preferences
   Saves the preferences set above and opens the regular :ref:`splash`.


Saving Defaults
===============

The preferences are automatically saved when changed. This behavior can be changed by following the instructions under
:ref:`Auto-Save Preferences <autosave-preferences>`

Changing the default startup file can be done via :menuselection:`File --> Defaults --> Save Startup File`. See
:ref:`Startup File <startup-file>`.

There are two areas where Blender's defaults are stored:

Preferences
   The :ref:`Preferences <prefs-menu>` file stores keymap, add-ons theme and other options.
Startup File
   The :ref:`Startup File <startup-file>` stores the scene and UI setup which are displayed at startup and when
   creating a new file (:menuselection:`File --> New`).


Loading Factory Settings
========================

You can revert your customizations to Blender's defaults:

Preferences
   The :ref:`Preferences <prefs-menu>` Load Factory Settings.
Startup File & Preferences
   :menuselection:`File --> Defaults --> Load Factory Settings`.

.. note::

   After loading the factory settings, the preferences won't be auto-saved.

   See :ref:`prefs-menu` for details.
