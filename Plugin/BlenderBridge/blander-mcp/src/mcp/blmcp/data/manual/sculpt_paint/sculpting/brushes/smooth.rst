
******
Smooth
******

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Smooths the positions of the vertices to either polish surfaces or remove volume from larger shapes.
Because this brush is so essential, it's always accessible by holding :kbd:`Shift` and sculpting.

Also available as a :doc:`Mesh Filter </sculpt_paint/sculpting/tools/mesh_filter>`
to smooth all unmasked areas at once.

.. note::

   The brush called *Smooth* will be used whenever holding :kbd:`Shift` and sculpting.
   If the smoothing strength or behavior needs to be changed, switch to the *Smooth*
   brush and adjust the settings there.


Brush Settings
==============

General
-------

Strength
   The strength of the smoothing is relative to the density of the mesh.
   If the resolution is increased on the sculpted mesh,
   the strength of the smooth brush will be weaker than before and needs to be increased.

Direction :kbd:`Ctrl`
   Smooth
      Smooths the surface of the mesh.
   Enhance Details
      Enhances details on the surface of the mesh by applying a smoothing operation in the opposite direction.

.. _bpy.types.Brush.smooth_deform_type:

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

Deformation
   There are two deformation types.

   :Laplacian:
      Smooths the surface and volumes. This is the default behavior.
   :Surface:
      Smooths only the surface of the mesh, while preserving the volume.

      .. _bpy.types.Brush.surface_smooth_shape_preservation:

      Shape Preservation
         How much of the original shape is preserved while smoothing. Increasing the value
         reduces the effect of having multiple iterations on the strength of smoothing.

      .. _bpy.types.Brush.surface_smooth_current_vertex:

      Per-Vertex Displacement
         How much the position of each individual vertex influences the final result.
         Increasing the value reduces the overall strength of smoothing.

      .. _bpy.types.Brush.surface_smooth_iterations:

      Iterations
         Number of smoothing iterations per brush step.

      .. note::

         This method works by applying regular smoothing, computing the difference between
         the original (blended between start of iteration and fully original based on *Shape Preservation*)
         and the smoothed mesh, smoothing these offsets, pushing vertices back using the smoothed offsets,
         and finally blending in the original mesh based on *Per-Vertex Displacement*.
