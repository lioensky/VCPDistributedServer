.. _bpy.ops.mesh.bevel:
.. _tool-mesh-bevel:
.. This page is copied into /modeling/meshes/editing/vertex/bevel_vertices.rst and should
.. describe both modes of the Bevel tool (not just "Edges" but also "Vertices").
.. --- copy below this line ---

*****
Bevel
*****

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Bevel Vertices`, :menuselection:`Edge --> Bevel Edges`
   :Shortcut:  :kbd:`Shift-Ctrl-B` (Bevel Vertices), :kbd:`Ctrl-B` (Bevel Edges)

The *Bevel* tool smooths out corners and edges. This helps make objects look more realistic --
after all, nothing in real life is infinitely sharp.

.. figure:: /images/modeling_meshes_editing_edge_bevel_cubes.png

   Cubes without and with bevel.

.. seealso::

   The :doc:`/modeling/modifiers/generate/bevel` does this non-destructively.


Usage
=====

Select one or more vertices, edges, or faces, then press either :kbd:`Ctrl-B` to smooth both edges and
corners or :kbd:`Shift-Ctrl-B` to smooth only corners. Move the mouse to increase the bevel radius
and roll the :kbd:`Wheel` to set the density of the new geometry.
Finally, press :kbd:`LMB`/:kbd:`Return` to confirm or :kbd:`RMB`/:kbd:`Esc` to cancel.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-1.png

          Before beveling.

     - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-2.png

          Increased bevel width.

     - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-3.png

          Increased bevel segments.


Options
=======

While the tool is active, the current settings are shown at the top of the 3D Viewport. Use the keyboard shortcuts
(also shown in the :doc:`status bar </interface/window_system/status_bar>`) to select a setting, then move the
mouse or type a number to change it. When moving the mouse, hold :kbd:`Shift` to change the value more slowly
for better precision, or :kbd:`Ctrl` to snap to coarse increments.

After confirming with :kbd:`LMB`, the settings can still be changed in the :ref:`bpy.ops.screen.redo_last` panel.

Affect :kbd:`V`
   Vertices
      Bevel the selected vertices, leaving the edges unchanged.
   Edges
      Bevel the selected edges, as well as the vertices where three or more edges meet.

Width Type :kbd:`M`
   The meaning of the *Width* setting. In the examples below, the *Width* is set to 50% for the
   "Percent" *Width Type* and to 1.0 for the other types.

   .. list-table::
      :widths: 1 1 1

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_width-type-original.png

             Before beveling

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_width-type-offset.png

             Offset

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_width-type-width.png

             Width

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_width-type-depth.png

             Depth

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_width-type-percent.png

             Percent

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_width-type-absolute.png

             Absolute

Width :kbd:`A`
   The size/radius of the bevel. The precise meaning depends on the *Width Type*.

   .. note::

      When multiple edges are beveled at the same time,
      it is sometimes impossible to make the width match the above definition on all edges simultaneously.
      Bevel tries to compromise in such cases.
      Sometimes turning off *Loop Slide* (see below) can make it easier for Bevel to make the widths as specified.

Segments :kbd:`S`
   The density of the new geometry. Higher values will give a smoother result.

   While the tool is active, this setting can be changed with :kbd:`Wheel` even if it is not selected.

Profile Shape :kbd:`P`
   A number between 0 and 1 that controls the shape of the profile (side view of each beveled edge).

   .. figure:: /images/modeling_meshes_editing_edge_bevel_profile-shape.png

   If *Miter Outer* or *Miter Inner* is set to *Arc*, this also controls the shape of the miters.

Material Index
   The 0-based index of the :ref:`material slot <bpy.types.MaterialSlot>` to assign to the newly created faces.
   If set to -1, the new faces inherit the materials of their neighbors.

Harden Normals :kbd:`H`
   When enabled, assigns :ref:`custom split normals <modeling_meshes_normals_custom>` to the newly created
   faces to make them appear :ref:`smoothly shaded <bpy.ops.object.shade_smooth>` without affecting the
   rest of the mesh.

Clamp Overlap :kbd:`C`
   Prevents beveled edges from overshooting past the end of their neighboring faces.

Loop Slide
   Whether the new inner edges should be perpendicular to the beveled edge or match the direction
   of the existing inner edges.

   .. list-table::
      :widths: 1 1 1

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_loop-slide-before.png

             Before beveling.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_loop-slide-off.png

             Loop Slide off.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_loop-slide-on.png

             Loop Slide on.

Mark
   Seams :kbd:`U`
      When beveling three or more edges that share a vertex, and two of those edges
      are marked as :doc:`UV Seams </modeling/meshes/uv/unwrapping/seams>`,
      the new edges between them will also be marked as Seams.
   Sharp :kbd:`K`
      Same as *Mark Seams*, but for :ref:`Sharp <bpy.ops.mesh.mark_sharp>` edges.

   .. list-table::
      :widths: 1 1 1

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_mark-seams-before.png

             Before beveling.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_mark-seams-off.png

             Mark Seams off.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_mark-seams-on.png

             Mark Seams on.

Miter Outer :kbd:`O`
   When beveling three or more edges connected to the same vertex, and two of those edges
   form a corner of more than 180° on the side where there are faces, the *Outer Miter*
   determines if any extra geometry is created in that corner to avoid pinching.

   .. list-table::
      :widths: 1 1 1

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-2.png

             Sharp outer miter (no extra geometry).

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-3.png

             Patch outer miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-4.png

             Arc outer miter.

(Miter) Inner :kbd:`I`
   When beveling two or more edges connected to the same vertex, and there are edges that form a
   corner of less than 180° on the side where there are faces, the *Inner Miter* determines if
   any extra geometry is created in those corners.

   .. list-table::
      :widths: 1 1

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-5.png

             Sharp inner miter (no extra geometry).

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-6.png

             Arc inner miter.

Spread
   The size of the *Inner Miter* when set to *Arc*. This also affects the *Outer Miter*.

Intersection Type :kbd:`N`
   The type of geometry to generate at points where three or more beveled edges meet.

   :Grid Fill:
      Fill the space between the edges with geometry that smoothly connects them.
   :Cutoff:
      Cap off each edge with a flat face.

   .. list-table::
      :widths: 1 1 1

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-1.png

             Grid fill.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-2.png

             Cutoff.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-3.png

             Cutoff with a center face.

Face Strength
   Whether to apply a *Face Strength* to the faces involved in the bevel.
   This can be used in conjunction with
   a :doc:`Weight Normals Modifier </modeling/modifiers/normals/weighted_normal>`
   (with the *Face Influence* option checked).

   :None:
      Do not set face strength.
   :New:
      Set the face strength of new faces along edges to *Medium*,
      and the face strength of new faces at vertices to *Weak*.
   :Affected:
      In addition to those set for the *New* case,
      also set the faces adjacent to new faces to have strength *Strong*.
   :All:
      In addition to those set for the *Affected* option,
      also set all the rest of the faces of the model to have strength *Strong*.

Profile Type :kbd:`Z`
   Determines the flow of the edges that are generated along each beveled edge.

   Superellipse
      Use an autogenerated profile based on the *Profile Shape* setting.

   Custom
      .. figure:: /images/modeling_modifiers_generate_bevel_profile-widget.png
         :align: right
         :width: 300px

         The custom profile widget.

      Use a custom profile as defined in the :ref:`ui-curve-widget` in the Adjust Last Operation
      panel. The curve is a side view of a bevel between two faces that meet at a right angle;
      the darkened area represents the inside of the mesh.

      Presets
         The *Support Loops* and *Steps* presets are built dynamically depending on
         the number of bevel *Segments*. If the number of segments is changed,
         the preset will have to be re-applied.

      Sample Straight Edges
         Whether to sample the profile in the middle of perfectly straight curve segments
         (lines between two control points with the *Vector* :ref:`handle type <ui-curve-widget-handle-type>`).
         This is disabled by default, as it's normally enough to sample the profile at the control
         points themselves.

      Sample Even Lengths
         By default, each profile segment (piece between two control points) receives the
         same number of sample points. By enabling this option, the sample points are instead
         distributed evenly along the whole length of the profile.
