
************************
Selecting Curve Elements
************************

Hair curves, while similar to regular curves are a bit different and have their own selection tools.
Many of these match their regular curve tools but are implemented differently
All hair curve selection operators are documented below for completeness.

These selection operators work in both Sculpt and Edit modes.


.. _bpy.ops.curves.set_selection_domain:

Selection Modes
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`3D Viewport Header --> Select Mode`
   :Shortcut:  :kbd:`1`, :kbd:`2`

   Note, this is only supported for "Hair Curves".

Selection modes limits selection operators to certain curve domains.
This feature is makes it easy to select whole segments at once, or to give more granular control over editing.

:Control Points:
   Allows selection of individual control points.
:Curve:
   Limits selection to whole curve segments.


.. _bpy.ops.curves.select_all:

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


.. _bpy.ops.curves.select_random:

Select Random
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Random`

Select Random control points.

Seed
   :term:`Seed` used by the pseudo-random number generator.
Probability
   Selects the defined percentage of control points.


.. _bpy.ops.curves.select_more:
.. _bpy.ops.curves.select_less:

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


.. _bpy.ops.curves.select_linked:

Select Linked
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Linked`
   :Shortcut:  :kbd:`Ctrl-L`

Selects all control points connected to the active control point.

This operator makes it easier to select or deselect entire segments of a curve, especially in
dense or complex curves, where manually selecting each point would be time-consuming.


.. _bpy.ops.curves.select_linked_pick:

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


Select Endpoints
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Endpoints`

Select endpoints of curves.

*Only supported in the Control Point selection mode.*
