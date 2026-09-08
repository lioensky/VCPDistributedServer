.. _3dview-camera-navigate:

***********
Camera View
***********

.. figure:: /images/editors_3dview_navigate_camera-view_example.png

   Demonstration of camera view.

The Camera view shows the current scene from the active camera's viewpoint.

The Camera view can be used to virtually compose shots and preview how the scene will look when rendered.
The rendered image will contain everything within the dashed frame.

.. seealso::

   :doc:`Camera Settings </render/cameras>` for details on how camera settings are used for display and rendering.

.. hint::

   While in camera view, you can select the camera by clicking the dashed frame
   (assuming the camera object isn't hidden).


.. _bpy.ops.view3d.view_camera:

Viewing the Active Camera
=========================

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`View --> Cameras --> Active Camera`, :menuselection:`View --> Viewpoint --> Camera`
   :Shortcut:  :kbd:`Numpad0`

This switches the view to the active camera.


.. _bpy.ops.view3d.object_as_camera:

Setting the Active Camera
=========================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`View --> Cameras --> Set Active Object as Camera`
   :Shortcut:  :kbd:`Ctrl-Numpad0`

.. figure:: /images/editors_3dview_navigate_camera-view_cameras.png

   Active camera (left) displayed with a solid triangle above it.

This sets the current active object as the active camera and switches to the camera view.

The active camera is the one that will be used for rendering,
and which you'll look through when choosing camera view.

Another way of setting the active camera is through the *Scene* tab of the
:doc:`Properties </editors/properties_editor>`.

.. note::

   The active camera is normally defined on the scene level, so that it's the same
   across all 3D Viewports. However, it's also possible to make a camera
   the active one within one Viewport only.
   See :ref:`Local Camera <bpy.types.SpaceView3D.use_local_camera>`.


Animated Camera Switching
-------------------------

While a scene contains only one camera by default, it's possible to have multiple.
You can then bind the cameras to specific time points in your animation
to create jump cuts showing different viewpoints.
See :ref:`Animating Cameras <bpy.ops.marker.camera_bind>`.


.. _bpy.ops.view3d.view_center_camera:

Frame Camera Bounds
===================

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`View --> Cameras --> Frame Camera Bounds`
   :Shortcut:  :kbd:`Home`

Centers the camera view inside the 3D Viewport's screen area
and resizes the view to fit within the area's bounds.


.. _bpy.ops.view3d.zoom_camera_1_to_1:

Zoom Camera 1:1
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`View --> Navigation --> Zoom Camera 1:1`

Zooms the view so that the camera frame has the exact same size
as the output resolution. This allows you to preview exactly how large
objects will be in the rendered image/animation.


Camera Positioning
==================

There are several different ways to position the camera in your scene.
Some of them are explained below.

.. hint::

   The active "camera" might be any kind of object,
   meaning these actions can also be used to position and aim a light for example.


.. _bpy.ops.view3d.camera_to_view:

Align Active Camera to View
---------------------------

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`View --> Align View --> Align Active Camera to View`
   :Shortcut:  :kbd:`Ctrl-Alt-Numpad0`

Moves and rotates the camera so it perfectly matches your current viewport view.


Camera Navigation
-----------------

By enabling :ref:`Lock Camera to View <bpy.types.SpaceView3D.lock_camera>` in
:menuselection:`Sidebar --> View` and switching to camera view or toggle the lock navigation gizmo button
when in camera view, the camera will become "glued" to the view and follow it around as you navigate.

.. seealso::

   :ref:`Fly/Walk Navigation <3dview-fly-walk>` for first person navigation that moves the active camera too.


Roll, Pan, Dolly, and Track
---------------------------

To perform these camera moves, the camera must first be selected so transform operations apply to it.
The following actions also assume that you are in camera view.
Having done so, you can now manipulate the camera using the same tools that are used to transform any object:

Roll
   Press :kbd:`R` to enter object rotation mode. The default will be to rotate the camera along its local Z axis
   (the axis orthogonal to the camera view), which is the definition of a camera "roll".
Vertical Pan or Pitch
   This is just a rotation along the local X axis. Press :kbd:`R` to enter object rotation mode,
   then :kbd:`X` twice. (The first press selects the *global* axis, the second the *local* axis.
   This works with any axis; see :doc:`Axis Locking </scene_layout/object/editing/transform/control/axis_locking>`).
Horizontal Pan or Yaw
   This corresponds to a rotation around the camera's local Y axis.
   Press :kbd:`R`, then :kbd:`Y` twice.
Dolly
   To dolly the camera, press :kbd:`G` then :kbd:`MMB` (or :kbd:`Z` twice).
Sideways Tracking
   Press :kbd:`G` and move the mouse (you can use :kbd:`X` or :kbd:`Y` twice
   to get purely horizontal or vertical tracking).
