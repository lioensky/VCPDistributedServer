
*******************
Installing on Linux
*******************

Check the :doc:`Downloading Blender </getting_started/installing/index>` page to find the minimum requirements and the
different versions that are available for Blender (if you have not done so yet).


Install from blender.org
========================

Download the Linux version for your architecture and decompress the file to the desired location (e.g. ``~/software``
or ``/usr/local``).

Blender can now be launched by double-clicking the executable.

When using this method of installation, it is possible to have multiple versions of Blender installed.

For ease of access, you may wish to add a menu entry and create blend-file associations for the file-browser. This can
be done by :ref:`Registering Blender <bpy.ops.preferences.associate_blend>`.

To make the installation and configuration fully self-contained, set up a :ref:`Portable Installation
<portable-installation>`.


Install from a Package Manager
==============================

Some Linux distributions may have a specific package for Blender in their repositories.

Installing Blender via the distribution's native mechanisms ensures consistency with other packages on the system and
may provide other features (given by the package manager), such as listing of packages, update notifications and
automatic menu configuration. Be aware, though, that the package may be outdated compared to the latest official
release, or not include some features of Blender. For example, some distributions do not build Blender with Cycles GPU
rendering support, for licensing or other reasons.

If there is a specific package for your distribution, you may choose what is preferable and most convenient.
Otherwise, the official binary is available on `blender.org <https://www.blender.org/download/>`__.


Install from Snap
=================

`Snap <https://snapcraft.io/>`__ is a universal package manager designed to work across a range of distributions.
Assuming snap is already installed, Blender can be installed through snap with::

   snap install blender --classic

Installing from this method has a benefit that updates to Blender are automatically installed.
Blender from Snap should have a more consistent distribution than individual package managers.


Running from the Terminal
=========================

See :doc:`Launching from the terminal </advanced/command_line/launch/linux>`.


Graphics System (X11 & Wayland)
===============================

Blender supports both X11 and Wayland. See :ref:`linux-windowing-environment` for details.


Avoiding Alt-Mouse Conflict
===========================

Some window managers default to :kbd:`Alt-LMB` and :kbd:`Alt-RMB` for moving and resizing windows.

Blender uses these for various operations, notably:

- :ref:`Emulate 3 Button Mouse <bpy.types.PreferencesInput.use_mouse_emulate_3_button>`.
- :ref:`bpy.ops.mesh.loop_multi_select`.
- :ref:`Changing multiple properties at once <keymap-common-properties>`.

To access Blender's full feature set, you can change the window manager settings to use the *Meta* key instead (also
called *Super* or *Windows* key):

Gnome
   Enter the following in a command line (effective at next login):

   .. code-block:: sh

      gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier '<Super>'

KDE
   :menuselection:`System Settings --> Window Management --> Window Behavior --> Window Actions`,
   Switch from 'Alt' to 'Meta' key.


Updating on Linux
=================

On Linux there are two ways to update Blender. This section covers the most common approaches.


Updating from blender.org
-------------------------

When an update for Blender is released, it can be downloaded directly from the
`Blender website <https://www.blender.org/download/>`__ and installed using the steps described in the section
`Install from blender.org`_.


Updating with a Package Manager
-------------------------------

Many Linux distributions have packages for Blender available, which can be installed using the distribution's package
manager. After installation, Blender can be updated using the same steps as updating any other application.

.. seealso::

   The Splash screen :doc:`/getting_started/configuration/defaults` page for information about importing settings from
   previous Blender versions and other quick settings.


Known Limitations
=================

Archive Extraction
------------------

Extracting Blender's archive using **7-zip** is not supported. TAR must be used instead. For more details, see issue
`#104070 <https://projects.blender.org/blender/blender/issues/104070#issuecomment-1276521>`__.
