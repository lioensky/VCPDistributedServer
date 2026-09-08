.. _bpy.types.MeshStatVis:
.. _modeling-mesh-analysis:

*************
Mesh Analysis
*************

.. reference::

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Header --> Overlays --> Mesh Analysis`

Mesh analysis is useful for displaying attributes of the mesh,
that may impact certain use cases.

The mesh analysis works in *Edit Mode* and *Solid* Viewport shading.
It shows areas with a high value in red, and areas with a low value in blue.
Geometry outside the range is displayed gray.

Currently the different modes target 3D printing as their primary use.


Overhang
========

Extrusion 3D printers have a physical limit to the overhang that can be printed,
this display mode shows the overhang with angle range and axis selection.

Minimum/Maximum
   Minimum/Maximum angle to display.
Axis
   Axis and direction to use as the bases to calculate the angle to visualize.

.. figure:: /images/modeling_meshes_mesh-analysis_overhang.png
   :width: 350px
   :align: center

   Overhang.


Thickness
=========

Printers have a limited *wall-thickness* where very thin areas cannot be printed,
this test uses ray casting and a distance range to the thickness of the geometry.

Minimum/Maximum
   Minimum/Maximum thickness to display.
Samples
   Number of samples to use to calculate the thickness.

.. figure:: /images/modeling_meshes_mesh-analysis_thickness.png
   :width: 400px
   :align: center

   Thickness.


Intersections
=============

Another common cause of problems for printing are intersections between surfaces,
where the inside/outside of a model cannot be reliably detected.

Unlike other display modes, intersections have no variance and are either on or off.

.. figure:: /images/modeling_meshes_mesh-analysis_intersections.png
   :width: 400px
   :align: center

   Intersecting faces.


Distortion
==========

Distorted geometry can cause problems since the triangulation of a distorted n-gon is undefined.

Distortion is measured by faces which are not flat,
with parts of the face pointing in different directions.

Minimum/Maximum
   Minimum/Maximum distortion to display.

.. figure:: /images/modeling_meshes_mesh-analysis_distortion.png
   :width: 300px
   :align: center

   Distorted Faces.


Sharp Edges
===========

Similar to wall-thickness, sharp edges can form shapes that are too thin to be able to print.

Minimum/Maximum
   Minimum/Maximum angle to display.

.. figure:: /images/modeling_meshes_mesh-analysis_sharp-edges.png
   :width: 350px
   :align: center

   Sharp edges.


Known Limitations
=================

There are some known limitations with mesh analysis:

- Currently only displayed with Deform Modifiers.
- For high-poly meshes the performance is low while editing.
