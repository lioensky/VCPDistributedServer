
*********
Face Data
*********

.. _bpy.ops.mesh.colors_rotate:

Rotate Colors
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Rotate Colors`

Rotates the colors for the active
:ref:`Color Attribute <modeling-meshes-properties-object_data-color-attributes>`
inside each selected face either clockwise or counterclockwise.


.. _bpy.ops.mesh.colors_reverse:

Reverse Colors
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Reverse Colors`

Mirrors the colors for the active Color Attribute inside each selected face.


Rotate UVs
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Rotate UVs`

See :ref:`bpy.ops.mesh.uvs_rotate`.


Reverse UVs
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Reverse UVs`

See :ref:`bpy.ops.mesh.uvs_reverse`.


.. _bpy.ops.mesh.flip_quad_tessellation:

Flip Quad Tessellation
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Flip Quad Tessellation`

Internally, every :term:`quad` is :term:`tessellated <Tessellation>` into two triangles.
This operator swaps the tesselation direction of the selected quads.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_flip-tesselation_before.png
     - .. figure:: /images/modeling_meshes_editing_face_flip-tesselation_after.png

.. seealso::

   :doc:`/modeling/meshes/editing/edge/rotate_edge`

.. _bpy.ops.mesh.mark_freestyle_face:

Mark/Clear Freestyle Face
=========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Mark/Clear Freestyle Face`

Marks or unmarks the selected faces as requiring special Freestyle behavior.
See :ref:`freestyle-face-marks`.
