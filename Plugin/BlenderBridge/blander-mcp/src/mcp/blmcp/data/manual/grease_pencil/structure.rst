
***********************
Grease Pencil Structure
***********************

Grease Pencil object has three main basic components: *points*, *edit lines* and *strokes*.

.. figure:: /images/grease-pencil_structure_example.png

   Example of Grease Pencil structure.


Points
======

The main element used in editing Grease Pencil objects are points.
Points represent a single point in 3D space.

Each point stores all the properties that define the final appearance of the strokes
as its location, thickness, alpha, weight and UV rotation for textures.

.. note::

   Point (Grease Pencil) and Vertex (meshes) are equivalent names.


Edit Lines
==========

Points are always connected by a straight line,
which you see when you are editing in Edit Mode or when you look at a stroke in wireframe view.
They are invisible on the rendered image and are used to construct the final stroke.


Strokes
=======

The stroke is the rendered image of the points and edit lines,
using a particular :doc:`Grease Pencil material </grease_pencil/materials/index>`.
(Grease Pencil materials are linked at stroke level.)
