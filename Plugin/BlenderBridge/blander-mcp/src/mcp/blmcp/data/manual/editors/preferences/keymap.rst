.. _prefs-input-keymap-editor:

******
Keymap
******

On this screen, you can configure keyboard and mouse shortcuts.

.. figure:: /images/editors_preferences_section_keymap.webp

   Blender Preferences Keymap section.

.. seealso::

   :doc:`/interface/keymap/index`


Presets
=======

At the top of the window, you can select and manage presets.

Keymap Presets
   The selector lets you choose from builtin presets:

   - :doc:`Blender </interface/keymap/blender_default>`: the default keymap,
     which is the one used throughout this manual.
   - Blender 27x: legacy keymap as used in Blender 2.79 and before.
   - :doc:`Industry Compatible </interface/keymap/industry_compatible>`: a keymap
     which more closely matches other 3D editing applications.

.. _bpy.ops.wm.keyconfig_preset_add:

:bl-icon:`add` Add Custom Keymap Configuration
   Add a custom keymap configuration.

.. _bpy.ops.wm.keyconfig_preset_remove:

:bl-icon:`remove` Remove Keymap Configuration
   Remove a custom keymap configuration.

.. _bpy.ops.preferences.keyconfig_import:

Import
   Opens a File Browser to select a ``.py`` file containing a custom preset.

.. _bpy.ops.preferences.keyconfig_export:

Export
   Saves the current keymap configuration as a preset others may use.

   All Keymaps
      When disabled, only the shortcut assignments that have been modified will be exported.
      This exported file may be thought of as a "keymap delta" instead of a full export.

      When enabled, the entire keymap is written.


Filtering
=========

Below the preset list, you can filter the list of operations so you can quickly find the one you need.

.. _bpy.types.SpacePreferences.filter_type:

Filter Type
   :Name:
      Filter the operations by their name (such as ``New File``).
   :Key Binding:
      Filter the operations by their currently assigned shortcut (such as ``ctrl n``).

.. _bpy.types.SpacePreferences.filter_text:

Search
   The text to search (leave blank to show all operations).


Preferences
===========

These preferences only apply to the *Blender* keymap.

.. _keymap-blender_default-prefs-select_with:

Select with Mouse Button
   Controls which mouse button is used to select items.

   :Left:
      :kbd:`LMB` selects items while :kbd:`RMB` opens the context menu.
   :Right:
      :kbd:`RMB` selects items while :kbd:`LMB` places the :doc:`/editors/3dview/3d_cursor`.

.. _keymap-blender_default-spacebar_action:

Spacebar Action
   Controls the action of :kbd:`Spacebar`.

   :Play:
      Starts/stops :doc:`animation playback </animation/index>`.
      This option is good for animation or video editing work.
   :Tools:
      Opens the Toolbar underneath the cursor to quickly change the active tool.
      This option is good if you are doing a lot of modeling or rigging work.

      You can select tools in multiple ways:

      - Press :kbd:`Spacebar`, then click a tool with the mouse.
      - Hold :kbd:`Spacebar`, move the mouse to a tool, and release :kbd:`Spacebar`.
      - Press :kbd:`Spacebar`, then press the key that's shown in the popover (e.g. :kbd:`T` for
        the Transform tool).
      - Press :kbd:`Spacebar` and the tool's key together, e.g. :kbd:`Spacebar-T` to select the
        Transform tool in one go.
   :Search:
      Opens up the :ref:`Menu Search <bpy.ops.wm.search_menu>`.
      This option is good for someone who is new to Blender and is unfamiliar with the menus and shortcuts.
      Even if you don't select this option, however, you can still access the search with :kbd:`F3`.

   If you select something other than *Play*, you can instead use :kbd:`Shift-Spacebar`
   to start/stop playback.

Activate Gizmo Event
   The activation event for :doc:`gizmos </editors/3dview/display/gizmo>` that support drag motion.
   This option is only available when *Select with Mouse Button* is set to *Left*.

   :Press:
      The gizmo's operation gets initiated (and additional options become available in the Status Bar)
      the moment you press down the mouse button on the gizmo.
   :Drag:
      The operation only gets initiated once you start dragging the gizmo.

Tool Keys
   Determines the behavior of tool activation keyboard shortcuts.

   :Immediate: The tool is immediately in use. For example, if you press :kbd:`Ctrl-B` while editing a mesh,
               this will immediately initiate a Bevel: you can move the mouse to change the size and then
               click :kbd:`LMB` to confirm.
   :Active Tool: The tool is only selected (same behavior as if you were to click on it in the Toolbar).
                 For example, if you press :kbd:`Ctrl-B` while editing a mesh, the Bevel tool will be selected
                 and the gizmo will become visible in the viewport; to actually perform a bevel, you then
                 need to drag this gizmo.

Alt Click Tool Prompt
   Tapping :kbd:`Alt` shows a prompt in the status bar prompting a second keystroke to activate the tool.
   Note that this option is not available when using
   :ref:`Emulate 3 Button Mouse <bpy.types.PreferencesInput.use_mouse_emulate_3_button>`.

Alt Tool Access
   Hold :kbd:`Alt` to use the :doc:`Active Tool </interface/tool_system>` when the gizmo would normally be required.
   (For example, with the Move tool selected, you can hold :kbd:`Alt` and drag the mouse anywhere in the viewport
   to move the selected object, rather than having to drag its gizmo.)
   This option is only available when *Select with Mouse Button* is set to *Left*
   and :ref:`Emulate 3 Button Mouse <bpy.types.PreferencesInput.use_mouse_emulate_3_button>` is disabled.

Select All Toggles
   Causes the *Select All* shortcut :kbd:`A` to deselect all when any selection exists.

Region Toggle Pie
   :kbd:`N` opens a :ref:`pie menu <bpy.types.UIPieMenu>` to toggle :doc:`/interface/window_system/regions`
   rather than always toggling the Sidebar region.


3D Viewport
-----------

Grave Accent / Tilde Action
   :Navigate:
      :ref:`Viewpoint <bpy.ops.view3d.view_axis>` pie menu, useful on systems without a numeric keypad.
   :Gizmos:
      Transform gizmos pie menu, useful for quickly switching between transform gizmos.
      Note that this doesn't apply to tools that force a certain gizmo (Move, Rotate, Scale
      and Transform); if you have such a tool selected, the gizmo will stay the same
      no matter what you choose in the pie menu.

Middle Mouse Action
   The action when :kbd:`MMB` dragging in the viewport. This also applies to trackpads.

   :Orbit:
      :ref:`Orbits <bpy.ops.view3d.view_orbit>` the view around a central point.
      :kbd:`Shift-MMB` is used for panning.
   :Pan:
      :ref:`Pans <bpy.ops.view3d.view_pan>` the view. :kbd:`Shift-MMB` is used for orbiting.

Alt Middle Mouse Drag Action
   How to determine the new :ref:`viewpoint <bpy.ops.view3d.view_axis>` when dragging :kbd:`Alt-MMB` in the viewport.

   :Relative:
      The new viewpoint depends on both the mouse movement direction and the current viewpoint. For example, dragging
      the mouse horizontally rotates the viewpoint 90° around the view's current vertical axis.
   :Absolute:
      The new viewpoint only depends on the mouse movement direction. For example, dragging the mouse to the right
      always puts the viewpoint on the positive side of the global X axis.

.. _keymap-pref-py_menu_on_drag:

Tab for Pie Menu
   By default, :kbd:`Tab` toggles Edit Mode and :kbd:`Ctrl-Tab` opens a pie menu for selecting from all
   :doc:`modes </editors/3dview/modes>`. This option flips these two shortcuts around.

Pie Menu on Drag
   When enabled, certain keys get different behavior when tapped and show a pie menu when holding them and dragging
   the mouse.

   :kbd:`Tab`
      :Tap: Toggle Edit Mode.
      :Drag: Show :doc:`Object Mode </editors/3dview/modes>` pie menu.
   :kbd:`Z`
      :Tap: Toggle wireframe view.
      :Drag: Show :doc:`/editors/3dview/display/shading` pie menu.
   :kbd:`AccentGrave`
      :Tap: Start first person :ref:`Fly/Walk Navigation <3dview-fly-walk>`.
      :Drag: Show viewpoint pie menu.

Extra Shading Pie Menu Items
   Show additional items in the shading menu (:kbd:`Z` key).

Transform Navigation with Alt
   Requires additionally holding :kbd:`Alt` to navigate the view while transforming something.
   In return, you don't need to hold :kbd:`Alt` to perform certain other operations.

   As an example: if this option is disabled, dragging :kbd:`MMB` always orbits the view, and when you're
   moving an object, you can drag with :kbd:`Alt-MMB` to lock the movement to an axis. If this option is enabled,
   these shortcuts get inverted while moving: :kbd:`MMB` does the axis lock, and you need to use :kbd:`Alt-MMB`
   to orbit, :kbd:`Shift-Alt-MMB` to pan, and :kbd:`Alt-Wheel` to zoom.

   This also applies to :doc:`/editors/3dview/controls/proportional_editing`
   (where :kbd:`Wheel` controls the size of the influence area) and :ref:`bpy.types.Pose.use_auto_ik`
   (where :kbd:`Wheel` controls the length of the temporary IK chain). If the option is disabled,
   :kbd:`Wheel` will zoom the view instead, and you need to use :kbd:`Alt-Wheel` to change these properties.

   .. seealso::
      :doc:`/modeling/transform/modal_map`


File Browser
------------

Open Folders on Single Click
   Navigate into folders by clicking on them once instead of twice.


.. _bpy.ops.preferences.keyitem:
.. _bpy.types.KeyMapItem:

Editor
======

The Keymap editor lets you change the default hotkeys for each of Blender's editors.

.. figure:: /images/editors_preferences_keymap_keymap-editor.png

   Keymap editor.


.. rubric:: Usage

#. Find the operation whose shortcut you want to change. Filtering can help with this.
#. Select whether the operation should be triggered by a keyboard key, a mouse button, or something else.
#. Click the button on the right and press the shortcut you want to assign.

.. _bpy.types.KeyMapItem.active:

Active
   Uncheck the checkbox to disable this keymap item.

.. _bpy.types.KeyMapItem.map_type:

Map Type
   :Keyboard: Single hotkey or key combination.
   :Mouse: Actions from mouse buttons, tablet or touchpad input.
   :NDOF: Movement or button from a 3D mouse (:term:`NDOF`) device.
   :Tweak: Mouse click and drag *(optionally map drag direction to different actions)*.
   :Text Input: Use this function by entering a text.
   :Timer: For Blender internal use.

.. _bpy.types.KeyMapItem.idname:

Operator ID Name
   The identifier for the operator to call.

   .. hint::

      See :mod:`blender_api:bpy.ops` for a list of operators (remove the ``bpy.`` prefix for the identifier).

Event
   .. _bpy.types.KeyMapItem.type:

   Type
      The key or button that activates this keymap item (depending on the map type).

   .. _bpy.types.KeyMapItem.value:

   Value
      The action (such as press, release, click, drag, etc.), (depending on the map type).

   .. _bpy.types.KeyMapItem.key_modifier:

   Modifier
      Additional keys to hold (such as :kbd:`Ctrl`, :kbd:`Shift`, :kbd:`Alt`).

Operator Properties
   Initial values for the operator-specific properties.

.. seealso::

   :ref:`keymap-customize` for more information on keymap editing.


Restoring
---------

If you want to restore the default settings for a keymap,
just click on the *Restore* button at the top right of this keymap.

.. tip::

   Instead of changing the default keymap, you can also add a new one.


Known Limitations
=================

Blender Versions
----------------

A problem with modifying your own keymap is that newer Blender versions may change the way tools are accessed,
breaking your customized keymap.

While the keymap can be manually updated, the more customizations you make, the higher the chance of conflicts
in newer Blender versions is.
