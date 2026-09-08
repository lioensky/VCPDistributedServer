.. index:: Object Constraints; Transformation Constraint
.. _bpy.types.TransformConstraint:

*************************
Transformation Constraint
*************************

This constraint is more complex and versatile than the other "transform" constraints.
It lets you set the location, rotation or scale of an object/bone based on the
location, rotation or scale of another, mixing and matching axes as you see fit.
An example could be to set a gear's X rotation based on the Y coordinate of
a rail next to it.

The constraint works with input and output value ranges, one for each axis.
It first clamps the input value to the *Map From* range, then offsets and scales it
to the corresponding *Map To* range. This lets you, say, map a Y coordinate
in the range (-3m, 3m) to an X rotation in the range (0, 180°).


Options
=======

.. figure:: /images/animation_constraints_transform_transformation_panel.png

   Transformation constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone to retrieve the transformation from.

Extrapolate
   By default, the input and output values are clamped to the *Min/Max* values.
   When you enable *Extrapolate*, they're allowed to go beyond these limits.
   This is illustrated with the graphs below, where the X axis represents the input
   (*Map From* set to *Min* = 1 and *Max* = 4) and the Y axis represents the output
   (*Map To* set to *Min* = 1 and *Max* = 2).

   .. _fig-constraints-transformation-extrapolate:

   .. list-table:: The Extrapolate option.

      * - .. figure:: /images/animation_constraints_transform_transformation_extrapolate-1.png

             Extrapolate disabled: the output values are limited to the Map To range.

        - .. figure:: /images/animation_constraints_transform_transformation_extrapolate-2.png

             Extrapolate enabled: the output values can extend beyond the limits.

:ref:`Target/Owner <rigging-constraints-interface-common-space>`
   The spaces for retrieving the transformation from the target and for applying it to the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.

Map From
--------

The transformation to read from the *Target*.

Location, Rotation, Scale
   The type of transformation to read.

Mode :guilabel:`Rotation`
   The type of rotation to use, including different :term:`Euler` orders,
   :term:`Quaternion`, and other :ref:`Rotation Channel Modes <drivers-variables-rotation-modes>`.
   Defaults to using the :term:`Euler` order of the constraint owner.

   In the *Quaternion* mode, the channels are converted to weighted angles in the same way as
   the swing angles of the :ref:`Swing and X/Y/Z Twist <drivers-variables-rotation-modes>` modes.

X/Y/Z Min, Max
   The input value range for each axis.


Map To
------

The transformation to apply to the owner.

Location, Rotation, Scale
   The type of transformation to apply.

Order :guilabel:`Rotation`
   Which :term:`Euler` order to use. Defaults to the order of the constraint owner.

X/Y/Z Source Axis
   For each of the three output axes, lets you choose the input axis that it should take
   its value from. You can select the same input axis multiple times.

Min, Max
   The output value range for each axis.

Mix
   Specifies how the result of the constraint is combined with the existing transformation.
   The set of available choices varies based on the type of transformation.

   Replace
      The result of the constraint replaces the existing transformation.
   Multiply :guilabel:`Scale`
      The new values are multiplied with the existing axis values.
   Add :guilabel:`Location` :guilabel:`Rotation`
      The new values are added to the existing axis values.
   Before Original :guilabel:`Rotation`
      The new rotation is added before the existing rotation, as if it were applied to
      a parent of the constraint owner.
   After Original :guilabel:`Rotation`
      The new rotation is added after the existing rotation, as if it were applied to
      a child of the constraint owner.

.. note::

   - For historical reasons, the *Mix* mode defaults to *Add* for location and rotation,
     and *Replace* for scale.
   - When using the rotation of the target as input,
     whatever the real values are, the constraint will always "take them back" into the (-180 to 180) range.
     E.g. if the target has a rotation of 420 degrees around its X axis,
     the values used as *X* input by the constraint will be:

     :math:`((420 + 180) modulo 360) - 180 = 60 - 180 = -120`

     As such, this constraint is not really suited for transforming an object based on a gear's rotation.
     Rotating a gear based on an object's transformation works fine, however.
   - Similarly, when using the scale transform properties of the target as input,
     whatever the real values are, the constraint will always take their absolute values (i.e. invert negative ones).
   - When a *Min* value is higher than its corresponding *Max* one,
     both are considered equal to the *Max* one. This means you cannot create "reversed" mappings.


Example
=======

In the following example, we add a constraint to a gear that sets its X rotation based on the
Y position of a rail:

- Target: Rail object

- Map From: Location

  - Y Min: -3m
  - Y Max: 3m

- Map To: Rotation

  - X Source Axis: Y
  - X Min: 0°
  - X Max: 180°

.. figure:: /images/animation_constraints_transform_example_before.png

   Before moving the rail.

.. figure:: /images/animation_constraints_transform_example_after.png

   After moving the rail.

By default, the gear will stop rotating if the rail goes outside the (-3m, 3m) range.
You can enable *Extrapolate* to change this.
