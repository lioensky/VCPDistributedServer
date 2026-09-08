
**********
Status Bar
**********

The Status Bar is located at the bottom of the Blender window and displays contextual information such as
keyboard shortcuts, messages, and statistical information.
The Status Bar can be hidden by disabling *Show Status Bar* in Window menu or by dragging from the top edge down.

.. figure:: /images/interface_window-system_status-bar_ui.png

   Status Bar.


Keymap Information
==================

The left side of the Status Bar displays mouse button shortcuts and the keymap of the active tool.
In editors with a Toolbar, tapping :kbd:`Alt` (or ``Option`` on macOS)
shows the hotkeys to change to a desired tool.

.. tip::

   This functionality can be disabled with the *Alt Click Tool Prompt*
   preference in the :doc:`Keymap Preferences </editors/preferences/keymap>`).

.. figure:: /images/interface_window-system_status-bar_ui-left.png
   :align: center


Status Messages
===============

The middle of the Status Bar displays information about in-progress operations.

.. figure:: /images/interface_window-system_status-bar_ui-center.png
   :align: center

Running Task
   Shows the progress of the currently running task (such as rendering or baking).
   Hovering the mouse pointer over the progress bar will display a time estimate.
   The task can be aborted by clicking the cancel button (:bl-icon:`cancel`).
Report Message
   Informational messages or warnings, such as after saving a file.
   They disappear after a short time.
   Click them to show the full message in the :doc:`Info Editor </editors/info_editor>`.


Resource Information
====================

The right side of the Status Bar displays information about the Blender instance.
Which information is shown can be chosen by :kbd:`RMB` on the Status Bar
or in the :ref:`Preferences <prefs-interface-status_bar>`.

.. figure:: /images/interface_window-system_status-bar_ui-right.png
   :align: center

Scene Statistics
   Shows information about the data in the active scene.

   - **Collection**: The name of the active :doc:`Collection </scene_layout/collections/index>`.
   - **Active Object**: The name of the active selected object.
   - **Geometry**: Information about the current scene depending on the mode and object type.
     This can be the number of vertices, faces, triangles, or bones.
   - **Objects**: The number of selected objects and the total count of objects.

Scene Duration
   Shows the total amount of time of the playback along with the current frame number and total frame count.
   The format of the duration text is determined by the
   :ref:`Timecode Style <bpy.types.PreferencesView.timecode_style>`.

System Memory
   Shows an estimate of Blender's RAM consumption. On a single-instance single-machine scenario,
   this estimate provides a measurement against the hardware limit of the machine.

Extensions Updates
   Shows the number of :doc:`extensions </advanced/extensions/index>` with available updates.

Blender Version
   Shows the version number of Blender that is currently running.
