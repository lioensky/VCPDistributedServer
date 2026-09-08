****************
Select More/Less
****************

Select More
===========

.. _bpy.ops.mesh.select_more:

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select More/Less --> More`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus`

Grows the selection to include the elements at its border.
Specifically, this adds the neighbors of the currently selected elements,
with the type of those neighbors (vertices, edges, or faces) depending on the
:doc:`Selection Mode </modeling/meshes/selecting/introduction>`.

Options
-------

Face Step
   Add whole neighboring faces even if they only share a single vertex.

.. figure:: /images/modeling_meshes_selecting_more-less_example.png

   From left to right: initial selection -- Select More -- Face Step enabled

.. _bpy.ops.mesh.select_less:

Select Less
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select More/Less --> Less`
   :Shortcut:  :kbd:`Ctrl-NumpadMinus`

Shrinks the selection to exclude the elements at its border.
Specifically, this deselects elements that have any unselected neighbors,
with the type of those neighbors (vertices, edges, or faces) depending on the
:doc:`Selection Mode </modeling/meshes/selecting/introduction>`.

Options
-------

Face Step
   Deselect elements that share a vertex with an unselected face.

.. _bpy.ops.mesh.select_next_item:

Select Next Active
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select More/Less --> Next Active`
   :Shortcut:  :kbd:`Shift-Ctrl-NumpadPlus`

Selects the element that "logically follows" the two most recently selected ones.

.. list-table::

   * - .. figure:: /images/modeling_meshes_selecting_more-less_select-active-1.png
          :width: 200px

          Initial selection.

     - .. figure:: /images/modeling_meshes_selecting_more-less_select-active-2.png
          :width: 200px

          Using Next Active once.

     - .. figure:: /images/modeling_meshes_selecting_more-less_select-active-3.png
          :width: 200px

          Using Next Active twice.

.. _bpy.ops.mesh.select_prev_item:

Select Previous Active
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select More/Less --> Previous Active`
   :Shortcut:  :kbd:`Shift-Ctrl-NumpadMinus`

Deselects the last selected element and makes the next-to-last one active again.
