.. _bpy.ops.mesh.select_nth:

****************
Checker Deselect
****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Checker Deselect`

Deselects mesh elements in a repeating pattern, starting at the active element.
The type of element that gets deselected (vertices, edges, or faces) depends on the
current selection mode.

If there are multiple disconnected "islands" in the selection, this tool will only affect
the one containing the active element.

Options
=======

Deselected
   The number of elements to deselect at the start of each pattern repetition.
Selected
   The number of elements to keep selected at the end of each pattern repetition.
Offset
   The number of elements to skip in the pattern in its first repetition.

Example
=======

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/modeling_meshes_selecting_checker-deselect-before.png

          Initial selection.

     - .. figure:: /images/modeling_meshes_selecting_checker-deselect-after-1.png

          Running with Deselected = 1 and Selected = 1.

     - .. figure:: /images/modeling_meshes_selecting_checker-deselect-after-2.png

          Deselected changed to 2.