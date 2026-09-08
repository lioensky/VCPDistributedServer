.. index:: Geometry Nodes; Scene Time
.. _bpy.types.GeometryNodeInputSceneTime:

.. --- copy below this line ---

***************
Scene Time Node
***************

.. figure:: /images/node-types_GeometryNodeInputSceneTime.webp
   :align: right
   :alt: Scene Time node.

The *Scene Time* node outputs the current time in the scene's animation in units of seconds or frames.


Inputs
======

This node has no inputs.


Outputs
=======

Seconds
   Current scene time in seconds.

Frames
   Current scene frame.
   As an input in geometry nodes, this output may also output non-round numbers,
   in order to support higher quality :doc:`motion blur </render/eevee/render_settings/motion_blur>`.
