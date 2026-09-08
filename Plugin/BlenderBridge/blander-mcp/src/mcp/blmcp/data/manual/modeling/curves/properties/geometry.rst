
********
Geometry
********

.. figure:: /images/modeling_curves_properties_geometry_panel.png
   :align: center

   Geometry panel.

The Geometry panel lets you turn a curve from a 1D line into a 2D ribbon or a 3D tube.

.. figure:: /images/modeling_curves_properties_geometry_intro.png

   Three copies of the same base curve: one without geometry (bright orange line);
   one with Offset and Extrude applied (blue ribbon); and one with Offset, Extrude,
   and Bevel applied (gray tube).

.. _bpy.types.Curve.offset:

Offset
   Moves the control points along their normals.

.. _bpy.types.Curve.extrude:

Extrude
   Turns the curve from a line into a ribbon by extruding it to the "sides":
   at each point, the curve normal is calculated as the "up" direction,
   and the curve is extruded to the "left" and "right."

.. hint::

   You can tweak the direction and distance of *Offset* and *Extrude* at each control point
   by changing its :ref:`modeling-curve-tilt` (rotation around the tangent axis) and
   :ref:`modeling-curve-radius` (scale factor).

.. _bpy.types.Curve.taper_object:

Taper Object
   A separate Curve object, consisting of a single, non-:ref:`cyclic <bpy.ops.curve.cyclic_toggle>`,
   2D spline, that controls the scale factor of the geometry along the length of each of the curve's splines.

   .. note::

      The "taper" in the name is misleading: this word means "to reduce in size towards the end,"
      while the *Taper Object* can apply any size anywhere. A better name might have been "Scale Curve."

   Specifically, the *Taper Object* defines a graph where the X axis represents the position on the
   curve and the Y axis represents the scale:

   - The first control point of the *Taper Object* spline corresponds to the first control point of
     each geometry spline. Same thing for the last points.
   - The first *Taper* point should have the highest X coordinate, and the last point the lowest
     (try :ref:`bpy.ops.curve.switch_direction` if the scaling doesn't seem to be working).
     The specific range of X coordinates doesn't matter: it could be [-10, 10], [-1, 1], or anything else.
   - A Y coordinate of 1.0 leaves the geometry unchanged. A coordinate of 0.5 makes it half as large,
     while 2.0 makes it twice as large.

   The Z coordinates of the *Taper Object* control points are ignored, but if you want,
   you can set the object's :ref:`Shape <bpy.types.Curve.dimensions>` to "2D" to force them to 0.

.. _bpy.types.Curve.taper_radius_mode:

Taper Radius
   How to combine the scale graph of the *Taper Object* with the radii of the control points.

   .. note::

      As above, this setting is not limited to tapering and does not define any single radius.
      A better name might have been "Scale Curve Mode."

   :Override: The *Taper Object* (scale curve) overrides the radii (scales) of the curve's control points.
   :Multiply: The scale given by the *Taper Object* is multiplied by that of the control points.
   :Add: The scale given by the *Taper Object* is added to that of the control points.

   .. list-table::
      Examples of a curve with a Radius of 0 on the left and 1 on the right.

      * - .. figure:: /images/modeling_curves_properties_geometry_taper-mode-override.png

             Override mode.

        - .. figure:: /images/modeling_curves_properties_geometry_taper-mode-multiply.png

             Multiply mode.

        - .. figure:: /images/modeling_curves_properties_geometry_taper-mode-add.png

             Add mode.

.. _bpy.types.Curve.use_map_taper:

Map Taper
   If geometry is only generated for part of the curve (which can be achieved by changing
   :ref:`Factor Start/End <bpy.types.Curve.bevel_factor_start>`), enabling *Map Taper* will
   make the endpoints of the *Taper Object* correspond to those of the geometry instead of
   those of the curve.


.. _bpy.types.Curve.bevel:

Bevel
=====

Apply a Bevel to turn the 1D line (or 2D ribbon when using :ref:`bpy.types.Curve.extrude`)
into a 3D tube.

Round
-----

The cross section of the tube becomes a circle (or pill when using Extrude).
You can also get a half circle by changing the :ref:`bpy.types.Curve.fill_mode`.

.. _bpy.types.Curve.bevel_depth:

Depth
   The size of the cross section.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel-depth.png
             :width: 320px

             Small Depth.

        - .. figure:: /images/modeling_curves_properties_geometry_bevel.png
             :width: 320px

             Large Depth.

.. _bpy.types.Curve.bevel_resolution:

Resolution
   Drives the number of vertices in the cross section.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel-resolution.png
             :width: 320px

             A low Resolution results in a blocky mesh.

        - .. figure:: /images/modeling_curves_properties_geometry_bevel.png
             :width: 320px

             A high Resolution results in a smooth mesh.

.. _bpy.types.Curve.use_fill_caps:

Fill Caps
   Seals the ends of the tube.


Object
------

This option lets you fully customize the shape of the cross section by selecting a separate Curve object.

.. figure:: /images/modeling_curves_properties_geometry_bevel_object.png
   :align: center

.. _bpy.types.Curve.bevel_object:

Object
   The curve that defines the cross section. It can be either closed (:ref:`cyclic <bpy.ops.curve.cyclic_toggle>`)
   or open.

   .. important::

      This curve should be flat in its local XY plane; using another plane will not give the
      desired result.

   .. note::
      If the selected curve has modifiers, these will not be taken into account.
      The bevel will use the original curve shape. This happens because curves turn into
      meshes internally when they have modifiers on them,
      at which point they can't be used as cross section curves anymore.

      To work around this, you can disable beveling on the path curve, and instead
      add geometry nodes to it: retrieve the cross section curve using an
      :doc:`/modeling/geometry_nodes/input/scene/object_info`, convert it from
      a mesh back into a curve using a
      :doc:`/modeling/geometry_nodes/mesh/operations/mesh_to_curve`,
      and finally pass both the path curve and the cross section curve to a
      :doc:`/modeling/geometry_nodes/curve/operations/curve_to_mesh`.

Profile
-------

This option lets you customize the shape of the cross section without having to create a separate
Curve object. However, unlike the *Object* option where the curve defines the full cross section,
the *Profile* in the :ref:`ui-curve-widget` only defines a quarter which is then repeated and mirrored.

.. figure:: /images/modeling_curves_properties_geometry_bevel_profile.png
   :align: center

The black dots on the profile represent the points where it's sampled (that is, where mesh vertices
will be created). You can increase the *Resolution* to get more sample points, and thus a smoother result.

Preset
   You can choose one of the predefined profiles instead of making your own.
   The *Support Loops* and *Steps* presets are generated dynamically based on the *Resolution*
   and need to be reapplied if you change it.

Reverse Path
   Mirrors the profile around the diagonal.

Toggle Profile Clipping
   Limits the X and Y coordinates of control points to the range [0, 1].

Sample Straight Edges
   Whether to sample the profile in the middle of perfectly straight segments
   (lines between two control points with the *Vector* :ref:`handle type <ui-curve-widget-handle-type>`).
   This is disabled by default, as it's normally enough to sample the profile at the control
   points themselves.

Sample Even Lengths
   By default, each profile segment receives the same number of sample points.
   By enabling this option, the sample points are instead distributed evenly
   along the whole length of the profile.

Start & End Mapping
===================

.. _bpy.types.Curve.bevel_factor_start:
.. _bpy.types.Curve.bevel_factor_end:

Factor Start, End
   The percentages along the length of the curve where the geometry should start
   and end. By default, these are set to 0 and 1, making the geometry cover the full length;
   but if you change them to 0.5 and 0.75, the geometry will only cover the third quarter
   of the curve.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_geometry_bevel.png
             :width: 320px

             A curve with Factor Start set to 0 and End to 1.

        - .. figure:: /images/modeling_curves_properties_geometry_bevel-start-end-factor.png
             :width: 320px

             Factor End changed to 0.6.

.. _bpy.types.Curve.bevel_factor_mapping_start:
.. _bpy.types.Curve.bevel_factor_mapping_end:

Mapping Start, End
   How to map the *Factor Start, End* percentages to positions on the curve.

   :Resolution:
      Only count control points, disregarding the lengths of the spline segments (pieces of
      spline between two control points). If a spline has three control points and *Factor Start*
      is set to 0.5, the geometry will always start at the second control point,
      even if its distances to the first and third control points are completely different.
   :Segments:
      Calculate an approximate percentage along the length of the spline by assuming that
      all the subdivisions within each segment are evenly distributed.
   :Spline:
      Calculate an accurate percentage along the length of the spline.

Examples
========

Open 2D Curve
-------------

An open (non-cyclic) curve with beveling applied becomes a tube.

.. figure:: /images/modeling_curves_properties_geometry_extrude-open-curve.png
   :width: 320px


Closed 2D Curve
---------------

A closed (cyclic) curve with beveling applied becomes a torus by default.
If the curve is 2D and you set the :ref:`bpy.types.Curve.fill_mode` to *Both*,
the top and bottom holes will be filled with flat discs, and you'll get a cylinder
with rounded edges instead.

.. figure:: /images/modeling_curves_properties_geometry_extrude-closed-curve.png
   :width: 320px

This doesn't work with 3D curves.

Taper
-----

By selecting a 2D curve as the *Taper Object* of another (2D or 3D) curve,
you can let the radius of the latter curve's geometry vary over the curve's
length without having to create additional control points.

.. figure:: /images/modeling_curves_properties_geometry_extrude-taper-example.png

Tilt
----

You can use the :ref:`modeling-curve-tilt` tool to rotate a control point around
its tangent axis, creating a twist in the curve. The example below also uses
a custom profile (cross section).

.. figure:: /images/modeling_curves_properties_geometry_extrude-bevel-curve-tilt.png
