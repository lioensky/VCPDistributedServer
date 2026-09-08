.. _tool-mesh-loop_cut:

********
Loop Cut
********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Loop Cut`
   :Shortcut:  :kbd:`Ctrl-R`

The *Loop Cut* tool is a modal tool version of the :ref:`bpy.ops.mesh.loopcut_slide` operator.
This tool splits a loop of faces by inserting new edge loops intersecting the chosen edge.


Usage
=====

The tool is interactive and has two steps:

#. Pre-Visualizing the Cut

   After the tool is activated, move the cursor over a desired edge.
   The cut to be made is marked with a magenta colored line as you move the mouse over the various edges.
   The to be created edge loop stops at the poles (triangles and n-gons) where the existing face loop terminates.

#. Perform the Cut

   Once the desired location of the new edge loop is found, the edge loop can be created via :kbd:`LMB`.

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_loop_before.png

          Mesh before inserting edge loop.

     - .. figure:: /images/modeling_meshes_tools_loop_preview.png

          Preview of edge loop location.

     - .. figure:: /images/modeling_meshes_tools_loop_placement.png

          Interactive placement of edge loop between adjacent loops.


Tool Settings
=============

Number of Cuts
   Increases and decreases the number of cuts to create.
   These cuts are uniformly distributed in the original face loop,
   and you will *not* be able to control their positions.

Correct UVs
   Corrects the corresponding UV coordinates, if these exist, to avoid image distortions.


Options
=======

After the modal tool is run
the :ref:`Loop Cut and Slide Options <modeling-meshes-editing-edge-loopcut-slide-options>`
are available in the :ref:`bpy.ops.screen.redo_last` panel.
