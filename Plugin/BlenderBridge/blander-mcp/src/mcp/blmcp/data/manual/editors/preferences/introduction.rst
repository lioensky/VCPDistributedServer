.. index:: Editors; Preferences

.. todo: use substitutions, see: https://stackoverflow.com/questions/56557296
.. |menu| unicode:: U+2630

************
Introduction
************

.. _bpy.ops.screen.userpref_show:

.. reference::

   :Menu:      :menuselection:`Edit --> Preferences...`
   :Shortcut:  :kbd:`Ctrl-Comma`

This chapter explains how to change Blender's default configuration with the *Preferences* editor.

The Blender *Preferences* contains settings to control how Blender behaves.
At the left of the editor, the available options are grouped into sections.

.. figure:: /images/editors_preferences_section_interface.webp

   Blender Preferences window.


.. _bpy.ops.preferences.copy_prev:
.. _prefs-menu:

Managing Preferences
====================

Default preferences are managed from the :menuselection:`☰` menu in the preferences window.

The following items are available in this menu:

Auto-Save Preferences
   By default changes to preferences are saved on exit,
   this allows changes to the keymap and Quick Favorites menu to be stored and used between
   :term:`Blender Sessions <Blender Session>`.

   .. _bpy.ops.wm.save_userpref:

   When disabled, a *Save Preferences* button is shown to manually perform the operation.

.. _bpy.ops.wm.read_userpref:

Revert to Saved Preferences
   Undoes any unsaved modifications, loading the previously saved state.

.. _bpy.ops.wm.read_factory_userpref:

Load Factory Preferences
   Completely undo all the modifications made to the preferences,
   resetting to the state used before making customizations.

   .. note::

      After running *Load Factory Preferences*, auto-save will be disabled for the current
      :term:`session`.

      This allows you to switch back to the factory settings for testing
      or following tutorials for example, without the risk of accidentally auto-saving
      over the preferences you have manually configured.

      If you wish to save these as your preferences, run *Save Preferences* manually.

   .. note::

      This only resets the preferences and will not affect settings stored in the startup file.
      This includes app templates, area locations, and any Blender properties not part of the preferences.

      These must be reverted though :menuselection:`File --> Defaults`.

.. tip::

   It can be valuable to make a backup of your preferences in the event that you lose your configuration.

   See the :doc:`directory layout </advanced/blender_directory_layout>`
   section to see where your preferences are stored.
