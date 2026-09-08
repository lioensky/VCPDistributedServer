.. _bpy.ops.mesh.merge:
.. _bpy.ops.mesh.remove_doubles:
.. _vertex-merging:

*****
Merge
*****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Merge`,
               :menuselection:`Context Menu --> Merge`
   :Shortcut:  :kbd:`M`

Merges the selected vertices together. The menu has the following options:

At Center
   Merge all selected vertices into one vertex placed at their geometric center
   (i.e. the average of their positions, not their bounding box center).
At Cursor
   Merge all selected vertices into one vertex placed at the :doc:`/editors/3dview/3d_cursor`.
Collapse
   Merge each island of connected vertices into one vertex placed at the average position.
At First
   Merge all selected vertices into the one that was selected first.
   Only available in the *Vertex* selection mode.
At Last
   Merge all selected vertices into the one that was selected last.
   Only available in the *Vertex* selection mode.
By Distance
   Merge each cluster of vertices that are closer to each other than a certain distance.

.. note::

   *At First* and *At Last* depend on the selection order which is easily lost (e.g. by
   changing the selection mode). They should typically be run right after making the selection.

.. seealso::

   The :doc:`/modeling/modifiers/generate/weld` merges vertices by distance non-destructively.

Options
-------

After merging, the following options are available in the :ref:`bpy.ops.screen.redo_last` panel:

Type
   The type of merge to perform.
UVs
   Corrects the :doc:`UV coordinates </editors/uv/introduction>` to avoid texture distortion.

*Merge By Distance* instead has the following options:

Merge Distance
   Vertices closer than this distance will be merged.
Centroid Merge
   Place each new vertex at the average position of the vertices that were merged together.
   When disabled, the position of the original vertex closest to this average is used.
Unselected
   Allow merging selected vertices with unselected ones.
Sharp Edges
   If the mesh uses :ref:`smooth shading <bpy.ops.object.shade_smooth>` and has
   :ref:`custom split normals <modeling_meshes_normals_custom>`, this option will add
   :ref:`edge marks <bpy.ops.mesh.mark_sharp>` where needed so that sharp edges will
   remain sharp after merging.
