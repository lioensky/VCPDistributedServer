.. _bpy.ops.mesh.inset:
.. _tool-mesh-inset_faces:

***********
Inset Faces
***********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Inset Faces`
   :Menu:      :menuselection:`Face --> Inset Faces`
   :Shortcut:  :kbd:`I`

This tool creates a border of faces around the selected faces, then allows adjusting
the thickness of that border by moving the mouse. As the border becomes thicker, the
outermost selected faces become thinner (while the inner ones stay the same).

While insetting, it's also possible to adjust the depth of the inset by holding
:kbd:`Ctrl`. Just like :doc:`/modeling/meshes/editing/face/extrude_faces_normal`,
this moves each selected vertex along its normal and can result in *all* faces changing their size.

Once the inset looks good, press :kbd:`LMB` or :kbd:`Return` to confirm.
Alternatively, press :kbd:`RMB` or :kbd:`Esc` to cancel.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_inset-faces_before.png

          Faces selected.

     - .. figure:: /images/modeling_meshes_editing_face_inset-faces_after.png

          First inset using only Thickness.

     - .. figure:: /images/modeling_meshes_editing_face_inset-faces_after-2.png

          Second inset using only Depth.

It's also possible to inset multiple disjoint "patches" of faces in one go.

Options
=======

.. figure:: /images/modeling_meshes_editing_face_inset-faces_options.png
   :align: right

   Inset operator options.

The keyboard shortcuts listed below can be used while insetting and are also shown in the status bar.

Boundary :kbd:`B`
   Also create border faces at boundary edges (that is, edges that are only part of one face instead of two).

Offset Even
   Maintain an even border width along the edges. When disabled, the border width will be
   even at the corners instead.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_inset-faces_offset-even-on.png

          Offset Even enabled (default).

     - .. figure:: /images/modeling_meshes_editing_face_inset-faces_offset-even-off.png

          Offset Even disabled.

Offset Relative
   Scale the Thickness and Depth offset of each border vertex by the average length of its two
   neighboring border edges.

Edge Rail
   Align the new edges between the border faces to the existing edges between the inset faces.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_inset-faces_edge-rail-off.png

          Edge Rail disabled.

     - .. figure:: /images/modeling_meshes_editing_face_inset-faces_edge-rail-on.png

          Edge Rail enabled.

Thickness
   The thickness of the newly created border faces.
Depth :kbd:`Ctrl`
   The distance to raise or lower the inset faces.
Outset :kbd:`O`
   Make the newly created border grow outward instead of inward.
Select Outer
   Switch the selection to the newly created border faces.
Individual :kbd:`I`
   Inset each face individually (instead of insetting each patch of faces as a connected whole).
Interpolate
   Interpolate mesh data for the newly created border vertices: UVs, Color Attributes,
   vertex group weights, etc.
