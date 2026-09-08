
*****************
Editing Keyframes
*****************

.. _bpy.ops.anim.keyframe_insert:

Insert Keyframe
===============

.. reference::

   :Mode:      Object Mode, Pose Mode, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Pose/Strip --> Animation --> Insert Keyframe`
   :Shortcut:  :kbd:`I`

There are several methods of adding new keys. Namely:

- In the 3D Viewport and Video Sequencer Preview, pressing :kbd:`I` will key properties based on the
  :ref:`Default Key Channels <bpy.types.PreferencesEdit.key_insert_channels>` User Preferences.
- When a :doc:`Keying Set </animation/keyframes/keying_sets>` is active,
  it is used instead of reading the User Preferences.
- Hovering over a property and pressing :kbd:`I` or with the context menu by :kbd:`RMB`
  a property and choose *Insert Keyframe* from the menu.
- With the User Preference "Pie Menu on Drag" enabled, holding down :kbd:`I`
  and moving the cursor will bring up a pie menu to insert one of Location, Rotation, Scale, and Available.


Auto Keyframe
-------------

.. figure:: /images/editors_timeline_keyframes-auto.png

   Timeline Auto Keyframe.

Auto Keyframe is the record button in the *Timeline* header. Auto Keyframe adds
keyframes automatically to the set frame if the value for transform type properties changes.

See :ref:`Timeline Keyframe Control <bpy.types.ToolSettings.use_keyframe_insert_auto>` for more info.


.. _bpy.ops.anim.keyframe_insert_menu:

Insert Keyframe with Keying Set
===============================

.. reference::

   :Mode:      Object Mode, Pose Mode, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Pose/Strip --> Animation --> Insert Keyframe with Keying Set`
   :Shortcut:  :kbd:`K`

Insert Keyframes for specified :doc:`Keying Set </animation/keyframes/keying_sets>`,
with menu of available Keying Sets.


.. _bpy.ops.anim.keyframe_delete:

Delete Keyframes
================

.. reference::

   :Mode:      Object Mode, Pose Mode, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Pose/Strip --> Animation --> Delete Keyframes...`
   :Shortcut:  :kbd:`Alt-I`

There are several methods of removing keyframes:

- In the 3D Viewport or Video Sequencer Preview press :kbd:`Alt-I` to remove keys from selected objects, bones or
  strips on the current frame.
- When the mouse is over a value, press :kbd:`Alt-I`.
- :kbd:`RMB` a value and choose *Delete Keyframe* from the menu.


.. _bpy.ops.anim.keyframe_clear:

Clear Keyframes
===============

.. reference::

   :Mode:      Object Mode, Pose Mode, Video Sequencer Preview
   :Menu:      :menuselection:`Object/Pose/Strip --> Animation --> Clear Keyframes...`
   :Shortcut:  :kbd:`Shift-Alt-I`

Removes all keyframes from the selected object, bone or strip.


Editing Keyframes
=================

Keyframes can be edited in two editors. To do so go to either
the :doc:`Graph Editor </editors/graph_editor/index>`
or the :doc:`Dope Sheet </editors/dope_sheet/index>`.


Examples
========

Keyframe Animation
------------------

This example shows you how to animate a cube's location, rotation, and scale.

#. First, in the Timeline, or other animation editors, set the frame to 1.
#. With the cube selected in Object Mode, press :kbd:`I` in the 3D Viewport.
   This will record the location, rotation, and scale, for the cube on frame 1.
#. Set the frame to 100.
#. Use Move :kbd:`G`, Rotate :kbd:`R`, Scale :kbd:`S`, to transform the cube.
#. Press :kbd:`I` in the 3D Viewport.

To test the animation, press :kbd:`Spacebar` to play.

.. figure:: /images/animation_keyframes_editing_keyframe-animation-examples.png
   :width: 600px

   The animation on frames 1, 50 and 100.
