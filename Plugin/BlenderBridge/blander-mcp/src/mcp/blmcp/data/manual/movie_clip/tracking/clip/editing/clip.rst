
****
Clip
****

.. _bpy.ops.clip.open:

Open Clip
=========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Clip --> Open Clip`
   :Shortcut:  :kbd:`Alt-O`

.. todo:: Add this information.


.. _bpy.ops.clip.set_scene_frames:

Set Scene Frames
================

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Set Scene Frames`

Sets end scene frame to match current clip duration.


.. _bpy.ops.clip.prefetch:

Prefetch
========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Clip --> Prefetch`
   :Shortcut:  :kbd:`P`

Fills cache with frames. As many frames as fits into cache are load form the drive.
This allows to fill in the cache as fast as possible when you really need to track something,
but this keeps CPU and drive bandwidth idle if you've got a Clip editor opened but not actually interacting with it.


.. _bpy.ops.clip.reload:

Reload Clip
===========

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Clip --> Open Clip`

Force reload the currently loaded movie clip. Is mainly useful when the clip gets edited outside of Blender.


Proxy
=====

.. todo:: Add this information.


.. _bpy.ops.clip.set_viewport_background:

Set as Background
=================

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Set as Background`

Sets the clip currently being edited as the camera background for all visible 3D Viewports.
If there is no visible 3D Viewports or the Clip Editor is open in full screen, nothing will happen.


.. _bpy.ops.clip.setup_tracking_scene:

Setup Tracking Scene
====================

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Clip --> Setup Tracking Scene`

Automatically performs the common steps needed to prepare a scene for match moving and compositing.

This operator sets up a basic VFX workflow by:

- Creating reference objects for the floor and a test object (a cube) to verify the track.
- Creating and configuring a camera object that matches the tracked motion.
- Setting up a compositor node tree that combines the rendered 3D scene with the background footage.

The resulting setup provides a starting point for integrating 3D objects into real footage.

.. tip::

   - Use the generated floor reference to align 3D objects to the ground plane of the footage.
   - The test cube can be replaced or used to check that tracked motion matches correctly.
   - The compositor setup can be customized further to include masks, color grading, or additional effects.

.. note::

   This operator is intended as a convenience feature.
   More complex VFX work may require building a custom compositor node setup or manually adjusting the scene.
