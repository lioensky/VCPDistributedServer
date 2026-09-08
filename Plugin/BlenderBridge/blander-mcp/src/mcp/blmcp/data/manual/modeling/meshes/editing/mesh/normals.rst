.. _bpy.ops.mesh.normals_tools:
.. _modeling-meshes-editing-normals-editing:

***************
Editing Normals
***************

The *Normals* menu can be accessed as a popover by pressing :kbd:`Alt-N`.

Most of the operators in this menu work with :ref:`custom split normals <modeling_meshes_normals_custom>`,
which are normal vectors that belong to face corners (not vertices). Selecting these corners can be done in
multiple ways:

- If the :ref:`selection mode <bpy.ops.mesh.select_mode>` is set to *Vertex* or *Edge*, selecting a
  vertex or edge also selects the nearest corners of the faces it's part of.
- If the selection mode is *Face*, selecting a face also selects its corners.
- If both the *Vertex* and *Face* modes are enabled, selecting a vertex and then adding a face
  will select just the matching face corner.
- Similar to the above, if both the *Edge* and *Face* modes are enabled, selecting an edge and
  then adding a face will select just the two matching face corners.

.. seealso::

   - The 3D Viewport :ref:`overlay <bpy.types.View3DOverlay.show_split_normals>` for visualizing normals.
   - The :doc:`/modeling/meshes/properties/custom_data` panel of the mesh properties for
     clearing custom normals.
   - Mesh Data Transfer (:doc:`operator </scene_layout/object/editing/link_transfer/transfer_mesh_data>`
     or :doc:`modifier </modeling/modifiers/modify/data_transfer>`) for copying normals from
     another mesh.
   - The :doc:`/modeling/modifiers/normals/normal_edit` and the
     :doc:`/modeling/modifiers/normals/weighted_normal` for calculating or changing normals
     based on certain criteria.

.. _bpy.ops.mesh.flip_normals:

Flip
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Flip`

Changes the orientation of the selected faces, turning their "front side" into their
"back side" and vice versa. This does not affect custom split normals.

The 3D Viewport's :ref:`bpy.types.View3DOverlay.show_face_orientation` overlay is useful for quickly
spotting faces that are oriented the wrong way.


.. _bpy.ops.mesh.normals_make_consistent:

Recalculate
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Recalculate Outside` and
               :menuselection:`Mesh --> Normals --> Recalculate Inside`
   :Shortcut:  :kbd:`Shift-N` and :kbd:`Shift-Ctrl-N`

Flips the orientation of the selected faces where necessary, making them all point outward (or inward).
The mesh does not need to be a closed volume for this.

As with `Flip`_, this operation does not affect custom split normals.

.. _bpy.ops.mesh.set_normals_from_faces:

Set from Faces
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Set from Faces`

Sets the custom split normals of each selected vertex to the average normal of its surrounding
selected faces.

Keep Sharp Edges
   When checked, face corners that are part of a :ref:`Sharp <bpy.ops.mesh.mark_sharp>` edge will
   keep their original custom normal.


.. _bpy.ops.transform.rotate_normal:

Rotate
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Rotate`
   :Shortcut:  :kbd:`R` followed by :kbd:`N`

Tool for rotating the custom split normals of the selected face corners by moving the mouse.
Click :kbd:`LMB` to confirm or :kbd:`RMB` to cancel.


.. _bpy.ops.mesh.point_normals:

Point to Target
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Point to Target`
   :Shortcut:  :kbd:`Alt-L`

Makes the custom split normals of the selected face corners point at a certain target.
After clicking the menu item or pressing the keyboard shortcut, choose the target by
pressing one of the following keys (also shown in the :doc:`status bar </interface/window_system/status_bar>`):

- :kbd:`M` for the mouse cursor.
- :kbd:`L` for the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`.
- :kbd:`O` for the :doc:`object origin </scene_layout/object/origin>`.
- :kbd:`Ctrl-LMB` for the :doc:`/editors/3dview/3d_cursor`. This also changes the location of the Cursor.
- :kbd:`Ctrl-RMB` for a certain vertex, edge, or face. Make sure not to click a space where there's no geometry,
  as doing so will :doc:`extrude </modeling/meshes/editing/vertex/extrude_cursor>` the selection instead.

In addition, the following options are available:

Invert :kbd:`I`
   Make the normals point away from the target instead.
Align :kbd:`A`
   All normals will point in the same direction: from the average position of the selected vertices
   to the target.
Spherize :kbd:`S`
   Interpolate between each normal's original and new orientation. The interpolation value can be set
   in the :ref:`bpy.ops.screen.redo_last` panel after confirming the operator.
Reset :kbd:`R`
   Reset the custom normals to what they were when the operation started.

After configuring the normals, press :kbd:`LMB` or :kbd:`Return` to confirm. The above options can
then still be changed in the Adjust Last Operation panel.

.. _bpy.ops.mesh.merge_normals:

Merge
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Merge`

Applies :ref:`smooth shading <bpy.ops.mesh.faces_shade_smooth>` to the selected faces and clears the
:ref:`Sharp <bpy.ops.mesh.mark_sharp>` mark for the selected edges. Then, at each selected vertex,
sets the custom normals that are part of a smooth-shaded face to their average orientation.
(Custom normals that are part of a flat-shaded face are left unchanged.)

To average the custom normals regardless of face selection, use the :ref:`bpy.ops.mesh.average_normals`
operator.

.. _bpy.ops.mesh.split_normals:

Split
=====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Split`

Applies :ref:`flat shading <bpy.ops.mesh.faces_shade_flat>` to the selected faces and marks the selected
edges as :ref:`Sharp <bpy.ops.mesh.mark_sharp>`. Then, at each selected vertex, sets each custom normal
that's part of a flat-shaded face to the normal of that face. (Custom normals that are part of a
smooth-shaded face are set to the average of the normals of those faces.)

.. _bpy.ops.mesh.average_normals:

Average
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Average`

For each selected vertex, divides the connected face corners into groups based on :ref:`Sharp
<bpy.ops.mesh.mark_sharp>` edges, then sets the custom normals of the face corners in each group to a certain average.
The :ref:`bpy.ops.screen.redo_last` panel has the following options:

Type
   :Custom Normal: Set the custom normals of the face corners in each group to their average.
   :Face Area: Set the custom normals of the face corners in each group to a weighted average of their
       face normals. The weights are determined by face area: larger faces have more influence on the final normal.
   :Corner Angle: Like *Face Area*, except the weights are determined by the face corner angles.
Weight
   If the *Type* is set to *Face Area* or *Corner Angle*, the *Weight* influences which face normals the
   averaged normal leans towards. If it's 50, a simple weighted average is used. If it's 100, the averaged normal
   is based solely on the faces with the largest area (or corners with the largest angle).
   If it's 1, the normal is based solely on the faces with the smallest area (or corners with the smallest angle).
Threshold
   Tolerance value for treating face areas (or corner angles) as equal.

.. figure:: /images/modeling_meshes_editing_mesh_normals_average.png

   Averaging the custom normals for two vertices. The top vertex has two groups of faces separated by Sharp edges,
   so two separate averages are calculated. The bottom vertex has no Sharp edges, so only one average is calculated.

.. seealso::

   The :doc:`/modeling/modifiers/normals/weighted_normal` does this non-destructively.

Copy Vector
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Copy Vector`

Copies a single normal vector to an internal clipboard:

- If a face is selected, its normal is copied.
- If a vertex is selected, its normal is copied, but only if all its custom split normals are the same.
- If a face corner is selected, its custom split normal is copied.


Paste Vector
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Paste Vector`

Pastes the previously copied normal vector onto the selected face corners.
The :ref:`bpy.ops.screen.redo_last` panel has the following option:

Absolute Coordinates
   When enabled, sets the custom split normals of the selected face corners to the
   pasted normal. When disabled, adds the pasted normal as an offset.

.. _bpy.ops.mesh.smooth_normals:

Smooth Vectors
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Smooth Vectors`

Smooths out the custom normals of each selected vertex by averaging with
the normals at neighboring vertices. The :ref:`bpy.ops.screen.redo_last`
panel has the following option:

Factor
   Smoothing strength. Specifically, this is the interpolation value between
   the original normals and the averaged ones.


Reset Vectors
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Reset Vectors`

Resets the custom normals of the selected face corners to their default.


.. _bpy.ops.mesh.mod_weighted_strength:

Select by Face Strength
=======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Select by Face Strength`

Selects the faces that have a specific *Strength* (Weak, Medium, or Strong)
and deselects the others.

This property is used by the :doc:`/modeling/modifiers/normals/weighted_normal`
if its *Face Influence* setting is enabled.


Set Face Strength
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Normals --> Set Face Strength`

Sets the *Strength* of the selected faces to Weak, Medium, or Strong.
By default, all faces have a strength of Medium.

This property is used by the :doc:`/modeling/modifiers/normals/weighted_normal`
if its *Face Influence* setting is enabled.
