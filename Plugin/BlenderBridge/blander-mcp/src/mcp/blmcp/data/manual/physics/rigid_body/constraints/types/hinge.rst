.. index:: Rigid Body Constraints; Hinge Constraint

****************
Hinge Constraint
****************

.. reference::

   :Panel:     :menuselection:`Physics --> Rigid Body Constraint`
   :Type:      Hinge

The hinge permits one degree of freedom between two objects. Translation is completely constrained.
Rotation is permitted about the Z axis of the object hosting the Physics constraint
(usually an :term:`Empty`, distinct from the two objects that are being linked).
Adjusting the position and rotation of the object hosting the constraint allows you to
control the anchor and axis of the hinge.

The Hinge is the only single-axis rotational constraint that uses the Z axis instead of the X axis.
If something is wrong with your hinge, check your other constraints to see if this might be the problem.

.. figure:: /images/physics_rigid-body_constraints_types_hinge_panel-example.png

   *Hinge* constraint options.


Options
=======

Limits
   Z Angle
      Enables/disables limit rotation around Z axis.

      Lower
         Lower limit of Z axis rotation.
      Upper
         Upper limit of Z axis rotation.
