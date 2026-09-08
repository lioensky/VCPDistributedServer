********
Clean Up
********

These operators can automatically clean up certain types of messy geometry.


.. _bpy.ops.mesh.delete_loose:

Delete Loose
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Delete Loose`

Deletes the selected vertices, edges, and optionally faces that aren't connected
to anything.


.. _bpy.ops.mesh.decimate:

Decimate Geometry
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Decimate Geometry`

Reduces the face count of the selected geometry while minimizing shape changes.

Ratio
   The target triangle count ratio. For example, enter 0.4 to keep collapsing edges
   until the triangle count is 40% of the original.
Vertex Group
   Use the active vertex group when choosing which edges to collapse.
   The higher the vertex weights for an edge, the more likely it is to be chosen,
   even taking priority over "better" (shorter) candidates.

   Weight
      Factor by which to multiply the vertex weights.
   Invert
      Inverts the vertex weights, making edges with *lower* weights get collapsed first.
Symmetry
   Maintain symmetry on either the *X*, *Y*, or *Z* axis.

.. seealso::

   The :doc:`/modeling/modifiers/generate/decimate` in *Collapse* mode
   performs the same operation non-destructively.


.. _bpy.ops.mesh.dissolve_degenerate:

Degenerate Dissolve
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Degenerate Dissolve`

Collapses any selected edges that are shorter than a certain length.
This also results in the removal of small faces.

If two vertices are near to each other but are not connected by an edge,
they will not be merged; see :ref:`Merge By Distance <bpy.ops.mesh.remove_doubles>`
for an alternative.

Merge Distance
   Edges shorter than this length will be collapsed.


Limited Dissolve
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Limited Dissolve`

See :ref:`bpy.ops.mesh.dissolve_limited`.


.. _bpy.ops.mesh.face_make_planar:

Make Planar Faces
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Make Planar Faces`

Flattens the selected faces.

Factor
   The flattening strength for each iteration. Note that even a value of 1 may not be enough to
   get faces perfectly flat -- increase the *Iterations* in that case.
Iterations
   Number of times to repeat the operation.


.. _bpy.ops.mesh.vert_connect_nonplanar:

Split Non-Planar Faces
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Split Non-Planar Faces`

Splits any selected faces that are bent beyond a given limit.

Max Angle
   Faces that are bent by more than this angle will be split.

.. hint::

   You can use :ref:`bpy.ops.mesh.edge_rotate` if you'd rather have certain
   newly created edges point in a different direction.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_cleanup_split-non-planar-before.png

          Original mesh.

     - .. figure:: /images/modeling_meshes_editing_mesh_cleanup_split-non-planar-after.png

          Result of Split Non-Planar Faces.


.. _bpy.ops.mesh.vert_connect_concave:

Split Concave Faces
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Split Concave Faces`

Splits any selected :term:`concave <Concave Face>` faces so that only convex ones remain.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_cleanup_split-concave-before.png

          Original mesh.

     - .. figure:: /images/modeling_meshes_editing_mesh_cleanup_split-concave-after.png

          Result of Split Concave Faces.


Merge by Distance
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Merge by Distance`

Merges the selected vertices that are closer to each other than a certain distance.

Merge Distance
   Vertices closer than this distance will be merged.
Unselected
   Allow merging selected vertices with unselected ones.
Sharp Edges
   If the mesh uses :ref:`smooth shading <bpy.ops.object.shade_smooth>` and has
   :ref:`custom split normals <modeling_meshes_normals_custom>`, this option will add
   :ref:`edge marks <bpy.ops.mesh.mark_sharp>` where needed so that sharp edges will
   remain sharp after merging.

.. seealso::

   The :ref:`bpy.types.WeldModifier` performs this operation non-destructively.


.. _bpy.ops.mesh.fill_holes:

Fill Holes
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Clean up --> Fill Holes`

Fills each hole in the selected geometry with a face.

Sides
   The maximum number of sides: if a hole has more edges than this number,
   it will not be filled. Set to 0 to fill all holes.

.. seealso::

   For filling a large hole that has many edges,
   :doc:`Face Fill </modeling/meshes/editing/face/fill>` or
   :doc:`/modeling/meshes/editing/face/grid_fill` may be a better option.
