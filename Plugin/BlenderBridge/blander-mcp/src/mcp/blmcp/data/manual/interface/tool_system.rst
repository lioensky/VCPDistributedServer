.. _ui-tool_system:
.. _bpy.ops.wm.tool:

***********
Tool System
***********

Tools are accessed from the :ref:`Toolbar <ui-region-toolbar>`.

This is a general introduction to tools. Individual tools have their own documentation.

There can only be one active tool per :doc:`Workspace </interface/window_system/workspaces>`
and :doc:`mode </editors/3dview/modes>`.
This tool is remembered: if you're in Edit Mode and have the Extrude tool selected,
then switch to Object Mode (which has no Extrude tool) and back to Edit Mode,
the Extrude tool will still be active.

Most tools are controlled using just :kbd:`LMB`, though some also have modifier keys
(shown in the :doc:`Status Bar </interface/window_system/status_bar>` while using the tool).
This can all be customized in the :doc:`Keymap Preferences </editors/preferences/keymap>`.

Some tools define gizmos (*Shear* and *Spin* for example) to help control them.


.. _ui-region-toolbar:

Toolbar
=======

.. reference::

   :Shortcut:  :kbd:`T`

.. figure:: /images/interface_tool-system_buttons-popup.png
   :align: right

   Expanded tool group.

The Toolbar contains buttons for the various tools.
Buttons with a small triangle in their bottom right corner are tool groups
which can be opened by holding :kbd:`LMB` on them for a moment
(or dragging :kbd:`LMB` to open them instantly).

Hovering your cursor over a tool for a short time will show its name,
while hovering longer will show the full tooltip.

Resizing the Toolbar horizontally will display the icons with two columns.
Expanding it further will display the icon and its text.


.. _bpy.ops.wm.toolbar:

Pop-Up Toolbar
==============

.. reference::

   :Shortcut:  :kbd:`Shift-Spacebar`

Pressing :kbd:`Shift-Spacebar` will pop up a small toolbar right at
your cursor for faster access.
The shortcuts for selecting the tools are displayed on the right.

Alternatively, you can map this action to :kbd:`Spacebar` in the Keymap Preferences.
Then you'll be able use :kbd:`Spacebar` like a modifier key
(similar to holding :kbd:`Ctrl` or :kbd:`Shift`).
For example, you can press :kbd:`Spacebar T` for Transform,
:kbd:`Spacebar D` for Annotate, :kbd:`Spacebar M` for Measure and so on.
See :ref:`Spacebar Action <keymap-blender_default-spacebar_action>`.


Quick Favorites
===============

.. reference::

   :Shortcut:  :kbd:`Q`

The Quick Favorites menu gathers your favorite tools.
Any tool or menu item can be added to this pop-up menu via its context menu.


Changing Tools
==============

If you have *Alt Click Tool Prompt* enabled in the Keymap Preferences,
tapping :kbd:`Alt` will display a tool prompt in the Status Bar.
You can then press a key to select the corresponding tool, or tap :kbd:`Alt` again to cancel the prompt.


.. _bpy.ops.wm.toolbar_fallback_pie:

Fallback Tool
-------------

The fallback tool is the one that's selected by default (so the one at the top of the Toolbar).
You can change it by either holding :kbd:`LMB` on the toolbar button or pressing :kbd:`Alt-W`
to get a pie menu.


Cycling Tools
-------------

If you bind a key to a tool which is part of a group, you can enable the *Cycle* option in the keymap editor.
Successive presses will then cycle through the tools in that group.

This is enabled by default for the selection tools in the 3D Viewport, for example:
pressing :kbd:`W` will cycle between Select Box, Select Circle and so on.


Properties
==========

Tools can have their own settings, which are available from multiple places:

- The :menuselection:`Tool --> Active Tool` panel in the Sidebar :kbd:`N`.
- The *Active Tool* tab in the :doc:`Properties editor </editors/properties_editor>`.
- The *Tool Settings* region below the area header.
