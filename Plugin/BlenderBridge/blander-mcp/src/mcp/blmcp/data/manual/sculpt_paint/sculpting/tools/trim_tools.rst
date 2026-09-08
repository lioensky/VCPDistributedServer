
******************
Trim Gesture Tools
******************

.. reference::

   :Mode:      Sculpt Mode

Trim gesture tools add or remove geometry based on a selection area.
This tool is especially useful for sketching an early base mesh for further
sculpting with the :doc:`voxel remesher </sculpt_paint/sculpting/tool_settings/remesh>`.

.. list-table::

   * - .. figure:: /images/sculpt-paint_sculpt_trim_lasso_visual_example_a.png

          Using Lasso Trim set to *Join*

     - .. figure:: /images/sculpt-paint_sculpt_trim_lasso_visual_example_b.png

          The symmetrized mesh.

     - .. figure:: /images/sculpt-paint_sculpt_trim_lasso_visual_example_c.png

          Sculpting with voxel remeshing.

New geometry is assigned to a new :ref:`Face Set <sculpting-editing-facesets>`.
When removing geometry, the new interior geometry along the selection will be assigned
a new face set instead.

.. note::

   It is not recommended to use this tool on a mesh above 100k
   vertices when using *Difference* or *Union* as the Trim Mode
   with the *Exact* Solver.
   This tool is using a Boolean operation so it might take a long time to process.
   For higher resolution meshes it is recommended to instead use the
   :doc:`Line Project </sculpt_paint/sculpting/tools/line_project>` tool or the *Fair Positions*
   mode of the :doc:`Edit Face Set </sculpt_paint/sculpting/tools/edit_face_set>` tool to trim geometry.


.. _tool-box-trim:

Box Trim
========

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Box Trim`

Performs a Boolean operation based on the area defined by a
:ref:`box gesture <gesture-tool-box>`.


.. _tool-lasso-trim:

Lasso Trim
==========

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Lasso Trim`

Performs a Boolean operation based on the area defined by a
:ref:`lasso gesture <gesture-tool-lasso>`.


.. _tool-line-trim:

Line Trim
=========

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Line Trim`

Performs a Boolean operation based on the area defined by a
:ref:`line gesture <gesture-tool-line>`.

.. note::

    The Line Trim tool does not support adding geometry. Only *Difference* mode is supported.


.. _tool-polyline-trim:

Polyline Trim
=============

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Polyline Trim`

Performs a Boolean operation based on the area defined by a
:ref:`polyline gesture <gesture-tool-polyline>`.


Tool Settings
=============

Solver
   Algorithm used to calculate the Boolean intersections.

   :Exact:
      Uses a complex solver which offers the best results and has full
      support for overlapping geometry; however, this solver is much slower.
   :Float:
      Uses a simple solver which offers the good performance;
      however, this solver lacks support for overlapping geometry.
   :Manifold:
      Uses a solver that is usually fastest but only works on :term:`Manifold` meshes,
      (plus the special case of Difference with a plane).

Trim Mode
   Geometry can be either added or removed by choosing one of these modes.

   :Difference:
      Removes geometry, filling any holes that are created.
   :Union:
      Creates a geometry and joins any intersections with existing geometry.
   :Join:
      Similar to *Union* but joins the mesh as separate geometry,
      without performing any Boolean operations with existing geometry.

Shape Orientation
   The method used to orientate the trimming shape.

   :View:
      Use the view to orientate the trimming shape.
   :Surface:
      Use the surface normal to orientate the trimming shape.

Extrude Mode
   :Fixed:
      Aligns new geometry orthogonally for 90 degree angles in depth.
   :Project:
      Aligns new geometry with the perspective of the current view for a tapered result.

Use Cursor for Depth
   Use cursor location and radius for the dimensions and position of the trimming shape.
   If not set, the tool uses the full depth of the object from the camera view.
