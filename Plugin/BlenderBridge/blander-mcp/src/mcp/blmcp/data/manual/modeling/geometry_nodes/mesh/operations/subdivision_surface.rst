.. index:: Geometry Nodes; Subdivision Surface
.. _bpy.types.GeometryNodeSubdivisionSurface:

************************
Subdivision Surface Node
************************

.. figure:: /images/node-types_GeometryNodeSubdivisionSurface.webp
   :align: right
   :alt: Subdivision Surface Node.

The *Subdivision Surface* node adds new faces to mesh geometry using a Catmull-Clark subdivision method.


Inputs
======

Mesh
   Standard geometry input.

Level
   The number of subdivisions to apply to the input geometry.

Edge Crease
   Controls how smooth edges should be with :ref:`modifiers-generate-subsurf-creases`.

Vertex Crease
   Controls how much the subdivision surface should be pulled towards the vertex.
   Similar to edge creases, but allows individual vertices to be creased.

Limit Surface
   Places vertices at the surface that would be produced with infinite
   levels of subdivision (smoothest possible shape).

UV Smooth
   Controls how subdivision smoothing is applied to UVs.

   :None: UVs remain unchanged.
   :Keep Corners: UV islands are smoothed, but their boundary remain unchanged.
   :Keep Corners, Junctions:
      UVs are smoothed, corners on discontinuous boundary and junctions of three or more regions are kept sharp.
   :Keep Corners, Junctions, Concave:
      UVs are smoothed, corners on discontinuous boundary,
      junctions of three or more regions and darts and concave corners are kept sharp.
   :Keep Boundaries: UVs are smoothed, boundaries are kept sharp.
   :All: UVs and their boundaries are smoothed.

Boundary Smooth
   Controls how open boundaries (and corners) are smoothed.

   :All: Smooth boundaries, including corners.
   :Keep Corners: Smooth boundaries, but corners are kept sharp.


Outputs
=======

Mesh
   Standard geometry output.
