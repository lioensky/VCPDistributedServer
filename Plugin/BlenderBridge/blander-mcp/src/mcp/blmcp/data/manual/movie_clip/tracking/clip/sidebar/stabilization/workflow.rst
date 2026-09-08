********
Workflow
********

Depending on the original footage's properties, achieving good stabilization results might be simple and easy,
or it might require some work, dedication and careful planning. This section covers some practical considerations
to help improving the results.


The Simple Case
===============

Whenever the camera is basically fixed, or at least "almost" stationary, and the footage is crisp and
without motion blur, perfect stabilization is easy to achieve. This might be the case when a tripod was used,
but wind or vibrations on the floor (e.g. on a stage) caused some minor shakes.
Shoulder camera shots done by an experienced operator also frequently fall into this category.

- Use as few points as possible. Start with a single point right on the main subject.
- Track this single point as accurate as possible. Beware of movements and shape changes of the tracked feature.
  Proceed in small increments (e.g. 50 frames), zoom in and readjust the target point manually when it drifts away.
  Another option is to use a larger target area for tracking; since we're tracking only a single point,
  the slower tracking speed might be acceptable.
- After enabling the basic (location) stabilization, consider if you really need rotation stabilization.
  Often, some minor, slow swinging movements are not really noticeable and do not warrant the additional working time
  and quality loss caused by rotation and scale stabilization.
- For rotation, start with one extra point, well spaced but preferably still attached to the main subject.
- Consider to fix some slow residual motion by manually animating the "*Expected* \*" parameters,
  before you even think of adding more tracking markers. Because doing so is often not worth the effort.
- If you need to add more points, the most important goal is to achieve *symmetry.*
  Place location tracking points symmetrically above and below the horizon.
  Place rotation tracking points into diagonally opposed direction, always centered around the main focal area.


Avoid Problematic Footage
=========================

The 2D stabilizer can not work miracles; some flaws simply can not be fixed satisfactory.
Notorious issues are motion blur, rolling shutter, pumping autofocus and moving compression artifacts.
Especially if you do succeed with basic stabilization, such image flaws become yet the more noticeable and annoying.
When on set or on location, it might be tempting to "fix matters in post production".
Resist that deception, it rarely works out well.

- Prefer a short exposure time to avoid motion blur.
  While motion blur is good to render filmed movements more smooth and natural,
  it seriously impedes the ability to track features precisely.
  As a guideline, try to get at least to 1/250 s.
- Prefer higher frame rates. The more *temporal resolution* the stabilizer has to work on, the better the results.
  If you have the option to choose between progressive and interlaced modes, by all means use interlaced
  and deinterlace the footage to the *doubled frame rate*. This can be done with
  the `yadif <https://ffmpeg.org/ffmpeg-filters.html#yadif-1>`__ filter of FFmpeg: use the mode 1 (``send_field``).
- Beware of the :term:`Rolling Shutter` effect. Avoid fast lateral movements.
  If you can, prefer a camera which produces less rolling shutter.
  Also, using a higher frame rate reduces the amount of rolling shutter; another reason to prefer
  interlaced over progressive for the purpose at hand.
- Switch off autofocus.
  Better plan your movement beforehand, set a fixed focus and rely on depth of field through using a small aperture.
  Pumping movements might not be so noticeable to the human observer, but the feature tracking tends to slide away
  on defocused image elements; fixing this manually after the fact can cause a huge waste of time.
- Increase the lighting level, at least use a higher sensitivity.
  This helps to set a fast shutter speed plus a small aperture.
  Better lighting and good exposure also help to reduce the impact of compression artifacts.
  If you can, also select a codec with less data reduction, better color space, etc.
  Inevitably, we're loosing some quality through the interpolation necessary for stabilization.
  Plus we're loosing some quality due to color space conversion.


Elaborate Movements
===================

When the footage builds on elaborate intended movement of the camera,
the process of stabilization becomes more involved --
especially when there is a shift in the main area of interest within the shot.
When working with many tracks and fine-grained animation,
it is easy to get into a situation where additional manipulations actually decrease the quality,
while it might be hard to spot and locate the root cause of problems.
Recommendation is to proceed systematically, starting from the general outline down to tweaking of specific aspects.

#. Understand the nature of the movements in the shot, both the intended and the accidental.
#. Track some relevant features for location.
#. Establish the basic location stabilization.
   This includes the decision, which feature to use for what segment of the shot.
   Work with the track weights to get an overall consistent movement of the weight center,
   in accordance with the inherent focus of the shot.
#. Define the panning movements of the virtual camera (through animation of the *Expected Position* parameter).
#. Add tracking for rotation and zoom stabilization.
#. Fine-tuning pass:

   Break down the whole duration of the shot into logical segments to define the intended camera movement.
   Then refine those segments incrementally step-by-step, until the overall result looks satisfactory...


Animating Stabilization Parameters
==================================

Animating some parameters over duration of the shot is often necessary, at least to get the final touch,
including control of the scale factor to hide the dancing black borders.
Unfortunately there is a **known limitation** in the current version:
it is not possible to open the generic animation editors (Graph editor and Dope Sheet)
for animation data beyond the 3D scene. So, while it *is possible* to set keyframes *right within the UI controls*
of the stabilizer (either through pressing the :kbd:`I` key or with the help of the context menu),
it is not possible to manipulate the resulting curves graphically.
The only way to readjust or remove a misguided keyframe is to locate
the timeline to the very frame and then use the context menu of the animated UI control.
(Hint: the color of the UI control changes when you have located at precisely the frame number of the keyframe.)


Irregular Track Setup
=====================

It might not be possible to track a given feature over the whole duration of the shot.
The feature might be blurred or obscured; it might even move out of sight entirely,
due to deliberate camera movement.
In such a situation, we need *another tracked feature* to take on its role, and we need some *overlap time*
to get a smooth transition without visible jump.

.. figure:: /images/movie-clip_tracking_clip_sidebar_stabilization_workflow_irregular-tracks.png
   :align: right
   :width: 250px

   Irregular Tracks.

The stabilizer is able to deal with gaps and partial coverage within the given tracks.
However, the basic assumption is that each track covers a single,
fixed reference point whenever there is any usable/enabled data.
Thus, you must not "reuse" a given track to follow several different points,
rather you should disable and thus end one track, when tracking this feature is no longer feasible.
You may include "gaps", when a tracking point is temporarily disabled or unavailable,
but you should start a new track for each distinct new feature to be tracked.

Each track contributes to the overall result by the degree controlled through its *Stab Weight* parameter.
It is evaluated on a per-frame basis, which enables us to control the influence of a track by *animating* this
*Stab Weight*. You may imagine the overall working of the stabilizer as if each tracking point "drags" the image
through a flexible spring: When you turn down the *Stab Weight* of a tracking point,
you decrease the amount of "drag"
it creates. Sometimes the contribution of different tracks has to work partially counter each other.
This effect might be used to cancel out spurious movement, e.g. as caused by perspective.
But when, in such a situation, one of the involved tracks suddenly goes away,
a jump in image position or rotation might be the result. Thus, whenever we notice
a jump at the very frame where some partially covered track starts or ends, we need to soften the transition.
We do so by animating the *Stab Weight* gradually down, so that it reaches zero at the boundary point.
In a similar vein, when we plan a "handover" between several partially covered tracks, we define a *cross-fade* over
the duration where the tracks overlap, again by animating the *Stab Weight* parameters accordingly.
But even with such cross-fade smoothing, some residual movement might remain,
which then needs to be corrected with the *Expected Position*
or *Expected rotation* parameters. It is crucial to avoid "overshooting" movements in such a situation --
always strive at setting the animation keyframes onto precisely the same frame number
for all the tracks and parameters involved.
