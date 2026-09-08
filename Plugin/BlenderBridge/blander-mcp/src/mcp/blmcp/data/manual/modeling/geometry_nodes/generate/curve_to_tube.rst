.. index:: Geometry Nodes; Curve to Tube

******************
Curve to Tube Node
******************

.. figure:: /images/node-types_GeometryNodeCurveToTube.webp
   :align: right
   :alt: Curve to Tube node.

The *Curve to Tube* node generates a mesh tube along an input curve.
It creates cylindrical or custom-profiled geometry that follows the curve shape,
with flexible control over radius, resampling, capping, and UV generation.
This node is useful for modeling cables, pipes, wires, or other tubular structures.


Inputs
======

Curve
   The input curve to generate the tube along.

.. section-inputs

Scale
   Distance factor multiplied by the curve's radius attribute to define the resulting tube radius.


Profile
-------

Profile Mode
   Method used to define the profile shape of the tube.

   :Round: Uses a circular profile to define the tube cross-section.
   :Custom: Uses a custom object or geometry as the profile shape.

Resolution :guilabel:`Round`
   The number of points around the circular profile.
   Also defines the resolution of the *Round* cap type.

Profile Input :guilabel:`Custom`
   Defines how the custom profile is provided.

   :Object: Uses a single object as the custom profile.
   :Geometry: Uses input geometry directly as the profile.

Object / Geometry :guilabel:`Custom`
   The specific object or geometry to use as the profile when *Custom* mode is active.

Shade Smooth
   Enables smooth shading for the generated mesh.


Resample
--------

Resamples the input curve before generating the mesh.
This helps achieve evenly distributed geometry and consistent resolution along the tube.

Resample Mode
   Determines how the curve is resampled.

   :Evaluated: Uses the existing evaluated curve points.
   :Auto: Automatically determines an appropriate sample length based on curve details.
   :Count: Uses a fixed number of sample points.
   :Length: Uses a fixed distance between sample points.

Scale :guilabel:`Auto`
   Scale factor applied to the automatically derived resample length when using *Auto* mode.

Count :guilabel:`Count`
   Number of sample points along the curve when using *Count* mode.

Length :guilabel:`Length`
   Distance between sample points when using *Length* mode.


Caps
----

Fills the open ends of the tube with cap geometry.

Caps Type
   Method used to fill the tube ends.

   :Flat: Uses a single n-gon to cap each end.
   :Round: Uses a half-circle shape for rounded caps.
   :Custom: Uses user-provided geometry or an object as the cap.

Smooth :guilabel:`Flat` :guilabel:`Round`
   Smooths the transition between the tube body and the caps instead of creating a sharp edge.

Caps Input :guilabel:`Custom`
   Defines how custom caps are provided.

   :Object: Uses a single object as the custom cap.
   :Geometry: Uses input geometry as the custom cap.

Start / End :guilabel:`Custom`
   Specifies the objects or geometry to use for the start and end caps when *Custom* mode is active.


UV Map
------

Name
   The name of the UV map to create or modify on the output mesh.

Parameter U/V
   Defines how the UVs are generated along the tube.

   :Factor: Uses a normalized 0-1 factor along the curve and profile.
   :Length: Maps UVs based on the real length of the curve and circumference.
   :Index: Uses the point indices along the curve and profile.

Consider Curve Radius
   When enabled, the UV generation takes into account variations in the curve's radius.


.. section-outputs

Outputs
=======

Mesh
   The generated mesh tube following the input curve, including optional caps and UV mapping.
