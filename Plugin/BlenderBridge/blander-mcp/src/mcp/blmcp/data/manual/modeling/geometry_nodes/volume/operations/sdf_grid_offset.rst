.. index:: Geometry Nodes; SDF Grid Offset
.. _bpy.types.GeometryNodeSDFGridOffset:

*********************
SDF Grid Offset Node
*********************

.. figure:: /images/node-types_GeometryNodeSDFGridOffset.webp
   :align: right
   :alt: SDF Grid Offset node.

The *SDF Grid Offset* node offsets the surface of a Signed Distance Field (SDF)
by a specified world-space distance.
This operation effectively dilates (expands) or erodes (contracts) the
surface while maintaining the correct signed distance values across the field.

A positive offset increases the surface thickness by pushing it outward,
while a negative offset shrinks it inward. This is a fundamental operation in
volumetric modeling, useful for adjusting wall thickness, creating shells,
expanding collision volumes, or controlling blend margins between shapes.


Inputs
======

Grid
   The input signed distance field to offset.

Distance
   The offset distance applied to the surface, in world units.
   Positive values expand the surface (dilation), and negative values contract it (erosion).
   The offset is applied uniformly in all directions, preserving smoothness and the signed distance property.


Outputs
=======

Grid
   The resulting SDF grid with the surface offset by the specified distance.
   The output preserves the SDF property, ensuring that distances remain
   accurate for subsequent operations such as booleans or conversion to a mesh.
