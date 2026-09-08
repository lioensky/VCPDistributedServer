
************
Introduction
************

Grease Pencil is a Blender object. It accepts the drawing information
from a mouse or pressure-sensitive stylus and places it in 3D space
as a collection of points, which are defined as a stroke.

The Grease Pencil object can be used to make traditional 2D animation, cut-out animation,
motion graphics, or used it as storyboard tool, among other things.

.. figure:: /images/grease-pencil_introduction_example.png

   An illustration in 3D space using the Grease Pencil object.

Strokes are created in :doc:`Draw Mode </grease_pencil/modes/draw/introduction>`,
which requires a new :doc:`keyframe <../animation/keyframes/editing>`
in the animation timeline for the Grease Pencil object.
Existing strokes can then be adjusted in :doc:`Edit Mode </grease_pencil/modes/edit/introduction>`
and :doc:`Sculpt Mode </grease_pencil/modes/sculpting/introduction>`.
Finally, artists can apply materials, modifiers, lighting, and visual effects to strokes.


Quick Start
===========

Artists can add Grease Pencil to any existing Blender scene, or start with a 2D Animation template.
The template offers some pre-configured options that are helpful for animation and storyboarding.


Create and Use Grease Pencil
----------------------------

#. From :doc:`Object Mode <../scene_layout/object/introduction>`, :menuselection:`Add --> Grease Pencil --> Blank`.
#. Create a new keyframe or turn on Auto Key. (See :doc:`Keyframe Editing <../animation/keyframes/editing>`)
#. Switch to :doc:`Draw Mode <./modes/draw/introduction>`.
#. Click and drag across the viewport to add strokes to the Grease Pencil object.


2D Animation Template
---------------------

To create a new Blender file using the "2D Animation"
project template use: :menuselection:`File --> New --> 2D Animation`.

Note the following pre-configured setup for the 2D Animation template:

- 2D Animation is the default active workspace.
- :menuselection:`World Properties --> Surface (Background) --> Color` is set to white.
- Color management :ref:`bpy.types.ColorManagedViewSettings.view_transform` is set to *Standard*.
- The :doc:`drawing plane <./modes/draw/drawing_planes>` is set to Front (X-Z).
- Line and Fill layers, along with some stroke materials, are configured for Grease Pencil.
- The animation timeline will automatically create a new keyframe when Grease Pencil is used on empty frames.

.. tip::

   Grease Pencil can read pressure-sensitivity information from a
   :ref:`Graphics Tablet <hardware-tablet>` or stylus.
