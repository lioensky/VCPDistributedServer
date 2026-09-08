.. _bpy.ops.transform.edge_slide:
.. _modeling-meshes-editing-edge-slide:
.. _tool-mesh-edge_slide:

**********
Edge Slide
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Slide`
   :Shortcut:  :kbd:`G` twice

Moves the selected edges across their neighboring faces.

.. hint::

   Use :ref:`bpy.ops.mesh.loop_select` to quickly select a chain of edges
   that goes around the mesh.

Usage
=====

Select one or more edges, press :kbd:`G` twice, move the mouse, and click :kbd:`LMB` to confirm
(or :kbd:`RMB` to cancel).

By default, the vertices on the selected edges all move by the same *percentage* towards their
neighbor:

.. list-table::
   :widths: 1 1

   * - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_before.png

          Selected edges.

     - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_after.png

          Repositioned edges.


In *Even* mode, the vertices instead keep the same *distance* from their neighbor.
The red dot indicates which side they look at (i.e. which neighbor they pick):

.. list-table::
   :widths: 1 1

   * - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_even.png

          Even Mode enabled.

     - .. figure:: /images/modeling_meshes_editing_edge_edge-slide_even-flip.png

          Even Mode with Flip enabled.

Options
=======

While the tool is active, the *Factor* is shown at the top of the 3D Viewport and the shortcuts
are shown in the :doc:`status bar </interface/window_system/status_bar>`. After confirming
with :kbd:`LMB`, the options can still be changed in the :ref:`bpy.ops.screen.redo_last` panel.

Factor
   Direction and amount to slide. Values of -1 and 1 move each selected edge fully towards
   one of its neighbors.
Even :kbd:`E`
   By default, each vertex is moved by the same percentage along the length of its edge.
   Use *Even* to instead move all vertices so they're at the same absolute distance from
   a neighboring vertex. (The *Factor* input is still a relative number, however.)
Flipped :kbd:`F`
   Use the other neighboring vertex when *Even* is active.
Clamp :kbd:`Alt` or :kbd:`C`
   Prevents the edges from moving outside their neighboring faces.
Mirror Editing
   Also slide matching edges on the other side of the mesh.
   :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>` needs to be enabled for this to work.
Correct UVs
   Corrects the UV coordinates of the moved vertices to avoid texture distortion.

.. seealso::

   :doc:`/modeling/meshes/editing/vertex/slide_vertices`
