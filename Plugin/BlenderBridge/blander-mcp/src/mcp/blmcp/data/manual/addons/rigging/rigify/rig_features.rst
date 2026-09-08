
**********************
Generated Rig Features
**********************

After human rig generation a new armature named ``rig`` will be added to your scene.
This is the character rig you have generated from the human meta-rig and will contain all the features.


Common Features
===============

.. _rigify.rig_ui_template.RigBakeSettings:
.. _rigify.rig_ui_template.RigUI:
.. _rigify.rig_ui_template.RigLayers:

Rig UI Panels
-------------

.. figure:: /images/addons_rigging_rigify_rig-features_rig-ui-panels.png
   :align: right
   :width: 200px

The generated rig is accompanied by a script that implements a set of panels that appear in the Item
tab of the 3D view sidebar when a bone belonging to the generated rig is active.

Rig Bake Settings
^^^^^^^^^^^^^^^^^

This panel is displayed if the armature has an active :doc:`Action </animation/actions>`, and
is used by operators that apply an operation to multiple keyframes.

Bake All Keyed Frames
   When enabled, the operator computes and keyframes its result on every frame that has a key for any of the
   bones, as opposed to just relevant ones.
Limit Frame Range
   When enabled, the operator is limited to a certain frame range.

   Start, End
      Specify the frame range to process.
   Get Frame Range
      Sets the baking frame range from the scene frame range.

Rig Main Properties
^^^^^^^^^^^^^^^^^^^

This panel shows properties and operators that are relevant to the selected bones.

Rig Layers
^^^^^^^^^^

This panel contains buttons for toggling visibility of bone collections.

The layout and labels of the buttons are defined in the metarig
:ref:`Bone Collection UI <bpy.types.BoneCollection.rigify_ui_row>` panel.


Common Controls
---------------

Rigify rigs are built from standardized components called sub-rigs, which are linked together in a parent-child
hierarchy. Although the precise behavior of each sub-rig is determined by its implementation, there are certain
conventions that are followed by many of them.

Root Bone
^^^^^^^^^

Every Rigify rig has a bone called `root`, which serves as a parent for all bones of the rig.
It is assigned to a bone collection called `Root`. Unless the metarig has a custom bone
of that name, it is positioned at the origin of the rig object. Its widget looks like
a circle with four arrow shaped protrusions.

.. figure:: /images/addons_rigging_rigify_rig-features_arm-controls.png
   :align: right
   :width: 200px

Limb Master
^^^^^^^^^^^

Many limb-like sub-rigs have a gear-shaped bone at their base.

This bone can in some cases be used to transform the whole sub-rig as a rigid unit, and is also used as a container
for its custom properties that are displayed in the *Rig Main Properties* panel. If you are looking in the Graph
editor for the animated values of the properties, this is most likely the bone to look at.

As an exception, if multiple controls of the sub-rig need their own copy of conceptually the same property,
it may be placed on those controls directly instead.

Tweak Controls
^^^^^^^^^^^^^^

These controls look like blue spheres in the default color scheme, and are the final control layer above the
deformation bones themselves.

Tweaks are subordinate to the general IK or FK limb position but can be moved apart, twisted and scaled freely,
even reaching virtually impossible limb shapes.

Rubber Tweak
   .. figure:: /images/addons_rigging_rigify_rig-features_rubber-tweak.png
      :align: right
      :width: 200px

   Some sub-rigs provide a slider in their *Rig Main Properties* when tweaks are selected, which controls
   the smoothness of the Bendy Bone joint at that position. When zero, the joint deforms with a sharp bend,
   while setting it to 1 makes the transition smooth for a more rubber hose cartoon like appearance.

Custom Pivots
^^^^^^^^^^^^^

Some bones that can be freely moved in space (like IK controls) can be optionally accompanied by a custom pivot
control. These controls usually look like a plain axes empty with the axis lines capped with squares or crosses,
like the one in the image above. The control can be freely moved to change the location of the pivot, and then
rotated or scaled to transform the target bone around the pivot.

IK and FK Switching
^^^^^^^^^^^^^^^^^^^

.. figure:: /images/addons_rigging_rigify_rig-features_ik-fk-switch.png
   :align: right
   :width: 200px

A number of rig types provides both IK and FK controls (red for IK and green for FK in the image above),
with an ability to switch and snap between them.

Switching is controlled by a slider in *Rig Main Properties*, usually blending between full IK at 0 and full FK at 1.

Snapping one type of controls to the shape of the other is done via buttons, which form a group of three
in their complete set:

- The main button will snap on the current frame, and auto-key the result if enabled.
- The *Action* button will bake the change on multiple keyframes, according to *Rig Bake Settings*.
- The *Clear* button will delete keyframes on the corresponding controls within the bake interval.

Parent Switching
^^^^^^^^^^^^^^^^

.. figure:: /images/addons_rigging_rigify_rig-features_parent-switch.png
   :align: right
   :width: 200px

Some freely movable controls, e.g. usually the IK controls, can have a mechanism to switch their parent bone
between a set of choices, including the root bone, or none at all.

This mechanism is exposed in the *Rig Main Properties* panel through a row with three controls:

- A button that presents a dropdown menu, which allows switching the parent on the current frame while
  preserving the bone position and orientation in the world space.
- A dropdown input field that directly exposes the switch property for keyframing and direct manipulation.
  Changing the value can cause the bone position to jump.
- A button to apply the position preserving parent switch over the bake range of keyframes.

.. note::
   When manually placing a Child Of constraint on the control bone, the built-in parent should be switched to none.

Limbs
=====

Limbs have a master bone and tweaks. Depending on the user defined meta-rig options,
multiple deform bone segments with tweaks will be created.

The IK control may have an optional custom pivot, as well as additional predefined pivots.

Rigify's limbs have the following controls in the Sidebar panel:

.. figure:: /images/addons_rigging_rigify_rig-features_limb-properties.png
   :align: right
   :width: 200px

FK Limb Follow :guilabel:`Slider`
   When set to 1 the FK limb will not rotate with the torso and will retain is rotation
   relative to the root bone instead.

IK-FK :guilabel:`Slider`
   Controls whether the limb follows IK or FK controls, blending between full IK at 0 and full FK at 1.

IK<->FK Snapping :guilabel:`Buttons`
   Snaps one type of controls to another.

IK Stretch :guilabel:`Slider`
   Blends between the limb stretching freely at 1, or having its maximum length constrained at 0.

Toggle Pole :guilabel:`Switch`
   When the toggle is Off, the IK limb will use the rotational pole vector (the arrow at the base of the limb).
   Rotating/translating/scaling the arrow will control the IK limb base.

   When the toggle is On, the classic pole vector will be displayed and used to orient the IK limb.
   The arrow will continue to handle the scale and the location of the IK limb base.

   Similar to *Parent Switching*, the row includes buttons to convert the current pose between types,
   or bake the whole action.

IK Parent :guilabel:`Switch`
   Switches the effective parent of the main IK control.

Pole Parent :guilabel:`Switch`
   Switches the effective parent of the classic IK Pole control.

Arms
----

.. figure:: /images/addons_rigging_rigify_rig-features_hand-controls.png
   :align: right
   :width: 200px

:ref:`Arms <rigify.rigs.limbs.arm>` have the simplest control structure: the IK controls consist of the main IK
control, the optional custom pivot control, and the optional wrist control (the bent circle), which pivots around
the tail rather than the head of the hand bone.

There are no additional controls in the *Rig Main Properties* panel.

Legs
----

:ref:`Legs <rigify.rigs.limbs.leg>` have a more complicated setup, which has:

.. figure:: /images/addons_rigging_rigify_rig-features_foot-controls.png
   :align: right
   :width: 200px

IK & FK Toe :guilabel:`Optional`
   Two separate IK and FK controls for the toe (this is on by default in the bundled metarigs,
   and is recommended for stable IK<->FK snapping).
IK Heel
   A heel control which can be rotated to command forward or backward roll, sideways rock, or yaw of the heel.
Toe Pivot :guilabel:`Optional`
   An extra pivot control rotating around the base of the toe.
Custom Pivot :guilabel:`Optional`
   A custom pivot control.

The properties panel has two additional features:

.. figure:: /images/addons_rigging_rigify_rig-features_foot-properties.png
   :align: right
   :width: 200px

IK->FK Snap With Roll :guilabel:`Buttons`
   Standard IK to FK snapping resets the transformations of all IK controls other than the main one. This is
   not convenient to use in an animation that involves the use of the heel control, because roll and rock would
   be folded into the transformation of the main control.

   This alternative snapping operator tries to deduce the rotation of the heel control so as to keep the main
   IK control parallel to the ground plane inferred from the *current* orientation of the IK control. The operator
   has options to specify which rotational axes to use for the heel control rotation.

Roll On Toe :guilabel:`Slider` :guilabel:`Optional`
   If enabled in the sub-rig settings, this slider can be used to control whether the heel rotation (excluding
   backward roll) is applied at the base or the tip of the toe.

Fingers & Tentacles
===================

Simple Tentacle
---------------

.. figure:: /images/addons_rigging_rigify_rig-features_simple-controls.png

The simplest type of rig for a finger or appendage in general is the
:ref:`simple tentacle <rigify.rigs.limbs.simple_tentacle>` sub-rig. It has only basic FK controls and tweaks,
with the only automation being the ability to copy certain axes of the local rotation of a FK control to the next one.

Advanced Finger
---------------

.. figure:: /images/addons_rigging_rigify_rig-features_finger-controls.png

For fingers specifically, Rigify has a dedicated :ref:`finger <rigify.rigs.limbs.super_finger>` sub-rig type,
which provides:

Master
   A master control (orange), which can be used to rotate the finger as a whole, as well as to bend it via Y scaling.
FK Chain
   FK control chain (green) that can also operate as semi-tweaks through allowing translation.
IK Control :guilabel:`Optional`
   IK control for the tip (red).

.. note::
   IK in this sub-rig is rudimentary and operates as an adjustment for FK. The intended way of use is to pose
   the finger in FK, and then enable IK after using IK->FK snap if it is necessary to pin the tip of the finger
   in place.

The properties panel has the following features:

.. figure:: /images/addons_rigging_rigify_rig-features_finger-properties.png
   :align: right
   :width: 200px

Finger IK :guilabel:`Slider` :guilabel:`Optional`
   Slider controlling the influence of the IK.

FK<->IK Snapping :guilabel:`Buttons` :guilabel:`Optional`
   Snaps the IK control to the end of the finger, or adjusts the FK controls to the result of the IK correction.

Curvature :guilabel:`Slider`
   Has the same effect as *Rubber Tweak* on limbs, controlling the rubber hose cartoon effect.

Spline Tentacle
---------------

.. figure:: /images/addons_rigging_rigify_rig-features_spline-controls.png

   Spline Tentacle (Stretch To Fit, Manual Squash & Stretch)

.. figure:: /images/addons_rigging_rigify_rig-features_spline-controls-tip.png

   Spline Tentacle (Direct Tip Control)

The :ref:`spline tentacle <rigify.rigs.limbs.spline_tentacle>` is an advanced rig for a flexible appendage (tentacle)
based on the :doc:`Spline IK </animation/constraints/tracking/spline_ik>` constraint. The IK control bones manage
control points of a Bezier spline curve, which in turn is followed by the IK chain.

The tentacle can be generated in three major modes:

Stretch To Fit
   In this simplest mode all bones of the sub-rig deform chain follow the curve and squash & stretch to match
   its length.
Manual Squash & Stretch
   This mode is almost the same, but the chain does not automatically scale to match the curve length.
   Instead, it tries to cover as much as possible of the curve given its manually scaled length.
   If the curve is too short, the chain will overhang it and straighten out, but this can result in jitter.
Direct Tip Control
   This mode is more similar to the behavior of IK limbs: the final bone of the chain is directly controlled by
   the tip IK control, while the other bones of the chain stretch and follow the curve to bridge the gap.

The tentacle sub-rig has the following control bones:

Master
   The tentacle has the same gear master control as other limbs (seen as a line in the images).
IK Start
   The IK control at the base of the tentacle, which can be used to control the base twist and sideways scale, and
   is one of the potential switchable parents for other IK controls.

   In the *Manual Squash & Stretch* mode it controls uniform scale of the tentacle in all directions.
IK Start (Extra) :guilabel:`Optional`
   Extra start controls, optional and hidden by default. Switchable parents default to the *IK Start* control.
   The scale of the control may optionally affect the thickness of the chain via the radius of the curve point.
IK Middle
   Controls for the middle of the curve. The switchable parents default to *Master*, but may be set to
   *IK Start* or *IK End* controls.
   The scale of the control may optionally affect the thickness of the chain via the radius of the curve point.
IK End (Extra) :guilabel:`Optional`
   Extra end controls, optional and hidden by default. Switchable parents default to the *IK End* control.
   The scale of the control may optionally affect the thickness of the chain via the radius of the curve point.

   The *Direct Tip Control* mode adds one more extra end control next to the middle ones that cannot be hidden.
IK End
   Controls the last control point of the curve, and is one of the potential parents for the other chain controls.

   In the *Direct Tip Control* mode also directly controls the last bone of the chain.
IK End Twist :guilabel:`Optional`
   This control is visually attached to the last bone of the chain, and must use Euler rotation.

   - *Stretch To Fit*: it controls the twist of the tip of the tentacle, interpolated to nothing at the base.
   - *Manual Squash & Stretch*: it also controls the scaling of the tip of the tentacle.
   - *Direct Tip Control*: the control does not exist.
FK Chain :guilabel:`Optional`
   If enabled, the rig has an alternative fully FK control chain.

The properties panel has the following features:

.. figure:: /images/addons_rigging_rigify_rig-features_spline-properties.png
   :align: right
   :width: 200px

Start/End Controls :guilabel:`Optional`
   If extra controls exist, this property controls how many of them are visible and active.

   When a control is disabled, it is snapped to a position extremely close to the corresponding end control point,
   thus effectively neutralizing its effect. Thus, changing the setting during an animation can cause jumps.

   The plus and minus buttons can help with maintaining a continuous transition in an animation by keyframing the
   change in the property value with Constant interpolation, and also snapping and keyframing the control itself
   to its 'hidden' position.

End Twist Estimate :guilabel:`Optional`
   In the *Direct Tip Control* mode the twist at the end of the tentacle is deduced from the free form orientation
   of the tip control, rather than using a separate twist control with constrained Euler rotation. However, for
   technical reasons, that can only give values within the 180 degrees range of neutral.

   A long tentacle can accept more twist than 180 degrees, so a workaround is necessary. This property allows
   specifying an approximate estimate of the twist value (effectively shifting the neutral position), and the
   rig then applies the automatic correction within 180 degrees of this value.

IK-FK, IK<->FK Snapping :guilabel:`Optional`
   If the FK controls are enabled, these provide standard IK-FK switching and snapping.

   However, unlike other limbs, for this rig automatic IK to FK snapping can only be approximate and requires
   manual tuning. For this reason, buttons for baking the snapping over a range of keyframes are not provided.

Parent Switch
   Switches the parent of the selected IK control.


Spine, Head & Tail
==================

.. figure:: /images/addons_rigging_rigify_rig-features_spine-controls.png
   :align: right
   :width: 200px

Spine
-----

The :ref:`spine <rigify.rigs.spines.basic_spine>` sub-rig provides a cube shaped torso control with
switchable parent, and bent circle shaped hip and chest controls subordinate to it. For low level deformation
tweak controls are provided.

The torso control can optionally be accompanied with a custom pivot control. The rig can also optionally
provide a full set of FK controls that are subordinate to the normal simplified ones, but above tweaks.

The rig properties panel for the spine controls usually includes options for the head and/or tail as well.


.. figure:: /images/addons_rigging_rigify_rig-features_head-controls.png
   :align: right
   :width: 200px

Head
----

The :ref:`head <rigify.rigs.spines.super_head>` sub-rig attaches to the end of the spine, and provides
rotational controls for the head and neck, as well as tweaks for fine control of the neck.

If the neck is three or more bones long, an additonal tweak-like translational
neck bend control is provided (the widget looks like a circle with arrows).

The properties panel contains the following options:

Neck Follow :guilabel:`Slider`
   .. figure:: /images/addons_rigging_rigify_rig-features_head-properties.png
      :align: right
      :width: 200px

   This slider controls the rotations isolation for the neck bones.
   The neck will follow the orientation of the Torso when set to 0, and the Chest when set to 1.

Head Follow :guilabel:`Slider`
   .. figure:: /images/addons_rigging_rigify_rig-features_tail-controls.png
      :align: right
      :width: 200px

   This slider controls the rotations isolation for the head.
   The head will follow the orientation of the Torso when set to 0, and the Chest when set to 1.

Tail
----

The :ref:`tail <rigify.rigs.spines.basic_tail>` sub-rig attaches to the start of the spine, and provides
FK controls for the tail, as well as a master control that replicates its local rotation around certain axes
to all individual bones.

The properties panel contains the following options:

Tail Follow :guilabel:`Slider`
   This slider controls the rotations isolation for the tail.
   The tail will follow the orientation of the Torso when set to 0, and the Hips when set to 1.

Face
====

.. note::
   This describes the new-style modular face produced by the Upgrade Face operator button.

Basic Concepts
--------------

Skin Bone Chains
^^^^^^^^^^^^^^^^

.. figure:: /images/addons_rigging_rigify_rig-features_face-chains.png
   :align: right
   :width: 300px

The foundation of the Rigify face is a network of Bendy Bone :ref:`chains <rigify.rigs.skin.basic_chain>` with
controls placed at every bone end. These controls affect all bones that meet at that specific point.

When the controls are merely translated, the B-Bone chains retain the normal automatic bezier handle behavior.
Local rotation and/or scaling of the controls are applied on top of that.

In case of :ref:`certain chains <rigify.rigs.skin.stretchy_chain>`, the transformation of the end and/or middle
controls is interpolated to other controls located between them. In such cases the controls often have different
colors and/or shapes.

Additionally, certain controls have :ref:`arbitrary constraints <rigify.rigs.skin.glue>` that partially copy
transformation from nearby control points.

Specialized Controllers
^^^^^^^^^^^^^^^^^^^^^^^

Certain areas of the face, like eyes or mouth, have additional specialized controllers that apply custom behavior
on top of the chains and their controllers within the relevant area.

Eyes
----

.. figure:: /images/addons_rigging_rigify_rig-features_eye-controls.png
   :align: right
   :width: 300px

The :ref:`eyes <rigify.rigs.face.skin_eye>` have the following controls in addition to the eyelid chains:

Master
   This large circular control can be used to transform the whole eye as one unit.
Common Target
   This large control enveloping all individual eye targets has a switchable parent and can
   be used to specify the point that the eyes should look at.
Eye Target
   These small circle controls within the common target control specify the point targeted by each
   individual eye. Their local scale can also be used to affect the iris or pupil of the eye,
   depending on how it was weight painted.

The rig properties panel contains the following options:

.. figure:: /images/addons_rigging_rigify_rig-features_eye-properties.png
   :align: right
   :width: 200px

Eyelids Follow :guilabel:`Slider`
   Controls how much the rotation of the eyeball affects the eyelids. Depending on the sub-rig generation
   options, this slider can be split to separately control the horizontal and vertical directions.

Eyelids Attached :guilabel:`Slider` :guilabel:`Optional`
   If enabled in the sub-rig generation options, this slider can be used to disable the mechanism that
   forces the eyelids to conform to the sphere of the eye.

Parent :guilabel:`Parent Switch`
   Selects the parent for the common target control.

Mouth
-----

.. figure:: /images/addons_rigging_rigify_rig-features_mouth-controls.png
   :align: right
   :width: 300px

The :ref:`mouth <rigify.rigs.face.skin_jaw>` has the following controls:

Jaw Master
   Controls rotation of the jaw, directly affecting the main jaw deform bone, as well
   as chains fully belonging to the jaw. Chains forming the lip loop(s) are adjusted to
   open the mouth as the jaw rotates or moves.
Mouth Master
   This control uniformly transforms the lips without moving the jaw.

The rig properties panel contains the following options:

.. figure:: /images/addons_rigging_rigify_rig-features_mouth-properties.png
   :align: right
   :width: 200px

Mouth Lock :guilabel:`Slider`
   This slider can be changed from 0 to 1 in order to suppress opening of the mouth
   when the jaw rotates or moves.
