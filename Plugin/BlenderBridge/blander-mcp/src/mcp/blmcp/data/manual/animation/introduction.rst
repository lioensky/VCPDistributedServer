
************
Introduction
************

Animation
=========

Animation is making an object move or change shape over time.
Objects can be animated in many ways:

Moving as a whole object
   Changing their position, orientation or size in time;
Deforming them
   Animating their vertices or control points;
Inherited animation
   Causing the object to move based on the movement of another object (e.g. its parent, hook, armature, etc.).

In this chapter, we will cover the first two,
but the basics given here are actually vital for understanding the following chapters as well.

Animation is typically achieved with the use of :doc:`keyframes </animation/keyframes/introduction>`.

.. seealso:: Related Sections

   - :doc:`Physical Simulation </physics/introduction>`
   - :doc:`Motion Tracking </movie_clip/index>`


.. _animation-state-colors:

State Colors
------------

.. figure:: /images/animation_introduction_state-colors.png

   State colors of properties.

Properties have different colors and menu items for different states.

.. object origin, 3D Viewport overlay

.. list-table::

   * - Gray
     - Not animated
   * - Yellow
     - Keyframed on the current frame
   * - Green
     - Keyframed on a different frame
   * - Orange
     - Changed from the keyframed value
   * - Purple
     - Controlled by a driver

The changed value highlight currently doesn't work with :doc:`NLA </editors/nla/introduction>`.


.. _animation-rigging:

Rigging
=======

Rigging is a general term used for adding controls to objects,
typically for the purpose of animation.

Rigging often involves using one or more of the following features:

:ref:`Armatures <armatures-index>`
   This allows mesh objects to have flexible joints and is often used for skeletal animation.
:ref:`Constraints <constraints-index>`
   To control the kinds of motions that make sense and add functionality to the rig.
:doc:`Object Modifiers </modeling/modifiers/index>`
   Mesh deformation can be quite involved, there are multiple modifiers that help control this.
:ref:`Shape Keys <animation-shape_keys-index>`
   To support different target shapes *(such as facial expressions)* to be controlled.
:ref:`Drivers <animation-drivers-index>`
   So your rig can control many different values at once,
   as well as making some properties automatically update based on changes elsewhere.

Rigging can be as advanced as your project requires. 
Rigs effective define a user interface for the animator to use, 
without being concerned with the underlying mechanisms

.. TODO nice images of rigged objects.


Examples
--------

- An armature is often used with a modifier to deform a mesh for character animation.
- A camera rig can be used instead of animating the camera object directly to simulate real-world camera rigs
  (with a boom arm, mounted on a rotating pedestal for example, effects such as camera jitter can be added too).

.. TODO more examples?

.. seealso::

   The content of this chapter is simply a reference to how rigging is accomplished in Blender.
   It should be paired with additional resources such as Nathan Vegdahl's excellent introduction to
   the fundamental concepts of character rigging,
   `Humane Rigging <https://www.youtube.com/playlist?list=PLE211C8C41F1AFBAB>`__.
