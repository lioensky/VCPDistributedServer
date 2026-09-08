.. index:: Geometry Nodes; Hair Attachment Info

********************
Hair Attachment Info
********************

The *Hair Attachment Info* node provides information about how and where hair curves
are attached to a surface mesh.
It allows nodes to retrieve stored attachment coordinates, verify whether the attachment
is still valid, and access the surface normal at the attachment point.
This information is essential for deformation, simulation, and reattachment of hair
when the surface mesh changes.


Inputs
======

Surface Geometry
   The surface geometry to which the hair curves are attached.
   This is typically the same mesh used during hair generation or interpolation.

Surface UV Map
   The UV map on the surface mesh used to locate the curve attachment points.
   It allows retrieving the stored attachment coordinates for each curve.


Outputs
=======

Attachment UV
   The UV coordinates on the surface where each curve is attached.
   These are typically stored per curve and used to find the correct attachment
   location even if the surface topology changes.

Attachment is Valid
   A boolean output indicating whether each curve has a valid stored attachment.
   This can be used to detect invalid or missing attachment data after topology edits
   or surface replacement.

Surface Normal
   The normal direction of the surface mesh evaluated at the curve's attachment point.
   This can be used for aligning hair roots, orienting instances, or driving deformation
   based on surface orientation.
