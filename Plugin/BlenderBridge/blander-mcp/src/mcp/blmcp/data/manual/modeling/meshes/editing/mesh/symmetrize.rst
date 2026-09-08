.. _bpy.ops.mesh.symmetrize:

**********
Symmetrize
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Symmetrize`

The *Symmetrize* operator is a quick way to make a mesh symmetrical.
It does the following:

#. Cuts the selected geometry at the :doc:`origin </scene_layout/object/origin>`
   of the object using an infinite plane, much like
   :doc:`/modeling/meshes/editing/mesh/bisect`.
#. Deletes the geometry on one side of the plane.
#. Copies the geometry on the other side of the plane and mirrors it.
#. Merges the vertices that lie on the plane.

.. seealso::

   - :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>` continuously
     maintains symmetry while editing the mesh.
   - The :doc:`/modeling/modifiers/generate/mirror` symmetrizes the mesh
     non-destructively.
   - The :doc:`/modeling/meshes/editing/mesh/mirror` operator simply flips the
     mesh without cutting or copying.

Options
=======

Direction
   The axis and direction of the effect, in the object's :term:`local space`.
   For example, *-X to +X* deletes the geometry that's to the right of the
   object origin (positive X coordinate) and replaces it by a mirrored copy
   of the geometry on the left (negative X coordinate).
Threshold
   The vertices in this range will be snapped to the plane of symmetry.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_symmetrize_example-1.png
          :width: 320px

          Mesh before Symmetrize.

     - .. figure:: /images/modeling_meshes_editing_mesh_symmetrize_example-2.png
          :width: 320px

          Mesh after Symmetrize.
