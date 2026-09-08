.. index:: Object Constraints; Maintain Volume Constraint
.. _bpy.types.MaintainVolumeConstraint:

**************************
Maintain Volume Constraint
**************************

The *Maintain Volume* constraint ensures that an object or bone keeps its
original volume by automatically scaling down two axes when another axis
is scaled up (and vice versa). This can be useful for stretching and squashing
stylized characters, for example.


Options
=======

.. figure:: /images/animation_constraints_transform_maintain-volume_panel.png

   Maintain Volume constraint.

Mode
   Specifies how the constraint handles scaling of the non-free axes.

   :Strict:
      Adjusts the scales of the non-free axes so that the volume is always exactly maintained.
      Scaling up the free axis will scale down both non-free axes. Scaling up a non-free axis
      will scale down the other non-free axis.
   :Uniform:
      Unlike *Strict*, this mode only maintains the volume correctly as long as the object
      is scaled equally along all three axes.

      Scaling up the free axis alone will also scale down the non-free axes, but
      in an exaggerated manner that results in a loss of volume. As such, this is
      not recommended.

      Scaling up a non-free axis has no effect on the other non-free axis. This
      makes it possible to deviate from the target volume.
   :Single Axis:
      Similar to *Uniform*, except the mode only maintains the volume correctly as long
      as the object is scaled purely along the free axis. Because only one axis needs to
      be adjusted to keep the volume instead of three, this may reduce the number of
      animation curves needed.

      Changing the scale of a non-free axis again has no effect on the other non-free axis.

Free Axis
   The axis that should keep its user-specified scale. The other two (non-free) axes will
   be adjusted to maintain the volume.

Volume
   The target volume as a ratio of the original volume (when all axes have a scale of 1).

   If all three axes have a default scale of 2 and this should be maintained, *Volume* should
   be set to 2×2×2 = 8.

:ref:`Owner <rigging-constraints-interface-common-space>`
   The space for determining and adjusting the scale of the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: 8f39c857-6e59-43d7-86a0-c0aa4549202f
