
**************
Default Keymap
**************

While this isn't a comprehensive list,
this page shows common keys used in Blender's default keymap.

.. Even though this is not intended to be comprehensive,
   it could be expanded.


Selecting
=========

Blender has two main selection modes: left-click select and right-click select.
See the :ref:`Select with Mouse Button <keymap-blender_default-prefs-select_with>` preference.

While left-click select is the default as it's the most common in other applications,
right-click select does have its advantages.
See: `Learn the benefits of right-click select <https://vimeo.com/76335056>`__.


Hovering
========

The following shortcuts can be pressed while hovering the mouse cursor
over an editable field.


.. _keymap-common-properties:

Properties
----------

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl-C`
     - Copy the (single) value of the field.
   * - :kbd:`Ctrl-V`
     - Paste the (single) value of the field.
   * - :kbd:`Ctrl-Alt-C`
     - Copy the entire vector or color of the field.
   * - :kbd:`Ctrl-Alt-V`
     - Paste the entire vector or color of the field.
   * - :kbd:`RMB`
     - Open the context menu.
   * - :kbd:`Backspace`
     - Reset the value to its default.
   * - :kbd:`Minus`
     - Invert the value's sign (multiply by -1.0).
   * - :kbd:`Ctrl-Wheel`
     - Change the value in incremental steps.

       For fields with a pop-up list of values, this cycles the value.
   * - :kbd:`Return`
     - Activates menus and toggles checkboxes.
   * - :kbd:`Alt`
     - Hold while editing values to apply the change to all selected items
       (objects, bones, sequence-strips).

       This can be used for number fields and toggles.


Dragging
========

The following shortcuts can be used while moving/rotating/scaling an object in the 3D Viewport,
dragging the slider of a value, and so on. Note that they should be pressed after starting
the drag, not before.

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl`
     - Snap to coarse increments, making it easier to (say) rotate an object by exactly 90°.
   * - :kbd:`Shift`
     - Make the value change more slowly in response to mouse movement, giving you more precision.
   * - :kbd:`Shift-Ctrl`
     - Snap to fine increments.


General
=======

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl-O`
     - Open file.
   * - :kbd:`Ctrl-S`
     - Save file.
   * - :kbd:`Ctrl-N`
     - New file.
   * - :kbd:`Ctrl-Z`
     - Undo.
   * - :kbd:`Shift-Ctrl-Z`
     - Redo.
   * - :kbd:`Ctrl-Q`
     - Quit.
   * - :kbd:`F1`
     - Help *(context sensitive)*.
   * - :kbd:`F2`
     - Rename active item.
   * - :kbd:`F3`
     - :ref:`Menu Search <bpy.ops.wm.search_menu>`.
   * - :kbd:`F4`
     - File context menu.
   * - :kbd:`F5` - :kbd:`F8`
     - *Reserved for user actions.*
   * - :kbd:`F9`
     - :ref:`Adjust Last Operation <bpy.ops.screen.redo_last>`.
   * - :kbd:`F10`
     - *Reserved for user actions.*
   * - :kbd:`F11`
     - Show render window.
   * - :kbd:`F12`
     - Render the current frame.
   * - :kbd:`Q`
     - Quick access (favorites).
   * - :kbd:`Ctrl-Spacebar`
     - Toggle Maximize :doc:`Area </interface/window_system/areas>`.
   * - :kbd:`Ctrl-PageUp` / :kbd:`Ctrl-PageDown`
     - Next/previous :doc:`Workspace </interface/window_system/workspaces>`.
   * - :kbd:`Spacebar`
     - User configurable; see :ref:`keymap-blender_default-spacebar_action`.
   * - :kbd:`Shift-Ctrl-Spacebar`
     - Playback animation (reverse).


Common Editing Keys
===================

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`X`
     - Delete the selected item with a confirmation dialog.
   * - :kbd:`Delete`
     - Delete the selected item without a confirmation dialog.


Common Editor Keys
==================

These keys are shared across editors such as the 3D Viewport, UV and Graph editor.

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`A`
     - Select all.
   * - :kbd:`Alt-A` /

       Double-tap :kbd:`A`
     - Select none.
   * - :kbd:`Ctrl-I`
     - Invert selection.
   * - :kbd:`H`
     - Hide selected items.
   * - :kbd:`Shift-H`
     - Hide unselected items.
   * - :kbd:`Alt-H`
     - Reveal hidden items.
   * - :kbd:`T`
     - Toggle Toolbar.
   * - :kbd:`N`
     - Toggle Sidebar.


3D Viewport Keys
================

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`MMB`
     - Orbit View
   * - :kbd:`Shift-MMB`
     - Pan View
   * - :kbd:`Ctrl-MMB`
     - Zoom View
   * - :kbd:`Tab`
     - Toggle Edit mode.
   * - :kbd:`Ctrl-Tab`
     - Toggle Pose mode for armatures, or show a :doc:`mode </editors/3dview/modes>` switching pie menu for others.
   * - :kbd:`1` - :kbd:`3`
     - In Edit Mode, switch between editing vertices (:kbd:`1`), edges (:kbd:`2`), or faces (:kbd:`3`).

       Hold :kbd:`Shift` to toggle one of these without disabling the others.

       Hold :kbd:`Ctrl` to alter how the selection is transformed from the old mode to the new.

       See :doc:`Mesh Selection Modes </modeling/meshes/selecting/introduction>` for details.
   * - :kbd:`AccentGrave`
     - Show 3D Viewport navigation pie menu.
   * - :kbd:`Ctrl-AccentGrave`
     - Toggle gizmos.
   * - :kbd:`Shift-AccentGrave`
     - Start :ref:`Fly/Walk Navigation <3dview-fly-walk>`.

.. seealso:: :doc:`3D Viewport Navigation </editors/3dview/navigate/navigation>`


Animation
=========

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`I`
     - Insert a :doc:`keyframe </animation/keyframes/introduction>`.
   * - :kbd:`Alt-I`
     - Clear the keyframe.
   * - :kbd:`Shift-Alt-I`
     - Clear all keyframes.
   * - :kbd:`Ctrl-D`
     - Assign a :doc:`driver </animation/drivers/introduction>`.
   * - :kbd:`Ctrl-Alt-D`
     - Clear the driver.
   * - :kbd:`K`
     - Add the property to the current
       :doc:`keying set </animation/keyframes/keying_sets>`.
   * - :kbd:`Alt-K`
     - Remove the property from the current keying set.


Python Scripting
================

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl-C`
     - When pressed while hovering over an :ref:`operator button <ui-operator-buttons>`,
       copies its Python command to the clipboard. This command can then be used in the
       :doc:`Python Console </editors/python_console>` or in the :doc:`Text Editor </editors/text_editor>`
       when writing scripts.
   * - :kbd:`Shift-Ctrl-C`
     - When pressed while hovering over a field, copies its relative data path (also available from
       the context menu). Useful when writing drivers or scripts.
   * - :kbd:`Shift-Ctrl-Alt-C`
     - When pressed while hovering over a field, copies its full data path.


Platform Specific Keys
======================

macOS
-----

The :kbd:`Cmd` key can be used instead of :kbd:`Ctrl` on macOS
for all but a few exceptions which conflict with the operating system.

List of additional macOS specific keys:

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Cmd-Comma`
     - Preferences.
