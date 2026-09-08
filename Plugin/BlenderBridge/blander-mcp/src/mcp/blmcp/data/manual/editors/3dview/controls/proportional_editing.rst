.. _bpy.types.ToolSettings.use_proportional_edit_objects:
.. _bpy.types.ToolSettings.use_proportional_edit:

********************
Proportional Editing
********************

.. reference::

   :Mode:      Object and Edit Mode
   :Location:  :menuselection:`Header --> Proportional Editing`
   :Shortcut:  :kbd:`O`

.. figure:: /images/editors_3dview_controls_proportional-editing_tool.png
   :align: right
   :width: 250px

   Proportional Editing popover.

Proportional Editing is a way of transforming selected elements while also affecting
the nearby unselected elements. The farther away an unselected element is, the less it will be affected
(hence the "proportional"). This feature is very useful for smoothly deforming dense meshes.

.. note::

   Blender also has a :ref:`painting-sculpting-index` workflow
   that contains brushes and tools for proportionally editing a mesh without seeing the individual vertices.


Controls
========

Disable :kbd:`O`
   Proportional Editing is off, only selected vertices will be affected.
Enable :kbd:`O`
   Vertices other than the selected vertex are affected, within a defined radius.


.. _bpy.types.ToolSettings.proportional_distance:

Proportional Size
-----------------

You can increase or decrease the radius of the tool's influence during a transform operation
from the Proportional Editing popover or with :kbd:`WheelUp`/:kbd:`WheelDown`, or :kbd:`PageUp`/:kbd:`PageDown`
respectively. As you change the radius, the points surrounding your selection will adjust their positions
accordingly.

.. figure:: /images/editors_3dview_controls_proportional-editing_influence.png
   :align: center

   Influence circle.


.. _bpy.types.ToolSettings.proportional_edit_falloff:

Falloff
-------

While editing, you can change the curve profile by either clicking the *Falloff* icon in the header
or pressing :kbd:`Shift-O` to get a pie menu.

.. list-table::
   :widths: 1 1 1

   * - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-constant.png

          Constant, No Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-random.png

          Random Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-linear.png

          Linear Falloff.

   * - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-sharp.png

          Sharp Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-root.png

          Root Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-sphere.png

          Sphere Falloff.

   * - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-smooth.png

          Smooth Falloff.

     - .. figure:: /images/editors_3dview_controls_proportional-editing_falloff-inverse-square.png

          Inverse Square Falloff.

     -


Object Mode
===========

Proportional Editing is typically used in *Edit Mode*, but it can also be used in *Object Mode*.
The tool then works on entire objects rather than individual mesh components.

In the image below, the leftmost cylinder is being scaled up vertically,
which also affects the cylinders near it.

.. figure:: /images/editors_3dview_controls_proportional-editing_object-mode.png
   :width: 50%
   :align: center

   Proportional Editing in Object Mode.


Edit Mode
=========

When working with dense geometry, it can become difficult to make subtle adjustments
without causing visible lumps and creases in the model's surface.
When you face situations like this, Proportional Editing can help.

.. figure:: /images/editors_3dview_controls_proportional-editing_mode.png
   :align: center

   Proportional Editing in Edit Mode.


Options
-------

.. _bpy.types.ToolSettings.use_proportional_connected:

Connected Only :kbd:`Alt-O`
   Rather than using a radius only, the proportional falloff spreads via connected geometry.
   This means that you can proportionally edit the vertices in a finger of a hand
   without affecting the other fingers. While the other vertices are physically close (in 3D space),
   they are far away following the topological edge connections of the mesh.
   The icon will have a blue center when *Connected* is active.
   This mode is only available in *Edit Mode*.

.. _bpy.types.ToolSettings.use_proportional_projected:

Projected from View
   Depth along the view is ignored when applying the radius.

   .. figure:: /images/editors_3dview_controls_proportional-editing_2d-compare.png

      The difference between having "Projected from View" disabled (left) and enabled (right).


Example
=======

The image below shows the final render of a low-poly landscape
obtained by moving up the vertices of a triangulated grid
with *Proportional Editing* enabled.

.. figure:: /images/editors_3dview_controls_proportional-editing_landscape.jpg

   A landscape obtained via Proportional Editing.
