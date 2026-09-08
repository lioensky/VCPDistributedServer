.. _bpy.ops.mesh.edges_select_sharp:

******************
Select Sharp Edges
******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Sharp Edges`

Adds edges at sharp corners to the selection.

.. note::
   This operator does not deal with edges that were manually :ref:`marked as Sharp <bpy.ops.mesh.mark_sharp>`.
   To select those, first select one Sharp edge by hand, then use
   :menuselection:`Select --> Select Similar --> Sharpness` to add the others.

Options
=======

Sharpness
   The minimum angle for an edge between two faces to be considered sharp. The angle is measured between
   the face normals, meaning that coplanar faces have an angle of 0° (not 180°) and sharp corners have
   greater angles than dull ones (not smaller).
