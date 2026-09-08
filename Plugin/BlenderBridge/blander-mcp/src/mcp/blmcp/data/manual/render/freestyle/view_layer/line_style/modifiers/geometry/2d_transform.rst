.. _bpy.types.LineStyleGeometryModifier_2DTransform:

************
2D Transform
************

The *2D Transform* modifier applies two-dimensional scaling and/or rotation to
the stroke backbone geometry. Scale is applied before rotation.

Pivot
   The center (pivot point) of these 2D transformations can be:

   :Stroke Center: The median point of the stroke.
   :Stroke Start: The beginning point of the stroke.
   :Stroke End: The end point of the stroke.
   :Stroke Point Parameter:
      The *Stroke Point Parameter* factor controls where along the stroke the pivot point is
      (start point if set to 0.0; end point if set to 1.0).
   :Absolute 2D Point:
      The *Pivot X* and *Y* values define the position of the pivot point in the final render
      (from the bottom left corner).

      .. important::

         Currently, you have to take into account the *real* render size,
         i.e. resolution **and** resolution percentage.

Scale X, Y
   The scaling factors, in their respective axes.

Rotation Angle
   The rotation angle.

.. figure:: /images/render_freestyle_parameter-editor_line-style_modifiers_geometry_2d-transform_example.png
   :width: 50%
   :align: center

   2D Transform modifier
   (`blend-file <https://archive.blender.org/wiki/2015/index.php/File:Toycar_Three_Contours.zip>`__).
