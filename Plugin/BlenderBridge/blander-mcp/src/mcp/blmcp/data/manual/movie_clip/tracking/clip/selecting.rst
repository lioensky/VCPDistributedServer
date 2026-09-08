
****************
Selecting Tracks
****************

.. _bpy.ops.clip.select_all:

All :kbd:`A`
   Selects all items.

None :kbd:`Alt-A`
   Deselects all items.

Inverse :kbd:`Ctrl-I`
   Selects non-selected items and deselects existing selection.

.. _bpy.ops.clip.select_box:

Box Select
==========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`

See :ref:`tool-select-box`.


.. _bpy.ops.clip.select_circle:

Circle Select
=============

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Circle Select`
   :Shortcut:  :kbd:`C`

See :ref:`tool-select-circle`.


.. _bpy.ops.clip.select_lasso:

Lasso Select
============

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Lasso Select`
   :Shortcut:  :kbd:`Ctrl-Alt-RMB`

See :ref:`tool-select-lasso`.

.. _bpy.ops.clip.select_grouped:

Select Grouped
==============

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Select --> Select Grouped`
   :Shortcut:  :kbd:`Shift-G`

Select all tracks from specified group.

Action
   The group of tracks to select.

   :Keyframed Tracks: Select all keyframed tracks.
   :Estimated Tracks: Select all estimated tracks.
   :Tracked Tracks: Select all tracked tracks.
   :Locked Tracks: Select all locked tracks.
   :Disabled Tracks: Select all disabled tracks.
   :Track with Same Color: Select all tracks with same color as active track.
   :Failed Tracks: Select all tracks which failed to be reconstructed.


.. _bpy.ops.clip.stabilize_2d_select:

Select Stabilization Tracks
===========================

.. reference::

   :Mode:      Tracking mode
   :Menu:      :menuselection:`Select --> Select Stabilization Tracks`

Select tracks which are used for translation stabilization.


.. _bpy.ops.clip.stabilize_2d_rotation_select:

Select Stabilization Rotation Tracks
====================================

.. reference::

   :Mode:      Tracking mode
   :Menu:      :menuselection:`Select --> Select Stabilization Rotation Tracks`

Select tracks which are used for rotation stabilization.
