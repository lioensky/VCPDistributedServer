
*****
Shape
*****

.. figure:: /images/modeling_curves_properties_shape_curves-shape-panel.png
   :align: center

   Shape panel.

.. _bpy.types.Curve.dimensions:

Dimensions
   By default, new curves are set to be 3D, which means that control points can be placed anywhere in 3D space.
   Curves can also be set to 2D which constrain the control points to the curve's local XY axis.

.. _bpy.types.Curve.resolution_u:
.. _bpy.types.Curve.render_resolution_u:

Resolution Preview/Render U
   The *resolution* property defines the number of points that are computed between every pair of control points.
   Curves can be made more or less smooth by increasing and decreasing the resolution respectively.
   The *Preview U* setting determines the resolution in the 3D Viewport while the *Render U* setting
   determines the curve's render resolution. If *Render U* is set to zero (0),
   then the *Preview U* setting is used for both the 3D Viewport and render resolution.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_shape_resolution-3.png

             Curves with a resolution of 3.

        - .. figure:: /images/modeling_curves_properties_shape_resolution-12.png

             Curves with a resolution of 12.

.. _bpy.types.Curve.twist_mode:

Twist Method
   A 3D curve has control points that are not located on the curve's local XY plane.
   This gives the curve a twist which can affect the curve normals.
   You can alter how the twist of the curve is calculated by choosing from
   *Minimum, Tangent* and *Z-Up* options from the select menu.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_shape_resolution-12.png

             Curves with a twist of Minimum.

        - .. figure:: /images/modeling_curves_properties_shape_twisting.png

             Curves with a twist of Tangent.

.. _bpy.types.Curve.twist_smooth:

Smooth
   Interactively removes twists from the curve. This is useful if a curve has noticeable "kinks"
   from over twisting; which can be possible when converting meshes to curves.

.. _bpy.types.Curve.fill_mode:

Fill Mode
   Fill determines the way a curve is displayed when it is beveled (see below for details on Beveling).
   When set to *Half* the curve is displayed as half a cylinder.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_shape_fill-half.png

             Curves with a fill of Half.

        - .. figure:: /images/modeling_curves_properties_shape_fill-full.png

             Curves with a fill of Full.

.. _bpy.types.Curve.fill_solver:

Fill Solver
   Triangulation solver used when filling 2D curves.

   :Sweep Line:
      Fast triangulation method intended for well-behaved outlines.
      Does not support self-intersecting curves.
   :Delaunay:
      Uses Constrained Delaunay Triangulation (CDT).
      More robust and supports self-intersecting curves, at the cost of being slower.

.. _bpy.types.Curve.fill_rule:

Fill Rule
   Fill rule used by the *Delaunay* *Fill Solver* to determine which regions are considered inside.

   :Even-Odd:
      Alternates inside/outside based on the number of boundary crossings.
      Overlapping regions may cancel out depending on the crossing count.
   :Non-Zero:
      Determines inside/outside based on winding direction.
      Overlapping curves with the same winding direction are filled as a union,
      while opposite winding directions can create holes.

.. _curve-shape-path-curve-deform:

Curve Deform
   .. _bpy.types.Curve.use_radius:

   Radius
      Causes the deformed object to be scaled by the set curve radius.
      Utilized when using a curve as a path or when using the :doc:`/modeling/modifiers/deform/curve`.

   .. _bpy.types.Curve.use_stretch:

   Stretch
      The *Stretch* curve option allows you to let the mesh object stretch, or squeeze, over the entire curve.
      To get the expected result, use this together with the *Bounds Clamp* option.
      Utilized when using the :doc:`/modeling/modifiers/deform/curve`.

   .. _bpy.types.Curve.use_deform_bounds:

   Bounds Clamp
      When this option is enabled, the object and mesh offset along the deformation axis is ignored.
      This can be useful with the *Stretch* option or when using a negative axis.
      Utilized when using the :doc:`/modeling/modifiers/deform/curve`.
