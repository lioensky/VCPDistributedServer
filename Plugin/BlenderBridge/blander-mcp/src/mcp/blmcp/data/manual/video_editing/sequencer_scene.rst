
***************
Sequencer Scene
***************

The video sequencer uses a separate scene data-block that contains the edit. This is the *Sequencer Scene*.

Having a separated scene for the video sequencer has multiple benefits, like managing different 
versions of an edit within the same file. Another important use-case is working with
different scenes in the file and scene strips. See the section below about working with multiple scenes
and scene strips.


Usage
=====

Creating a Sequencer Scene
--------------------------

To start using the Sequencer, you first need to create or use an existing Scene.

#. Open a workspace that contains a :doc:`Video Sequence Editor </editors/video_sequencer/index>`.
#. Press the "New" button in the :doc:`Sequencer header region </editors/video_sequencer/sequencer/navigating>` to
   create a new Sequencer Scene, or select an existing Scene.


Working with Multiple Scenes
----------------------------

Since the sequencer scene is separate from the active scene in the window
it is possible to work with scene strips in the sequencer while also viewing
and editing the referenced scenes within the same workspace.

A common setup includes:

* Workspace with a Video Sequence Editor and a 3D Viewport.
* In the VSE, a Sequencer Scene (e.g. called "Edit").
* Multiple other scenes in the same file e.g. for different locations or shots.

Now add a few scene strips in the sequencer using the existing scenes (or new scenes).
Then enable the Sync Scene Time option in the Sequencer Playback Controls region.
This will update the active scene (and therefor what is visible in the 3D Viewport)
with whatever scene the current scene strip in the Sequencer references.

This setup allows for quick switching between different scenes just by scrubbing/playing
the Sequencer timeline.


Playback Context
================

Since the Sequencer Scene can be different from the active scene, playback is contextual,
meaning that depending on where playback is started, a different scene might be playing.

Playing back the scene from the Sequencer plays the Sequencer Scene.
All other editors play back the active scene in the window.


Rendering
=========

The render and output settings of the Sequencer Scene are the same as for regular scenes.
They can be found in the Output tab in the Properties editor. Note that these settings
follow the active scene in the window by default (unless there is a Scene pinned to the
properties editor).

When the active scene is different from the Sequencer Scene in the current workspace,
the "Render" menu will include separate options to render the Sequencer Scene (and not the active Scene).