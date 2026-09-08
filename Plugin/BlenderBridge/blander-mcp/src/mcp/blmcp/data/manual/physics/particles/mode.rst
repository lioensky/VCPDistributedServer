.. _bpy.types.ParticleEdit:

******************
Particle Edit Mode
******************

Using *Particle Edit Mode* you can edit the keyed points (keyframes)
and paths of :doc:`Hair </physics/particles/hair/index>`,
:doc:`Particle </physics/particles/index>`, :doc:`Cloth </physics/cloth/index>`, and
:doc:`Soft Body </physics/soft_body/index>` simulations. (You can also edit and style hair before baking.)

Since working in Particle Edit Mode is pretty easy and very similar
to working with vertices in the 3D Viewport, we will show how to set up
a particle system and then give a reference of the various functions.

.. important::

   Particle Edit Mode, specifically for hair is deprecated;
   please use the new :ref:`bpy.ops.object.curves_empty_hair_add`
   object with its associated :doc:`Sculpt Mode </sculpt_paint/curves_sculpting/introduction>` instead.

.. important::

   Editing a cached cloth simulation is not currently working, see:
   `blender/blender#77114 <https://projects.blender.org/blender/blender/issues/77114>`__ for details.


Usage
=====

.. tip:: Only Frames Baked to Memory are Editable!

   If you cannot edit the particles, check that you are not baking to
   a :doc:`Disk Cache </physics/particles/emitter/cache>`.


Setup for Hair Particles
------------------------

#. Create a *Hair* particle system.
#. Give it an initial velocity in the *Normal* direction.
#. Create a simulation.
#. Check the *Hair Dynamics* box.

.. figure:: /images/physics_particles_mode_example.png

   Editing hair strands in Particle Edit Mode.


Setup for Particle, Cloth, and Soft Body Simulations
----------------------------------------------------

#. Use *Emitter* particles, or a cloth/soft body simulation.
#. Create a simulation by setting up objects and/or emitters,
   set your time range (use a small range if you are just starting out and experimenting),
   set up the simulation how you want it, play the animation to preview it.


Bake the Simulation
-------------------

Once you are happy with the general simulation, :doc:`bake </physics/particles/emitter/cache>`
the simulation from Object Mode. The simulation must be baked to enable editing.


Edit the Simulation
-------------------

Switch to *Particle Edit* from the *Mode* select menu in the header of the 3D Viewport
to edit the particle's paths/Keyframes. You may need to press :kbd:`T` from within the 3D Viewport
to see the *Particle Edit* toolbox. Move to the frame you want to edit and use the various
tools to edit your simulation.

.. _particle-edit-selecting:

Selecting
=========

.. tip::
   Switch to the *Point select mode* (see below) in the header of the 3D Viewport to be able to
   see and select the keypoints.

- Select single: :kbd:`LMB`.
- Add to/remove from selection: :kbd:`Shift-LMB`.
- All: :kbd:`A`.
- None: :kbd:`Alt-A`.
- Invert: :kbd:`Ctrl-I`.
- Box select: :kbd:`B`.
- Circle Select: :kbd:`C`.
- Lasso Select: :kbd:`Ctrl-Alt-LMB`.
- Select Linked: Move the mouse over a path and press :kbd:`L` to add all its points to the selection.
- Unselect Linked: Move the mouse over a path and press :kbd:`Shift-L` to remove all its points
  from the selection.
- Root/Tips: :menuselection:`Select --> Roots / Tips`.


.. _bpy.ops.particle.select_random:

Select Random
-------------

Randomly selects particles.

Percent
   Percent of particles to randomly select.
Random Seed
   Seed value to use for the selection.
Action
   Select random can be either used to select or deselect particles.
Type
   Selects either hair or points. Here these terms can be confusing because
   hair/point does not refer to the particle type but the path/points of the hair/particle.


.. _bpy.types.ParticleEdit.select_mode:

Select Modes
------------

.. figure:: /images/physics_particles_mode_select-modes.png

   Select Modes.

:Path: No keypoints are visible, you can select/deselect only all particles.
:Point: You see all of the keypoints.
:Tip: You can see and edit (including the brushes) only the tip of the particles, i.e. the last keypoint.


.. _bpy.types.ParticleBrush:

Tools
=====

.. reference::

   :Mode:      Particle Edit Mode
   :Tool:      :menuselection:`Toolbar`


Comb
----

Moves the keypoints (similar to the Proportional Editing tool).

Deflect Emitter
   Hair particles only -- Do not move keypoints through the emitting mesh.

   Distance
      The distance to keep from the Emitter.


Smooth
------

Parallels visually adjacent segments.


Add
---

Adds new particles.

Count
   The number of new particles per step.
Interpolate
   Interpolate the shape of new hairs from existing ones.
Steps
   Amount of brush steps.
Keys
   How many keys to make new particles with.


Length
------

Scales the segments, so it makes the hair longer with *Grow* or shorter with *Shrink*.

Grow/Shrink
   Sets the brush to add the effect or reverse it.


Puff
----

Rotates the hair around its first keypoint (root).
So it makes the hair stand up with *Add* or lay down with *Sub*.

Puff Volume
   Apply puff to unselected end points, (Helps to maintain the hair volume when puffing the root.)


Cut
---

Scales the segments until the last keypoint reaches the brush.


Weight
------

This is especially useful for soft body animations, because the weight defines the soft body *Goal*.
A keypoint with a weight of 1 will not move at all,
a keypoint with a weight of 0 subjects fully to soft body animation.
This value is scaled by the Strength *Min* to *Max* range of soft body goals...

.. Not more true, I think: "Weight is only displayed for the complete hair (i.e. with the value of the tip),
   not for each keypoint, so it's a bit difficult to paint".


Common Options
--------------

Below the brush types, their settings appear:

Radius :kbd:`F`
   Set the radius of the brush.
Strength :kbd:`Shift-F`
   Set the strength of the brush effect (not for Add brush).


Options
=======

.. reference::

   :Mode:      Particle Edit Mode
   :Panel:     :menuselection:`Tool Settings --> Options`

Auto-Velocity :guilabel:`Emitter`
   Recalculate velocities of particles according to their edited paths.
   Otherwise, the original velocities values remains unchanged
   regardless of the actual distance that the particles moves.

Mirror X
   Enable mirror editing across the local X axis.

Preserve
   Strand Length
      Keep the length of the segments between the keypoints when combing or smoothing the hair.
      This is done by moving all the other keypoints.
   Root Positions
      Keep first key unmodified, so you cannot transplant hair.


Cut Particles to Shape
----------------------

Shape Object
   A mesh object which boundary is used by the *Shape Cut* tool.

Cut
   This grooming tool trims hairs to a shape defined by the *Shape Object*.
   This is a quicker way of avoiding protruding hair sections from lengthening than using the Cutting tool.
   It works especially well for characters with extensive fur,
   where working in a single plane with the Cutting tool becomes tedious.

.. list-table:: Shape Cut example.

   * - .. figure:: /images/physics_particles_mode_shapecut-before.png

          Before.

     - .. figure:: /images/physics_particles_mode_shapecut-after.png

          After.


Viewport Display
----------------

Path Steps
   The number of steps used to draw the path; improves the smoothness of the particle path.
Children :guilabel:`Hair`
   Displays the children of the particles too.
   This allows to fine-tune the particles and see their effects on the result,
   but it may slow down your system if you have many children.
Particles :guilabel:`Emitter`
   Displays the actual particles on top of the paths.
Fade Time
   Fade out paths and keys further away from current time.

   Frames
      How many frames to fade.


Editing
=======

Moving Keypoints or Particles
-----------------------------

- To move selected keypoints press :kbd:`G`, or use one of the various other methods to move vertices.
- To move a particle root you have to turn off Keep *Root* in the Toolbar.
- You can do many of the things like with vertices, including scaling,
  rotating and removing (complete particles or single keys).
- You may not duplicate or extrude keys or particles,
  but you can subdivide particles which adds new keypoints
  :menuselection:`Particle --> Subdivide`.
- Alternatively you can re-key a particle
  :menuselection:`Particle --> Rekey`.

How smoothly the hair and particle paths are displayed depends on the *Path Steps*
setting in the Toolbar. Low settings produce blocky interpolation between points,
while high settings produce a smooth curve.


Mirror
------

.. reference::

   :Mode:      Particle Edit Mode
   :Menu:      :menuselection:`Particle --> Mirror`

If you want to create an X axis symmetrical haircut you have to do following steps:

#. Select all particles with :kbd:`A`.
#. Mirror the particles with :menuselection:`Particle --> Mirror`.
#. Turn on *X Mirror* in :menuselection:`Sidebar Region --> Tool --> Options`.

It may happen that after mirroring two particles occupy nearly the same place.
Since this would be a waste of memory and render time,
you can use *Merge by Distance* from the *Particle* menu.


Unify Length
------------

.. reference::

   :Mode:      Particle Edit Mode
   :Menu:      :menuselection:`Particle --> Unify Length`

This tool is used to make all selected hair uniform length by finding the average length.


Show/Hide
---------

.. reference::

   :Mode:      Particle Edit Mode
   :Menu:      :menuselection:`Particle --> Show/Hide`

Hiding and unhiding of particles works similar as with vertices in the 3D Viewport.
Select one or more keypoints of the particle you want to hide and press :kbd:`H`.
The particle in fact does not vanish, only the key points.

Hidden particles (i.e. particles whose keypoints are hidden)
do not react on the various brushes. But:

If you use *Mirror Editing* even particles with hidden keypoints may be moved,
if their mirrored counterpart is moved.

To unhide all hidden particles press :kbd:`Alt-H`.
