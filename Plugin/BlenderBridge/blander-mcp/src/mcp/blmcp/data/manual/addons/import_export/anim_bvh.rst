
******************************
BioVision Motion Capture (BVH)
******************************

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Motion Capture (.bvh)`

Imports or exports bvh-files or files with BioVision Hierarchical data
or data of a skeleton (rig) including its animation.
Useful for importing data from motion capture devices.


Enabling Add-on
===============

This add-on is enabled by default, in case it is not:

#. Open Blender and go to :doc:`/editors/preferences/addons` section of the :doc:`/editors/preferences/index`.
#. Search "BioVision Motion Capture (BVH) format" and check the *Enable Add-on* checkbox.


Properties
==========

Import
------

Target
   The motion capture data type.

   :Armature: The bvh-file contains an animated rigged skeleton such as a walking motion capture.
   :Object: The bvh-file contains a static (not animated) mesh object such as a character model.


Transform
^^^^^^^^^

Scale
   Factor to increase the physical size of the BVH.
Rotation
   Rotation order of the BVH.
Forward / Up
   Since many applications use a different axis for pointing upwards, these are axis conversion for these settings,
   Forward and up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y forward, Z up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z forward, Y up is needed.


Animation
^^^^^^^^^

Start Frame
   The start frame, in Blender, to start playback of the BVH animation.
Scale FPS
   Scales the frame rate from the BVH file to the scene frame rate set in Blender,
   otherwise each BVH frame maps directly to a frame in Blender.
Loop
   Cycles the animation playback.
Update Scene FPS
   Set the scene's frame rate to match the frame rate of the BVH file.
Update Scene Duration
   Extend the scene's duration to match the BVH's duration.


Export
------

Transform
^^^^^^^^^

Scale
   Factor to increase the physical size of the BVH.
Rotation
   Rotation order of the BVH.
Root Translation Only
   Only write the translation animation channels for the root bone.


Animation
^^^^^^^^^

Start / End
   Sets the range of animation to export to the BVH file.
