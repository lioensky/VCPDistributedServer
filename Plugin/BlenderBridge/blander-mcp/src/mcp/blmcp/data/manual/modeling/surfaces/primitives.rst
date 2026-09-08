.. _bpy.ops.surface.primitive*add:

******************
Surface Primitives
******************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Menu:      :menuselection:`Add --> Surface`
   :Shortcut:  :kbd:`Shift-A`

.. seealso::

   After adding a primitive, you can change :ref:`options <object-common-options>`
   such as its radius.

The *Add Surface* menu offers the following primitives:

.. list-table::

   * - .. figure:: /images/modeling_surfaces_primitives_curve.png

          NURBS curve primitives.

     - .. figure:: /images/modeling_surfaces_primitives_surface.png

          NURBS surface primitives.


NURBS Curve
   Adds a simple curve of four control points forming an arc.

NURBS Circle
   Adds a closed loop of control points forming a circle.

NURBS Surface
   Adds a simple surface patch consisting of a 4×4 grid with the center points slightly raised.

NURBS Cylinder
   Adds an open cylinder, consisting of an extruded *NURBS Circle*.

NURBS Sphere
   Adds a generic sphere constructed from control points arranged in a cube.

NURBS Torus
   Adds a doughnut-shaped primitive created by rotating a circle around an axis.
