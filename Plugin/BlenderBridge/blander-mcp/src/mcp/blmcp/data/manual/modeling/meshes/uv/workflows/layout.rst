
***************
Layout Workflow
***************

This page contains various unwrapping tips.

Unwrapping in Multiple Steps
============================

If you unwrap an entire mesh in one go, the resulting UV map may look rather messy.
In the example below, the ear and facial features are squashed and the neck is stretched
out way too far:

.. figure:: /images/modeling_meshes_uv_workflows_layout_combining-uv-maps-1.png

   Bad unwrap, note ear and neck.

While you could of course start fixing this UV map by hand, it's probably a better
idea to drop it and unwrap the mesh differently. We'll divide it into pieces,
unwrapping each one separately with the most suitable projection.

We start by selecting just the head -- excluding the eyes, ears, and neck --
and unwrapping it using :ref:`bpy.ops.uv.sphere_project`:

.. figure:: /images/modeling_meshes_uv_workflows_layout_combining-uv-maps-2.png

   Unwrapping just the head.

Next, select the ear, align the 3D Viewport view to look straight at it,
and unwrap it using :ref:`bpy.ops.uv.project_from_view`.

.. figure:: /images/modeling_meshes_uv_workflows_layout_combining-uv-maps-3.png

   Unwrapping the ear.

The UV Editor only shows the ear at this point, but don't worry: the UV coordinates
for the head are still there, just hidden. To make them visible again, either
select the head in the 3D Viewport again or enable
:ref:`bpy.types.ToolSettings.use_uv_select_sync` in the UV Editor.

Next, you can unwrap the neck using :ref:`bpy.ops.uv.cylinder_project`.

.. hint::

   Instead of selecting and unwrapping each piece individually, you can also
   use :doc:`/modeling/meshes/uv/unwrapping/seams` to mark cutting lines
   around the ear and neck, then run a single :ref:`bpy.ops.uv.unwrap`
   to map all three parts in one go.

Once everything is unwrapped, you can select the whole mesh in the 3D Viewport to
see to the full UV map. Most likely, the different UV parts or "islands" will be
overlapping; you can fix this in the following ways:

- For each island, select a vertex and press :kbd:`Ctrl-L` to select all the vertices
  it's connected (Linked) to. You can also hover over the vertex and press :kbd:`L`,
  or simply set the :ref:`bpy.ops.uv.select_mode` to *Island*.
  Once the island is selected, scale it down and move it to a place where it no
  longer overlaps the others.
- Alternatively, you can simply click :ref:`bpy.ops.uv.pack_islands` in the menu
  to have Blender lay out the islands automatically.

.. figure:: /images/modeling_meshes_uv_workflows_layout_combining-uv-maps-4.png

   UV maps arranged together and stitched.

As a final step, you can align the islands to each other by moving and scaling,
then connect them using :ref:`bpy.ops.uv.weld` -- or better yet, :ref:`bpy.ops.uv.stitch`.


Refining the Layout
===================

After using the unwrapping tools, you may want to manually tweak the UV map,
for example scaling up an area so it receives more pixels of the texture
and can thus be more detailed. You can also use :ref:`bpy.ops.uv.minimize_stretch`
if the UV map is too warped compared to the 3D mesh.


Multiple UV Maps
================

A mesh can have more than one UV map, where each map can assign different UV coordinates
to the same 3D vertex. This is useful if, say, you need one UV map for textures and another
for storing :ref:`prebaked lighting <bpy.ops.uv.lightmap_pack>`.

You can add and remove UV maps in the :ref:`UV Maps panel <uv-maps-panel>`.


Transferring UV Maps
====================

You can copy a UV map from one mesh to another in several ways. If the meshes have
the exact same topology and only differ in vertex positions, you can use
:ref:`bpy.ops.object.join_uvs`. If they have (approximately) the same surface
but different topology, you can instead use
:doc:`/scene_layout/object/editing/link_transfer/transfer_mesh_data`.
