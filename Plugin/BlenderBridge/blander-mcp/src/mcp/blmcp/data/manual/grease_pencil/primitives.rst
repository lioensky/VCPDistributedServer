.. _bpy.ops.object.grease_pencil_add:

************************
Grease Pencil Primitives
************************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Menu:      :menuselection:`Add --> Grease Pencil`
   :Shortcut:  :kbd:`Shift-A`

In Object Mode, the *Add* menu provides three different Grease Pencil primitives
with preset materials and 2D layers:

.. figure:: /images/grease-pencil_primitives_all.png

   Grease Pencil primitives.


Blank
=====

Adds a Grease Pencil object without any stroke.


Stroke
======

Adds a Grease Pencil object with a simple stroke as a reference.


Monkey
======

It creates a 2D monkey head. The Monkey's name is "Suzanne" and is Blender's mascot.
2D Suzanne is very useful as a standard test.


Scene Line Art
==============

Sets up a :doc:`/grease_pencil/modifiers/generate/line_art` for the active scene
by creating an "empty" Grease Pencil object with a Line Art modifier referencing each object in the scene.


Collection Line Art
===================

Sets up a :doc:`/grease_pencil/modifiers/generate/line_art` for the active collection
by creating an "empty" Grease Pencil object with a Line Art modifier referencing each object in the collection.


Object Line Art
===============

Sets up a :doc:`/grease_pencil/modifiers/generate/line_art` for the active object
by creating an "empty" Grease Pencil object with a Line Art modifier referencing the active object.
