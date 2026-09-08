.. _bpy.ops.transform.vert_slide:
.. _tool-mesh-vertex-slide:

**************
Slide Vertices
**************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Slide Vertices`
   :Shortcut:  :kbd:`G` twice or :kbd:`Shift-V`

Moves each selected vertex along one of its adjacent edges. After activating the tool,
move the mouse along the direction of the desired edge, then click :kbd:`LMB`
to confirm (or :kbd:`RMB` to cancel).

The following options are available in the :ref:`bpy.ops.screen.redo_last` panel after confirming.
The ones with a shortcut can also be changed while moving -- the shortcuts and current settings are
displayed in the status bar.

Factor
   Relative movement distance.
Even :kbd:`E`
   By default, each vertex is moved by the same percentage along the length of its edge.
   Use *Even* to move all vertices by the same absolute distance instead.
   (The *Factor* input is still a relative number, however.)
Flipped :kbd:`F`
   Move each vertex to the same absolute distance from its "opposing" vertex (on the other
   end of its sliding edge). Only available when *Even* is active.
Clamp :kbd:`Alt` or :kbd:`C`
   When disabled, vertices are allowed to go outside the original boundaries of their edge.
Mirror Editing
   Also slide matching vertices on the other side of the mesh.
   :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>` needs to be enabled for this to work.
Correct UVs
   Correct the UV coordinates of the moved vertices to avoid texture distortion.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_vertex_slide-vertices_example-1.png

          Vertices selected.

     - .. figure:: /images/modeling_meshes_editing_vertex_slide-vertices_example-2.png

          Sliding vertices.

     - .. figure:: /images/modeling_meshes_editing_vertex_slide-vertices_example-3.png

          Slide confirmed.

.. seealso::

   :doc:`/modeling/meshes/editing/edge/edge_slide`
