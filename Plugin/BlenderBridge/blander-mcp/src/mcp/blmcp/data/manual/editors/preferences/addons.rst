
*******
Add-ons
*******

The Add-ons section lets you manage secondary scripts, called “Add-ons” that extends Blender's functionality.
Most of the time you can get add-ons as part of the :ref:`Extensions <extensions-index>` system.

In this section you can search, install, enable and disable Add-ons.

.. figure:: /images/editors_preferences_section_addons.webp

   Blender Preferences Add-ons section.

.. tip::

   If the Add-on does not activate when enabled,
   check the :ref:`Console window <command_line-index>`
   for any errors that may have occurred.


Filtering Add-ons
=================

.. _bpy.types.WindowManager.addon_search:

Search Add-ons
   Blender comes with some preinstalled Add-ons already, ready to be enabled.
   But you can also add your own, or any interesting ones you find on the web.

.. _bpy.types.PreferencesView.show_addons_enabled_only:

Enabled Add-ons Only
   Shows only enabled add-ons for the current Category.

Add-on Tags
   Add-ons are assigned categories by what areas of Blender they affect.


Add-on Settings
===============

Refresh Local
   Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting).
   Any issues are reported as warnings.
Install from Disk
   Install an extension from a ``.zip`` package.
   This is installed to a Local Repository and no updates will be available.

   This can also be used to install legacy Add-ons, for more information see:
   :ref:`prefs-extensions-install_legacy_addon`.


.. _bpy.ops.preferences.addon_enable:
.. _bpy.ops.preferences.addon_disable:

Enabling & Disabling Add-ons
============================

To enable or disable an add-on check or uncheck the box to the right of the add-ons.

The add-on functionality should be immediately available.


Add-on Information
==================

You can click the arrow at the left of the add-on box to see more information,
such as its location, a description and a link to the documentation.
Here you can also find a button to report a bug specific of this add-on.

.. _bpy.types.AddonPreferences:

Add-on Preferences
------------------

Some add-ons may have their own preferences which can be found
in the *Preferences* section of the add-on information box.

Some add-ons use this section for example to enable/disable
certain functions of the add-on. Sometimes these might even all default to off.
So it is important to check if the enabled add-on has any particular preferences.


.. _prefs-extensions-install_legacy_addon:

Installing Legacy Add-ons
=========================

To install legacy add-ons, click the *Install from Disk* menu item and select the add-on's
``.py`` file (if it has only one such file) or its ``.zip`` file.

The add-on will not be automatically enabled after installation; click the checkbox to do that.

Refresh
   Scans the :ref:`Add-on Directory <blender-directory-layout>` for new add-ons.

.. tip::

   While this screen doesn't allow installing a folder-based addon with loose ``.py`` files,
   you can still do so by adding it as a :ref:`Script Directory <bpy.types.ScriptDirectory>`:

   #. Create an empty directory in a location of your choice (e.g. ``my_scripts``).
   #. Add a subdirectory under ``my_scripts`` called ``addons``
      (it *must* have this name for Blender to recognize it).
   #. Place your addon folder inside this ``addons`` folder.
   #. Open the *File Paths* section of the *Preferences*.
   #. Add a *Script Directories* entry pointing to your script folder (e.g. ``my_scripts``).
   #. Save the preferences and restart Blender for it to recognize the new add-on location.

   The add-ons in this folder will automatically become available; all you need to
   do is enable them.
