
*******
Sidebar
*******

Item
====

Shows :doc:`Transform </scene_layout/object/editing/transform/introduction>` settings
of the active object.


Tool
====

Shows settings of the active tool and Workspace.


View
====

View Panel
----------

The *View* panel lets you change other settings regarding the 3D Viewport.

.. _bpy.types.SpaceView3D.lens:

Focal Length
   Control the focal length of the 3D Viewport camera.

.. _bpy.types.SpaceView3D.clip_start:
.. _bpy.types.SpaceView3D.clip_end:

Clip Start/End
   Adjust the minimum and maximum distances for geometry to be visible.
   Geometry closer than *Start* or further away than *End* will not be shown.

   .. note::

      In Orthographic view, the viewport uses negative *End* instead of *Start*.

   .. warning::

      A large clipping range will allow you to see both near and far objects,
      but reduces the depth precision resulting in artifacts.

      In some cases, a very large range may cause operations that depend on the depth buffer to become unreliable,
      although this depends on the graphics card and drivers.

      See :ref:`Troubleshooting Depth Buffer Glitches <troubleshooting-depth>` for more information.

.. _bpy.types.SpaceView3D.use_local_camera:
.. _bpy.types.SpaceView3D.camera:

Local Camera
   Allow this 3D Viewport to have its own :doc:`active camera </editors/3dview/navigate/camera_view>`,
   separate from the global active camera that's defined in the scene.
   The selector next to the checkbox lets you choose this camera.

.. _bpy.types.View3DOverlay.show_camera_passepartout:

Passepartout
   Show :ref:`camera passepartout <bpy.types.Camera.show_passepartout>`
   when in :ref:`camera view <bpy.ops.view3d.view_camera>`.

.. _bpy.types.SpaceView3D.use_render_border:

Render Region
   Use the :ref:`Render Region <editors-3dview-navigate-render-region>`.
   Defining the region with :kbd:`Ctrl-B` will automatically enable this option.

   Note that if you're viewing the scene through the active camera, this option has no effect --
   in this case, you instead need to use the checkbox :menuselection:`Output Properties --> Format --> Render Region`
   in the Properties editor. This will affect not just the viewport, but also the final render.


View Lock
^^^^^^^^^

.. _bpy.types.SpaceView3D.lock_object:

Lock to Object
   Lets you select an object to become the point of interest of the viewpoint.
   The view will then orbit around, and zoom towards, that object.
   This option is not available when viewing the scene through the active camera.

.. _bpy.types.SpaceView3D.lock_cursor:

Lock -- To 3D Cursor
   Makes the 3D Cursor the point of interest of the viewpoint.
   This option is only available when *Lock to Object* is not active.

.. _bpy.types.SpaceView3D.lock_camera:

Lock -- Camera to View
   When looking through a camera, the camera becomes "glued" to the view
   and will follow it around as you navigate.
   The camera frame will be outlined with a red dashed line.

.. _bpy.types.RegionView3D.lock_rotation:

Lock -- Rotation
   Prevent changes to the orientation and perspective of the 3D Viewport.

.. hint::

   If the camera is parented to an object, you can choose to enable
   :ref:`Camera Parent Lock <bpy.types.Object.use_camera_lock_parent>`
   in the camera's properties. This will cause viewport navigation to transform
   the camera's root parent rather than the camera itself.


3D Cursor
---------

.. _bpy.types.View3DCursor.location:

Location
   The location of the 3D Cursor.

.. _bpy.types.View3DCursor.rotation_quaternion:
.. _bpy.types.View3DCursor.rotation_euler:
.. _#bpy.types.View3DCursor.rotation_axis_angle:

Rotation
   The rotation of the 3D Cursor.

.. _bpy.types.View3DCursor.rotation_mode:

Rotation Mode
   Method for calculating rotations, additional information can be found
   in the :doc:`manual's appendix </advanced/appendices/rotations>`.

   :Euler:
      Coordinate axes are aligned to the :term:`Euler` axis,
      allowing you to see the discreet XYZ axis underlying the Euler rotation,
      as well as possible :term:`Gimbal Lock`.
   :Axis Angle:
      The X, Y, and Z coordinates define a point relative to the object origin.
      This point and the origin define an axis around the W value defines the rotation.
   :Quaternion:
      X, Y, Z and W correspond to the :term:`Quaternion` components.


.. _bpy.types.SpaceView3D.use_local_collections:

Collections
-----------

The *Collections* panel shows a list of :doc:`collections </scene_layout/collections/index>`
and can be used to control their visibility.
If a collection contains objects, there is a circle to the left of its name.

Local Collections
   Allows setting collection visibility per viewport rather than globally.

Hide in Viewport (eye icon)
   Shows or hides the collection.

You can also "isolate" a collection by clicking its name. This will show the collection
as well as its ancestors and descendants, and hide all other collections.


Annotations
-----------

See :doc:`Annotations </interface/annotate_tool>` for more information.

:doc:`Animation <animation/index>`
==================================

:doc:`Global Transform <animation/copy_global_transform>`
---------------------------------------------------------

.. toctree::
   :hidden:

   animation/index.rst
