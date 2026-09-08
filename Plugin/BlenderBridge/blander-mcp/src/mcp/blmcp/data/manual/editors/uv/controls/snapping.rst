
********
Snapping
********

Snapping lets you easily align UV elements to others.
It can be toggled by clicking the magnet icon in the UV Editor's header,
or more temporarily by holding :kbd:`Ctrl`.

This page is about the Snap header button; for the Snap menu,
see :ref:`UV Editing <bpy.ops.uv.snap_selected>`.

.. _bpy.types.ToolSettings.snap_uv_element:

Snap Target
===========

.. reference::

   :Header:    :menuselection:`Snapping --> Snap To`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

Increment
   Snaps to grid points.

   This option snaps to an imaginary grid that starts at the selection's original location and has the same
   resolution as the grid displayed in the editor. In other words, it lets you move the selection in
   "increments" of the grid cell size.

Grid
   Snaps to grid points.

Vertex
   Snaps to the vertex that's closest to the mouse cursor.


Additional Options
==================

Snap Base :guilabel:`Vertex`
   See :ref:`3D Viewport Snapping <bpy.types.ToolSettings.snap_target>` for more information.


Affect
======

Specifies which transformations are affected by snapping.
By default, snapping only happens while moving something,
but you can also enable it for rotating and scaling.


Rotation Increment
==================

Angle used in incremental snapping for the rotation operator.
The second value is the **Rotation Precision Increment**, used for finer transformations
and activated by default with the :kbd:`Shift` key.
