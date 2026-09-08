
*******
Filters
*******

Filters are tools which provide an alternative way of sculpting, because they do not rely on a brush radius.
Instead they will affect any vertices that are visible and not masked.

.. figure:: /images/sculpt-paint_filter_example.png

The strength is controlled by click & dragging from left to right.
The position of the cursor can be used to only affect specific areas, if auto-masking is used.

Many of the same brush types are also available as a filter type.
This way much of the mesh can simultaneously be smoothed, colored or have some cloth simulation applied.

.. tip::

   A common example for using the :doc:`Mesh Filter </sculpt_paint/sculpting/tools/mesh_filter>`
   is to smooth everything after increasing the resolution with
   the :doc:`Voxel Remesher </sculpt_paint/sculpting/tool_settings/remesh>`
   or :doc:`Dyntopo </sculpt_paint/sculpting/tool_settings/dyntopo>`.

.. seealso::

   More information at :doc:`Mesh Filter </sculpt_paint/sculpting/tools/mesh_filter>`,
   :doc:`Cloth Filter </sculpt_paint/sculpting/tools/cloth_filter>`,
   :doc:`Color Filter </sculpt_paint/sculpting/tools/color_filter>`
   and :ref:`bpy.ops.sculpt.mask_filter`.
