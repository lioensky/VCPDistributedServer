
********
Surfaces
********

The surface shader defines the light interaction at the surface of the mesh.
One or more :abbr:`BSDF (Bidirectional Scattering Distribution Function)`\ s specify
if incoming light is reflected back, refracted into the mesh, or absorbed.

Emission defines how light is emitted from the surface,
allowing any surface to become a light source.


Terminology
===========

BSDF
   Stands for Bidirectional Scattering Distribution Function.
   It defines how light is reflected and refracted at a surface.
Reflection
   BSDFs reflect an incoming ray on the same side of the surface.
Transmission
   BSDFs transmit an incoming ray through the surface, leaving on the other side.
Refraction
   BSDFs are a type of *Transmission*, transmitting an incoming ray and
   changing its direction as it exits on the other side of the surface.


BSDF Parameters
===============

A major difference from non-physically-based renderers is that direct light reflection from
lights and indirect light reflection of other surfaces are not decoupled, but rather handled
using a single :abbr:`BSDF (Bidirectional Scattering Distribution Function)`.
This limits the possibilities a bit, but we believe overall it is helpful in creating
consistent-looking renders with fewer parameters to tune.

Roughness
   For the glossy :abbr:`BSDF (Bidirectional Scattering Distribution Function)`\ s,
   the *roughness* parameter controls the sharpness of the reflection, from 0.0 (perfectly sharp)
   to 1.0 (very soft).
