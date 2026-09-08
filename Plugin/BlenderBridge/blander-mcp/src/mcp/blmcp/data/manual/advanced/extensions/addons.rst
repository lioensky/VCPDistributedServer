.. _extensions-addons:
.. index:: Add-ons Extensions
.. index:: Add-ons
.. .. _bpy.types.Addon:
.. .. _bpy.ops.wm.addon:
.. .. _bpy.types.WindowManager.addon:

*******
Add-ons
*******

*Add-ons* let you extend Blender's functionality using Python.
Most of the time you can get add-ons as part of the :ref:`Extensions <extensions-index>` system.

.. tip::

   If the Add-on does not activate when enabled,
   check the :ref:`Console window <command_line-index>`
   for any errors that may have occurred.


Internet Access
===============

If the add-on needs to use internet, it must check for the (read-only) property ``bpy.app.online_access``.
This option is controlled by Preferences, which can be overriding via command-line
(``--offline-mode`` / ``--online-mode``).

For better error messages, you can check also for ``bpy.app.online_access_override``,
to determine whether users can turn :ref:`Allow Online Access <bpy.types.PreferencesSystem.use_online_access>`
on the preferences, or not.

.. note::

   Add-ons that follow this setting will only connect to the internet if enabled.
   However, Blender cannot prevent third-party add-ons from violating this rule.


Bundle Dependencies
===================

For add-ons to be bundled as extensions, they must be self-contained.
That means they must come with all its dependencies. In particular 3rd party Python modules.

There are a few options for this:

Bundle with :ref:`Python Wheels <extensions-python_wheels>`.
   This is the recommended way to bundle dependencies.

Bundle other add-ons together.
   This is recommended if an add-on depends on another add-on.

   Make sure that both the individual and the combined add-on
   check for already registered types (Operators, Panels, ...).
   This avoids duplication of operators and panels on the interface
   if the add-ons are installed as a bundle and individually.

Bundle with `Vendorize <https://pypi.org/project/vendorize>`__
   This can be used as a way to bundle a pure Python dependencies as a sub-module.

   This has the advantage of avoiding version conflicts although it requires some work to setup each package.


Local Storage
=============

Add-ons must not assume their own directory is user writable since this may not be the case for "System" repositories.
Writing files into the add-on's directory also has the down side that upgrading the extension will remove all files.

Add-ons which need their own user directory should use a utility function provided for this purpose:

.. code-block:: python

   extension_directory = bpy.utils.extension_path_user(__package__, path="", create=True)

If you wish create subdirectories, this can be done with the ``path`` argument.

This directory will be kept between upgrades but will be removed if the extension is uninstalled.


.. This section is reference for legacy add-on installation.
.. _bpy.ops.preferences.addon_install:

Legacy vs Extension Add-ons
===========================

With the introduction of Extensions in Blender 4.2, the old way of creating add-ons is considered deprecated.
While the changes are rather small they impact existing add-ons.

In order to allow a smooth transition process, the so-called legacy add-ons will continue to be supported by Blender.
They can be installed via :ref:`Install legacy Add-on <prefs-extensions-install_legacy_addon>` button in the User
Preferences.

All add-on maintainers are urged to convert the add-ons they want to share, so they are future proof and can support
features like updating from the extensions platform.


Converting a Legacy Add-on into an Extension
--------------------------------------------

#. Create a :ref:`manifest file <extensions-getting_started>`.
#. Remove the ``bl_info`` information (this is now in the manifest).
#. Replace all references to the module name to ``__package__``.
#. Make all module imports to use relative import.
#. Use `wheels <https://pythonwheels.com/>`__ to pack your external Python dependencies.
#. Remember to test it thoroughly.

.. note::

   For testing it is important to :ref:`install the extension from disk <prefs-extensions>` and check if
   everything is working well. This will get you as close to the final experience as possible.


Extensions and Namespace
------------------------

The legacy add-ons would use their module name to access the preferences. This could lead to a name clash when
extensions with the same name (from different repositories) would be installed.
To prevent this conflict, the repository name is now part of the namespace.

For example, now instead of ``kitsu`` the module name would be ``bl_ext.{repository_module_name}.kitsu`` instead.

This has a few implications for preferences and module imports.


User Preferences and ``__package__``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add-ons can define their own preferences which use the package name as an identifier.
This can be accessed using ``__package__``.

This was already supported in the legacy add-ons, but not reinforced.
As such this can break backward compatibility.

Before:

   .. code-block:: python

      class KitsuPreferences(bpy.types.AddonPreferences):
          bl_idname = "kitsu"
          # ... snip ...

      # Access with:
      addon_prefs = bpy.context.preferences.addons["kitsu"]

Now:

   .. code-block:: python

      class KitsuPreferences(bpy.types.AddonPreferences):
          bl_idname = __package__
          # ... snip ...

      # Access with:
      addon_prefs = bpy.context.preferences.addons[__package__]

Sub-packages
   An add-on that defines sub-packages (sub-directories with their own ``__init__.py`` file)
   that needs to use this identifier will have to import the top-level package using a relative import.

   .. code-block:: python

      from .. import __package__ as base_package

   Then ``base_package`` can be used instead of ``__package__``.
   The ``..`` imports relative to the packages parent, sub-sub-packages must use ``...`` and so on.

.. note::

   - The value of ``__package__`` will vary between systems so it should never be replaced with a literal string.
   - Extensions must not manipulate the value of ``__package__`` as this may cause unexpected behavior or errors.


Relative Imports
^^^^^^^^^^^^^^^^

   :before: ``from kitsu import utils``
   :now: ``from . import utils``

Importing packages within the add-on module need to use relative paths.
This is a standard Python feature and only applicable for add-ons that have multiple folders.

This was already supported in the legacy add-ons, but not reinforced. As such this can break backward compatibility.
