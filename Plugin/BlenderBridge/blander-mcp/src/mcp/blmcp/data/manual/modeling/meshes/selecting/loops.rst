
************
Select Loops
************

.. _bpy.ops.mesh.loop_select:
.. _bpy.ops.mesh.loop_multi_select:

Select Edge Loops
=================

.. reference::

   :Mode:      Edit Mode (Vertex or Edge select mode)
   :Menu:      :menuselection:`Select --> Select Loops --> Edge Loops`
   :Shortcut:  :kbd:`Alt-LMB` or :kbd:`Shift-Alt-LMB`

Selecting an edge with :kbd:`Alt-LMB` will also select the edges that are connected to it in a
(topologically) straight line. Use :kbd:`Shift-Alt-LMB` to add to the previous selection
instead of replacing it.

The resulting chain of edges is called an :ref:`edge loop <modeling_meshes_structure_topology>`
in Blender terminology because it typically forms a closed loop around the mesh.
However, as shown below, this doesn't have to be the case.

.. figure:: /images/modeling_meshes_selecting_loops_edge-loops.png

   Selecting edge loops. The clicked edge is highlighted in green.

.. hint::

   Selecting edge loops by clicking edges is also possible in the Vertex selection mode.

.. note::

   When :ref:`bpy.types.PreferencesInput.use_mouse_emulate_3_button` is enabled,
   the :kbd:`Alt-LMB` shortcut won't work because it serves as a replacement for :kbd:`MMB`.
   To select edge loops in this case, double-click with :kbd:`LMB` instead.

All Boundaries
--------------

Running the edge loop selection on a boundary edge twice will select the whole boundary.

.. figure:: /images/modeling_meshes_selecting_loops_edge-boundary-loops.png

   First and second edge loop selection.

See also :ref:`bpy.ops.mesh.region_to_loop`.

.. _modeling-meshes-selecting-face-loops:

Select Face Loops
=================

.. reference::

   :Mode:      Edit Mode (Face select mode)
   :Shortcut:  :kbd:`Alt-LMB` or :kbd:`Shift-Alt-LMB`

In *Face* selection mode, clicking an edge with :kbd:`Alt-LMB` will select the row
of faces that's perpendicular to that edge. Use :kbd:`Shift-Alt-LMB` to add to the
previous selection instead of replacing it.

The resulting row of faces is called a :ref:`face loop <modeling_meshes_structure_topology>`
in Blender terminology because it typically forms a closed loop around the mesh.
However, as shown below, this doesn't have to be the case.

.. figure:: /images/modeling_meshes_selecting_loops_face-loops.png

   Selecting face loops. The clicked edge is highlighted in green.

In Vertex selection mode, the same can be achieved using
:ref:`modeling-meshes-selecting-edge-rings`.

.. note::

   When :ref:`bpy.types.PreferencesInput.use_mouse_emulate_3_button` is enabled,
   the :kbd:`Alt-LMB` shortcut won't work because it serves as a replacement for :kbd:`MMB`.
   To select face loops in this case, double-click the edge with :kbd:`LMB` instead.

.. _modeling-meshes-selecting-edge-rings:

Select Edge Rings
=================

.. reference::

   :Mode:      Edit Mode (Edge select mode)
   :Menu:      :menuselection:`Select --> Select Loops --> Edge Rings`
   :Shortcut:  :kbd:`Ctrl-Alt-LMB` or :kbd:`Shift-Ctrl-Alt-LMB`

Selecting an edge with :kbd:`Ctrl-Alt-LMB` will also select the parallel edges that lie
in the face row perpendicular to the edge. Use :kbd:`Shift-Ctrl-Alt-LMB` to add to the
previous selection instead of replacing it.

The resulting set of edges is called an :ref:`edge ring <modeling_meshes_structure_topology>`
in Blender terminology because it typically forms a closed ring around the mesh.
However, as shown below, this doesn't have to be the case.

.. figure:: /images/modeling_meshes_selecting_loops_edge-ring.png

   Selecting edge rings in Edge mode. The clicked edge is highlighted in green.

This shortcut also works in Vertex selection mode, but results in a face loop selection instead:

.. figure:: /images/modeling_meshes_selecting_loops_edge-ring_vertex-mode.png

   Selecting edge rings in Vertex mode.

.. hint::

   To convert an edge ring selection to a face loop, either switch to Vertex mode or
   switch to Face mode while holding :kbd:`Ctrl`
   (see :ref:`modeling_meshes_selecting_switch-mode_expand-contract`).


.. _bpy.ops.mesh.loop_to_region:

Select Loop Inner-Region
========================

.. reference::

   :Mode:      Edit Mode (Edge select mode)
   :Menu:      :menuselection:`Select --> Select Loops --> Select Loop Inner-Region`

Selects all faces that are inside the selected, closed loop of edges.
While it's possible to use this operator in the *Vertex* and *Face* selection modes,
results may be unexpected.

Note that if the selected edges do not form a closed loop,
all connected faces will be selected.

Options
-------

Select Bigger
   Select the faces outside the edge loop instead of those inside it.

Examples
--------

.. figure:: /images/modeling_meshes_selecting_loops_inner-region1.png

   Single edge loop to region.

.. figure:: /images/modeling_meshes_selecting_loops_inner-region2.png

   Multiple edge loops.

.. figure:: /images/modeling_meshes_selecting_loops_inner-region3.png

   Holes are also supported.


.. _bpy.ops.mesh.region_to_loop:

Select Boundary Loop
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Loops --> Select Boundary Loop`

Replaces the current face selection by an edge selection going around the border of
each face "island." This is essentially the opposite of :ref:`bpy.ops.mesh.loop_to_region`.

This operator can be run in any selection mode. When run in Face mode,
it will automatically switch to Edge mode.

.. figure:: /images/modeling_meshes_selecting_loops_boundary-loop.png

   Before and after running Select Boundary Loop.
