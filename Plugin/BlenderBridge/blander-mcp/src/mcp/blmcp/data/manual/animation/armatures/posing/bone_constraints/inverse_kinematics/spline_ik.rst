
*********
Spline IK
*********

Spline IK is a constraint which aligns a chain of bones along a curve. By leveraging the ease
and flexibility of achieving aesthetically pleasing shapes offered by curves and
the predictability and well-integrated control offered by bones,
Spline IK is an invaluable tool in the riggers' toolbox.
It is particularly well suited for rigging flexible body parts such as tails, tentacles,
and spines, as well as inorganic items such as ropes.

Full description of the settings for the spline IK can be found on
the :doc:`Spline IK </animation/constraints/tracking/spline_ik>` page.


Basic Setup
===========

The Spline IK Constraint is not strictly an *Inverse Kinematics* method (i.e. IK Constraint),
but rather a *Forward Kinematics* method (i.e. normal bone posing). However,
it still shares some characteristics of the IK Constraint,
such as operating on multiple bones, not being usable for Objects,
and being evaluated after all other constraints have been evaluated. It should be noted that
if a Standard IK chain and a Spline IK chain both affect a bone at the same time the Standard
IK chain takes priority. Such setups are best avoided though,
since the results may be difficult to control.

To setup Spline IK,
it is necessary to have a chain of connected bones and a curve to constrain these bones to:

#. With the last bone in the chain selected,
   add a :doc:`Spline IK </animation/constraints/tracking/spline_ik>`
   Constraint from the Bone Constraints tab in the Properties.
#. Set the *Chain Length* setting to the number of bones in the chain
   (starting from and including the selected bone) that should be influenced by the curve.
#. Finally, set the *Target* field to the curve that should control the curve.

Congratulations, the bone chain is now controlled by the curve.


Settings and Controls
=====================

For the precise list of options, see :doc:`Spline IK </animation/constraints/tracking/spline_ik>` constraint.
This section is intended to introduce the workflow.


Roll Control
------------

To control the :term:`Roll` of the Spline IK chain,
the standard methods of rotating the bones in the chain along their local Y axes still apply.
For example, start at the farthest bone and simply rotate the bones in the chain around their
local Y axes to adjust the roll of the chain from that point onward.

Applying Copy Rotation constraints on the bones also works.

.. note::

   There are a couple of limitations to consider:

   - Bones do not inherit a curve's :ref:`tilt <modeling-curve-tilt>` value to control their roll.

   - There is no way of automatically creating a twisting effect
     where a dampened rotation is inherited up the chain.
     Consider using :doc:`Bendy Bones </animation/armatures/bones/properties/bendy_bones>` instead.


Offset Controls
---------------

The entire bone chain can be made to follow the shape of the curve while still being able to
be placed at an arbitrary point in 3D space when the *Chain Offset* option is enabled.
By default, this option is not enabled,
and the bones will be made to follow the curve in its untransformed position.


Length Control
--------------

The *Y Scale Mode* setting can be used to choose the way bones are scaled length-wise.
The available options allow stretching the bone chain to fit the curve, using the pre-IK
scaling, or doing neither. In addition, the scale of the curve Object affects the result.


Thickness Controls
------------------

The thickness of the bones in the chain is controlled using the constraint's *XZ Scale Mode* setting.
This setting determines the method used for determining the scaling on
the X and Z axes of each bone in the chain.

The available modes are:

None
   This option keeps the X and Z scaling factors as 1.0.
Volume Preserve
   The X and Z scaling factors are taken as the inverse of the Y scaling factor (length of the bone),
   maintaining the 'volume' of the bone.
Bone Original
   This options just uses the X and Z scaling factors the bone would have after being evaluated in the standard way.

In addition to these modes, there is an option, *Use Curve Radius*.
When this option is enabled, the average radius of the radii of the points on the curve where
the joints of each bone are placed, are used to derive X and Z scaling factors.
This allows the scaling effects, determined using the modes above,
to be tweaked as necessary for artistic control.


Tips for Nice Setups
====================

- For optimal deformations, it is recommended that the bones are roughly the same length,
  and that they are not too long, to facilitate a better fit to the curve.
  Also, bones should ideally be created in a way that follows the shape of the curve in its 'rest pose' shape,
  to minimize the problems in areas where the curve has sharp bends
  which may be especially noticeable when stretching is disabled.
- For control of the curve, it is recommended that hooks (in particular, Bone Hooks)
  are used to control the control points of the curve, with one hook per control point.
  In general, only a few control points should be needed for the curve
  (e.g. one for every 3-5 bones offers decent control).
- The type of curve used does not really matter,
  as long as a path can be extracted from it that could also be used by the Follow Path Constraint.
  This really depends on the level of control required from the hooks.
