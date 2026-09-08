
************
Introduction
************

*Curves Sculpt Mode* allows working with curves using various brushes.
It is commonly used for hair grooming, but can be used with all kinds of curves.

The curves' surface object plays an important role in many curves sculpting brushes.
Most brushes such as :doc:`Add Curves </sculpt_paint/curves_sculpting/brushes/add_curves>`
require the surface to be set already.

.. note::

    Curves Sculpt tools only use the original mesh of the surface object and don't take its modifiers into account.


Curves Menu
===========

.. _bpy.ops.curves.snap_curves_to_surface:

Snap to Deformed Surface
   Re-attach curves to a deformed surface using the existing attachment information.
   This only works when the topology of the surface mesh has not changed.

Snap to Nearest Surface
   Find the closest point on the surface for the root point of every curve and move the root there.
   This needs to be run after the surface mesh topology changed

.. _bpy.ops.curves.convert_to_particle_system:

Convert to Particle System
   Add a new hair particle system, or update an system on the surface object.
   The operator is used for backwards compatibility with the old
   :doc:`hair type particle system </physics/particles/hair/introduction>`.


Selection Modes
===============

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`3D Viewport Header --> Select Mode`
   :Shortcut:  :kbd:`1`, :kbd:`2`

Selection modes limits selection operators to certain curve domains.
This feature is makes it easy to select whole segments at once, or to give more granular control over editing.

:Control Points:
   Allows selection of individual control points.
:Curve:
   Limits selection to whole curve segments.


Select Menu
===========

All
   Select all control points or curves.

None
   Deselect all control points or curves.

Invert
   Invert the selection.

.. _bpy.ops.sculpt_curves.select_random:

Random
   Randomizes inside the existing selection or create new random selection if nothing is selected already.

.. _bpy.ops.curves.select_ends:

Endpoints
   Select endpoints of curves.
   Only supported in the Control Point selection mode.

   Amount Start, End
      Number of points to select from the front or back of the curve.

.. _bpy.ops.sculpt_curves.select_grow:

Grow
   Select points or curves which are close to already selected elements.


Controls
========

Sculpt mode provides several properties that give advanced control of the tool's behavior.
These options can be found in the right-hand side of the 3D Viewport's Header.

.. _bpy.types.Curves.use_mirror_z:

Mirror
   Allows tools to affect curves symmetrically according to the chosen axis.

.. _bpy.types.Curves.use_sculpt_collision:

Use Sculpt Collision
   Prevents the curve segments from passing through the :ref:`Surface Object <bpy.types.Curves.surface>`.


Display
=======

Overlays
--------

.. _bpy.types.View3DOverlay.show_sculpt_curves_cage:
.. _bpy.types.View3DOverlay.sculpt_curves_cage_opacity:

Cage Opacity
   Shows the original curves that are currently being edited
   which is useful with when procedural deformations or child curves are used.
