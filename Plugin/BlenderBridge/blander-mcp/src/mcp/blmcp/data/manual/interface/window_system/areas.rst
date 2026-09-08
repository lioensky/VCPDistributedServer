.. _bpy.types.Area:
.. _bpy.types.AreaSpaces:
.. _bpy.ops.screen.actionzone:

*****
Areas
*****

.. figure:: /images/interface_window-system_areas_borders.png
   :align: right
   :width: 250px
   :figwidth: 250px

   Area boundaries are indicated by rounded corners (yellow highlights).

The Blender window is divided into a number of rectangles called Areas.
Areas reserve screen space for :doc:`/editors/index`, such as the
:doc:`3D Viewport </editors/3dview/introduction>` or the
:doc:`Outliner </editors/outliner/introduction>`.
Each editor offers a specific piece of functionality.

Areas are grouped into :doc:`Workspaces </interface/window_system/workspaces>`,
which are geared towards particular tasks (modeling, animating and so on).

.. note::

   While some keyboard shortcuts in Blender are global (such as :kbd:`Ctrl-S` for saving),
   many depend on which editor the mouse cursor is hovering over.

   As an example, say you just selected two objects in the Outliner and want to join them.
   If you pressed the shortcut for this (:kbd:`Ctrl-J`)
   while the cursor is still in the Outliner, nothing would happen as the shortcut isn't valid there;
   you first need to move your cursor to the 3D Viewport.

.. tip::

   - The size of the border around areas can be adjusted in the
     user preferences with :ref:`Border Width <bpy.types.PreferencesView.border_width>`.
   - Handles can be enabled to always remain visible, which can help with area management on touch-enabled
     devices. See :ref:`bpy.types.PreferencesView.show_area_handle`.


.. _bpy.ops.screen.area_move:

Resizing
========

.. figure:: /images/interface_window-system_areas_resize.png
   :align: right
   :width: 250px
   :figwidth: 250px

You can resize areas by dragging their borders with :kbd:`LMB`.
Move your mouse cursor over the border between two areas,
so that the cursor changes to a double-headed arrow, and then click and drag.
Hold :kbd:`Ctrl` to snap the size of areas to convenient sizes.


Docking
=======

Docking describes several ways an area a user can interactively manipulate
the size and location of areas along with splitting an area into new areas.

To start the interactive process, placing the mouse cursor
in an area corner will change the cursor to a cross (+).
Once the cursor is a cross, press and hold :kbd:`LMB` to preform any of the following actions:

If you press :kbd:`Esc` or :kbd:`RMB` before releasing the mouse, the operation will be canceled.


.. _bpy.ops.screen.area_join:

Joining
-------

.. figure:: /images/interface_window-system_areas_join.png
   :align: right
   :width: 250px
   :figwidth: 250px

   Properties is being joined to the Outliner.

Dragging from an area corner into the space of a second area will *join* two areas.
The areas that will be joined will be displayed brighter.


.. _bpy.ops.screen.area_split:

Splitting
---------

.. figure:: /images/interface_window-system_areas_split.png
   :align: right
   :width: 250px
   :figwidth: 250px

Splitting an area will create a new area.
Dragging from an area corner left/right will split the area vertically,
to split the area horizontally drag up/down.

You can split and join areas at once by dragging a split operation into a separate area.

Dragging an area into the middle of an second area will replace the second area with the first area.


.. _bpy.ops.screen.area_options:

Area Options
============

:kbd:`RMB` on the border opens the *Area Options*.

Vertical/Horizontal Split
   Shows an indicator line that lets you select the area and position where to split.
   :kbd:`Tab` switches between vertical/horizontal.
Join Up/Down/Left/Right
   Shows the join direction overlay.
Swap Areas
   Swaps this area with the adjacent one.


.. _bpy.ops.screen.area_swap:

Swapping Contents
=================

You can swap the contents of two areas by pressing :kbd:`Ctrl-LMB`
on one of the corners of the initial area, dragging towards the target area,
and releasing the mouse there. The two areas do not need to be side-by-side,
though they must be inside the same window.


.. _bpy.ops.screen.screen_full_area:

Maximize Area
=============

.. reference::

   :Menu:      :menuselection:`View --> Area --> Toggle Maximize Area`
   :Shortcut:  :kbd:`Ctrl-Spacebar`

Expands the editor area so it fills the whole window, while keeping the Topbar and Status Bar visible.
This is useful for focusing on a single editor (e.g. 3D Viewport, Shader Editor) without changing your workspace
layout.

In the 3D Viewport, maximizing the area temporarily hides:

- :ref:`Navigation Gizmos <navigation-gizmo>`
- :ref:`bpy.types.View3DOverlay.show_text` overlay
- :ref:`bpy.types.View3DOverlay.show_stats` overlay

To return to normal size, use the shortcut again or click the *Back to Previous* button in the Topbar.


.. _bpy.ops.screen.back_to_previous:

Restore Area
============

.. reference::

   :Menu:      :menuselection:`View --> Area --> Restore Area`
   :Shortcut:  :kbd:`Ctrl-Spacebar`

Returns the maximized area back to its original size and restores the previous screen layout.


Focus Mode
==========

.. reference::

   :Menu:      :menuselection:`View --> Area --> Focus Mode`
   :Shortcut:  :kbd:`Ctrl-Alt-Spacebar`

Expands the editor area so it fills the entire window, hiding:

- The Topbar
- The Status Bar
- Secondary :doc:`regions </interface/window_system/regions>` (such as toolbars, sidebars, headers, etc.) of the
  editor itself.

This mode gives the maximum possible screen space for the active editor.

To return to normal size, use the shortcut again or click the :bl-icon:`fullscreen_exit`
icon in the top-right corner of the editor (visible only when hovering over the area).


.. _bpy.ops.screen.area_dupli:

Duplicate Area into New Window
==============================

.. reference::

   :Menu:      :menuselection:`View --> Area --> Duplicate Area into New Window`

Creates a new floating window containing a duplicate of the current editor area.
The new window is fully functional and part of the same Blender instance.

This is especially useful when working with multiple monitors.

.. tip::

   You can also create a new window by holding :kbd:`Shift-LMB` on an area corner
   and dragging outward slightly.
