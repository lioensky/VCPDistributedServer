.. _bpy.ops.mesh.tris_convert_to_quads:

******************
Triangles to Quads
******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Triangles to Quads`
   :Shortcut:  :kbd:`Alt-J`

Merges adjacent triangles in the selection into quads. This is essentially the opposite of
:doc:`/modeling/meshes/editing/face/triangulate_faces` and can be run on a complete mesh in one go.

The operator uses angle thresholds to prevent creating malformed quads,
meaning that some triangles may remain.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_triangles-quads_before.png

          Before converting triangles to quads.

     - .. figure:: /images/modeling_meshes_editing_face_triangles-quads_after.png

          After converting.

Options
=======

Max Face Angle
   The maximum allowed angle between triangle normals (that is, coplanar triangles are considered to have an
   angle of 0°, not 180°). Triangle pairs that exceed this limit will not be merged.
Max Shape Angle
   The maximum tolerance for non-rectangular quads. If this is set to 0°, only triangles that form a quad
   with perfect 90° corners will be merged. If set to 40°, corners between 50° and 130° are allowed, and so on.
Topology Influence
   How much to prefer creating new quads that match the topology of existing quads.

   .. tip::

      For best results, set Topology Influence between 100-130% and Max Angle to 180°.
      Lower values may leave behind parallelograms and triangles, while higher values may cause errors.
Compare UVs
   Don't merge triangles that are disjoint in any UV map.
Compare Color Attributes
   Don't merge triangles that, for any :ref:`Color Attribute
   <modeling-meshes-properties-object_data-color-attributes>`, have different colors at their shared edge.
Compare Seam
   Don't dissolve edges that are marked as :doc:`UV Seams </modeling/meshes/uv/unwrapping/seams>`.
Compare Sharp
   Don't dissolve edges that are marked as :ref:`Sharp <bpy.ops.mesh.mark_sharp>`.
Compare Materials
   Don't merge triangles that have different materials.
Deselect Joined
   Deselect the triangles that were successfully merged into quads.
   Useful for identifying the remaining triangles that still need to be converted.
