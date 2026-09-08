.. index:: Object Constraints; Stretch To Constraint
.. _bpy.types.StretchToConstraint:

*********************
Stretch To Constraint
*********************

The *Stretch To* constraint makes an object or bone point at, and scale towards,
a target. Unlike the other "track" constraints, it can only do this using the local Y axis,
making it mainly useful for bones.

The constraint can also perform "volume preservation," making the owner thinner when the
target moves away and thicker when it comes closer. This is useful for stretching
and squashing of stylized characters, for example. However, because it simply
adjusts the X and Z scales according to the Y scale, it works for any type of object,
not just meshes.


Options
=======

.. figure:: /images/animation_constraints_tracking_stretch-to_panel.png

   Stretch To constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone to stretch towards.

Original Length
   The rest distance between owner and target, i.e.
   the distance at which there is no stretching of the owner.

   :bl-icon:`x` (Reset Original Length)
      Sets the *Original Length* to the current distance between owner and target.

.. _constraints-stretch-to-volume-preservation:

Volume Variation
   Exponent that either exaggerates (> 1) or reduces (< 1) the thickness change caused
   by volume preservation. Setting this to 0 is the same as setting *Maintain Volume* to
   *None*.

Volume Min, Max
   Lower and upper limits for the thickness factor applied by volume preservation.

   If *Maintain Volume* is set to XZ, the X and Z factors are each bound to the square
   root of these limits. For example, if *Volume Max* is set to 4, both the X and Z scale
   can grow to no more than twice their original value.

   If *Maintain Volume* is set to X or Z, the factor for the chosen axis is bound to these
   limits. In the above example, the axis could grow to no more than 4 times its original value
   (while the other axis would not grow or shrink at all).

Smooth
   A higher value will slow down the thickness change as it approaches the limits.
   This prevents an abrupt stop once the limits are reached.

Maintain Volume
   Whether to make the owner thicker/thinner as it contracts/stretches to meet the target.

   :XZ: Scale along both the X and Z axes.
   :X: Scale along the X axis only.
   :Z: Scale along the Z axis only.
   :None: Don't change the X and Z scales.

   .. seealso::

      :doc:`/animation/constraints/transform/maintain_volume`

Rotation
   How the owner should be rotated to track the target with its Y axis.

   :XZ: Tries to keep the local X axis close to its original orientation.
   :ZX: Tries to keep the local Z axis close to its original orientation.
   :Swing:
      Uses a :term:`swing` rotation, much like the :doc:`/animation/constraints/tracking/damped_track`.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 50ecc2bc-44e1-4c5f-a3fc-6353a4624f0d
