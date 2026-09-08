.. _bpy.ops.mesh.polybuild:
.. _tool-mesh-poly-build:

**********
Poly Build
**********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Poly Build`

*Poly Build* combines several mesh editing tools into one, letting you work more quickly.
It's especially useful for retopology.

Tool Settings
=============

Create Quads
   When creating a new triangle that shares an edge with an existing one,
   automatically :ref:`dissolves <bpy.ops.mesh.dissolve>` this edge so you're left with a quad.


Controls
========

Adding Geometry :kbd:`Ctrl-LMB`
   Creates a new vertex at the mouse cursor, then creates a triangle using this new vertex
   and the nearest existing edge. If the existing edge already has two neighboring faces,
   instead creates a new edge using the new vertex and the nearest existing vertex.
   Holding :kbd:`Ctrl` will preview the result in blue.
Deleting Geometry :kbd:`Shift-LMB`
   Dissolves the vertex/deletes the face under the mouse cursor.
   Holding :kbd:`Shift` will highlight the target element in red.
Moving Vertices :kbd:`LMB`
   You can move a vertex by dragging it.
Extruding Edges :kbd:`LMB`
   You can :doc:`extrude </modeling/meshes/editing/edge/extrude_edges>` an edge into a quad by dragging it.

.. tip::

   It is useful to enable :doc:`/editors/3dview/controls/snapping` and
   :ref:`bpy.types.ToolSettings.use_mesh_automerge` while tweaking vertices to combine them.
