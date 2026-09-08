
**************
Control Points
**************

Extrude Curve and Move
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Extrude Curve and Move`
   :Shortcut:  :kbd:`E`

Extrudes points by duplicating the selected points, which then can be moved,
and connecting those points back to the original curve creating a continuous curve.


.. _bpy.ops.curves.handle_type_set:

Set Handle Type
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Control Points --> Set Handle Type`
   :Shortcut:  :kbd:`V`

Handle types are a property of :ref:`Bézier curves <curve-bezier>` and
can be used to alter features of the curve.
For example, switching to *Vector handles* can be used to create curves with sharp corners.
Read the :ref:`Bézier curves <curve-bezier-handle-type>` page for more details.

Type
   The handle type to switch to.

   :Auto:
      This handle has a completely automatic length and direction
      which is set by Blender to ensure the smoothest result.
      These handles convert to *Align* handles when moved.
   :Vector:
      Both parts of a handle always point to the previous handle or the next handle which allows
      you to create curves or sections thereof made of straight lines or with sharp corners.
      Vector handles convert to *Free* handles when moved.
   :Align:
      These handles always lie in a straight line,
      and give a continuous curve without sharp angles.
   :Free:
      The handles are independent of each other.
   :Toggle Free/Align:
      Replaces Free handles with Align, and all Align with Free handles.


.. _modeling-curves-tilt:

Tilt
====

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Tilt`
   :Shortcut:  :kbd:`Ctrl-T`

This setting controls how the normals twist around each control point.
The tilt will be interpolated from point to point (you can check it with the normals).


.. _bpy.ops.curves.tilt_clear:

Clear Tilt
==========

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Alt-T`

You can also reset the tilt to its default value (i.e. perpendicular to the original curve plane).
