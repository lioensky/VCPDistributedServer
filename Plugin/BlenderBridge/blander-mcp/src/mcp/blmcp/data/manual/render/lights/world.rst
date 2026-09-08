.. _bpy.types.World:

*****************
World Environment
*****************

.. figure:: /images/render_lights_world_environment-lighting.jpg
   :align: right

   Lighting with an HDR image.

The world defines the environment that the scene is in.
The surface shader sets the background and environment lighting,
either as a fixed color, sky model or HDRI texture.
With volume shaders the entire scene can be covered in mist or other volumetric effects.


Surface
=======

.. reference::

   :Panel:     :menuselection:`World --> Surface`

The surface shader defines the light emission from the environment into the scene.
The world surface is rendered as if it is very distant from the scene,
and as such there is no two-way interacting between objects in the scene and the environment,
only light coming in. The only shader accepted is the Background node with a color input and
strength factor for the intensity of the light.


Image Based Lighting
--------------------

For image based lighting,
use the Environment Texture node rather than the Image Texture node for correct mapping.
This supports *Equirectangular* (also known as latitude/longitude) for environment maps,
and *Mirror Ball* mapping for converting photos of mirror balls to environment maps.


Volume
======

.. reference::

   :Panel:     :menuselection:`World --> Volume`

A volume shader can be applied to the entirely world, filling the entire space.

Currently this is most useful for night time or other dark scenes,
as the world surface shader or sun lights will have no effect if a volume shader is used.
This is because the world background is assumed to be infinitely far away,
which is accurate enough for the sun for example.
However, for modeling effects such as fog or atmospheric scattering,
it is not a good assumption that the volume fills the entire space,
as most of the distance between the sun and the earth is empty space.
For such effects it is be better to create a volume object surrounding the scene.
The size of this object will determine how much light is scattered or absorbed.


Viewport Display
================

.. reference::

   :Panel:     :menuselection:`World --> Viewport Display`

.. _bpy.types.World.color:

Color
   The color to render the 3D Viewport background when choosing
   :ref:`World Background <bpy.types.View3DShading.background_type>`.
