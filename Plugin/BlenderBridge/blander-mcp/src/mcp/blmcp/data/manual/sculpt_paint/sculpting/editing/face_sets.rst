.. _sculpting-editing-facesets:

*********
Face Sets
*********

This page details the face set related hotkey operators and menu operators in sculpt mode.


.. tip::

   There is a face set pie menu that can be accessed with :kbd:`Alt-W`.


.. _bpy.ops.sculpt.face_sets_create:

Face Set from Masked
====================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Face Set from Masked`

Creates a new face set from :ref:`Masked Geometry <sculpt-mask-menu>`.


Face Set from Visible
=====================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Face Set from Visible`

Creates a new face set from all visible geometry.


Face Set from Edit Mode Selection
=================================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Face Set from Edit Mode Selection`

Creates a new face set corresponding to the Edit Mode face selection.


.. _bpy.ops.sculpt.face_sets_init:

Initialize Face Sets
====================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Initialize Face Sets`

Initializes all face sets on the mesh at once based off one of several mesh attribute properties.

Mode
   The mesh data attribute used to define the boundaries for the face sets.

   :By Loose Parts: Creates a new face set per discontinuous part of the mesh.
   :By Face Set Boundaries:
      Creates a face set for each isolated face set.
      This mode is useful for splitting the patterns created by :ref:`Face Set Expand <face_set_expand>`
      into individual Face Sets for further editing.
   :By Materials: Creates a face set per :ref:`Material Slot <bpy.types.MaterialSlot>`.
   :By Normals: Creates face sets for Faces that have similar :ref:`Normals <modeling-meshes-structure-normals>`.
   :By UV Seams: Creates face sets using :doc:`UV Seams </modeling/meshes/uv/unwrapping/seams>` as boundaries.
   :By Edge Creases: Creates face sets using :ref:`Edge Creases <bpy.ops.transform.edge_crease>` as boundaries.
   :By Edge Bevel Weight:
      Creates face sets using :ref:`Bevel Weights <bpy.ops.transform.edge_bevelweight>` as boundaries.
   :By Sharp Edges: Creates face sets using :ref:`Sharp Edges <bpy.ops.mesh.mark_sharp>` as boundaries.

Threshold
   The minimum value to consider a certain attribute a boundary when creating the face sets.


.. _bpy.ops.sculpt.face_set_edit:

Grow/Shrink Face Sets
=====================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Grow/Shrink Face Sets`
   :Tool:      :doc:`/sculpt_paint/sculpting/tools/edit_face_set`
   :Shortcut:  :kbd:`Ctrl-W`, :kbd:`Ctrl-Alt-W`

Expands or contracts the face set under the cursor by adding or removing surrounding faces.


.. _bpy.ops.mesh.face_set_extract:


Expand Face Set
===============

.. note::

   More info on Face Set Expand at the :ref:`Expand page <bpy.ops.sculpt.expand>`.


Extract Face Set
================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Extract Face Set`

Creates a new mesh based on the selected face set.
Once the operator is initiated, hover over the face set and :kbd:`LMB` to create the new mesh.
After the operator is finished the new mesh will be selected in Object Mode.


.. _bpy.ops.sculpt.face_sets_randomize_colors:

Randomize Colors
================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Face Sets --> Randomize Colors`

Generates a new set of random colors to render the face sets in the 3D Viewport.


Display Settings
================

.. reference::

   :Mode:      Sculpt Mode
   :Popover:   :menuselection:`Viewport Overlays -- Sculpt --> Face Sets`

The face sets display can be toggled as a :doc:`viewport overlay </editors/3dview/display/overlays>`.
In the overlay popover, the opacity of the face sets overlay can be adjusted
to make it more or less visible on the mesh.
