
******
Remesh
******

.. reference::

   :Mode:      Sculpt Mode
   :Header:    :menuselection:`Tool Settings --> Remesh`
   :Panel:     :menuselection:`Sidebar --> Tool --> Remesh`
   :Shortcut:  :kbd:`Ctrl-R`

For a general explanation to remeshing, visit the :doc:`Introduction </sculpt_paint/sculpting/introduction/adaptive>`.

Voxel Size :kbd:`R`
   The resolution or the amount of detail the remeshed mesh will have.
   The value is used to define the size, in object space, of the :term:`Voxel`.
   These voxels are assembled around the mesh and are used to determine the new geometry.
   For example a value of 0.5m will create topological patches that are about 0.5m
   (assuming *Preserve Volume* is enabled).
   Lower values preserve finer details but will result in a mesh with a much more dense topology.

   The voxel size also be adjusted from the 3D Viewport using :kbd:`R`.
   Using the shortcut displays an interactive grid overlay showing the resulting voxel size.
   Moving the mouse closer to center of the grid decreases the voxel size
   while moving away from the center increase the voxel size.
   Holding :kbd:`Shift` increases the precision; adjusting the voxel size in small increments.

   Sample Voxel Size
      Used to adjust the *Voxel Size* by picking an area of the mesh
      to match the denseness of polygons after the remesh operation.

Adaptivity
   Reduces the final face count by simplifying geometry where detail is not needed.
   This introduce triangulation to faces that do not need as much detail.
   Note, an *Adaptivity* value greater than zero disables *Fix Poles*.

Fix Poles
   Tries to produce less :term:`poles <Pole>` at the cost of some performance to produce a better topological flow.

Preserve
   Volume
      Tells the algorithm to try to preserve the original volume of the mesh.
      Enabling this could make the operator slower depending on the complexity of the mesh.
   Paint Mask
      Reprojects the :ref:`paint mask <sculpt-mask-menu>` onto the new mesh.
   Face Sets
      Reprojects :ref:`Face Sets <sculpting-editing-facesets>` onto the new mesh.
   Color Attributes
      Reprojects the :ref:`Color Attributes <modeling-meshes-properties-object_data-color-attributes>` onto the
      new mesh.

Voxel Remesh
   Performs the remeshing operation to create a new manifold mesh based on the volume of the current mesh.
   Performing this will lose all mesh object data layers associated with the original mesh.

.. seealso::

   :doc:`Remesh modifier </modeling/modifiers/generate/remesh>`


Known Limitations
=================

- Remeshing only works on the original mesh data and
  ignores generated geometry from modifiers, shape keys, rigging, etc.
- Remeshing will not work with the :doc:`/modeling/modifiers/generate/multiresolution`.
