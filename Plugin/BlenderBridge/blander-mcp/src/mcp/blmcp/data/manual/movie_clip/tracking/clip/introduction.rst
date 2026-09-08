
************
Introduction
************

The Clip View is the main part of the Movie Clip editor;
almost all motion tracking tools are concentrated within the Clip View.

It should be mentioned that the camera solver consists of three quite separate steps:

#. 2D tracking of footage.
#. Camera intrinsics (focal length, distortion coefficients) specification/estimation/calibration.
#. Solving camera, scene orientation, and scene reconstruction.


Main View
=========

When a clip is loaded a Timeline is shown at bottom of the Preview.
It expands over the full area limited by the animation range.
You can move the Playhead by dragging with :kbd:`LMB`.

The Timeline is composed of the following visual elements:

- Blue line: Playhead
- Yellow: Motion track
- Yellow line: Keyframe
- Orange line: Shape keyframe
- Purple: Prefetched frames
- Light green line: Solve start/end keyframe
