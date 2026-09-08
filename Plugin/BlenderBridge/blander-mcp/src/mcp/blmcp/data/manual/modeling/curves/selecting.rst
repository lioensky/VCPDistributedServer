
************************
Selecting Curve Elements
************************

This page discusses specific selecting tools for curve objects in Edit Mode.
The Curve Edit more also uses the general select tools used which are described
in the :doc:`interface section </interface/selecting>`.

Curve selection in *Edit Mode* has fewer options than with meshes.
Mainly this is, because there is only one selectable element type, the control points
(no select mode needed here...). These points are a bit more complex than simple vertices,
however, especially for Bézier curves, as there is the central vertex, and its two handles...

The basic tools are the same as with :doc:`meshes </modeling/meshes/selecting/index>`,
so you can select a simple control point with the :kbd:`LMB`,
add to current selection with :kbd:`Shift-LMB`, Box Select :kbd:`B`, and so on.

One word about the Bézier control points: when you select the main central vertex,
the two handles are automatically selected too, so you can move it as a whole,
without creating an angle in the curve. However, when you select a handle,
only this vertex is selected, allowing you to modify this control vector...

Note that, unlike mesh edges, you cannot directly select a segment. Instead,
select all of the control points that make up the segment you want to edit.


Select Menu
===========

With curves, all "advanced" selection options are grouped
in the *Select* menu of the 3D Viewport header.


.. _bpy.ops.curve.select_all:

All
===

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> All`
   :Shortcut:  :kbd:`A`

Select all selectable elements.


None
====

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> None`
   :Shortcut:  :kbd:`Alt-A`

Deselect all elements, but the active element stays the same.


Invert
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Invert`
   :Shortcut:  :kbd:`Ctrl-I`

Selects all the geometry that are not selected, and deselect currently selected components.


Box Select
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`

Interactive :ref:`box selection <tool-select-box>`.


Circle Select
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Circle Select`
   :Shortcut:  :kbd:`C`

Interactive :ref:`circle selection <tool-select-circle>`.


Lasso Select
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Lasso Select`
   :Shortcut:  :kbd:`Ctrl-Alt-LMB`

See :ref:`tool-select-lasso`.


.. _bpy.ops.curve.select_random:

Select Random
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Random`

Select Random control points.

Percent
   Selects the defined percentage of control points.
Random Seed
   :term:`Seed` used by the pseudo-random number generator.
Action
   Controls whether the operator *Selects* or *Deselects* control points.


.. _bpy.ops.curve.select_nth:

Checker Deselect
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Checker Deselect`

This tool applies an alternating selected/deselected checker pattern.
This only works if you already have more than one control point selected.

It works by changing the current selection so that only every Nth
control points will remain selected, starting from the active one.

Deselected
   The number of deselected elements in each pattern repetition.
Selected
   The number of selected elements in each pattern repetition.
Offset
   Offset from the starting point.


.. _bpy.ops.curve.select_more:
.. _bpy.ops.curve.select_less:

Select More/Less
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> More/Less`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus`, :kbd:`Ctrl-NumpadMinus`

Their purpose, based on the currently selected control points, is to reduce or enlarge this selection.

More
   For each selected control point, select *all* its linked points (i.e. one or two...).
Less
   For each selected control point, if *all* points linked to this point are selected, keep this one selected.
   Otherwise, deselect it.

This implies two points:

#. When *all* control points of a curve are selected, nothing will happen
   (as for *Less*, all linked points are always selected, and of course, *More* cannot add any).
   Conversely, the same goes when no control points are selected.
#. Second, these tools will never "go outside" of a curve
   (they will never "jump" to another curve in the same object).


.. _bpy.ops.curve.select_linked:

Select Linked
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Linked`
   :Shortcut:  :kbd:`Ctrl-L`

Selects all control points connected to the active control point.

This operator makes it easier to select or deselect entire segments of a curve, especially in
dense or complex curves, where manually selecting each point would be time-consuming.


.. _bpy.ops.curve.select_linked_pick:

Select Linked Pick
------------------

.. reference::

   :Mode:      Edit Mode
   :Hotkeys:  :kbd:`L`, :kbd:`Shift-L`

Selects (:kbd:`L`) or deselects (:kbd:`Shift-L`) control points
connected to the control point nearest the mouse cursor.

.. note::

   For Bézier curves with a handle selected,
   this selection operator will select the whole control point **and** all the linked ones.


.. _bpy.ops.curve.select_similar:

Select Similar
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Similar`
   :Shortcut:  :kbd:`Shift-G`

Selects control points that have certain similar properties to the active one.
The :ref:`bpy.ops.screen.redo_last` panel provides several selection options:

Type
   Type
      Selects splines that have the same spline Type i.e. Bézier, NURBS or Poly.
   Radius
      Selects control points that have a similar Radius value.
   Weight
      Selects all points that have a similar Weight value.
   Direction
      Selects control points that have a similar handles direction.

Compare
   For quantitative properties, this property selects the type of comparison to between the two numerical values.

   :Equal: Select items with the same value as the active item's chosen property.
   :Greater: Select items with a larger value as the active item's chosen property.
   :Less: Select items with a smaller value as the active item's chosen property.
Threshold
   For quantitative properties, this property controls how
   close the property's values have to be in the comparison.


.. _bpy.ops.curve.de_select_first:
.. _bpy.ops.curve.de_select_last:

(De)select First/Last
=====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> (De)select First`,
               :menuselection:`Select --> (De)select Last`

These operators will toggle the selection of the first or last control point(s) of the curve(s)
in the object. This is useful to quickly find the start of a curve
(e.g. when using it as path...).


.. _bpy.ops.curve.select_next:
.. _bpy.ops.curve.select_previous:

Select Next/Previous
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Next`, :menuselection:`Select --> Select Previous`

These operators will select the next or previous control point(s),
based on the current selection
(i.e. the control points following or preceding the selected ones along the curve).
In case of a cyclic curve, the first and last points are not considered as neighbors.


Pick Shortest Path
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Menu Search --> Pick Shortest Path`
   :Shortcut:  :kbd:`Ctrl-LMB`

Selects the curve segments between two control points: the active and the one under the cursor.
In the case of a closed curve, the shortest path will be selected.
