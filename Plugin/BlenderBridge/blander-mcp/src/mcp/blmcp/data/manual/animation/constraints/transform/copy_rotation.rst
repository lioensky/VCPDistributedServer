.. index:: Object Constraints; Copy Rotation Constraint
.. _bpy.types.CopyRotationConstraint:

************************
Copy Rotation Constraint
************************

The *Copy Rotation* constraint forces an object or bone to match the rotation of a target.
As a side effect, it also removes shearing.

Options
=======

.. figure:: /images/animation_constraints_transform_copy-rotation_panel.png

   Copy Rotation constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The object or bone whose rotation to copy.

Order
   The :term:`Euler` order to use during the copy operation.
   Defaults to the order of the owner.

Axis
   The axes for which to copy rotation angles.

Invert
   The axes for which invert the sign (so an angle of 10° becomes -10° and vice versa).

Mix
   Specifies how the target's current rotation (from all its constraints)
   is combined with the owner's original rotation (from its preceding constraints).

   :Replace:
      The target's angles replace the owner's.
   :Add:
      The target angles are added to the owner's.
   :Before Original:
      The target's rotation is applied before the owner's. The result is the same as
      the owner's rotation if it were a child of the target and there was no constraint.
   :After Original:
      The target's rotation is applied after the owner's. The result is the same as
      the target's rotation if it were a child of the owner and there was no constraint.
   :Offset (Legacy):
      This replicates the behavior of the original Offset checkbox. It was intended
      to be similar to *Before Original*, but does not work correctly with multiple axes
      and is thus deprecated.

:ref:`Target/Owner <rigging-constraints-interface-common-space>`
   The spaces for retrieving the angles from the target and for applying them to the owner.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.


Example
=======

.. peertube:: e28df5a9-3947-4c26-8969-5c8e029cd52e
