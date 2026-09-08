
***********************
Configuring Peripherals
***********************

Displays
========

A full HD display (1920x1080) or higher is recommended. Multi-monitor setups are supported, and workspaces can be
configured to span multiple monitors.

.. figure:: /images/getting-started_configuration_hardware_multi-monitor.jpg

   Example of Blender's multi-monitor support.


Input Devices
=============

Blender supports various types of input devices:

- Keyboard (recommended: keyboard with numeric keypad, English layout works best)
- Mouse (recommended: three button mouse with scroll wheel)
- Graphic Tablet
- Touchpad
- NDOF Device (also known as *3D Mouse*)

.. note::

   If you don't have a middle mouse button or numeric keypad, you can emulate these in the
   :doc:`Input Preferences </editors/preferences/input>`. However, be aware that these emulations may cause the loss
   of some shortcut keys. Where possible, it is suggested to use the recommended hardware.


Mouse
-----

A number of Blender interactions utilize the middle button (clicking the scroll wheel), or the use of the scroll
wheel. This is why the recommendation for a mouse is a two-button mouse with an added scroll wheel that acts as a
middle button (effectively a 3-button mouse). This will allow for the most efficient workflow within all of Blender's
modules.

Mouse Button Emulation
^^^^^^^^^^^^^^^^^^^^^^

If you do not have a 3 button mouse, you will need to emulate it by checking the option in the
:doc:`Preferences </editors/preferences/input>`.

The following table shows the combinations used:

.. list-table::
   :stub-columns: 1

   * - 3-button Mouse
     - :kbd:`LMB`
     - :kbd:`MMB`
     - :kbd:`RMB`
   * - 2-button Mouse
     - :kbd:`LMB`
     - :kbd:`Alt-LMB`
     - :kbd:`RMB`


Keyboard
--------

A number of Blender interactions utilize the keyboard's number pad (or numpad).  This is the set of 10 numeric keys
plus mathematical functions that appears on the right side of a
`traditional 104-key full-sized keyboard <https://en.wikipedia.org/wiki/Keyboard_layout#/media/File:Qwerty.svg>`__.
This will allow for the most efficient workflow within all of Blender's modules.

Numpad Emulation
^^^^^^^^^^^^^^^^

If you do not have a number pad on the side of your keyboard, you may want to emulate one. You can then use the number
row at the top of the keyboard instead, but will no longer have access to these keys' original functions (such as
switching between vertex/edge/face selection in Edit Mode).

.. seealso::

   Read more about *Numpad Emulation* in the :doc:`Preferences </editors/preferences/input>`.


Non-English Keyboards
^^^^^^^^^^^^^^^^^^^^^

If you use a keyboard with a non-English layout, you may still benefit from switching to the UK or US layout while
working with Blender.

.. note::

   You can also change the keymap from the :doc:`Preferences </editors/preferences/input>`. However, this manual
   assumes you are using the default keymap.


.. _hardware-touch:

Touch Screens
-------------

Blender has several settings that can be enabled to improve the experience on touch-enabled devices.
These options make it easier to manage areas, menus, and interactions without relying on precise
mouse input.

- Enable :ref:`Show Handles <bpy.types.PreferencesView.show_area_handle>`
  to simplify resizing and rearranging :doc:`/interface/window_system/areas`.
- Increase the :ref:`Border Width <bpy.types.PreferencesView.border_width>`
  to make area edges easier to select with a finger.


.. _hardware-tablet:

Graphic Tablet
--------------

Graphics tablets can be used to provide a more traditional method of controlling the mouse cursor using a pen. This
can help provide a more familiar experience for artists who are used to painting and drawing with similar tools, as
well as provide additional controls such as pressure sensitivity.

.. note::

   If you are using a graphic tablet instead of a mouse and pressure sensitivity does not work properly, try to place
   the mouse pointer in the Blender window and then disconnect/reconnect your graphic tablet. This might help.


.. _hardware-ndof:

Touchpad
--------

Touchpad controls are available on Windows, macOS and Linux with Wayland. If you are working from a laptop without a
mouse, you can emulate controls using multi-touch gestures with the trackpad from
:doc:`Preferences </editors/preferences/input>`.

.. list-table:: Supported multi-touch gestures
   :header-rows: 1

   * - Gesture
     - Effect
   * - Pan
     - Hold the :kbd:`Shift` key while dragging two fingers on the pad.
   * - Zoom
     - Hold the :kbd:`Ctrl` or :kbd:`OSKey` key while dragging two fingers on the pad.
   * - Orbit
     - Drag two fingers on the pad.
   * - Emulate right-click
     - Tap two fingers on the pad.

NDOF (3D Mouse)
---------------

3D mice or :abbr:`NDOF (N-Degrees of Freedom)` devices are hardware that you can use to navigate a scene in Blender.
Currently only devices made by 3Dconnexion, such as the SpaceMouse™, are supported. These devices allow you to explore
a scene, and make :ref:`Fly/Walk Navigation <3dview-fly-walk>` easier to control. The NDOF device can be configured in
the :ref:`Preferences <editors_preferences_input_ndof>`. These settings can also be accessed directly from the
viewport using the :kbd:`NDOFMenu` button on the NDOF device.

.. seealso::

   See :doc:`Input Preference </editors/preferences/input>` for more information on configuring peripherals.


.. _hardware-head-mounted-displays:

Head-Mounted Displays (Virtual Reality)
=======================================

:abbr:`HMDs (Head-Mounted Displays)` make it possible to place users in an interactive, virtual environment. Attached
to the head, they track head movements to project a seemingly surrounding world onto small screens in front of the
user's eyes. If the system works well, they experience the virtual environment as if they were really inside of it.


Supported Platforms
-------------------

Virtual reality support in Blender is implemented through the multi-platform OpenXR standard. This standard is new and
therefore support for it is still limited.

.. list-table:: OpenXR compatible platforms.
   :header-rows: 1

   * - Platform
     - Operating System
     - Notes
   * - `HTC Vive Cosmos`_
     - Windows
     - `Developer Preview <https://forum.htc.com/topic/9046-vive-openxr-support-for-vive-cosmos/>`__
   * - `HTC Vive Focus 3`_
     - Windows
     - `Developer Preview <https://forum.htc.com/topic/9876-focus-3-openxr-support-status/page/3/>`__
   * - `Monado`_
     - GNU/Linux
     - *Not* recommended for general use yet.
   * - `Meta (formerly Oculus)`_ (Rift and Quest)
     - Windows
     - Requires Oculus v31 Software Update. Oculus Link required for Quest.
   * - `SteamVR`_
     - Windows, GNU/Linux
     - Requires SteamVR 1.16 or greater.
   * - `Varjo`_
     - Windows
     - --
   * - `Windows Mixed Reality`_
     - Windows
     - Requires Windows 10 May 2019 Update (1903).


Getting Started
---------------

The following subsections describe how an HMD can be set up for usage with the `supported platforms`_. If this is not
done, Blender will report an error when trying to start a virtual reality session.


HTC Vive Cosmos
^^^^^^^^^^^^^^^

The dedicated platform for the `HTC Vive Cosmos <https://www.vive.com/eu/product/#cosmos%20series>`__ is currently
targeted at developers and may lack features found in other platforms.

- Follow the steps from the
  `Vive Developer Forums <https://forum.htc.com/topic/9046-vive-openxr-support-for-vive-cosmos/>`__.
- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.


HTC Vive Focus 3
^^^^^^^^^^^^^^^^

The dedicated platform for the `HTC Vive Focus 3 <https://www.vive.com/eu/product/vive-focus3/overview/>`__ is
currently targeted at developers and may lack features found in other platforms.

- Follow the steps from the
  `Vive Developer Forums <https://forum.htc.com/topic/9876-focus-3-openxr-support-status/page/3/>`__.
- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.


Monado
^^^^^^

`Monado <https://monado.dev/>`__ is a :doc:`free and open source </getting_started/about/license>` XR platform for
Linux. It is not yet ready for production usage and should only be used for testing purposes.

- Packages are available for the following distributions:

  - Ubuntu (`Eoan, Focal <https://launchpad.net/~monado-xr/+archive/ubuntu/monado>`__)
  - Debian (`bullseye <https://packages.debian.org/bullseye/libopenxr1-monado>`__,
    `sid <https://packages.debian.org/sid/libopenxr1-monado>`__)

  For other systems, it has to be compiled from source, which in this case is not recommended for people with little
  experience in compiling software. Follow the
  `Getting Started Guides <https://gitlab.freedesktop.org/monado/monado/-/blob/main/README.md>`__ from Monado to do so
  nevertheless.
- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.


Meta (formerly Oculus)
^^^^^^^^^^^^^^^^^^^^^^

`Meta (formerly Oculus) <https://www.meta.com/quest/>`__ provides full support for OpenXR as of the Oculus v31
Software Update.

- Download and install the `Oculus Rift/Oculus Link software <https://www.meta.com/quest/setup/>`__.
- Set Oculus as the active OpenXR runtime via the *General* tab in the Oculus App Settings.

.. figure:: /images/getting-started_configuration_hardware_xr_runtime_oculus.jpg
   :scale: 50 %

- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.

.. admonition:: Passthrough Support
   :class: note

   Currently, passthrough support over OpenXR is disabled by default in the Quest Link app, and must be manually
   enabled in it's settings to use this feature.

   The performance of the passthrough render varies with the quality of the connection between the headset and the
   computer. For better results, connecting the headset directly through USB to the PC, or at least connecting the
   computer to the local network over Ethernet, is recommended.


SteamVR
^^^^^^^

`SteamVR <https://www.steamvr.com/>`__ provides full support for OpenXR as of SteamVR 1.16.

- Set SteamVR as the active OpenXR runtime via the *Developer* tab in the SteamVR Settings.

.. figure:: /images/getting-started_configuration_hardware_xr_runtime_steamvr.jpg
   :scale: 50 %

- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.

.. note::

   The SteamVR runtime can also be used for HTC Vive Cosmos, Oculus, and Windows Mixed Reality HMDs.


Varjo
^^^^^

`Varjo <https://varjo.com/>`__ includes full OpenXR support with its required Varjo Base software.

- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.


Windows Mixed Reality
^^^^^^^^^^^^^^^^^^^^^

`Windows Mixed Reality <https://www.microsoft.com/windows/windows-mixed-reality>`__ provides full support for OpenXR.
To check if a PC meets the requirements to run the software, Microsoft offers the
`Windows Mixed Reality PC Check <https://www.microsoft.com/en-us/p/windows-mixed-reality-pc-check/9nzvl19n7cnc>`__
application.

- Make sure the Windows 10 May 2019 Update (1903) is installed.
- If the system meets all requirements, the Mixed Reality Portal should already be installed. It is also available in
  the `Microsoft Store <https://www.microsoft.com/en-us/p/mixed-reality-portal/9ng1h8b3zc7m>`__.
- Launch the Mixed Reality Portal. Click the menu button ``...`` in the lower left corner. In the menu it opens,
  select the *Set up OpenXR*.
- Enable the :doc:`VR Scene Inspection add-on </addons/3d_view/vr_scene_inspection>` in Blender.

.. note::

   To switch to Windows Mixed Reality from another OpenXR runtime (e.g. SteamVR), download the OpenXR Developer Tools
   from the `Microsoft Store
   <https://www.microsoft.com/en-us/p/openxr-developer-tools-for-windows-mixed-reality/9n5cvvl23qbt>`__ and set
   Windows Mixed Reality as the active runtime.

.. figure:: /images/getting-started_configuration_hardware_xr_runtime_wmr.jpg
   :scale: 50 %
