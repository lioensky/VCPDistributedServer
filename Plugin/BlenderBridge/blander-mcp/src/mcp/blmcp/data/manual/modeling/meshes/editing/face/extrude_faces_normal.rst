.. _bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten:

***************************
Extrude Faces Along Normals
***************************

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Extrude Along Normals`
   :Menu:      :menuselection:`Face --> Extrude Faces Along Normals`,
               :menuselection:`Mesh --> Extrude --> Extrude Faces Along Normals`

This tool is similar to :doc:`/modeling/meshes/editing/face/extrude_faces`, but instead of moving
all vertices along the same axis, it moves each vertex along its normal. This means an outward
extrusion on a convex surface will make the faces larger, for example.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_before.png

          Before extrusion

     - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_extrude-standard.png

          Regular extrusion

     - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_extrude-normals.png

          Extrusion along normals

After extruding, the following options are available in the :ref:`bpy.ops.screen.redo_last` panel:

Flip Normals
   Flip the normals of the newly created faces, as they might be pointing the wrong way
   depending on the extrusion direction. See the :ref:`bpy.types.View3DOverlay.show_face_orientation`
   overlay of the 3D Viewport to check whether they are correct.

Dissolve Orthogonal Edges
   When enabled, newly created faces will be merged with surrounding existing faces
   (potentially turning them into :term:`n-gons <n-gon>`) *if* they form a flat surface together.

Offset
   Distance to move the vertices.

Offset Even
   When disabled, each vertex is offset by the same distance. When enabled, each *face* is offset
   by the same distance.

   This option can also be toggled while extruding by pressing :kbd:`S` or holding :kbd:`Alt`.
   (These shortcuts are shown in the status bar.)

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_offset-even-before.png

          Before extrusion

     - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_offset-even-off.png

          Offset Even off (default)

     - .. figure:: /images/modeling_meshes_editing_face_extrude-faces-normal_offset-even-on.png

          Offset Even on

Mirror Editing
   Enabling this option moves the corresponding vertices on the other side of the mesh *without*
   extruding any faces, making it not very useful here.

:doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
   Enabling this option also moves the surrounding unselected vertices along their normals,
   making it not very useful for extrusion.

.. seealso::

   :doc:`/modeling/meshes/editing/mesh/transform/shrink-fatten` for moving vertices along their
   normal without extruding.
