.. index:: Grease Pencil Modifiers; Vertex Weight Angle Modifier
.. _bpy.types.GreasePencilWeightAngleModifier:

****************************
Vertex Weight Angle Modifier
****************************

This modifier sets the weights of the given vertex group,
based on a predetermined angle.

.. warning::

   This modifier does implicit clamping of weight values in the standard (0.0 to 1.0) range.
   All values below 0.0 will be set to 0.0, and all values above 1.0 will be set to 1.0.


Options
=======

.. figure:: /images/grease-pencil_modifiers_modify_weight-angle_panel.png
   :align: center

   The Vertex Weight Angle modifier panel.

Vertex Group
   The vertex group to affect.

   :bl-icon:`arrow_leftright` Invert
      Inverts the influence of the selected vertex group. The setting reverses the weight values of the group.

Angle
   Sets the angle for the maximum weights value.

Axis
   The axis along which the angle affects the weights.

   X, Y, Z

Space
   Coordinate space to be used.

Minimum
   Minimum value for vertex weight.

Multiply Weights
   Multiply the calculated weights with the existing values in the vertex group.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
