.. index:: Modeling Modifiers; Edge Split Modifier
.. _bpy.types.EdgeSplitModifier:

*******************
Edge Split Modifier
*******************

The *Edge Split* modifier splits, duplicates edges within a mesh,
breaking 'links' between faces around those split edges.

The edges to split can be determined from the edge angle (i.e. angle between faces forming that edge),
and/or edges marked as :ref:`Sharp <bpy.ops.mesh.mark_sharp>`.

Splitting an edge affects vertex normal generation at that edge, making the edge appear sharp.
It can also be used for manual control of the smoothing process,
where the user defines which edges should appear smooth or sharp
(see :ref:`Mesh Smoothing <modeling-meshes-editing-normals-shading>` for other ways to do this).
If desired, both modes can be active at once.

.. note::

   This modifier is kept mostly for historical/compatibility reasons.
   Everything it can do in shading, and much more,
   can now be achieved using :ref:`custom normals <modeling_meshes_normals_custom>`.

   Unless you really need the topology changes it generates, it is not advised to use it in new projects.

.. note::

   Splitting edges can also be :ref:`performed manually <bpy.ops.mesh.edge_split>` in Edit Mode.


Options
=======

.. figure:: /images/modeling_modifiers_generate_edge-split_panel.png
   :align: right
   :width: 300px

   The Edge Split modifier.

Edge Angle
   When enabled, an edge will be split if the angle between its
   two adjacent faces is greater than the *Split Angle*.

   Split Angle
      On 0: all edges are split. On 180: no edges are split.

Sharp Edges
   When enabled, edges will be split if they were :ref:`marked as sharp <bpy.ops.mesh.mark_sharp>`.

.. note::

   :term:`Non-manifold` edges will always be split.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_modifiers_generate_edge-split_example-1.png

          Flat shading.

     - .. figure:: /images/modeling_modifiers_generate_edge-split_example-2.png

          Smooth shading.

   * - .. figure:: /images/modeling_modifiers_generate_edge-split_example-3.png

          Smooth shading with Edge Split.

     - .. figure:: /images/modeling_modifiers_generate_edge-split_example-4.png

          Smooth shading with Edge Split and Subdivision Surface.
