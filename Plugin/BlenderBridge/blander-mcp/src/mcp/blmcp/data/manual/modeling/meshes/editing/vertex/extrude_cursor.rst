.. _bpy.ops.mesh.dupli_extrude_cursor:

************************
Extrude to Cursor or Add
************************

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Ctrl-RMB`

Either creates a new vertex at the mouse cursor, or extrudes the selected vertices/edges
up to the mouse cursor.

If nothing is selected, pressing :kbd:`Ctrl-RMB` will create a vertex at the depth of the
:doc:`/editors/3dview/3d_cursor`.

If there are one or more selected vertices that are isolated (not connected to any edge or face),
pressing :kbd:`Ctrl-RMB` will extrude each one into an edge. The new vertices will be placed at
the same depth from the current viewpoint as the original ones. In addition, the original vertices
will be deselected and the new ones will be selected, so that this operation can be repeated to
create chains of edges.

.. figure:: /images/modeling_meshes_tools_extrude-cursor_vertex.png

   Extruding vertices into edges.

Finally, if there are two or more selected vertices that are connected by edges, pressing
:kbd:`Ctrl-RMB` will extrude them into faces.

.. figure:: /images/modeling_meshes_tools_extrude-cursor_quad.png

   Extruding edges into faces.

The previously selected edges will be rotated to get a smoother result. If this is not desired,
press :kbd:`Shift-Ctrl-RMB` instead.

.. tip::

   When extruding, use a top or side :doc:`view </editors/3dview/navigate/viewpoint>` to
   stay within a global plane. For example, using the top view will ensure that the new
   vertices have the same global Z coordinate as the previous ones.
