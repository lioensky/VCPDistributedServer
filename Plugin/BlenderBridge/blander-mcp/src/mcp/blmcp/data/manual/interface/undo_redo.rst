.. _bpy.ops.ed:

***********
Undo & Redo
***********

The tools listed below will let you roll back an accidental action,
redo your last action, or let you choose to recover to a specific point,
by picking from a list of recent actions recorded by Blender.


.. _bpy.ops.ed.undo:

Undo
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Undo`
   :Shortcut:  :kbd:`Ctrl-Z`

If you want to undo your last action, just press :kbd:`Ctrl-Z`.

.. seealso::

   :ref:`Memory & Limits Preferences <prefs-system-memory-and-limits>` to change undo settings.


.. _bpy.ops.ed.redo:

Redo
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Redo`
   :Shortcut:  :kbd:`Shift-Ctrl-Z`

To roll back the Undo action, press :kbd:`Shift-Ctrl-Z`.


.. _bpy.ops.screen.redo_last:

Adjust Last Operation
=====================

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Adjust Last Operation...`
   :Shortcut:  :kbd:`F9`

You can tweak the parameters of an :doc:`operator </interface/operators>` after running it.
In editors that support it, there is a "head-up display" panel in the bottom left
based on the last performed operation.
Alternatively, you can create a pop-up with :kbd:`F9` which does the same thing.

For example, if your last operation was a rotation in *Object Mode*,
Blender will show you the last value changed for the angle
(see Fig. :ref:`fig-interface-redo-last-object-mode` left),
where you can change your action back completely by typing :kbd:`Numpad0` in the *Angle* Field.
There are other useful options, based on the operator,
and you cannot only Undo actions, but change them completely using the available options.

If you are in *Edit Mode*,
Blender will also change its contents based on your last action taken.
In the second example (on the right), the last operation was a Move in Object Mode;
but a *Scale* on a Face in Edit Mode, and, as you can see,
the contents of *Adjust Last Operation* are different, because of the mode (Edit Mode)
(See Fig. :ref:`fig-interface-redo-last-edit-mode` right).

.. list-table:: Adjust Last Operation.

   * - .. _fig-interface-redo-last-object-mode:

       .. figure:: /images/interface_undo-redo_redo-last-object-mode.png
          :width: 310px

          Rotation (Object Mode, 60 degrees).

     - .. _fig-interface-redo-last-edit-mode:

       .. figure:: /images/interface_undo-redo_redo-last-edit-mode.png
          :width: 310px

          Scale (Edit Mode, Resize face).

.. tip::

   Some operations produce particularly useful results by using *Adjust Last Operation*.
   For example, adding a Circle in the 3D Viewport; if you reduce the *Vertices* to three,
   you get a perfect equilateral triangle.

.. tip::

   The *Adjust Last Operation* region can be hidden by :menuselection:`View --> Adjust Last Operation`.


.. _bpy.ops.ed.undo_history:

Undo History
============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Undo History`

.. figure:: /images/interface_undo-redo_undo-history-menu.png
   :align: right

   The Undo History menu.

There is also an Undo History of the last actions taken, recorded by Blender.

The top of the list corresponds to the most recent actions.
A small icon of a dot next to one of the entries indicates the current status.
Rolling back actions using the *Undo History* feature will take you back to
the action you choose. Much like how you can alternate between going backward in
time with *Undo* and then forward with *Redo*,
you can hop around on the Undo timeline as much as you want as long as you do not make a new change.
Once you do make a new change, the Undo History is truncated at that point.
Selecting one of the entries in the list takes the current status to that position.


.. _bpy.ops.screen.repeat_last:

Repeat Last
===========

.. reference::

   :Mode:      All Modes
   :Panel:     :menuselection:`Edit --> Repeat Last`
   :Shortcut:  :kbd:`Shift-R`

The Repeat Last feature will repeat your last action when you press :kbd:`Shift-R`.

In the example images below, we duplicated a *Monkey* mesh and moved it a bit.
Using repeat :kbd:`Shift-R`, the *Monkey* was duplicated and moved a second time.

.. list-table::

   * - .. figure:: /images/interface_undo-redo_repeat-last1.png

          Suzanne.

     - .. figure:: /images/interface_undo-redo_repeat-last2.png

          After a :kbd:`Shift-D` and move.

     - .. figure:: /images/interface_undo-redo_repeat-last3.png

          After a :kbd:`Shift-R`.


.. _bpy.ops.screen.repeat_history:

Repeat History
==============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Repeat History...`

.. figure:: /images/interface_undo-redo_repeat-history-menu.png
   :align: right

   The Repeat History menu.

The *Repeat History* feature will present you a list of the last repeated actions,
and you can choose the actions you want to repeat.
It works in the same way as the Undo History, explained above,
but the list contains only repeated actions.

.. container:: lead

   .. clear

.. important::

   When you quit Blender, the complete list of user actions will be lost, even if you save your file before quitting.

.. seealso::

   Troubleshooting section on :doc:`Recovering your lost work </troubleshooting/recover>`.
