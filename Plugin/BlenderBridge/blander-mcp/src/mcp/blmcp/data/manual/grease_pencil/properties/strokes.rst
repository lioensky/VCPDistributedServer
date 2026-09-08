
********
Settings
********

General settings for Grease Pencil strokes.

.. figure:: /images/grease-pencil_properties_strokes_panel.png
   :align: center

   Settings panel.

.. _bpy.types.GreasePencil.stroke_depth_order:

Stroke Depth Order
   Defines how the strokes are ordered in 3D space (for objects not displayed *In Front*).

   :2D Layers:
      The Strokes drawing order respect the order of the 2D layers list (top to bottom)
      and ignores the real position of the strokes in 3D space.
      See :doc:`2D Layers </grease_pencil/properties/layers>` for more information.
   :3D Location:
      The strokes drawing order is based on the stroke location in 3D space.

   .. list-table::

      * - .. figure:: /images/grease-pencil_properties_strokes_depth-order-2d.png
            :width: 320px

            Blue, Green and Red strokes in three different layers using 2D Layers depth order.

        - .. figure:: /images/grease-pencil_properties_strokes_depth-order-3d.png
             :width: 320px

             Blue, Green and Red strokes in three different layers using 3D Location depth order.
