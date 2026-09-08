.. index:: Modeling Modifiers; Bevel Modifier
.. _bpy.types.BevelModifier:

**************
Bevel Modifier
**************

.. figure:: /images/modeling_modifiers_generate_bevel_panel.png
   :align: right
   :width: 250px

   The Bevel modifier.

The *Bevel* modifier bevels the edges of the mesh it is applied to,
with some control of how and where the bevel is applied to the mesh.

It is a non-destructive alternative to
the :doc:`Bevel Operation </modeling/meshes/editing/edge/bevel>` in Edit Mode.

.. list-table:: Side views of a cube.
   :align: center

   * - .. figure:: /images/modeling_modifiers_generate_bevel_square-not.png
          :width: 250px

          Not beveled.

     - .. figure:: /images/modeling_modifiers_generate_bevel_square.png
          :width: 250px

          Beveled.

.. container:: lead

   .. clear


Options
=======

Affect
   :Vertices:
      Only the areas near vertices are beveled, the edges remain unchanged.
   :Edges:
      Bevel the edges, creating intersections at vertices.

   .. figure:: /images/modeling_modifiers_generate_bevel_cubes-vertices-only.png

      Three cubes with 0.1, 0.3 and 0.5 bevel widths, with *Vertices* option selected.

.. figure:: /images/modeling_modifiers_generate_bevel_width-methods.png
   :align: right
   :width: 250px

Width Type
   Defines how *Width* will be interpreted to determine the amount of bevel.

   :Offset:
      The distance from the new edge to the original.
   :Width:
      The distance between the two new edges formed by the bevel
      (or the edges on either side of the bevel if there is more than one segment).
   :Depth:
      Value is the perpendicular distance from the new bevel face to original edge.
   :Percent:
      The percentage of the length of adjacent edge length that the new edges slide along.
   :Absolute:
      The exact distance along edges adjacent to the beveled edge. A difference from **Offset** is visible
      when the unbeveled edges attached to beveled edges meet at an angle besides a right angle.

Width
   The size of the bevel effect. See *Width Method* below.

   .. figure:: /images/modeling_modifiers_generate_bevel_cubes.png

      Three Cubes with 0.1, 0.3 and 0.5 bevel widths.

Segments
   The number of edge loops added along the bevel's face.

Limit Method
   Used to control where a bevel is applied to the mesh.

   :None:
      No limit, all edges will be beveled.
   :Angle:
      Only bevels edges whose angle of adjacent face normals plus the defined *Angle* is less than 180 degrees.
      Intended to allow you to bevel only the sharp edges of an object without affecting its smooth surfaces.
   :Weight:
      Use an attribute to determine the width of a bevel.
      When the bevel weight is 0.0, no bevel is applied.

      Any attribute on the input mesh can be chosen. By default the ``bevel_weight_edge`` and ``bevel_weight_vert``
      attributes adjusted in :doc:`edit mode </modeling/meshes/editing/edge/edge_data>` are used.
      For convenience, the modifier lists the attributes from the original mesh in the dropdown,
      but attributes created by previous modifiers can also be used. Attributes with non-matching
      :ref:`domains <attribute-domains>` or :ref:`types <attribute-data-types>` will be automatically
      interpolated to the correct type.
   :Vertex Group:
      Use weights from a vertex group to determine the width of the bevel.
      When the vertex weight is 0.0, no bevel is applied.
      An edge is only beveled if both of its vertices are in the vertex group.
      See :doc:`here </modeling/meshes/properties/vertex_groups/vertex_groups>` about adjusting vertex group weights.

      :bl-icon:`arrow_leftright` Invert
         Inverts the influence of the selected vertex group, meaning that the group
         now represents vertices that will not be deformed by the modifier.

         The setting reverses the weight values of the group.


Profile
-------

Superellipse
^^^^^^^^^^^^

Creates a bevel with a uniform concave or convex curve.

Shape
   The shape of the bevel, from concave to convex. It has no effect if *Segments* is less than 2.


Custom Profile
^^^^^^^^^^^^^^

.. figure:: /images/modeling_modifiers_generate_bevel_profile-widget.png
   :align: right
   :width: 250px

   The custom profile widget.

This widget allows the creation of a user-defined profile with more complexity than
with the single profile parameter. The modal tool allows toggling the custom profile,
but the shape of the profile is only editable in the options panel after the operation is confirmed.

The profile starts at the bottom right of the widget and ends at the top left, as if it
were between two edges meeting at a right angle. Control points are created in the widget and
then the path is sampled with the number of segments from the Bevel modifier.

.. container:: lead

   .. clear

Miter Shape
   The shape of the miter patterns, from concave to convex. It has no effect if *Segments* is less than 2.

   .. note::

      The *Miter Shape* slider stays active when miters are enabled
      because it still controls the shape of the miter profiles.

Presets
   The *Support Loops* and *Steps* presets are built dynamically depending on the number of segments in the bevel.
   If the number of segments is changed, the preset will have to be re-applied.

Sampling
   Samples will first be added to each control point, then if there are enough samples,
   they will be divided evenly between the edges. The *Sample Straight Edges* option toggles whether
   the samples are added to edges with sharp control points on either side. If there aren't enough samples
   to give each edge the same number of samples, they will just be added to the most curved edges,
   so it is recommended to use at least as many segments as there are control points.


Geometry
--------

Miter Inner/Outer
   A *miter* is formed when two beveled edges meet at an angle.
   On the side where the angle is greater than 180 degrees, if any, it is called an *outer miter*.
   If it is less than 180 degrees, then it is called an *inner miter*.
   The outer and inner miters can each be set to one of these patterns:

   :Sharp:
      Edges meet at a sharp point, with no extra vertices introduced on the edges.
   :Patch:
      Edges meet at a sharp point but in addition, two extra vertices are introduced near the point
      so that the edges and faces at the vertex may be less pinched together than
      what occurs in the *Sharp* case.
      This pattern does makes no sense for inner miters, so it behaves like *Arc* for them.
   :Arc:
      Two vertices are introduced near the meeting point, and a curved arc joins them together.

      The *Spread* slider controls how far the new vertices are from the meeting point.

      The *Profile* curve widget controls the shape of the arc.

   .. list-table:: Diagrams of the miter patterns.

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-2.png

             Sharp outer miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-3.png

             Patch outer miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-4.png

             Arc outer miter.

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-5.png

             Sharp inner miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-6.png

             Arc inner miter.

        - ..

Spread
   The value used to spread extra vertices apart for non-sharp miters.
   This option is available when Miter Inner is set to Arc.

Intersections
   When more than two beveled edges meet at a vertex, a mesh is created as a way to complete the intersection
   between the generated geometry. This option controls the method used to create that mesh.

   :Grid Fill:
      The default method for building intersections, useful when a smooth continuation of
      the bevel profile is desired. Without *Custom Profile* enabled, the curve of the profile continues through
      the intersection, but with a custom profile it just creates a smooth grid
      within the boundary of the intersection.
   :Cutoff:
      Creates a cutoff face at the end of each beveled edge coming into the vertex.
      This is most useful for custom profiles when the new intersection is too complex for a smooth grid fill.

      With a three way intersection, when the inner corners of the cutoff profiles faces meet at
      the same location, no center face is created.

      The direction of the cutoff faces depends on the original vertex's normal.

   .. list-table:: Intersection method options.

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-1.png
             :width: 200px

             Grid fill intersection method.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-2.png
             :width: 200px

             Three way cutoff intersection where the inner vertices are merged.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-3.png
             :width: 200px

             Cutoff intersection method with a center face.

Clamp Overlap
   Limits the width of each beveled edge so that edges cannot cause
   overlapping intersections with other geometry.
Loop Slide
   If there are unbeveled edges along with beveled edges into a vertex,
   the bevel tries to slide along those edges when possible.
   Turning the option off can lead to more even bevel widths.


Shading
-------

Harden Normals
   When enabled, the per-vertex face normals of the bevel faces are adjusted to
   match the surrounding faces, and the normals of the surrounding faces are not affected.
   This will keep the surrounding faces flat (if they were before),
   with the bevel faces shading smoothly into them. For this effect to work,
   a mesh must have a :ref:`custom split normals <modeling_meshes_normals_custom>` attribute.
   As a convenience, a ``custom_normal`` attribute will be created if one does not already exist.

Mark
   Seam
      If a seam edge crosses a non-seam one and you bevel all of them,
      this option will maintain the expected propagation of seams.
   Sharp
      Similar to Mark Seams, but for sharp edges.

Material Index
   The index of the material slot to use for the bevel.
   When set to -1, the material of the nearest original face will be used.

Face Strength
   Set *Face Strength* on the faces involved in the bevel, according to the mode specified here.
   This can be used in conjunction with a following
   :doc:`Weighted Normals </modeling/modifiers/normals/weighted_normal>` modifier
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
      In addition to those set for the *Affected* case,
      also set all the rest of the faces of the model to have strength *Strong*.
