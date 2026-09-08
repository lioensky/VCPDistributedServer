.. _ui-curve-widget:

************
Curve Widget
************

.. figure:: /images/interface_controls_templates_curve_ui.png
   :align: right

   Curve widget.

This widget is used to edit two types of curves:

- *Profile* curves that simply describe a two-dimensional shape.
- *Mapping* curves that map an input value on the X axis to an output value on the Y axis.

The available options are slightly different depending on this type. Also, unlike profile curves,
mapping curves can't have overhang: each X value must correspond to exactly one Y value.

Control Points
==============

Like all curves in Blender, the curve in this widget is defined using *control points*.

Add
   Click :kbd:`LMB` anywhere on the curve where there is not already a control point.
Move
   Drag the point with :kbd:`LMB`.
Remove
   Select the point and click the :bl-icon:`x` button at the bottom right.
   Alternatively, press :kbd:`X`.

Controls
========

:bl-icon:`zoom_in` Zoom In
   Zoom in to show more details and provide more accurate control.
   To navigate around the curve while zoomed in, click and drag with :kbd:`LMB` in an empty area.

:bl-icon:`zoom_out` Zoom Out
   Zoom out to show fewer details and view the curve as a whole.
   You cannot zoom out further than the clipping region (see *Clipping* below).

:bl-icon:`arrow_leftright` Reverse Path :guilabel:`Profile Curves`
   Mirror the curve around the diagonal.

:bl-icon:`clipuv_hlt` Clipping Options :guilabel:`Mapping Curves`
   Use Clipping
      Force curve points to stay between the specified values.
   Min X/Y and Max X/Y
      Set the minimum and maximum bounds of the curve points.

:bl-icon:`downarrow_hlt` Specials
   Reset View
      Zoom the view all the way out.

   Extend Options :guilabel:`Mapping Curves`
      Controls how the curve is extended before the first point and after the last point.

      Extend Horizontal
         Causes the curve to "go flat."

      Extend Extrapolated
         Causes the curve to maintain its direction.

      .. list-table::

         * - .. figure:: /images/interface_controls_templates_curve_extend-horizontal.png

                Extend Horizontal.

           - .. figure:: /images/interface_controls_templates_curve_extend-extrapolate.png

                Extend Extrapolated.

   Reset Curve
      Resets the curve to the default (removes all added points).

.. _ui-curve-widget-handle-type:

Handle Type
   The handle type of the selected control point.
   This determines the shape of the curve segments around it.

   :bl-icon:`handle_auto` Auto Handle
      Results in a smooth curve without the need to manually set up handles.
   :bl-icon:`handle_vector` Vector Handle
      Results in straight lines and a sharp corner.
   :bl-icon:`handle_free` Free Handle :guilabel:`Profile Curves`
      Shows freely movable Bézier handles that are independent of each other.
      This can result in a sharp corner at the control point.
   :bl-icon:`handle_aligned` Aligned Free Handles :guilabel:`Profile Curves`
      Shows freely movable Bézier handles that are locked together to always point in opposite directions.
      This ensures the curve is always smooth at the control point.
   :bl-icon:`handle_autoclamped` Auto Clamped Handle :guilabel:`Mapping Curves`
      Like *Auto Handle*, but also prevents overshoot.

   .. list-table::

      * - .. figure:: /images/interface_controls_templates_curve_handle-vector.png

             Vector Handles.

        - .. figure:: /images/interface_controls_templates_curve_handle-auto.png

             Auto Handles.

        - .. figure:: /images/interface_controls_templates_curve_handle-auto-clamped.png

             Auto Clamped Handles.

X, Y
   The coordinates of the selected control point.
:bl-icon:`x` Delete :kbd:`X`
   Remove the selected control point. The first and last points cannot be deleted.
Copy/Paste :kbd:`Ctrl-C`, :kbd:`Ctrl-V`
   The whole curve can be copied from one Curve Widget to another by hovering over
   it and pressing :kbd:`Ctrl-C`, :kbd:`Ctrl-V`.

Presets :guilabel:`Brush Curve Widgets Only`
   A number of preset curves that the curve can be set to.
   The exact shape depends on whether the default curve for the property has a positive
   or negative slope.

   .. list-table:: Custom Preset Types with Positive Slope.

      * - .. figure:: /images/curve_smooth_positive_preset.png

               Smooth

        - .. figure:: /images/curve_round_positive_preset.png

               Round

        - .. figure:: /images/curve_root_positive_preset.png

               Root

      * - .. figure:: /images/curve_sharp_positive_preset.png

               Sharp

        - .. figure:: /images/curve_linear_positive_preset.png

               Linear

        - .. figure:: /images/curve_constant_preset.png

               Constant

   .. list-table:: Custom Preset Types with Negative Slope.

      * - .. figure:: /images/curve_smooth_negative_preset.png

               Smooth

        - .. figure:: /images/curve_round_negative_preset.png

               Round

        - .. figure:: /images/curve_root_negative_preset.png

               Root

      * - .. figure:: /images/curve_sharp_negative_preset.png

               Sharp

        - .. figure:: /images/curve_linear_negative_preset.png

               Linear

        - .. figure:: /images/curve_constant_preset.png

               Constant
