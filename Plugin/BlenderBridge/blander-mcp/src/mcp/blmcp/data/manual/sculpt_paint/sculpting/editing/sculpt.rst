
******
Sculpt
******

This page details the general hotkey operators and menu operators in sculpt mode.


Transform
=========

Move
   Change the position of the object.
Rotate
   Change the orientation of the mesh.
Scale
   Increase/decrease the size of the mesh.
Sphere
   Morph the mesh to a spherical shape.

.. seealso::

   :doc:`Transform Tools </sculpt_paint/sculpting/tools/transforms>`.


.. _bpy.ops.paint.hide_show:

Show & Hide
===========

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt`

Some very common hotkey operators to control the visibility based on face sets.
These are not part of any menu and have to be used via the shortcuts.
More visibility operators can be found in the :doc:`Face Sets Menu </sculpt_paint/sculpting/editing/face_sets>`
and the Pie Menu shortcut :kbd:`Alt-W`. (Since visibility is often toggled via face sets.)

Box Hide
   Draw a box to hide faces of a mesh.
Box Show
   Draw a box to reveal hidden faces.
   This works similar to the :ref:`Box Select <tool-select-box>` tool.

.. _bpy.ops.sculpt.face_set_change_visibility:

Toggle Visibility :kbd:`Shift-H`
   Hide all face sets except the active one (under the cursor).
   If face sets are already hidden, then this operator will show everything.

Hide Active Face Set :kbd:`H`
   Hide the face set under the cursor. Press :kbd:`Shift-H` afterwards to show everything.

.. _bpy.ops.paint.hide_show_all:

Show All :kbd:`W`, :kbd:`Alt-H`
   Reveal all hidden geometry.

.. _bpy.ops.paint.visibility_invert:

Invert Visible
   Hides all visible geometry and makes all hidden geometry visible.

.. _bpy.ops.paint.hide_show_masked:

Hide Masked
   Hides all masked vertices.

.. _bpy.ops.paint.visibility_filter:

Grow/Shrink Visibility :kbd:`PageUp`, :kbd:`PageDown`
   Grows or shrinks the visible area of the mesh along its surface.

.. seealso::

   For a more general introduction see
   :doc:`Visibility, Masking & Face Sets </sculpt_paint/sculpting/introduction/visibility_masking_face_sets>`.


Fairing
=======

These operators smooths geometry patches based of a :doc:`Face set </sculpt_paint/sculpting/editing/face_sets>`.

.. seealso::

   :doc:`Edit Face Set Tool </sculpt_paint/sculpting/tools/edit_face_set>`

Fair Positions
   Creates a perfectly flat and smooth geometry patch from the face set.
   This is the ideal way to trim parts of your mesh
   if the vertex count is too high for other operations,
   or the vertex IDs must not be altered
   (Like when using :doc:`Multires </modeling/modifiers/generate/multiresolution>` sculpting).

Fair Tangency
   Creates a smooth as possible geometry patch from the face set
   by minimizing changes in vertex :term:`tangents <Tangent>`.
   This is ideal for creating smooth curved surfaces on complex topology,
   where just using the smooth brush will not lead to desired results


Trimming
========

The trimming operators add or remove geometry from the mesh based on a gesture input.
These operators are especially useful for sketching an early base mesh for further
sculpting with the :doc:`voxel remesher </sculpt_paint/sculpting/tool_settings/remesh>`.

.. _bpy.ops.sculpt.project_line_gesture:

:doc:`/sculpt_paint/sculpting/tools/line_project`
   Flattens the geometry along a plane determined by the camera view and a drawn line.
   The region of the mesh being flattened is visualized by the side of the line that is shaded.

.. _bpy.ops.sculpt.trim_box_gesture:

:ref:`tool-box-trim`
   Removes geometry based on a :ref:`box selection <tool-select-box>`.

.. _bpy.ops.sculpt.trim_lasso_gesture:

:ref:`tool-lasso-trim`
   Removes geometry based on a :ref:`lasso selection <tool-select-lasso>`.

:ref:`Box Add <tool-box-trim>`
   Adds geometry based on a :ref:`box selection <tool-select-box>`.

:ref:`Lasso Add <tool-lasso-trim>`
   Adds geometry based on a :ref:`lasso selection <tool-select-lasso>`.


.. _bpy.ops.sculpt.mesh_filter:

Mesh Filters
============

Applies a deformation to all vertices in the mesh at the same time.
Masking, auto-masking and visibility will be taken into account.

To use these operators, click and drag away from left to right
or from right to left for a negative effect.

.. seealso::

   :doc:`Mesh Filter Tool </sculpt_paint/sculpting/tools/mesh_filter>`

Smooth
   Smooths the positions of the vertices to either polish surfaces or remove volume from larger shapes.
   Especially useful to fix most of the artifacts of the voxel remesher.
   This filter works similar to the :doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>` brush.
Surface Smooth
   Eliminates irregularities of the mesh by making the positions
   of the vertices more uniform while preserving the volume of the object.
   This filter works similar to the *Surface* deformation type of the
   :doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>` brush.
Inflate
   Displaces vertices uniformly along their normal.
   This filter works similar to the :doc:`Inflate </sculpt_paint/sculpting/brushes/inflate>` brush.
Relax Topology
   Tries to create an even distribution of quads without deforming the volume of the mesh.
   This filter works the same as holding :kbd:`Shift` with the
   :doc:`Slide Relax </sculpt_paint/sculpting/brushes/slide_relax>` brush.
Relax Face Sets
   This will remove the jagged lines visible after drawing or creating a face set.
   This filter works the same as holding :kbd:`Shift` with the
   :doc:`Draw Face Set </sculpt_paint/sculpting/brushes/draw_facesets>` brush.
Sharpen
   Sharpens and smooths the mesh based on its curvature,
   resulting in pinching hard edges and polishing flat surfaces.
   Especially useful when sculpting hard surfaces and stylized models
   with creasing and flattening brushes.
Enhance Details
   Increases the high frequency surface details of the mesh
   by intensifying the difference between creases and valleys.
   This filter works similar to the inverted direction of the
   :doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>` brush.
Erase Multires Displacement
   Deletes displacement information of
   the :doc:`Multires Modifier </modeling/modifiers/generate/multiresolution>`,
   resetting the mesh to a regular subdivision surface result.
   This can be used to reset parts of the sculpt or to fix reprojection artifacts
   after applying a :doc:`Shrinkwrap Modifier </modeling/modifiers/deform/shrinkwrap>`.

   Negative strokes will intensify the displacement details,
   this method works similar to *Enhance Details* and can give better results in some circumstances.
Randomize
   Randomly moves vertices along the vertex normal.
   This filter works similar to the :ref:`Randomize Transform <bpy.ops.object.randomize_transform>`.


Sample Color
============

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Sample Color`
   :Shortcut:  :kbd:`Shift-X`, :kbd:`Shift-Ctrl-X`

Samples a color from the viewport and assigns it to the active
:doc:`Paint </sculpt_paint/sculpting/brushes/paint>` brush.

This allows quickly matching the brush color to existing painted details
directly on the model.

- Press :kbd:`Shift-X` to sample a color at the mouse cursor position.
- Press :kbd:`Shift-Ctrl-X` to sample the **merged viewport color**,
  including lighting, shading, and all visible layers.

The sampled color becomes the primary color of the active Paint brush.


.. _bpy.ops.sculpt.set_pivot_position:

Set Pivot
=========

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Set Pivot`

Like Object and Edit Mode, Sculpt Mode also has a :term:`Pivot Point`.
This is because the basic :doc:`move, rotate and scale </sculpt_paint/sculpting/tools/transforms>`
transforms are also supported in Sculpt Mode.
But the pivot point in Sculpt Mode is unique. It always moves together with the transformed mesh
and can be both manually & automatically placed.

Origin
   Sets the pivot to the origin of the sculpt.
Unmasked
   Sets the pivot position to the average position of the unmasked vertices.
Mask Border
   Sets the pivot position to the center of the mask's border.
   This operation will automatically happen when using :ref:`bpy.ops.sculpt.expand`.
Active Vertex
   Sets the pivot position to the active vertex position.
Surface :kbd:`Shift-RMB`
   Sets the pivot position to the surface under the cursor.

.. tip::

   For more convenient placement of the pivot point it's recommended to use the shortcut assigned to *Surface*.

.. seealso::

   For a more general introduction see :doc:`Transforming </sculpt_paint/sculpting/introduction/transforming>`.


.. _bpy.ops.sculpt.optimize:

Rebuild BVH
===========

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Rebuild BVH`

Recalculates the :term:`BVH` used by :doc:`/sculpt_paint/sculpting/tool_settings/dyntopo`
to improve performance, which might degrade over time while using Dyntopo.

.. seealso::

   For a more general introduction see :doc:`Adaptive Resolution </sculpt_paint/sculpting/introduction/adaptive>`.


Dynamic Topology Toggle
=======================

Toggles :doc:`/sculpt_paint/sculpting/tool_settings/dyntopo`.


Transfer Sculpt Mode
====================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Transfer Sculpt Mode`
   :Shortcut:  :kbd:`Alt-Q`

Switches Sculpt Mode from the :term:`Active` object to the object under the mouse.
See :ref:`bpy.ops.object.transfer_mode` for more information.

.. seealso::

   For a more general introduction see
   :doc:`Working with Multiple Objects </sculpt_paint/sculpting/introduction/multiple_objects>`.
