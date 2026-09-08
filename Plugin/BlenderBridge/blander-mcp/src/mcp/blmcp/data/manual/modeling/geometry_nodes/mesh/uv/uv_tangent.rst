.. index:: Geometry Nodes; UV Tangent
.. _bpy.types.GeometryNodeUVTangent:

***************
UV Tangent Node
***************

.. figure:: /images/node-types_GeometryNodeUVTangent.webp
   :align: right
   :alt: UV Tangent node.

The *UV Tangent* node generates tangent direction vectors based on a specified UV map.
Tangents are unit-length vectors that lie along the surface of the geometry
and point in the direction of increasing *U* coordinates in the UV space.
They are commonly used in shading and texturing workflows, for example in
normal mapping or anisotropic effects.

This node allows for either exact or approximate tangent computation, offering
a balance between precision and performance depending on the use case.


Inputs
======

Method
   The algorithm used to compute the tangents:

   :Exact:
      Uses the *MikkTSpace* algorithm for tangent computation.
      Produces consistent and accurate results that match the tangents used in
      Blender's shading system and exported geometry.
      This method ensures that tangents align with the normal map space used in rendering.
   :Fast:
      A faster approximate method that interpolates tangents across face corners with matching UVs.
      It provides similar results at a much lower computational cost but may
      produce less consistent results on complex or uneven surfaces.
      For an exact tangent aligned to the surface, the cross product of the
      result with the surface normal can be used.

UV
   The UV map used to calculate the tangent direction.
   The UV coordinates define how the tangent vectors are oriented across the surface.


Outputs
=======

Tangent
   The tangent direction vector derived from the input UV map.
   The output is a normalized vector field that lies along the surface and
   indicates the direction of increasing *U* values in the UV space.
   It can be combined with normals and bitangents for constructing a complete tangent space basis.
