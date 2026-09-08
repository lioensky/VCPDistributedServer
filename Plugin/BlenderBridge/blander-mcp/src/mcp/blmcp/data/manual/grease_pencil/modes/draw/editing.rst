******************
Drawing Operations
******************

Active Layer
============

.. reference::

   :Mode:      Draw Mode
   :Menu:      :menuselection:`Draw --> Active Layer`
   :Shortcut:  :kbd:`Y`

Select the active layer.


Animation
=========

.. reference::

   :Mode:      Draw Mode
   :Menu:      :menuselection:`Draw --> Animation`
   :Shortcut:  :kbd:`I`

The stroke animation operations are described in the :doc:`Animation </grease_pencil/animation/tools>` section.


Interpolate Sequence
====================

.. reference::

   :Mode:      Draw Mode
   :Menu:      :menuselection:`Draw --> Interpolate Sequence`

See :ref:`bpy.ops.grease_pencil.interpolate_sequence`.


.. _bpy.ops.grease_pencil.erase_lasso:

Erase Lasso
===========

.. reference::

   :Mode:      Draw Mode
   :Shortcut:  :kbd:`Ctrl-Alt-RMB`

The *Erase Lasso* operator erases all Grease Pencil strokes within a freeform selection.

- Press and hold :kbd:`Ctrl-Alt-RMB`, then draw a lasso shape around the area you want to erase.
- Release the mouse button to apply the eraser.
- Only points within the lasso region are removed.


.. _bpy.ops.grease_pencil.erase_box:

Box Erase
=========

.. reference::

   :Mode:      Draw Mode
   :Shortcut:  :kbd:`B`

The *Box Erase* operator erases all Grease Pencil strokes within a rectangular selection.

- Press :kbd:`B`, then click and drag to define a rectangular area.
- Release the mouse button to apply the eraser.
- All points of strokes within the box are removed.
