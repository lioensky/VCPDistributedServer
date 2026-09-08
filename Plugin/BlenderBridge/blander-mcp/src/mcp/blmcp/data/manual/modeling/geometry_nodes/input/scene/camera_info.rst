.. index:: Geometry Nodes; Camera Info
.. _bpy.types.GeometryNodeCameraInfo:

****************
Camera Info Node
****************

.. figure:: /images/node-types_GeometryNodeCameraInfo.webp
   :align: right
   :alt: Camera Info node.

The *Camera Info* node outputs the information about the selected camera object.

It can be used to customize geometry based on the camera's parameters,
for example when building camera-based visual effects or aligning geometry with the camera view.


Inputs
======

Camera
   The camera object to retrieve information from.

   To get the active camera, use the :doc:`/modeling/geometry_nodes/input/scene/active_camera`.


Outputs
=======

Projection Matrix
   A 4x4 matrix that represents the camera's projection transform, combining focal length,
   sensor size, shift, and clipping range. Can be used to project 3D coordinates into screen space.

Focal Length
   The focal length of the camera in millimeters. Affects field of view in perspective cameras.

Sensor
   The physical size of the camera sensor in millimeters, as a 2D vector (X and Y dimensions).
   This value is influenced by the sensor fit properties.

Shift
   Horizontal and vertical shift of the camera view, expressed as a 2D vector.

Clip Start
   The near clipping distance of the camera.

Clip End
   The far clipping distance of the camera.

Focus Distance
   The distance from the camera to the focus point, in Blender units.
   Typically used for depth of field calculations.

Is Orthographic
   A boolean output that is *true* when the camera is in orthographic mode, and *false* when in perspective mode.

Orthographic Scale
   The orthographic scale used when the camera is set to orthographic mode.
   Controls the size of the view area instead of using focal length.
