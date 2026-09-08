.. _bpy.types.LightProbeSphere:

******************
Light Probe Sphere
******************

A light probe sphere records the light incoming from many directions at a single location.

They are used for smooth and semi-rough reflections.
Sphere probes smoothly blend to light probe volume lighting for completely diffuse reflections.

If *Raytracing* is turned on, they are used as a fallback if a ray misses.

.. note::

   In both usages, the light probe spheres are shadowed by light probe volume.
   This is done in order to reduce light leaking in shadowed areas and reduce the need to
   setup more light probe spheres.

Adjusting their resolution is done inside the :doc:`Scene data </render/eevee/scene_settings>` panel.

The world also has an internal light probe sphere with a resolution that can be adjusted
in the :doc:`World data </render/eevee/world_settings>` panel.


Properties
==========

.. reference::

   :Panel:     :menuselection:`Object Data --> Probe`

.. _bpy.types.LightProbeSphere.influence_type:

Type
   Shape of the influence volume. Can be set to Sphere or Box.

Radius / Size
   A probe object only influences the lighting of nearby surfaces.
   This influence zone is defined by the size parameter and object scaling.

.. _bpy.types.LightProbeSphere.falloff:

Falloff
   Percentage of the influence distance in which the influence of a probe fades linearly.


Capture
-------

.. note::

   In the viewport, capture only happens if an update is detected on the light probe data or position.
   For renders, the capture happens at the start of each frame.

.. _bpy.types.LightProbeSphere.clip_end:

Clipping Start, End
   Define the near and far clip distances when capturing the scene.


.. _bpy.types.LightProbeSphere.use_custom_parallax:
.. _bpy.types.LightProbeSphere.parallax_type:
.. _bpy.types.LightProbeSphere.parallax_distance:

Custom Parallax
---------------

.. reference::

   :Panel:     :menuselection:`Object Data --> Custom Parallax`

By default, the influence volume is also the parallax volume.
The parallax volume is a volume on which the recorded light is projected.
It should roughly fit it surrounding area. In some cases it may be better to
adjust the parallax volume without touching the influence parameters.
In this case, enable the *Custom Parallax* and
change the shape and radius of the parallax volume independently.


Viewport Display
----------------

Data
   Show the captured light using a reflective sphere of the given size.

Clipping
   Show the clipping distance in the 3D Viewport.

Influence
   Show the influence bounds in the 3D Viewport. The inner sphere is where the falloff starts.

.. _bpy.types.LightProbeSphere.show_parallax:

Parallax
   Show the *Custom Parallax* shape in the 3D Viewport.
