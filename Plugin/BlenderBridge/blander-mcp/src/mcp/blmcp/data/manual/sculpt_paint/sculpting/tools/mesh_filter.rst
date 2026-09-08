
***********
Mesh Filter
***********

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Mesh Filter`

Applies a deformation to all vertices in the mesh at the same time.
Masking, auto-masking and visibility will be taken into account.

To use this tool, click and drag away from left to right
or from right to left for a negative effect.


Tool Settings
=============

Filter Type
   These are all of the available filter deformations.

   :Smooth:
      Smooths the positions of the vertices to either polish surfaces or remove volume from larger shapes.
      Especially useful to fix most of the artifacts of the voxel remesher.
      This filter works similar to the :doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>` brush.
   :Scale:
      Increases the size of the mesh.
      This filter works similar to the :ref:`Scale Transform <bpy.ops.transform.resize>`.
   :Inflate:
      Displaces vertices uniformly along their normal.
      This filter works similar to the :doc:`Inflate </sculpt_paint/sculpting/brushes/inflate>` brush.
   :Sphere:
      Morphs the mesh progressively into a sphere.
      This filter works similar to the :ref:`To Sphere Transform <bpy.ops.transform.tosphere>`.
   :Random:
      Randomly moves vertices along the vertex normal.
      This filter works similar to the :ref:`Randomize Transform <bpy.ops.object.randomize_transform>`.
   :Relax:
      Tries to create an even distribution of quads without deforming the volume of the mesh.
      This filter works the same as holding :kbd:`Shift` with the
      :doc:`Slide Relax </sculpt_paint/sculpting/brushes/slide_relax>` brush.
   :Relax Face Sets:
      This will remove the jagged lines visible after drawing or creating a face set.
      This filter works the same as holding :kbd:`Shift` with the
      :doc:`Draw Face Set </sculpt_paint/sculpting/brushes/draw_facesets>` brush.
   :Surface Smooth:
      Eliminates irregularities of the mesh by making the positions
      of the vertices more uniform while preserving the volume of the object.
      This filter works similar to the *Surface* deformation type of the
      :doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>` brush.

      Shape Preservation
         How much of the original shape is preserved when smoothing.
      Per-Vertex Displacement
         How much the position of each individual vertex influences the final result.
   :Sharpen:
      Sharpens and smooths the mesh based on its curvature,
      resulting in pinching hard edges and polishing flat surfaces.
      Especially useful when sculpting hard surfaces and stylized models
      with creasing and flattening brushes.

      Smooth Ratio
         How much smoothing is applied to polished surfaces.
      Intensify Details
         Increases the high frequency surface details of the mesh
         by intensifying the difference between creases and valleys.
      Curvature Smooth Iterations
         The number of times the smoothing operation is applied per brush step.
         Controls how much smooth the resulting shape is, ignoring high-frequency details.
   :Enhance Details:
      Increases the high frequency surface details of the mesh
      by intensifying the difference between creases and valleys.
      This filter works similar to the inverted direction of the
      :doc:`Smooth </sculpt_paint/sculpting/brushes/smooth>` brush.
   :Erase Displacement:
      Deletes displacement information of
      the :doc:`Multires Modifier </modeling/modifiers/generate/multiresolution>`,
      resetting the mesh to a regular subdivision surface result.
      This can be used to reset parts of the sculpt or to fix reprojection artifacts
      after applying a :doc:`Shrinkwrap Modifier </modeling/modifiers/deform/shrinkwrap>`.

      Negative strokes will intensify the displacement details,
      this method works similar to *Enhance Details* and can give better results in some circumstances.

Strength
   The amount of effect the filter has on the mesh.
   At certain object scales it can be useful to change this value.

Deformation Axis
   Apply the deformation only on the selected axis.

Orientation
   :doc:`Orientation </editors/3dview/controls/orientation>` of the axis to limit the filter displacement.

   :Local: Use the local axis to limit the displacement.
   :World: Use the global axis to limit the displacement.
   :View: Use the view axis to limit the displacement.
