.. _bpy.types.Spline:

*************
Active Spline
*************

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Sidebar --> Item --> Active Spline`

The *Active Spline* panel is used in Edit Mode to control properties of the currently selected spline.


.. _spline-common-options:
.. _bpy.types.Spline.use_cyclic_u:
.. _bpy.types.Spline.resolution_u:
.. _bpy.types.Spline.use_smooth:

.. rubric:: Common Options

Cyclic U
   Closes the active spline.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_active-spline_nurbs-default.png

             Default NURBS curve.

        - .. figure:: /images/modeling_curves_properties_active-spline_nurbs-cyclic.png

             A NURBS curve with Cyclic applied.

Resolution U
   Alters the :ref:`resolution <bpy.types.Curve.resolution_u>`
   of each segment by changing the number of subdivisions.
Smooth
   Use :ref:`Smooth Shading <modeling-meshes-editing-normals-shading>` for any 3D geometry.


Poly
====

.. figure:: /images/modeling_curves_properties_active-spline_panel-poly.png

   Active Spline panel: Poly Spline.

Cyclic U
   See :ref:`Common Options <spline-common-options>`.
Smooth
   See :ref:`Common Options <spline-common-options>`.


.. _bpy.types.Spline.tilt_interpolation:
.. _bpy.types.Spline.radius_interpolation:

Bézier
======

.. figure:: /images/modeling_curves_properties_active-spline_panel-bezier.png
   :align: center

   Active Spline panel: Bézier Spline.

Cyclic U
   See :ref:`Common Options <spline-common-options>`.
Resolution U
   See :ref:`Common Options <spline-common-options>`.
Interpolation Tilt
   Alters how the tilt of a segment is calculated.
Radius
   Alters how the radius of a beveled curve is calculated.
   The effects are easier to see after :ref:`increasing the radius <modeling-curve-radius>`.
Smooth
   See :ref:`Common Options <spline-common-options>`.


.. _bpy.types.Spline.use_bezier_u:
.. _bpy.types.Spline.use_endpoint_u:
.. _bpy.types.Spline.order_u:

NURBS
=====

One of the characteristics of a NURBS object is the *knot vector*.
This is a sequence of numbers used to determine the influence of the control points on the curve.
While you cannot edit the knot vectors directly,
you can influence them through the *Endpoint* and *Bézier* options in the Active Spline panel.
Note that, the *Endpoint* and *Bézier* settings only apply to open NURBS curves.

.. figure:: /images/modeling_curves_properties_active-spline_panel-nurbs.png
   :align: center

   Active Spline: NURBS Spline.

.. _modeling-curve-knot:

Cyclic U
   See :ref:`Common Options <spline-common-options>`.
Bézier U
   Makes the NURBS curve act like a Bézier curve.
   The NURBS control points act like *Free* handles of Bézier curve.
Endpoint U
   Makes the curve contact the end control points.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_active-spline_nurbs-default.png

             Default NURBS curve.

        - .. figure:: /images/modeling_curves_properties_active-spline_nurbs-endpoint.png

             A NURBS curve with Endpoint enabled.

.. _modeling-curve-order:

Order U
   The order of the NURBS curve determines the area of influence of the control points over the curve.
   Higher order values means that a single control point has a greater
   influence over a greater relative proportion of the curve.
   The valid range of *Order* values is 2-6 depending on the number of control points present in the curve.

   .. list-table::

      * - .. figure:: /images/modeling_curves_properties_active-spline_nurbs-default.png

             NURBS curves with orders of 4.

        - .. figure:: /images/modeling_curves_properties_active-spline_nurbs-order.png

             NURBS curves with orders of 2.

Resolution U
   See :ref:`Common Options <spline-common-options>`.
Smooth
   See :ref:`Common Options <spline-common-options>`.
