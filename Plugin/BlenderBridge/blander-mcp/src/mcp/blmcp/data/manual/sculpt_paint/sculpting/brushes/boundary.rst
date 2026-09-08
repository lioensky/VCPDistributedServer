
********
Boundary
********

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

Similar to the :doc:`Pose </sculpt_paint/sculpting/brushes/pose>` brush
but deforms the open boundaries of a mesh.
The tool detects the mesh boundary closest to the active vertex and
propagates the deformation using the brush :doc:`Falloff </sculpt_paint/brush/falloff>` into the mesh.

The main use cases of this brush are the *Bend* and *Expand* geometry,
which leads to the best results on evenly distributed quad based topology.
Use the *Inflate*, *Grab*, *Twist*, and *Smooth* deformation modes,
to further adjustments and tweaks to the result
(which do not depend that much on a clean topology).

.. tip::

   Boundaries to hidden geometry will also be counted as an open boundary.

The boundary origin is displayed via a white line, which indicates the reach of the deformation.
The targeted boundary that will be deformed is highlighted in the brush cursor color.

If the :ref:`Deformation Target <bpy.types.Brush.deform_target>`
is changed, the brush can also be used for cloth sculpting.

.. note::

   Evenly distributed and quad based topology will lead to much better results.
   Triangles and N-gons are also supported but may lead to unpredictable outcomes.


Brush Settings
==============

General
-------

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.

Unique
------

.. _bpy.types.Brush.boundary_deform_type:

Deformation
   Deformation type that is used by the brush.

   :Bend:
      Rotates the boundary around the local Y axis.
      Useful for creating folding shapes, like sleeves.
   :Expand:
      Moves/extends the mesh boundary in the local X direction.
      Useful for extending the boundaries along the surface.
   :Inflate:
      Works similar to the :doc:`Inflate </sculpt_paint/sculpting/brushes/inflate>` tool but,
      the vertices that are inflated are constrained to the mesh boundary.
   :Grab:
      Works similar to the :doc:`Grab </sculpt_paint/sculpting/brushes/grab>` tool but,
      the vertices that are grabbed are constrained to the mesh boundary.
   :Twist:
      Rotates the active boundary around the local Z axis.
      Useful for creating folds like on a skirt.
   :Smooth:
      Works similar to the :doc:`Grab </sculpt_paint/sculpting/brushes/smooth>` tool but,
      the vertices that are smoothed are constrained to the mesh boundary.

.. _bpy.types.Brush.boundary_falloff_type:

Boundary Falloff
   How the brush :doc:`Falloff </sculpt_paint/brush/falloff>` is applied across the boundary.

   :Constant:
      Applies the same deformation in the entire boundary.
   :Brush Radius:
      Applies the deformation only within the brush radius.
   :Loop:
      Applies the brush falloff in a loop pattern along the boundary.
   :Loop and Invert:
      Applies the falloff radius in a loop pattern,
      inverting the direction back & forth.

.. _bpy.types.Brush.boundary_offset:

Boundary Origin Offset
   Offset of the boundary origin in relation to the brush radius.
