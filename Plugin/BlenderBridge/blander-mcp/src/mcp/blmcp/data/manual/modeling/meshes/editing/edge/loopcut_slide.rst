.. _bpy.ops.mesh.loopcut_slide:

******************
Loop Cut and Slide
******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Loop Cut and Slide`
   :Shortcut:  :kbd:`Ctrl-R`

*Loop Cut and Slide* splits a loop of faces into two or more parallel loops.
The new edges are created in the middle by default, but you can also slide them closer to a side.


Usage
=====

The tool is interactive and has two steps:

#. Choose the face loop to cut

   After activating the tool, move the cursor over an edge through which the cut should pass
   (that is, an edge that's perpendicular to the cutting direction). Blender shows a yellow line
   previewing the cut that will be made. Click :kbd:`LMB` to confirm and move to the next step,
   or :kbd:`RMB` to abort.

#. Slide the new edge loop(s)

   You can now move the mouse to change the position of the new edge loop.
   Click :kbd:`LMB` to create the cut at the chosen location,
   or :kbd:`RMB` to create it at the center.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_tools_loop_before.png
          :width: 240px

          Mesh before inserting edge loop.

     - .. figure:: /images/modeling_meshes_tools_loop_preview.png
          :width: 240px

          Choosing the face loop.

     - .. figure:: /images/modeling_meshes_tools_loop_placement.png
          :width: 240px

          Sliding the new edge loop.

.. seealso::
   The :ref:`tool-mesh-edge_slide` tool for sliding existing edge loops.

.. _modeling-meshes-editing-edge-loopcut-slide-options:

Options
=======

These options are available while the tool is in use, and later in
the :ref:`bpy.ops.screen.redo_last` panel.

Number of Cuts :kbd:`Wheel`
   During the first step, you can change the number of cuts to create by
   scrolling :kbd:`Wheel`, typing a number, or pressing :kbd:`PageUp`/:kbd:`PageDown`.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_multicut.png

             Preview of multiple edge loops.

        - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_multicut-after.png

             Result of using multiple cuts.

Smoothness
   How much to offset the newly created edges along their normals to maintain surface curvature.
   You can change this in the first step using :kbd:`Alt-Wheel`, but because the smoothness
   isn't previewed at that stage, it's typically better to change it afterwards in the
   *Adjust Last Operation* panel.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_unsmooth.png

             Added edge loop without smoothing.

        - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_smooth.png

             Same edge loop, but with smoothing value.

Falloff
   Falloff type for *Smoothness*. Changes the shape of the profile.

Factor
   Position of the edge loop relative to the surrounding ones.

Even :kbd:`E`
   Makes the new edge loop have an even distance to an existing adjacent one
   (instead of a distance that's proportional to the length of each
   perpendicular edge it crosses). You can press :kbd:`E` during the second
   step to toggle it.

Flipped :kbd:`F`
   Keep an *Even* distance to the other adjacent edge. You can press :kbd:`F`
   during the second step to toggle it.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_uneven.png

          Cut with *Even* disabled.

     - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_even.png

          Cut with *Even* enabled. The red dot shows the side to which an even
          distance is kept.

     - .. figure:: /images/modeling_meshes_editing_edge_loopcut-slide_even_flipped.png

          Cut with *Even* and *Flipped* enabled.

Clamp :kbd:`C`
   When unchecked, the new edge loop can go outside the face loop's boundary edges.
   You can press :kbd:`C` or hold :kbd:`Alt` during the second step to toggle it.

Mirror Editing
   When checked, sliding the newly created edges will also slide any existing edges
   on the other side of the mesh. :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>`
   needs to be enabled for this to work.

Correct UVs
   When unchecked, the faces in the :doc:`UV map </editors/uv/introduction>` will be split
   uniformly even if the cut was placed off-center on the 3D mesh.
