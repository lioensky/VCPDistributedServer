.. _bpy.ops.mesh.knife:
.. _tool-mesh-knife:

*******************
Knife Topology Tool
*******************

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Knife`
   :Menu:      :menuselection:`Mesh --> Knife Topology Tool`
   :Shortcut:  :kbd:`K`

The Knife tool allows to interactively "cut through" faces,
subdividing them and creating a chain of new edges along the way.


Usage
=====

First, select the tool in the Toolbar or press :kbd:`K`. The cursor
will change into a scalpel to indicate it's active.

Click :kbd:`LMB` at the place where you want to start cutting.
This can be anywhere: on an existing vertex, edge, or face,
or even outside of the mesh.

Move your mouse to the next location. You'll see a yellow line indicating
the new edges that will be created, and aqua dots indicating the new
vertices. Click :kbd:`LMB` to confirm and start on the next cutting segment.

Once you're done, press :kbd:`Spacebar` or :kbd:`Return` to apply the cuts.
Alternatively, press :kbd:`Esc` to cancel.

.. hint::

   By using :ref:`3dview-multi-object-mode`, you can cut multiple objects
   at the same time.

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_knife_line-before.png

          Mesh before knife cut.

     - .. figure:: /images/modeling_meshes_tools_knife_line-active.png

          Knife cut active.

     - .. figure:: /images/modeling_meshes_tools_knife_line-after.png

          After applying knife cut.


Tool Settings
=============

These settings are only available when using the tool from the Toolbar
(not when pressing :kbd:`K`). They can be found in the *Tool* tab of the
:doc:`/editors/properties_editor` editor and of the Sidebar.

Occlude Geometry
   Only cut geometry visible on screen. By disabling this, you can cut all the way
   through the mesh, including faces that are on the backside or behind others.

Only Selected
   Only cut through selected geometry. You can press :kbd:`Shift-K` instead of
   :kbd:`K` to start cutting with this option enabled.

X-Ray
   Show the cutting path even if it's occluded by geometry.

Measurements
   The measurements to show along the cutting path: distances, angles, or both.

   .. list-table::
      :widths: 1 1 1

      * - .. figure:: /images/modeling_meshes_tools_knife-measurement-distance.png

             Only distances.

        - .. figure:: /images/modeling_meshes_tools_knife-measurement-angles.png

             Only angles.

        - .. figure:: /images/modeling_meshes_tools_knife-measurement-both.png

             Both distances and angles.

Angle Snapping
   Whether to constrain the cutting lines to multiples of the *Snap Increment* angle.

   :None: No snapping.
   :Screen: Snap in screen space (the viewing plane).
   :Relative: Snap in a plane on the geometry, relative to an adjacent edge or cutting line.

   .. list-table::
      :widths: 1 1

      * - .. figure:: /images/modeling_meshes_tools_knife_angle-before.png

             Relative snapping at 90°. Blender highlights the reference edge in red
             and shows the snapping direction in white.

        - .. figure:: /images/modeling_meshes_tools_knife_angle-after.png

             Doing a few more cuts and applying.

Snap Increment
   The angle to use for *Angle Snapping*.


Controls
========

These keyboard shortcuts are shown in the
:doc:`status bar </interface/window_system/status_bar>` while cutting.
They're available both when using the tool from the Toolbar and when pressing :kbd:`K`.

Cut :kbd:`LMB`
   You can either click to add a new cutting line, or drag to create cutting lines
   as you move the mouse over edges.

Close Loop - Double-click :kbd:`LMB`
   Adds a cutting point at the cursor (just like when single-clicking) and then connects
   it to the first point in the current path, closing the loop.

Stop :kbd:`RMB`
   Completes the current cutting path and begins a new one. The cursor will snap to previously
   defined cuts.

   .. list-table::
      :widths: 1 1

      * - .. figure:: /images/modeling_meshes_tools_knife_multiple-before.png

             After defining the horizontal cut, press :kbd:`RMB` and define
             the vertical one.

        - .. figure:: /images/modeling_meshes_tools_knife_multiple-after.png

             Result after applying.

Confirm :kbd:`Spacebar` or :kbd:`Return`
   Confirms the cut, turning the cutting paths into edges.

Cancel :kbd:`Esc`
   Cancels the cut.

Undo :kbd:`Ctrl-Z`
   Undoes the previous cutting line (or, if you dragged the mouse before, all the cutting
   lines created during that drag).

Midpoint Snap :kbd:`Shift`
   Hold to snap the cursor to the center of edges.

Ignore Snap :kbd:`Ctrl`
   Hold to temporarily stop the cursor from snapping to existing vertices, edges,
   and cutting lines.

Cut Through :kbd:`C`
   Also cut through occluded faces, instead of only the visible ones.
   This is linked to (and the opposite of) the *Occlude Geometry* setting above.

Axis :kbd:`X`, :kbd:`Y`, or :kbd:`Z`
   Constrains the current cutting line to a global axis. Press a second time to use the
   object's local axis, and a third time to disable the constraint again.

Measure :kbd:`S`
   Cycles between measurements to show: distances, angles, or both.

X-Ray :kbd:`V`
   Toggles whether to display cuts occluded by geometry.

Angle Constraint :kbd:`A`
   Constrains cutting lines to multiples of the *Snap Increment* angle. This angle
   can be specified in the Tool Settings before cutting (see above) or typed
   while cutting with *Angle Constraint* active.

   By default, the snapping is done in the *Screen* plane. Press :kbd:`A`
   a second time to snap in planes on the geometry, *Relative* to an automatically
   chosen edge or cutting line. You can press :kbd:`R` to select a different reference line.

   Press :kbd:`A` a third time to disable the snapping again.


Known Limitations
=================

Duplicate Vertices
------------------

If a cut creates duplicate vertices, this is often caused by the clipping range
being too large. Try increasing the :ref:`Clip Start <bpy.types.SpaceView3D.clip_start>`
to avoid this problem.
Also see :ref:`Depth Troubleshooting <troubleshooting-depth>` for details.
