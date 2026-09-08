
*************
Tool Settings
*************

Options
=======

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Header:    :menuselection:`Sidebar --> Tool --> Options`


Transform
---------

.. _bpy.types.ToolSettings.use_transform_data_origin:
.. _bpy.types.ToolSettings.use_transform_pivot_point_align:

Affect Only
   Origins :kbd:`Ctrl-Period`
      Directly transforms the object's :doc:`origin </scene_layout/object/origin>`.
      This only works for objects with data which can be transformed;
      i.e. it will not work on object lights.

      When enabled, the object axes are displayed.

      Take care using this option since it transforms the object-data which may cause linked
      duplicates to be moved unintentionally.

      .. hint::

         Changing the object location and the object-data may impact
         modifiers, constraints and keyframe animation.

         If you are only temporarily setting the pivot point,
         use the :ref:`3D cursor <editors-3dview-3d_cursor>` instead.

   Locations
      Changes the position of the object's origin relative to another point during transformation.
      In other words, the pivot point and the origin cannot share the same location.
      This will not affect the object local transforms, just its position in world space.

      In the examples below, a comparison of the scaling and rotation of objects,
      when *Location* is enabled (middle) and disabled (right).

      .. figure:: /images/scene-layout_object_tools_tool-settings_rotate.png

         Rotation example.

      .. figure:: /images/scene-layout_object_tools_tool-settings_scale.png

         Scaling example.

   Parents
      Transforms :doc:`Parent Objects </scene_layout/object/editing/parent>`
      while leaving their children objects unaffected.
