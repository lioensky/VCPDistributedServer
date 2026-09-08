.. _bpy.types.LightProbePlane:

*****************
Light Probe Plane
*****************

A light probe plane records the light incoming from a single direction for all visible points on a plane.
The specular reflection direction is the only one currently available.

This type of light probe is suited to smooth planar surfaces.

Each visible planar light probe increases the render time as the scene needs to be rendered for
each of them.

Light probe planes only work when the ray tracing method is set to ``Screen-Trace``.
When enabled, they accelerate the tracing process and complete the missing data from the screen space ray tracing.

.. note::

   Reflections and volumetrics are not supported inside Light probe planes.


Placement
=========

If Backface Culling is not enabled, snapping the light probe plane to the planar surface
will effectively capture the underside of the surface.

You can manually move the light probe plane above the surface enough for it to not appear in the capture.
Alternatively you can disable the light probe visibility in the object visibility panel.


Properties
==========

.. reference::

   :Panel:     :menuselection:`Object Data --> Probe`

.. _bpy.types.LightProbe.influence_distance:

Distance
   A probe object only influences the lighting of surfaces inside its influence zone.
   This influence zone is defined by the distance parameter and the object's scale.

   For light probe planes, the influence distance is the distance from the plane.
   Only surfaces whose normals are aligned with the Reflection Plane will receive the captured reflection.


Capture
-------

Clipping Offset
   Define how far below the plane the near clip is when capturing the scene.
   Increasing this can fix reflection contact problems.


Viewport Display
----------------

.. reference::

   :Panel:     :menuselection:`Object Data --> Viewport Display`

Arrow Size
   Size of the arrow showing the reflection plane normal.

Capture
   Show the captured reflected image onto a fully reflective plane in the 3D Viewport.

Influence
   Show the influence bounds in the 3D Viewport.
