.. _bpy.ops.sculpt.mask_expand:
.. _bpy.ops.sculpt.expand:

******
Expand
******

This is a multi-purpose modal operator to intuitively create and edit masks/face sets.
When executed, it uniformly expand outwards a pattern from the vertex under the cursor.

.. note::

   These operators are meant to be used interactively through the shortcut.

There is also a `full showcase of the Expand features and use cases <https://www.youtube.com/watch?v=XT7h6lmE5bc>`__.

.. figure:: /images/sculpt-paint_sculpting_expand_example.png

      A preview of *Expand Mask by Topology*


Expand Mask by Topology
=======================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Expand Mask by Topology`
   :Shortcut:  :kbd:`Shift-A`

Expands a mask from the active vertex.

Usage
-----

Mask from A to B
   Start the operator and expand a mask from an origin to your mouse cursor distance.
   Then confirm with :kbd:`LMB` or :kbd:`Return`

   By default the expansion will use a *Geodesic* falloff :kbd:`1`
   to create perfectly accurate distances along the surfaces.
   Use other falloff types via :kbd:`2`, :kbd:`3` & :kbd:`4` to expand via
   triangles, whole faces or scene distances instead.

   .. figure:: /images/sculpt-paint_sculpting_expand_falloff_example.png

      The typical result when using the *Diagonals* falloff to expand along the quads of the face.

   Start Expand while pointing at an open boundary to expand from the entire boundary loop.
   This will always use the *Topology* falloff mode.

   .. needs visual practical example

Fill Connected Meshes
   Move your cursor outside of the boundaries of the mesh to mask the entire connected mesh.
   This can be done repeatedly to quickly mask separate meshes.

Fill Face Sets
   Hold :kbd:`Ctrl` to snap to face sets under your cursor and fill them.
   Any face set that was already fully covered in the expansion will be filled as well.

Automatically Set Transform Pivot
   While using any Transform tool, the pivot point
   will automatically snap the border of an Expand result.
   This way areas (Like limbs) can be masked and then immediately rotated or otherwise transformed.

   .. figure:: /images/sculpt-paint_sculpting_expand_auto_pivot.png

Pattern Creation
   The different falloff types can be used for circular, triangular and square patterns.
   More loops can also be added/removed via :kbd:`W` & :kbd:`Q` to repeat the pattern across the mesh.

   .. figure:: /images/sculpt-paint_sculpting_expand_pattern1.png

      An example of using expand with mirror options,
      loops and a recursion to create wood carving patterns.

   .. tip::

      :doc:`Mirror options </sculpt_paint/sculpting/tool_settings/symmetry>`
      can also be combined with the expansion.

   Linear gradients :kbd:`G` or brush falloff gradients :kbd:`B` will help to add slanted surfaces
   to the patterns.

   A "Recursions" with :kbd:`R` or :kbd:`Alt-R` will start
   a new expansion along the border of the current expansion.
   Doing this multiple times, can help for increasingly random patterns
   or advanced pattern creation.

   .. figure:: /images/sculpt-paint_sculpting_expand_pattern2.png

      An example of using loops and gradients with multiple expanded masks.

   .. tip::

      Remember that Expand only affects visible geometry.
      So if a pattern should only be created on a part of the mesh,
      :doc:`hide </sculpt_paint/sculpting/editing/sculpt>` the other geometry first.

   Use the :doc:`Mesh Filter </sculpt_paint/sculpting/tools/mesh_filter>`
   to deform the geometry and the :doc:`Color Filter </sculpt_paint/sculpting/tools/color_filter>`
   to add colors, to apply the patterns on the sculpt.


Expanding Textures
   Textures can be used to affect the shape and gradients of the expanded mask.
   This feature can be combined with loops and recursion to create unique results.

   .. needs visual example with Michel fur patterns

   To use a texture, you need to assign it to your currently active brush in the
   :doc:`Texture </sculpt_paint/brush/texture>` Brush Settings. The texture can be edited/created
   in the :doc:`Texture Properties </render/materials/legacy_textures/index>`.

   .. note::

      This texture only works when the :ref:`Mapping <bpy.types.BrushTextureSlot.map_mode>` is set to *3D*.

   Use :kbd:`Y` and :kbd:`T` to increase or decrease the affect the texture has on the edge of the mask.


Controls
--------

:Invert: :kbd:`F`
   Flips between expanding a positive mask (value of one) or a negative mask (value of zero).
   In the case of face sets, this option flips between including areas inside the masked area
   or areas outside the masked area.
   .. needs visual technical examples for both
:Toggle Preserve State: :kbd:`E`
   Accumulate the new mask on top of the previous one or replace it.
   For Face Sets, this will toggle between creating Face Sets boundaries
   or replacing the existing Face Sets.
:Move Origin: :kbd:`Spacebar`
   Moves the initial vertex used for calculating the falloff.
   .. needs visual technical example
:Geodesic Falloff: :kbd:`1`
   Uses a falloff based on the :term:`Geodesic` distances from the edge boundary to the active vertex.
:Topology Falloff: :kbd:`2`
   Uses a falloff based on a flood fill using edges.
:Diagonals Falloff: :kbd:`3`
   Uses a falloff based on a flood fill using polygon diagonals and edges.
:Spherical Falloff: :kbd:`4`
   Uses a falloff based on the Euclidean distances from the edge boundary to the active vertex.
   .. needs visual technical examples
:Toggle Gradient: :kbd:`G`
   Enables linear gradient of values from the origin to the current active vertex.
:Toggle Brush Gradient: :kbd:`B`
   Similar to linear gradient but uses the current brush :doc:`Falloff </sculpt_paint/brush/falloff>`
   to define the shape of the falloff.
   .. needs visual technical examples
:Geodesic Recursive Step: :kbd:`R`
   Start a new expansion with a :term:`Geodesic` falloff from the boundary of the current falloff.
:Topology Recursive Step: :kbd:`Alt-R`
   Start a new expansion with a topology falloff from the boundary of the current falloff.
   .. needs visual technical examples
:Snap Expanded to Face Sets: :kbd:`Ctrl`
   Isolates the expanded region to the boundary of the face set under the cursor.
:Loop Count Increase: :kbd:`W`
   Increase the number of loops or iterations the operator is run;
   using four loops will split the mask into four parts.
:Loop Count Decrease: :kbd:`Q`
   Decrease the number of loops or iterations the operator is run;
   using four loops will split the mask into four parts.
   .. needs visual technical examples
:Texture Distortion Increase: :kbd:`Y`
   Increases the falloff distance when using a texture to distort the mask shape.
:Texture Distortion Decrease: :kbd:`T`
   Decreases the falloff distance when using a texture to distort the mask shape.
   ..needs visual technical examples


Expand Mask by Normals
======================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Expand Mask by Normals`
   :Shortcut:  :kbd:`Shift-Alt-A`

Expand a mask, following the curvature of the surface.
This operator uses the same internal operator as :ref:`bpy.ops.sculpt.expand`
meaning all the shortcuts and functionality works the same as that tool.

This operator is especially useful for hard surface sculpting.

.. tip::

    If one expansion does not properly fill the entire desired surface,
    use the operator repeatedly with a different starting point.

.. needs visual practical example

.. note::

   Using any of the Falloff shortcuts :kbd:`1-4`
   will replace the curvature falloff of this operator.


.. _face_set_expand:

Expand Face Set by Topology
===========================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Expand Face Set by Topology`
   :Shortcut:  :kbd:`Shift-W`

Expands a face set from the active vertex.
This operator uses the same internal operator as :ref:`bpy.ops.sculpt.expand`
meaning all the hotkeys and functionality works the same as that tool,
with the gradient features as the exception.

Usage
-----

Saving Masks
   Expanding Face Sets has all the same use cases as expanding masks.
   The advantage for this one is that they will be saved for repeated usage.
   Face sets can be filled any time with a mask,
   so assigning areas face sets will save you time.
   (And of course face sets can be used to
   :doc:`hide face sets </sculpt_paint/sculpting/editing/sculpt>`)

Pivot Points for Pose Brush
   When using the :doc:`Pose Brush </sculpt_paint/sculpting/brushes/pose>` it is most predictable when using it with
   Face Sets to define the face set boundaries as pivot point locations.
   Face Sets can be expanded from a point or from a boundary between hidden face sets
   to create them quickly.
   Alternatively :ref:`Grow/Shrink Face Sets <bpy.ops.sculpt.face_set_edit>`
   or use the :ref:`Expand Active Face Set <face_set_expand_active>` to dynamically grow/shrink them.

   .. Visual examples for pose brush on fingers, expanding face set from finger segment boundary
   .. and growing face set segment.

Cloth Sculpting
   Tools like the :doc:`Cloth Filter </sculpt_paint/sculpting/tools/cloth_filter>`
   and :doc:`Cloth Brush </sculpt_paint/sculpting/brushes/cloth>`
   work especially well when only simulating small areas at a time.
   Face Sets can very easily be created with Expand to assign areas of action.

   .. needs visual examples with grids & a ribbon

.. _face_set_expand_active:

Expand Active Face Set
======================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Expand Face Set by Topology`
   :Shortcut:  :kbd:`Shift-Alt-W`

Expands an existing face set with a geodesic falloff.
This operator uses the same internal operator as :ref:`bpy.ops.sculpt.expand`
meaning all the hotkeys and functionality works the same as that tool.

.. note::

   Using any of the Falloff shortcuts :kbd:`1-4`
   the operator to switch to :ref:`Expand Face Set by Topology <face_set_expand>`.

Usage
-----

Resizing Face Sets
   Resize a Face Set along the surface distances.
   It is an alternative to :ref:`Grow/Shrink Face Sets <bpy.ops.sculpt.face_set_edit>`
   which follows the topology instead of geodesic distances.

   .. needs visual examples side by side

Joining Face Sets
   When holding :kbd:`Ctrl` the expansion will instead snap to other Face Sets.
   This is a fast way of joining multiple face sets into one.

   .. needs visual examples side by side
