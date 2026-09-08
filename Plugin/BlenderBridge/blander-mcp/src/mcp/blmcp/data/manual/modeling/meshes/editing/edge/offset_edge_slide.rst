.. _bpy.ops.mesh.offset_edge_loops_slide:

*****************
Offset Edge Slide
*****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Offset Edge Slide`
   :Shortcut:  :kbd:`Shift-Ctrl-R`

Creates two new edges surrounding each selected edge.

Usage
=====

#. Select one or more edges.
#. Click the menu item or press :kbd:`Shift-Ctrl-R`.
#. Move the mouse to the right to increase the distance or to the left to decrease it.
   Hold :kbd:`Shift` to move more slowly for better precision.

   Alternatively, type a number.
#. Press :kbd:`LMB` or :kbd:`Return` to confirm.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_editing_edge_offset-edge-slide_before.png

          Edges selected.

     - .. figure:: /images/modeling_meshes_editing_edge_offset-edge-slide_after.png

          Surrounding edges created.

     - .. figure:: /images/modeling_meshes_editing_edge_offset-edge-slide_cap.png

          *Cap Endpoint* enabled.

Options
=======

While the tool is active, the *Factor* is shown at the top of the 3D Viewport and the shortcuts
are shown in the :doc:`status bar </interface/window_system/status_bar>`. After confirming
with :kbd:`LMB`, the options can still be changed in the :ref:`bpy.ops.screen.redo_last` panel.

Cap Endpoint
   Creates triangles at the endpoints of each edge chain.

Factor
   Relative distance across the surrounding faces at which to create the new edges.

Even :kbd:`E`
   When enabled, the new vertices will keep an absolute distance from the edge chain or the
   surrounding edges (instead of a relative distance).

Flipped :kbd:`F`
   Switch between matching the shape of the edge chain or the surrounding edges when *Even*
   is enabled.

.. list-table::
   :widths: 1 1

   * - .. figure:: /images/modeling_meshes_editing_edge_offset-edge-slide_even.png

          *Even* enabled.

     - .. figure:: /images/modeling_meshes_editing_edge_offset-edge-slide_even-flip.png

          *Even* and *Flipped* enabled.

Clamp :kbd:`Alt` or :kbd:`C`
   Prevents the new edges from moving outside their neighboring faces.

Mirror Editing
   When checked, sliding the newly created edges will also slide any existing edges
   on the other side of the mesh. :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>`
   needs to be enabled for this to work.

Correct UVs
   Set the :doc:`UV coordinates </editors/uv/introduction>` of the new vertices according
   to their position on the mesh. When unchecked, the newly created vertices will have the same
   UV coordinates as the originally selected ones.
