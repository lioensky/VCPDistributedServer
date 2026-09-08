
*******
Falloff
*******

The *Falloff* is a curve that determines how the strength of the brush decreases
with increasing distance from the center. You can set up a custom curve or choose
a predefined one.

.. figure:: /images/sculpt-paint_brush_falloff_brush-curve.png

   Brush falloff example.

.. _bpy.ops.brush.curve_distance_falloff_preset:
.. _bpy.types.Brush.curve:

Curve Preset
   Custom
      Shows a :doc:`/interface/controls/templates/curve` for configuring a custom falloff.
      The left side of the curve corresponds to the center of the brush while the right side
      corresponds to the edge.


   Predefined
      The predefined falloff curves look as follows:

      .. list-table:: Built-in falloff curves

         * - .. figure:: /images/sculpt-paint_brush_falloff_smooth.png

                Smooth

           - .. figure:: /images/sculpt-paint_brush_falloff_smoother.png

                Smoother

           - .. figure:: /images/sculpt-paint_brush_falloff_sphere.png

                Sphere

         * - .. figure:: /images/sculpt-paint_brush_falloff_root.png

                Root

           - .. figure:: /images/sculpt-paint_brush_falloff_sharp.png

                Sharp

           - .. figure:: /images/sculpt-paint_brush_falloff_linear.png

                Linear

         * - .. figure:: /images/sculpt-paint_brush_falloff_sharper.png

                Sharper

           - .. figure:: /images/sculpt-paint_brush_falloff_invsquare.png

                Inverse Square

           - .. figure:: /images/sculpt-paint_brush_falloff_constant.png

                Constant

.. _bpy.types.Brush.falloff_shape:

Falloff Shape
   Determines how the falloff distance is calculated.

   :Sphere:
      The falloff is calculated using a sphere in three-dimensional world space.
      If two points on the mesh appear near each other in the 3D Viewport but are
      far away in the world, painting one will not affect the other.
   :Projected:
      The falloff is calculated using a circle in two-dimensional screen space.
      If two points on the mesh appear near each other in the 3D Viewport, painting
      one will also affect the other, no matter their distance in the world.

   Texture Paint Mode does not have this option -- it always uses *Projected*.

.. _bpy.types.ImagePaint.use_normal_falloff:
.. _bpy.types.Brush.use_frontface_falloff:

Normal Falloff / Front-Face Falloff
   Weakens the brush strength for faces whose normal points towards the screen edges
   instead of the camera.

   This feature is not available in Sculpt Mode.

   .. _bpy.types.ImagePaint.normal_angle:

   Angle
      The minimum angle between the face normal and the viewing direction for the
      falloff to start.
