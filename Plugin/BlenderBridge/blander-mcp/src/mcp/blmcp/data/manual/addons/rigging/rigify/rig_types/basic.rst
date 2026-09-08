
*****
Basic
*****

These rig types are used to generate simple single-bone features,
and for custom rigging done directly in the meta-rig.

The single-bone rig types must be applied separately to every bone even within a connected chain,
and can have connected children controlled by a different rig type.
This is unlike chain-based rig types that usually consume the whole connected chain.


.. _rigify.rigs.basic.copy_chain:

basic.copy_chain
================

Copies the bone chain keeping all the parent relations within the chain untouched.
Useful as a utility rig type for custom rigs.

Requirement: A chain of at least two connected bones.

Control (Boolean)
   When enabled control bones and widgets will be created.
Deform (Boolean)
   When enabled deform bones will be created.


.. _rigify.rigs.basic.pivot:

basic.pivot
===========

Single-bone rig type that creates a 'custom pivot' control for rotating and scaling its child sub-rigs.

This type of control transforms its children when rotated or scaled, while moving it
merely changes the pivot point used by rotation or scaling.

Master Control
   When enabled an extra parent control bone with a box widget is created to allow moving the rig.
   It is also required by all other options besides *Deform Bone*.

Widget Type
   Allows selecting one of the predefined widgets to generate for the master control instead of the default cube.

Switchable Parent
   Generates a mechanism for switching the effective parent of the rig based on the value of a custom property.

Register Parent
   Registers the rig as a potential parent scope for its child sub-rigs' parent switches.

   Tags
      Specifies additional comma-separated tag keywords for the registered parent scope.
      They can be used by other rigs to filter parent choices, or for selecting the default parent.

      Some of the existing tags that are useful here:

      ``injected`` (special)
         The parent scope will be made available for all children of the *parent* sub-rig,
         rather than just this rig's children.
      ``held_object``
         A control for the object held in the character's hand. Preferred by finger IK.

         The ``injected,held_object`` combination is perfect for such a control.

Pivot Control
   Disabling this avoids generating the actual custom pivot control, effectively turning this rig type
   into a version of `basic.super_copy`_ with parent switching support and a different widget.

Deform Bone
   When enabled a deform bone will be created.


.. _rigify.rigs.basic.raw_copy:

basic.raw_copy
==============

Single-bone rig type that copies the bone without the ``ORG-`` name prefix.

Normally all bones copied from the meta-rig are prefixed with ``ORG-`` and placed on an invisible layer.
This precludes their use as controls or deforming bones, which makes it difficult to transfer complex
fully custom rigging verbatim from the meta-rig.

This rig type does not add the automatic prefix, thus allowing an appropriate ``ORG-``, ``MCH-`` or ``DEF-``
prefix to be manually included in the meta-rig bone name, or alternatively using no prefix to create
a control bone.

Relink Constraints
   Allows retargeting constraints belonging to the bone to point at bones created in the process
   of generating the rig, thus allowing custom rigging to integrate with generated bones.

   To use this feature, add ``@`` and the intended target bone name to the constraint name, resulting
   in the ``...@bone_name`` syntax. After all bones of the rig are generated, the constraint target
   bone will be replaced. If the new bone name is just ``CTRL``, ``MCH`` or ``DEF``, this will just
   replace the ``ORG`` prefix in the existing target bone name. For the Armature constraint you can add
   a ``@`` suffix for each target, or just one ``@CTRL``, ``@MCH`` or ``@DEF`` suffix to update all.

   Parent
      If the field is not empty, applies the same name substitution logic to the parent of the bone.

   When this feature is enabled, the bone will not be automatically parented to the root bone even
   if it has no parent; enter ``root`` in the *Parent* field if that is necessary.


.. _rigify.rigs.basic.super_copy:

basic.super_copy
================

Single-bone rig type that simply copies the bone. Useful as utility rig type for
adding custom features or specific deform bones to your rigs.

Control (Boolean)
   When enabled a control bone and widget will be created.
Widget (Boolean)
   When enabled a widget will be created in replacement to the standard.
Widget Type (String):
   Allows selecting one of the predefined widget types to generate instead of the default circle.
Deform (Boolean)
   When enabled a deform bone will be created.
Relink Constraints
   Works the same as in the `basic.raw_copy`_ rig. In addition, when enabled any constraints that have
   names prefixed with ``CTRL:`` are moved to the control, and with ``DEF:`` to the deform bone.
