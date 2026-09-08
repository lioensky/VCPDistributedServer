
*************
Startup Scene
*************

After closing the :doc:`splash screen </interface/window_system/splash>`,
the startup scene is displayed in the 3D Viewport (if no other blend-file was loaded).
This startup scene can be :ref:`customized <startup-file>`.

.. figure:: /images/editors_3dview_startup-scene_labels.png

   The startup scene.


Elements
========

Cube
   The gray cube in the center of the scene is a :doc:`mesh </modeling/meshes/index>` object.
   Its orange outline indicates that it's selected.
   The orange dot in the center is its :doc:`Origin </scene_layout/object/origin>`,
   which indicates its precise location.

Light
   The set of concentric black circles is a :doc:`light source </render/lights/light_object>`
   illuminating the cube.

Camera
   The pyramid with a big triangle above it is the :doc:`camera </render/cameras>`,
   which is used as the point of view for rendering.
3D Cursor
   The :doc:`3D cursor </editors/3dview/3d_cursor>`, a cross with a red-and-white circle,
   determines where newly added objects are placed and can also serve as a
   transformation :doc:`pivot point </editors/3dview/controls/pivot_point/index>`.
Grid Floor
   The gray lines forming a floor mark the zero height of the world.
   The red and green lines are the axes of the world coordinate system.
   They meet at the world origin, which is also where the origin of the *Cube* is located.
   The Grid Floor settings are in the :doc:`Viewport Overlays </editors/3dview/display/overlays>` popover.


Text Info
---------

The top left corner of the viewport shows various bits of information --
see :doc:`Viewport Overlays </editors/3dview/display/overlays>` for details.
