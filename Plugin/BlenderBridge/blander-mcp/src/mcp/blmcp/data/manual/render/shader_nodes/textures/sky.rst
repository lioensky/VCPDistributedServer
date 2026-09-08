.. _bpy.types.ShaderNodeTexSky:

****************
Sky Texture Node
****************

.. figure:: /images/node-types_ShaderNodeTexSky.webp
   :align: right
   :alt: Sky Texture Node.

The *Sky Texture* node generates a procedural sky. It's typically used in combination
with the :doc:`/render/shader_nodes/output/world`.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.


Properties
==========

Sky Type
   Sky model to use.

   Single Scattering
      Improved version of the 1993
      `model <https://www.scratchapixel.com/lessons/procedural-generation-virtual-worlds/simulating-sky/simulating-colors-of-the-sky.html>`__
      by Nishita et al, accounts for single bounces in the atmosphere.
      This is legacy and may be removed in a future version.
   Multiple Scattering
      Based on `this <https://fgarlin.com/blog/spectral-sky/>`__ work by Fernando García Liñán, it is the most
      accurate model as it accounts for multiple bounces of light in the atmosphere.
   Preetham
      Based on the 1999 `paper <https://doi.org/10.1145/311535.311545>`__ by Preetham et al.
      This is legacy and will be removed in a future version.
   Hosek/Wilkie
      Based on the 2012 `paper <https://cgg.mff.cuni.cz/projects/SkylightModelling/>`__ by Hosek and Wilkie.
      This is legacy and will be removed in a future version.

.. note::

   Single and Multiple Scattering skies are very bright by default (hence accurate).
   You can lower the Exposure of the scene in :menuselection:`Properties --> Color Management --> Exposure` to fix
   this.

Sun Direction
   Sun direction vector.

Turbidity
   Atmospheric turbidity.

   - 2: Arctic like
   - 3: clear sky
   - 6: warm/moist day
   - 10: hazy day

Ground Albedo
   Amount of light reflected from the planet surface back into the atmosphere.

Sun Disc :guilabel:`Cycles Only`
   Enable/Disable sun disc lighting.

Sun Size
   Angular diameter of the sun disc (in degrees).

Sun Intensity
   Multiplier for sun disc lighting.

Sun Elevation
   Rotation of the sun from the horizon (in degrees).

Sun Rotation
   Rotation of the sun around the zenith (in degrees).

Altitude
   The distance from sea level to the location of the camera.
   For example, if the camera is placed on a beach then a value of 0 should be used.
   However, if the camera is in the cockpit of a flying airplane then a value of 10 km will be more suitable.

Air
   Density of air molecules.
   A value of 1 corresponds roughly to urban city air, while 0 is no air.

Aerosols
   Density of aerosol particles (water droplets).
   A value of 1 corresponds roughly to urban city aerosols, while 0 is no aerosols.

Ozone
   Density of ozone molecules; useful to make the sky appear bluer.
   A value of 1 corresponds roughly to urban city ozone, while 0 is no ozone.


Outputs
=======

Color
   Texture color output.


Examples
========

.. figure:: /images/render_shader-nodes_textures_sky_example.webp

   Example of lighting with Sky Texture.
