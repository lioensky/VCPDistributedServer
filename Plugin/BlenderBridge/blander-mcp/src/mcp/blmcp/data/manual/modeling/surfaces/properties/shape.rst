
*****
Shape
*****

.. reference::

   :Editor:    Properties
   :Mode:      Object Mode, Edit Mode
   :Panel:     :menuselection:`Object Data --> Shape`

.. figure:: /images/modeling_surfaces_properties_shape_resolution-panel.png
   :align: center

   Shape panel.

.. _bpy.types.Curve.resolution_v:

Resolution Preview U/V
   The density of the generated surface mesh in the 3D Viewport. The higher this number, the more vertices
   there will be and the smoother the surface will look.
Render U/V
   The density of the generated surface mesh in the render. If a number is 0, the corresponding number
   from *Resolution Preview* will be used instead.

   .. list-table::

      * - .. figure:: /images/modeling_surfaces_properties_shape_resolution-1x1-wire.png

             Resolution 1×1.

        - .. figure:: /images/modeling_surfaces_properties_shape_resolution-3x3-wire.png

             Resolution 3×3.

.. seealso::

   The preview resolution can also be configured for each individual surface within a Surface object.
   See the :doc:`/modeling/surfaces/properties/active_spline` panel in the Sidebar.
