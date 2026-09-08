.. index:: Modeling Modifiers; Mirror Modifier
.. _bpy.types.MirrorModifier:

***************
Mirror Modifier
***************

The *Mirror* modifier mirrors a mesh along its local X, Y and/or Z axes, across the :term:`Object Origin`.
It can also use another object as the mirror center, then use that object's local axes instead of its own.


Options
=======

.. figure:: /images/modeling_modifiers_generate_mirror_panel.png
   :align: right
   :width: 300px

   The Mirror modifier.

Axis
   The X, Y, Z axis along which to mirror, i.e. the axis perpendicular to the mirror plane of symmetry.

   To understand how the axis applies to the mirror direction, if you were to mirror on the X axis,
   the positive X values of the original mesh would become the negative X values on the mirrored side.

   You can select more than one of these axes. And will then get more mirrored copies.
   With one axis you get a single mirror, with two axes four mirrors, and with all three axes eight mirrors.

Bisect
   If the mesh is already on both sides of the mirror plane, it is cut by that plane,
   and only one side (the "positive" one by default) is kept to perform the mirror process.

Flip
   When *Bisect* is enabled on an axis, you can use this setting to switch the side kept and mirrored
   (i.e. when it is enabled, the "negative" side will be kept, instead of the "positive" one).

Mirror Object
   An :ref:`Object Selector <ui-data-id>` to select an object (usually an empty),
   which position and rotation will be used to define mirror planes
   (instead of using the ones from the modified object).

   You can animate it to move the mirror axis.

Clipping
   Prevents vertices from moving through the mirror plane(s) when you transform them in Edit Mode.

   If it is enabled but vertices are beyond the mirror plane and outside of the *Merge Distance*,
   the vertices will not be merged. But as soon as the vertices are within *Merge Distance*
   they are snapped together and cannot be moved beyond the mirror plane.

   .. note::

      Vertices on the mirror plane will be unable to move away from the mirror plane
      as long as *Clipping* is enabled.
      You must disable it to be able to move the vertices along the mirror axis again.

Merge
   Where a vertex is in the same place (within the *Merge Distance*) as its mirror
   it will be merged with the mirrored vertex.

   Merge Distance
      The maximum distance between a vertex and its mirror copy at which they are merged together
      (being snapped on the mirror plane). Needs *Merge* to be enabled.

Bisect Distance
   Distance from the bisect plane within which vertices are removed.


Data
----

Flip UV
   With this option you can mirror the UV texture coordinates across the middle of the image.

   E.g. if you have a vertex with UV coordinates of (0.3, 0.9),
   its mirror copy will have UV coordinates of (0.7, 0.1).

UV Offsets
   Amount to shift mirrored UVs on the U/V axes.

   It's useful for baking (as overlapping UVs can cause artifacts to appear in the baked map),
   so the UVs can be moved outside the image and not used for baking, but still be used for display.

Vertex Groups
   Try to mirror existing vertex groups, with the following specific prerequisites:

   - The vertex groups you want to mirror must be named following the usual left/right pattern
     (i.e. with suffixes like ".R", ".right", ".L", etc.).
   - The mirror side vertex group must already exist (it will not be created automatically).
     It must also be completely empty (no vertices assigned to it).

Flip UDIM
   Mirror the texture coordinates around each tile center.


Hints
=====

Many modeling tasks involve creating objects that are symmetrical.
This modifier offers a simple and efficient way to do this, with real-time update of the mirror as you edit it.
Once your modeling is completed you can either click *Apply* to make a real version of your mesh,
or leave it as-is for future editing.


Accurately Positioning the Mirror Plane
---------------------------------------

To apply a *Mirror* modifier, it is common to have to move the object's origin onto
the edge or face that is to be the axis for mirroring.
This can be tricky when attempted visually.

A good technique to achieve an exact position is
to select the edge, then :doc:`snap </editors/3dview/controls/snapping>` *Cursor to Selection*.
This will position the 3D Cursor in the center of the edge.
Finally, use the :ref:`Set Origin <bpy.ops.object.origin_set>` menu, and select *Origin to 3D Cursor*.
This will move the object's origin (and thus, the mirror plane) to where the 3D cursor is located,
and the mirroring will be exact.

An alternative is to use an empty as a *Mirror Object* that you move to the correct position.
