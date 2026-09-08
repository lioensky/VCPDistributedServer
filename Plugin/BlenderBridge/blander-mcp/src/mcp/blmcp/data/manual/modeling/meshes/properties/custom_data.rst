
*************
Geometry Data
*************

This panel is used to manage any generic data attributes that a mesh could have.

.. warning::

   Clearing any data will result in the data loss of these values.

.. _bpy.ops.mesh.customdata_mask_clear:

Clear Sculpt Mask Data
   Deletes the internal ``sculpt_mask`` attribute.
   This attribute is used by the :ref:`Sculpt Masking Feature <face_sets>`.

.. _bpy.ops.mesh.customdata_skin_clear:
.. _bpy.ops.mesh.customdata_skin_add:

Add/Clear Skin Data
   Used to manage the skin data which is used by the :doc:`/modeling/modifiers/generate/skin`.
   This operator can be needed in case a Skin modifier is created but no skin data exist.

.. _bpy.ops.mesh.reorder_vertices_spatial:

Reorder Mesh Spatially
   The operation sorts the vertex and face indices according to their location in space,
   so nearby geometry elements are also nearby in memory.

   This does not change the visible geometry or topology of the mesh.
   This does however improve performance in areas where spatial coherence is important, such as:

   - Faster BVH (Bounding Volume Hierarchy) building for rendering and viewport performance.
   - Improved memory access patterns during sculpting on high-poly meshes.
   - Potentially smoother interaction in edit and sculpt modes on dense geometry.

   .. warning::

      - Vertex and face indices will change.
        This can break any workflows that rely on stable indices, such as shape keys, UV maps,
        or external scripts referencing vertex indices.
      - Use with caution on meshes that are already bound to rigs or shape keys.

   .. tip::

      This operator is most useful for static high-resolution meshes used in sculpting or rendering,
      where index stability is less important than performance.

      For meshes used in animation or deformation, it is generally safer to avoid reordering.

.. _bpy.ops.mesh.customdata_custom_splitnormals_clear:
.. _bpy.ops.mesh.customdata_custom_splitnormals_add:

Add/Clear Custom Split Normals Data
   Adds :ref:`Custom Split Normals <modeling_meshes_normals_custom>` data, if none exists yet.
