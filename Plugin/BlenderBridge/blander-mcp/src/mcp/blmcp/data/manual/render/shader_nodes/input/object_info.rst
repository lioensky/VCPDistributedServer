.. _bpy.types.ShaderNodeObjectInfo:

****************
Object Info Node
****************

.. figure:: /images/node-types_ShaderNodeObjectInfo.webp
   :align: right
   :alt: Object Info Node.

The *Object Info* node gives information about the object instance.
This can be useful to give some variation to a single material assigned to multiple instances,
either manually controlled through the object index, based on the object location,
or randomized for each instance. For example a Noise texture can give random colors or a Color
Ramp can give a range of colors to be randomly picked from.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Location
   Location of the object in world space.
Color
   Object color, same as *Color* in the :menuselection:`Properties --> Object Properties --> Viewport Display`.
Alpha
   The :term:`Alpha Channel` component of the object's viewport display color (see the *Color* output for
   more details).
Object Index
   Object pass index, same as *Pass Index*
   in the :menuselection:`Properties --> Object Properties --> Relations`.
Material Index
   Material pass index, same as *Pass Index*
   in the :menuselection:`Properties --> Material --> Settings`.
Random
   Random number unique to a single object instance. Output is a Float between 0.0 and 1.0

.. note::

   Note that this node only works for material shading nodes;
   it does nothing for light and world shading nodes.


Example
=======

.. figure:: /images/render_shader-nodes_input_object-info_example.png
   :width: 640px

.. figure:: /images/render_cycles_render-settings_motion-blur_example-cubes.jpg
   :width: 640px

   `Example blend-file <https://archive.blender.org/wiki/2015/uploads/0/03/Blender2.65_motion_blur.blend>`__.
