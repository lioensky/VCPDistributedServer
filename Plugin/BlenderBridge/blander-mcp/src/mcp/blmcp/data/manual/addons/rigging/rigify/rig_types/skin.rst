.. todo: make permanent 'new', development

****
Skin
****

These rigs implement a flexible system for rigging skin using multiple interacting B-Bone chains.
This is developed as the base for a new modular Rigify face rig.
These are the main ideas of the system:

Generic B-Bone Chain
   One core idea of the system is that most of the deformation should be implemented
   using a standard powerful B-Bone chain rig. These chains support advanced behavior by
   interacting with other rig components. This is in contrast to having multiple domain-specific rigs
   that each generate their own deform chains.

   The implementation provides two versions of the chain rig: `skin.basic_chain`_ merely
   attaches B-Bones to the controls with no automation added to the controls themselves.
   The `skin.stretchy_chain`_ rig in addition interpolates motion of the end (and an optional middle)
   controls to the other controls of the chain.

Automatic Control Merging
   The deformation part of the system consists of chains of one or more B-Bones connecting
   control points (nodes). Whenever controls for two chains would completely overlap,
   they are automatically merged.

   For each merged control, one of the chains is selected as the owner, based on heuristic factors
   like parent depth from root, presence of ``.T``/``.B`` ``.L``/``.R`` symmetry markers,
   and even alphabetical order as the last resort. This can be overridden by an explicit priority setting
   in cases when it guesses wrong.

   The owner and its parents determine additional automation that is placed on the control.
   As a special case, if a control is merged with its ``.T``/``.B`` ``.L``/``.R`` symmetry counterparts
   (detected purely by naming), the automation from all of the symmetry siblings
   of the owner is averaged.

.. _rigify.rigs.skin.skin_parents:

Parent Controllers
   Rather than simply using the parent meta-rig bone (ORG) as parent for controls and chain mechanisms,
   the new system includes an interface for parent rigs. It explicitly provide parent bones and generate control
   parent automation mechanisms for their child chain controls by inheriting from the appropriate base
   and overriding methods.

   This allows implementing rigs that integrate and manage their child chains in intelligent ways in order
   to add extra automation specific to certain areas. The base skin system includes one simple example
   `skin.transform.basic`_ rig, which translates its child control points according to
   its control bone transformation.

Custom Rigging
   Finally, the new system provides ways to integrate with custom automation directly included in the meta-rig
   via two extra rig components.

   The `skin.anchor`_ rig generates a single control with inherited constraints etc., similar to
   :ref:`basic.super_copy <rigify.rigs.basic.super_copy>`. However, it also integrates into the skin system
   as a zero length chain with highest priority. This allows overriding the normal behavior by providing
   a control point under full control of the user, which other chains would automatically attach to.

   The `skin.glue`_ rig on the other hand will attach itself to the control that is generated at
   its position (it is an error if there is none). It can be used to read the position of the control
   from custom rigging in the meta-rig, or inject constraints into the control bone. It is possible to
   also detect the control at the tail of the glue bone and use it as target in the constraints,
   thus copying transformation between the controls.


.. _rigify.rigs.skin.basic_chain:

skin.basic_chain
================

This is the basic chain rig, which bridges controls with B-Bones but does not add
any automation to the controls themselves.

When controls are merely moved, the chains behave as if using standard
automatic handles, but rotating and optionally scaling the controls will adjust the result.

B-Bone Segments
   Specifies the number of segments to use. Setting this to 1 disables
   all advanced behavior and merely bridges the points with a Stretch To bone.
Merge Parent Rotation and Scale
   This can be enabled to let the chain respond to rotation and scale induced by parents of
   controls owned by other chains that this chain's control merged into.
Use Handle Scale
   Enables using control scale to drive scale and/or easing of the B-Bone.
Connect With Mirror
   Specifies whether the ends of the chain should smoothly connect when merging controls
   with its ``.T``/``.B`` ``.L``/``.R`` symmetry counterpart. The relevant option must be enabled
   on both chains to work.
Connect Matching Ends
   Specifies whether the end of the chain should connect to the opposite end of a different chain
   when merging controls. Thus forming a continuous smooth chain in the same direction.
   The relevant options must be enabled on both chains.
Sharpen Corner
   Specifies whether the rig should generate a mechanism to form a sharp corner at
   the relevant connected end, depending on the angle formed by adjacent control locations.
   When the control angle becomes sharper than the specified value, ease starts reducing from 1 to 0.
Orientation
   Specifies that the controls should be oriented the same as the selected bone, rather than being
   aligned to the chain.

   Copy To Selected
      Copy to selected rigs that have the same option. Thus allowing to indiscriminately selecting bones
      without assigning unnecessary values.
Chain Priority
   Allows overriding the heuristic used to select the primary owner when merging controls.


.. _rigify.rigs.skin.stretchy_chain:

skin.stretchy_chain
===================

This rig extends the basic chain with automation that propagates movement of the start and end,
and an optional middle control, to other controls. This results in stretching the whole chain
when moving one of the ends, rather than just the immediately adjacent B-Bones.

Middle Control Position
   Specifies the position of the middle control within the chain; disabled when zero.
Falloff
   Specifies the influence falloff curves of the start, middle and end controls.
   Zero results in linear falloff, increasing widens the influence, and -10 disables
   the influence propagation from that control completely.
Spherical Falloff
   Toggle buttons to change the shape of the falloff curve from a power curve that at falloff 1 forms a parabola
   :math:`1 - x^{2^f}` to a curve forming a circle :math:`(1 - x^{2^f})^{2^{-f}}`.
Falloff Along Chain Curve
   Computes the falloff curve along the length of the chain, instead of projecting on the straight
   line connecting its start and end points.
Propagate Twist
   Specifies whether twist of the chain should be propagated to control points between main controls.
Propagate Scale
   Specifies whether perpendicular scaling of the chain should be propagated to control points between main controls.
Propagate to Controls
   Allows other chains to see propagated twist and scale via *Merge Parent Rotation and Scale* when their
   controls are merged into this chain, instead of it being completely local to this chain.
Primary Control Layers
   Optionally specifies bone collections for the end controls.
Secondary Control Layers
   Optionally specifies bone collections for the middle control, falling back to *Primary Control Layers* if not set.

The main controls with active falloff have the effect of *Merge Parent Rotation and Scale*
automatically enabled just for them.


.. _rigify.rigs.skin.anchor:

skin.anchor
===========

This rig effectively acts as a zero-length chain with highest priority,
ensuring that it becomes the owner when merging controls with other chains.
And also allowing one to input custom automation influence into the skin system.

All constraints on the meta-rig bone are moved to the created control.

Generate Deform Bone
   Creates a deformation bone parented to the control.
Suppress Control
   Makes the control a hidden mechanism bone to hide it from the user.
Widget Type
   Selects which widget to generate for the control.
Relink Constraints
   Operates the same as in :ref:`basic.raw_copy <rigify.rigs.basic.raw_copy>`,
   except all constraints are moved from ORG to the control bone.
Orientation
   Specifies the bone used to orient the control, like for other chains.


.. _rigify.rigs.skin.glue:

skin.glue
=========

This rig is in concept similar to `skin.anchor`_, but instead of overriding controls,
it is used to read or adjust the state of controls generated by other rigs.
The head of the bone must overlap a control of another skin rig.

The rig sets up its ORG bone to read the state of the control,
while moving all constraints that were originally on the bone to the control.

Glue Mode
   Specifies how the ORG bone is connected to the skin control.

   Child Of Control
      Makes the ORG bone a child of the control bone.
   Mirror Of Control
      Makes the ORG bone a sibling of the control with a Copy Transforms constraint from the control.
      The resulting local space transformation is the same as control's local space.
   Mirror With Parents
      Parents the ORG bone to the parent automation a control owned by
      the glue rig would have had, while making it follow the actual control.
      This includes both direct and parent-induced motion of the control into
      the local space transformation of the bone.
   Deformation Bridge
      Other than adding glue constraints to the control, the rig acts as a one segment basic deform chain.
      This is convenient when a pair of controls need to be bridged both with glue and a deform bone.

Relink Constraints
   Operates the same as in :ref:`basic.raw_copy <rigify.rigs.basic.raw_copy>`,
   except all constraints are moved from ORG to the control bone.
Use Tail Target
   Relinks ``TARGET`` or any constraints with an empty target bone and no relink specification
   to reference the control located at the tail of the glue bone.
Target Local With Parents
   Switches the tail target to operate similarly to *Mirror With Parents*.
Add Constraint
   Allows to add a typical glue constraints with specific *Influence*, as if it were at
   the start of the ORG bone constraint stack.


.. _rigify.rigs.skin.transform.basic:

skin.transform.basic
====================

This rig provides a simplistic :ref:`parent controller <rigify.rigs.skin.skin_parents>`, which uses regular
translation, rotation, or scale to modify locations but not orientations or scale of its child chain controls.

Generate Control
   Specifies whether to generate a visible control, or use the transformation of the ORG bone
   as a part of more complex and specific rig setup.
