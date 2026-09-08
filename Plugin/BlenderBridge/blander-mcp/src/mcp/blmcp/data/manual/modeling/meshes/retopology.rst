*********
Remeshing
*********

Blender offers several tools for regenerating a mesh so that it has (approximately) the same
shape but fewer faces, more faces, or better topology.

.. figure:: /images/modeling_meshes_retopology_example.png

   Remeshing to clean up messy geometry.

.. _bpy.types.Mesh.remesh:
.. _bpy.ops.object.voxel_remesh:

Remeshing
=========

.. reference::

   :Mode:      Object Mode, Sculpt Mode
   :Panel:     :menuselection:`Properties --> Data --> Remesh`

Remeshing automatically rebuilds the mesh with a uniform topology.
You can run it with a high resolution to make a simple mesh denser, making it
more suitable for :doc:`sculpting </sculpt_paint/sculpting/introduction/general>`.
Alternatively, you can run it with a low resolution to simplify and clean up
overly dense or messy geometry, such as from a sculpt or a 3D scan.

.. note::

   - Remeshing only works on the original mesh data -- it ignores
     :doc:`modifiers </modeling/modifiers/introduction>`,
     :doc:`shape keys </animation/shape_keys/introduction>` and so on.
   - Remeshing is not possible on objects with a
     :doc:`/modeling/modifiers/generate/multiresolution`.

The *Remesh* panel lets you choose between two different modes:

Voxel
-----

The :term:`Voxel` remesher works by placing the mesh in a virtual 3D grid,
seeing which points of the grid are closest to the mesh's outer
surface, and generating a new mesh with vertices at those points.
This means the resulting mesh has uniform topology and has no inner
(self-intersecting) geometry.

It's useful for the following cases:

- Changing the resolution of, or generally cleaning up, a mesh that you
  want to sculpt. Notably, by setting up the resolution before sculpting,
  you can leave :ref:`Dyntopo <dyntopo_introduction>` disabled and avoid
  its performance impact.
- Cleaning up a mesh for 3D printing.
- Generating a simplified standin mesh for use with physics simulation.

However, because the topology is just a simple grid, the Voxel remesher
should *not* be used for the following:

- Creating topology for a mesh that will be deformed (e.g. a character
  that will be animated). Such topology has to follow the flow of the
  geometry, and no perfect automatic tools exist for this right now;
  it has to be done manually. See `Retopology`_.
- Generating a mesh for applying the
  :doc:`/modeling/modifiers/generate/subdivision_surface`
  or the :doc:`/modeling/modifiers/generate/multiresolution`.
  It's better to use the :ref:`bpy.ops.object.quadriflow_remesh` mode for this.
- Reducing the face count of a mesh that otherwise has no problems with
  its geometry. It's better to use :ref:`bpy.ops.mesh.decimate` for this.

Voxel remesh has the following settings:

Voxel Size
   The size of each voxel (3D grid cell). Use a low value to get a detailed
   but dense mesh, or a high value for a light but coarse one.

Adaptivity
   Reduces the final face count by simplifying geometry where detail is not needed.
   A value greater than zero disables *Fix Poles* and can introduce triangulation.

Fix Poles
   Tries to reduce the number of :term:`Poles <Pole>` at the cost of some performance,
   to produce a better topological flow.

Preserve
   Volume
      Try to preserve the original volume of the mesh.
      Enabling this could make the operator slower depending on the complexity of the mesh.
   Attributes
      Transfer attributes to the new mesh: the :ref:`paint mask <sculpt-mask-menu>`,
      any :ref:`face sets <sculpting-editing-facesets>`,
      :ref:`color attributes <modeling-meshes-properties-object_data-color-attributes>`,
      and so on.

.. seealso::

   The :doc:`/modeling/modifiers/generate/remesh` can perform this operation non-destructively
   and offers more remeshing methods.

.. _bpy.ops.object.quadriflow_remesh:

Quad
----

The :term:`Quad` remesher uses the Quadriflow algorithm, which can produce better results
but is also slower. It's not a replacement for the Voxel remesher, however, because it
doesn't clean up intersecting geometry.

It's useful for the following cases:

- Generating a mesh for applying the :doc:`/modeling/modifiers/generate/subdivision_surface`
  or the :doc:`/modeling/modifiers/generate/multiresolution`.

However, it's not recommended for the following:

- Cleaning up a mesh for sculpting or 3D printing. The Voxel remesher is more suited for this.
- Creating final topology for a mesh that will be deformed (e.g. a character
  that will be animated). Such topology has to follow the flow of the
  geometry, and no perfect automatic tools exist for this right now;
  it has to be done manually. See `Retopology`_.
- Reducing the face count of a mesh that otherwise has no problems with
  its geometry. It's better to use :ref:`bpy.ops.mesh.decimate` for this.

Quadriflow Remesh
   Opens a pop-up to set parameters for the remesh operation.

Use Mesh Symmetry
   Generates a symmetrical mesh using the :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>` options.

Preserve Sharp
   Try to preserve sharp features of the mesh.
   Enabling this could make the operator slower depending on the complexity of the mesh.

Preserve Mesh Boundary
   Try to preserve the original volume of the mesh.
   Enabling this could make the operator slower depending on the complexity of the mesh.

Preserve Attributes
   Transfer attributes to the new mesh: the :ref:`paint mask <sculpt-mask-menu>`,
   any :ref:`face sets <sculpting-editing-facesets>`,
   :ref:`color attributes <modeling-meshes-properties-object_data-color-attributes>`,
   and so on.

Smooth Normals
   Apply :ref:`bpy.ops.object.shade_smooth` to the new mesh.

Mode
   How to specify the amount of detail for the new mesh.

   :Ratio: Specify target number of faces relative to the current mesh.
   :Edge Length: Specify target edge length in the new mesh.
   :Faces: Specify target number of faces in the new mesh.

Seed
   Random :term:`Seed` to use with the solver;
   different seeds will cause the remesher to generate different quad layouts on the mesh.

.. _modeling-meshes-remesh-retopology:

Retopology
==========

The automatic remesh tools generally don't result in topology that lends itself to deformation.
Therefore, if you have sculpted a character and want to simplify it for animation,
you'll typically have to do this manually in a process known as retopologizing.

To do this, you typically create a new mesh that overlaps the original one,
then adjust it until it fully covers the original mesh and matches its shape.

- The :ref:`bpy.types.View3DOverlay.show_retopology` overlay of the 3D Viewport is useful here,
  as it lets you see the original mesh through the retopologized one and vice versa --
  without getting distracted by geometry on the other side as would be the case with
  :ref:`X-Ray <bpy.types.View3DShading.show_xray>`.
- You can use the :doc:`/modeling/meshes/tools/poly_build` tool to quickly add, change,
  and remove faces.
- Use :doc:`/editors/3dview/controls/snapping` to align new vertices to the original mesh.
