
**********
Navigating
**********

2D Viewport
===========

Panning can be done by dragging with :kbd:`MMB`.

Zooming can be done using :kbd:`Wheel` or :kbd:`NumpadPlus`/:kbd:`NumpadMinus`.


.. _editors-uv-navigate-gizmos:

Gizmos
======

At the top of the UV Editor, next to the Sidebar region, navigation gizmos are available.
These provide on-screen controls for panning and zooming the view, which can be useful when
a mouse wheel is not available or when working on touch-based or pen-based devices.

The pan gizmo allows dragging the view in any direction, while the zoom gizmo adjusts the
view scale interactively.

When using the zoom gizmo, the current zoom level is displayed as a percentage, providing
immediate feedback about the scale of the image.

Holding :kbd:`Shift` while dragging the zoom gizmo enables more precise control.
Holding :kbd:`Ctrl` snaps the zoom level to 10% increments, allowing consistent and
predictable adjustments.


View Menu
=========

Also see :doc:`/editors/image/navigating` in the Image Editor.

Frame Selected :kbd:`NumpadPeriod`
   Change the view so that all selected UV vertices are visible.


2D Cursor
=========

Just like the :doc:`3D Viewport </editors/3dview/3d_cursor>`, the UV Editor has a Cursor
that you can jump to (:menuselection:`View --> Center View to Cursor`). It can also serve as
a :doc:`pivot point </editors/3dview/controls/pivot_point/index>` and a
:ref:`snapping target <bpy.ops.uv.snap_selected>`.

To change the Cursor's position, either press :kbd:`LMB` with the Cursor tool selected,
or :kbd:`Shift-RMB` with any tool selected. You can also change the "Location X/Y" fields
in the *View* tab of the Sidebar, in either relative coordinates (0 to 1) or
:ref:`pixel coordinates <bpy.types.SpaceUVEditor.show_pixel_coords>`.
In both cases, the lower left corner of the image serves as the origin (0, 0).

You can press :kbd:`Shift-C` to move the Cursor to the center.
