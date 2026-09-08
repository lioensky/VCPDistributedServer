.. _blender-directory-layout:

**************************
Blender's Directory Layout
**************************

This page documents the different directories used by Blender.

This can be helpful for troubleshooting, automation and customization.


User Directories
================

User directories store preferences, startup file, installed extensions,
presets and more. By default these use the standard configuration folders
for each operating system.

Linux
-----

.. parsed-literal:: $HOME/.config/blender/|BLENDER_VERSION|/

If the ``$XDG_CONFIG_HOME`` environment variable is set:

.. parsed-literal:: $XDG_CONFIG_HOME/blender/|BLENDER_VERSION|/

macOS
-----

.. parsed-literal:: /Users/$USER/Library/Application Support/Blender/|BLENDER_VERSION|/

Windows
-------

.. parsed-literal:: %USERPROFILE%\\AppData\\Roaming\\Blender Foundation\\Blender\\\ |BLENDER_VERSION|\\

.. _portable-installation:

Portable Installation
---------------------

When running Blender from a portable drive, it's possible to keep the configuration
files on the same drive to take with you.

To enable this, create a folder named ``portable`` at the following locations:

- Windows: Next to the Blender executable, in the unzipped folder
- Linux: Next to the Blender executable, in the unzipped folder
- macOS: Inside the application bundle at ``Blender.app/Contents/Resources``

This folder will then store preferences, startup file, installed extensions
and presets.

Environment Variables
---------------------

The ``BLENDER_USER_RESOURCES`` :ref:`environment variable <command-line-args-environment-variables>`
can be set to a custom directory to replace the default user directory.

System Directories
==================

System directories store files that come bundled with Blender and
are required for it to function. This includes scripts, presets, essential
assets and more.

Linux
-----

Archive downloaded from blender.org:

.. parsed-literal:: ./|BLENDER_VERSION|/

Linux distribution packages:

.. parsed-literal:: /usr/share/blender/|BLENDER_VERSION|/

macOS
-----

.. parsed-literal:: ./Blender.app/Contents/Resources/|BLENDER_VERSION|/

Windows
-------

Zip file downloaded from blender.org:

.. parsed-literal:: ./|BLENDER_VERSION|/

Installer downloaded from blender.org:

.. parsed-literal:: %ProgramFiles%\\Blender Foundation\\Blender\\\ |BLENDER_VERSION|\\

Microsoft Store installation:

.. parsed-literal:: %ProgramFiles%\\WindowsApps\\BlenderFoundation.Blender<HASH>\\Blender\\\ |BLENDER_VERSION|\\


Environment Variables
---------------------

``BLENDER_SYSTEM_SCRIPTS`` and ``BLENDER_SYSTEM_EXTENSIONS``
:ref:`environment variables <command-line-args-environment-variables>`
can be used to :ref:`bundle additional scripts and extensions <deploying-blender-bundling>`,
that are not part of the regular Blender installation.

Other ``BLENDER_SYSTEM`` environment variables can override other system paths,
though are not commonly used in practice.

.. _blender-directory-path-layout:

Path Layout
===========

``./autosave``
  Autosave blend-file location. (Windows only, temp directory used for other systems.)

  Located in user directories.

``./config``
  User configuration and session info.

  Located in user directories.

  ``./config/startup.blend``
    Blend file to load on startup.

  ``./config/userpref.blend``
    User preferences.

  ``./config/bookmarks.txt``
    File Browser bookmarks.

  ``./config/recent-files.txt``
    Recent file menu list.

  ``./config/{APP_TEMPLATE_ID}/startup.blend``
    Startup file for an application template.

  ``./config/{APP_TEMPLATE_ID}/userpref.blend``
    User preferences file for an application template.

``./datafiles``
  Data files loaded at runtime.

  Located in both user and system directories. User data files either override
  or add to system data files.

  ``./datafiles/colormanagement``
    Default OpenColorIO configuration.

  ``./datafiles/fonts``
    User interface fonts.

  ``./datafiles/studiolights``
    Studio light images for 3D viewport.

``./extensions``
  Extension repositories.

  Located in both user and system directories. Repositories are loaded from
  both directories.

``./scripts``
  Add-ons, presets, templates, user interface, startup scripts.

  Located in both user and system directories. Scripts are loaded from
  both directories.

  ``./scripts/addons/*.py``
    Python add-ons which may be enabled in the Preferences include import/export format support,
    render engine integration and many handy utilities.

  ``./scripts/addons/modules/*.py``
    Modules for add-ons to use
    (added to Python's ``sys.path``).

  ``./scripts/addons_core/*.py``
    The add-ons directory which is used for bundled add-ons.

  ``./scripts/addons_core/modules/*.py``
    Modules for ``addons_core`` to use (added to Python's ``sys.path`` when it found).

  ``./scripts/modules/*.py``
    Python modules containing our core API and utility functions for other scripts to import
    (added to Python's ``sys.path``).

  ``./scripts/startup/*.py``
    Scripts which are automatically imported on startup.

    ``./scripts/startup/bl_app_templates_user/{APP_TEMPLATE_ID}``
      Application templates installed in user directories.

    ``./scripts/startup/bl_app_templates_system/{APP_TEMPLATE_ID}``
      Application templates automatically loaded from system directories.

  ``./scripts/presets/{preset}/*.py``
    Presets used for storing user-defined settings for cloth, render formats, etc.

  ``./scripts/templates_py/*.py``
    Example scripts which can be accessed from :menuselection:`Text Editor --> Templates --> Python`.

  ``./scripts/templates_osl/*.osl``
    Example OSL shaders which can be accessed from
    :menuselection:`Text Editor --> Templates --> Open Shading Language`.

``./python``
  Bundled Python distribution.

  Located in system directories.


.. _local-cache-dir:

Local Cache Directory
=====================

The cache directory is used to store persistent caches locally. Currently it is only used for the indexing of
:ref:`Asset Libraries <what-is-asset-library>`. The operating system is not expected to clear this automatically.

The following path will be used:

- :Linux: ``$XDG_CACHE_HOME/blender/`` if ``$XDG_CACHE_HOME`` is set, otherwise ``$HOME/.cache/blender/``
- :macOS: ``/Library/Caches/Blender/``
- :Windows: ``%USERPROFILE%\AppData\Local\Blender Foundation\Blender\Cache\``


.. _temp-dir:

Temporary Directory
===================

The temporary directory is used to store various files at run-time
(including render layers, physics cache, copy-paste buffer and crash logs).

The temporary directory is selected based on the following priority:

- User Preference (see :ref:`prefs-file-paths`).
- Environment variables (``TEMP`` on Windows, ``TMP`` & ``TMP_DIR`` on other platforms).
- The ``/tmp/`` directory.
