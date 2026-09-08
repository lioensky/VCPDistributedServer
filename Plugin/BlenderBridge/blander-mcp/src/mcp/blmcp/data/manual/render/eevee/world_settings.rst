**************
World Settings
**************

The world environment can emit light, ranging from a single solid color
to arbitrary textures.

In EEVEE, the world lighting contribution is stored into an internal
:doc:`Light Probe </render/eevee/light_probes/index>`.
This makes the lighting less precise than Cycles.

EEVEE considers the world lighting contribution as indirect lighting
whereas Cycles considers it as direct lighting.

.. _bpy.types.WorldMistSettings:

Mist Pass
=========

.. reference::

   :Panel:     :menuselection:`World --> Mist Pass`

.. note::

   The mist pass must be enabled in the View Layer tab
   of the :doc:`Properties Editor </editors/properties_editor>`
   before the settings below are available in the World tab.

Mist can greatly enhance the illusion of depth in your rendering. To create mist,
Blender generates a render layer with a depth map ranging between 0.0 and 1.0
that can be used in the Compositor to generate a mist effect.

.. _bpy.types.WorldMistSettings.start:

Start
   The distance from the camera at which the mist starts to fade in.

.. _bpy.types.WorldMistSettings.depth:

Depth
   The distance from *Start* of the mist, that it fades in over.
   Objects further from the camera than *Start + Depth* are completely hidden by the mist.

.. _bpy.types.WorldMistSettings.falloff:

Falloff
   The curve function that controls the rate of change of the mist's strength further and further into the distance.

   :Quadratic:
      Uses the same calculation as light falloff (:math:`1\over{x^2}`) and provides the smoothest
      transition from transparent (0.0) to opaque (1.0).
   :Linear: Has a steeper start than quadratic (:math:`1\over{x}`).
   :Inverse Quadratic:
      Has the steepest start (:math:`1\over{\sqrt{x}}`) and approaches 1.0 faster than the other two functions.

.. tip::

   A visualization can be activated in the :menuselection:`Camera --> Viewport Display` panel.

.. figure:: /images/render_cycles_world-settings_mist-example1-BI.jpg

   Mist example
   (`blend-file <https://archive.blender.org/wiki/2015/index.php/File:25-Manual-World-Mist-Example1.blend>`__).


Settings
========

.. reference::

   :Panel:     :menuselection:`World --> Light Probe`


Light Probe
-----------

.. _bpy.types.World.probe_resolution:

Resolution
   The resolution used to store the light from the world.
   This is equivalent to the resolution for light probe spheres.

.. seealso::

   :doc:`Light Probe Sphere </render/eevee/light_probes/sphere>`.

Sun
---

EEVEE can separate the light from intense light sources
(e.g. a sun from an outdoor :abbr:`HDRI (High Dynamic Range Imaging)`) and
replace them with a sun light. This increases the quality of the lighting as the internal light probes
alone cannot reproduce this type of lighting with enough precision.

Threshold
   If non-zero, the maximum value for world contribution that will be recorded inside the world light probe.
   The excess contribution is converted to a sun light.
   This reduces the light bleeding caused by very bright light sources.
   A value of zero will disable this feature and all lighting will be stored inside the internal light probes.

Angle
   Angular diameter of the extracted sun light as seen from the Earth.

Use Shadow
   Enable shadow casting on the extracted sun light.

.. seealso::

   The shadow properties control the extracted sun shadows.
   They are exactly the same as for a sun light object.
   :doc:`Light Properties </render/eevee/light_settings>`.
