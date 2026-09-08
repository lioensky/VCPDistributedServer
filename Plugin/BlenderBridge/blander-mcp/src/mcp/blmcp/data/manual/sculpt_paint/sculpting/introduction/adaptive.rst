
*******************
Adaptive Resolution
*******************

In order for sculpting to give accurate and predictable results, Blender needs enough geometry.
Instead of starting out with a highly subdivided mesh, add geometry dynamically
by using either of the following adaptive sculpting methods.


Voxel Remesher
==============

"Voxel remeshing" rebuilds the geometry with a perfectly even distributed topology.
Depending on the set voxel size, this will lead to a lower or higher resolution.

This technique is especially useful to block out the initial shape of an object.
It also has the advantage of removing any overlapping geometry and creating a manifold volume as a result.

.. figure:: /images/sculpt-paint_sculpt_voxel_merge.png

Any currently used mask, face sets and color attributes will be re-projected on the remeshed result.
Reaching high vertex counts should still be achievable with this technique, depending on the used hardware.

.. note::

   This technique will not work on objects that do not have an enclosed volume.
   Make sure to fill any holes in the mesh before remeshing.
   Or avoid any holes in the mesh/volume that are larger than the defined voxel size.

.. tip::

   If in doubt, you can fill all holes in edit mode or by using the
   :ref:`Mask Slice and Fill Holes <bpy.ops.sculpt.paint_mask_slice>`
   operation to fill all holes in the mesh. If nothing is masked, it only fills any holes.

   ..
      this is a useful workaround. But once the voxel remesher automatically checks for holes
      or a dedicated Fill Holes operation is added, this tip should be removed.

To more easily access this feature, use the shortcuts :kbd:`R` to define the resolution,
and :kbd:`Ctrl-R` to execute the remeshing.

.. figure:: /images/sculpt-paint_sculpt_voxel_grid.png

.. seealso::

   More information at :doc:`Remesh </sculpt_paint/sculpting/tool_settings/remesh>`.


.. _dyntopo_introduction:

Dyntopo
=======

Dynamic topology (aka Dyntopo) is a dynamic tessellation
sculpting method that automatically adds and removes topology under the brush.

.. figure:: /images/sculpt-paint_sculpt_dyntopo_example.png

Unlike the Voxel Remesher, this makes it possible to sculpt complex shapes
without thinking about the resolution or topology.
It also allows to define a different resolution wherever necessary.
Much more complex base mesh sculpting is especially useful with this technique.

The disadvantages of this technique are a slower performance and limited support for some sculpt mode features.
Custom attributes like Color Attributes, UV Maps and Face Sets are also lost or corrupted when using Dyntopo.

This feature shares the same shortcuts with voxel remeshing when enabled.
Use :kbd:`R` to define the resolution and :kbd:`Ctrl-R` to flood fill the resolution (if Constant Detail is used).

.. note::

   Because Dyntopo and the Voxel Remesher are mutually exclusive and cannot be used at the same time,
   both use the same shortcut to define the remeshing resolution.

.. figure:: /images/sculpt-paint_sculpt_dyntopo_detail.png

Brushes like :doc:`Density </sculpt_paint/sculpting/brushes/simplify>`,
:doc:`Snake Hook </sculpt_paint/sculpting/brushes/snake_hook>`
and :doc:`Clay Strips </sculpt_paint/sculpting/brushes/clay_strips>` work especially well with this feature.


.. seealso::

   More information at :doc:`Dyntopo </sculpt_paint/sculpting/tool_settings/dyntopo>`.


Multiresolution
===============

The Multiresolution Modifier can be used for subdivision based sculpting.
This means the object will be subdivided, similar to the
:doc:`Subdivision Surface Modifier </modeling/modifiers/generate/subdivision_surface>`,
only that the subdivisions can be freely sculpted for very high resolution detailing.

.. figure:: /images/sculpt-paint_sculpt_multires_example.png

.. note::

   For this technique it is highly recommended to use on a clean topology base mesh.
   This means the base mesh should be only made of quads
   and avoid non-manifold faces, as well as poles with two connected edges.
   More information at :ref:`bpy.ops.object.quadriflow_remesh` Remeshing for an automatic retopology method.

This technique has the advantage of sculpting with multiple resolutions,
meaning you have the ability to sculpt on any level of subdivision.
This allows to add a much higher resolution of details for rendering and sculpting,
while displaying lower resolutions for better viewport performance.
It also allows sculpting on lower resolutions any time for broader changes.

As an example, you can sculpt general proportions in subdivision level 1,
add high resolution details in level 4 and switch back to subdivision 1 to correct the shape further.

The disadvantages are that you may end up with some mesh distortions
because the topology is not dynamic like voxel remeshing and dyntopo.
The topology should also not be changed once already subdivided,
since any edits to the base mesh will result in corrupted subdivision details.

.. tip::

   Pay attention to the topology that you sculpt and how much it gets stretched.
   If more resolution is needed you can always subdivide another time,
   but there will be worse performance and slower level switching once more than 5 subdivisions are used.
   Alternatively use the :doc:`Slide Relax </sculpt_paint/sculpting/brushes/slide_relax>`
   brush to slide topology to where it is needed.

Additional brushes like the :doc:`Multires Eraser </sculpt_paint/sculpting/brushes/multires_displacement_eraser>` and
:doc:`Multires Smear </sculpt_paint/sculpting/brushes/multires_displacement_smear>` are recommended for adjustments.

Here are general shortcuts to use the feature.

- Step up one multires level :kbd:`Alt-2`
- Step down one multires level :kbd:`Alt-1`
- Set multires level / Create multires modifier :kbd:`Ctrl-0` to :kbd:`Ctrl-5`

.. seealso::

   More information at :doc:`Multiresolution Modifier </modeling/modifiers/generate/multiresolution>`.
