.. _bpy.types.ViewLayer.use_freestyle:
.. _bpy.types.FreestyleSettings:

*********
Freestyle
*********

.. reference::

   :Panel:     :menuselection:`Properties --> View Layer --> Freestyle`

There is only one view map per view layer. It controls the edge detection parameters.
Freestyle can be enabled/disabled per View Layer by toggling the checkbox in the panel header.

.. figure:: /images/render_freestyle_view-layer_freestyle-panel.png
   :align: center

   View Layer: Freestyle panel.

.. _bpy.types.FreestyleSettings.mode:

Control Mode
   Which detected edges are actually rendered, and how, can be controlled either through:

   :Parameter Editor Mode:
      Lines are rendered via parameters defined in a user-friendly interface
      to define and control Line Sets and line styles.

      A view map (hence a view layer) can have multiple Line Sets,
      and each line set is linked to one line style.
   :Python Scripting Mode:
      Lines are rendered via :doc:`Python scripting </render/freestyle/python>`, powerful but complex.

.. _bpy.types.FreestyleSettings.use_view_map_cache:

View Map Cache
   An option to reuse a previously computed view map for subsequent rendering.
   The cache is automatically updated when the mesh geometry of the input 3D scene has been changed.

   This functionality offers a major performance boost for Freestyle animation rendering
   when the camera-space mesh geometry is static, as well as for repeated still renders
   with updates of line stylization options.

   Although the *View Map Cache* checkbox is a view layer option,
   the cache memory is shared by all view layers and scenes.
   This means that if Freestyle is used for two or more view layers
   (possibly in different scenes through the Compositor),
   then the cached view map for one view layer is replaced by a new view map
   for another view layer and hence no performance gain is expected.

.. _bpy.types.FreestyleSettings.as_render_pass:

As Render Pass
   Freestyle lines will not immediately be visible on top of the render image.
   Instead, Freestyle lines are rendered as a :doc:`Render Pass </render/layers/passes>`
   which can be composited with the rendered image with an Alpha Over node.


Edge Detection
==============

.. _bpy.types.FreestyleSettings.crease_angle:

Crease Angle
   If two adjacent faces form an angle less than the defined *Crease Angle*,
   the edge between them will be rendered when using *Crease* edge type selection in a line set.
   The value also affects *Silhouette* edge type selection.

.. _bpy.types.FreestyleSettings.use_culling:

Culling
   Ignore the edges that are out of view.
   (Saves some processing time and memory, but may reduce the quality of the result in some cases.)

.. _bpy.types.FreestyleSettings.use_smoothness:

Face Smoothness
   Takes *Smooth Shading* into account for edges calculation.

.. _bpy.types.FreestyleSettings.sphere_radius:

Sphere Radius
   Affects the calculation of curvatures for *Ridge*, *Valley*
   and *Suggestive Contour* edge type selection in a line set.
   The curvature at each vertex is computed by averaging the shape
   of the surface within the specified radius.
   Increasing the value reduces noise and detail.

.. _bpy.types.FreestyleSettings.kr_derivative_epsilon:

Kr Derivative Epsilon
   Controls the threshold on the minimum rate of change of curvature used to filter the output
   of the *Suggestive Contour* edge type selection. Increasing the value reduces the amount of
   rendered lines, starting from smoother areas of the object (further information in
   `this PDF <https://archive.blender.org/wiki/2015/index.php/File:Manual-2.6-Render-Freestyle-
   PrincetownLinestyle.pdf>`__).
