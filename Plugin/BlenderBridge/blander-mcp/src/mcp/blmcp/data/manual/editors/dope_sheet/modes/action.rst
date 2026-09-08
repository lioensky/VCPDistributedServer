
*************
Action Editor
*************

While the *Dope Sheet* mode lets you work with keyframes of all animation in the
scene at the same time, the *Action Editor* mode focuses on the keyframes inside
a single :doc:`action </animation/actions>`.

.. figure:: /images/editors_dope-sheet_action-editor.png

   The Action Editor.

Actions are Blender's container for animation data. Objects and other animatable
data-blocks reference actions to get animated by the animation data inside.
Data-blocks can reference one action as their *active action* and additional
actions through :doc:`Nonlinear Animation tracks </editors/nla/tracks>`.


Header
======

.. note::

   The Previous/Next Layer (down/up arrows) operators have been removed from the UI in 4.4
   and are slated to be removed completely in 5.0.
   See `#119626 <https://projects.blender.org/blender/blender/issues/119626>`_.


.. _dopesheet-action-action:

Action
   A :ref:`data-block menu <ui-data-block>` that lets you change -- or clear -- the object's active action.

.. _bpy.types.ActionSlot.name_display:
.. _bpy.ops.anim.slot_new_for_id:
.. _bpy.ops.anim.slot_unassign_from_id:

Slot Display Name
   Name of the slot, for display in the user interface.
   This name combined with the slot's data-block type is unique within its Action.


Action Menu
===========

.. note::

   The "Merge Animation" and "Separate Slots" operators will only work with
   :ref:`directly-assigned actions <working_with_actions>`,
   and will ignore actions referenced by NLA strips.


.. _bpy.ops.anim.merge_animation:

Merge Animation
   This operator merges the animation of all selected objects into the animation of the
   active object. Since the data is moved and not copied, the source Actions might end up
   empty and without users.
   Note that this will not only merge the object level Action, but Actions on related data-blocks
   as well (See :ref:`Related data-blocks <working_with_actions>`). As a result of that
   this operator can also be used to merge Actions of one Object. For example
   Translation & Rotation and animation on Shape Keys.


.. _bpy.ops.anim.separate_slots:

Separate Slots
   This splits all Slots of the Action on the active Object into separate Actions.
   All users of those Slots will be re-assigned to their respective Action and
   the newly created Actions are named after the Slot.
   The source Action will not be deleted, but might end up with 0 users if no
   :ref:`Fake User <data-system-datablock-fake-user>` is set.


.. _bpy.ops.anim.replace_action:

Replace Action
   Shows a pop-up, in which you can choose another action. 
   The operator then looks at the action on the active object, 
   and finds all data-blocks that use that action. On all of those it replaces the action 
   with the one chosen in the pop-up.
   Note that this does *not* replace the action on NLA strips and action constraints.
   If those should be replaced see :ref:`Remap Users <bpy.ops.outliner.id_operation>`.


.. _bpy.ops.anim.slot_channels_move_to_new_action:

Move Slots to new Action
   This moves Slots selected in the :ref:`Channels Region <editors-graph_editor-channels_region>`
   to a newly created Action. All users of those Slots are re-assigned to the new Action.
   If more than one Slot is selected, all Slots are moved into a single Action.

Push Down Action
   Creates a new NLA track below the Action Track and moves the active action into it.
   This is the same as clicking :ref:`Push Down Action <bpy.ops.nla.action_pushdown>`
   in the NLA editor.

Stash Action
   Creates a new *muted* NLA track at the bottom of the NLA tracks and moves the active action into it.
   In effect, this sets the action aside for later use, disabling it so it no longer
   affects the animation. Later, you can choose to either unmute it again or delete it.

   If you click *New Action* in the data-block menu for an object that already has an
   active action, that previous action will be stashed automatically.

.. note::

   Both *Push Down* and *Stash* leave the object without an active action (meaning the Action Editor
   becomes empty and the action can no longer be edited). If you still want to make changes to the
   action, you can select it in the NLA editor and press :kbd:`Tab` to enter Tweak Mode.