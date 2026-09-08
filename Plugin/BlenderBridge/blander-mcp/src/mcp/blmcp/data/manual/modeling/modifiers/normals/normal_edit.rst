.. index:: Modeling Modifiers; Normal Edit Modifier
.. _bpy.types.NormalEditModifier:

********************
Normal Edit Modifier
********************

The *Normal Edit* modifier affects (or generates) custom normals. It uses a few simple parametric methods
to compute them (quite useful in game development and architecture areas), and mixes back those generated normals
with existing ones.


Options
=======

.. figure:: /images/modeling_modifiers_modify_normal-edit_panel.png
   :align: right
   :width: 300px

   Normal Edit Modifier.

Radial
   Aligns normals with the ``(origin, vertex_coordinates)`` vector, in other words all normals seems to radiate
   from the given center point, as if they were emitted from an ellipsoid surface.
Directional
   Makes all normals point (converge) towards a given target object.

Target
   Uses this object's origin as reference point when generating normals.

   Optional in *Radial* mode, mandatory in *Directional* one.

Parallel Normals
   Makes all normals parallel to the line between both objects' origins,
   instead of converging towards target's origin.

   Only relevant in *Directional* mode.


Mix
---

Mix Mode
   How to affect existing normals with newly generated ones.

   Note that the *Multiply* option is **not** a cross product, but a faster component-by-component multiplication.

Mix Factor
   How much of the generated normals get mixed into existing ones.

Vertex Group
   Allows per-item fine control of the mix factor. The vertex group influence can be inverted by using
   the arrow button to the right.

Max Angle
   Forbids new generated normals to have an angle to the original normal above that given threshold.
   This is useful to prevent extreme changes, that can even lead to inverting the front/back sides of a face,
   and consequently to shading artifacts.

   :bl-icon:`unlock` / :bl-icon:`locked` Lock Polygon Normals
      Prevents flipping (reversing front/back sides) of polygons which normal does not match anymore
      the side to which point its corners' custom normals. Can also help to avoid shading issues.


Offset
------

Gives modified object's origin an offset before using it to generate normals.

Only relevant in *Radial* mode if no *Target Object* is set,
and in *Directional* mode when *Parallel Normals* is set.


Usage
=====

This modifier can be used to quickly generate radial normals for low-poly tree foliage or
"fix" shading of toon-like rendering by partially bending default normals...

.. tip::

   More complex normal manipulations can be achieved by copying normals from one mesh to another,
   see the :doc:`Data Transfer Modifier </modeling/modifiers/modify/data_transfer>`.
   Some shading effects can also make use of
   the :doc:`Weighted Normals modifier </modeling/modifiers/normals/weighted_normal>`.


Example
=======

.. figure:: /images/modeling_modifiers_modify_normal-edit_example.jpg
   :width: 680px

   Editing custom normals to point towards a given direction
   (`blend-file <https://download.blender.org/ftp/mont29/persistent_data/sapling_CN.blend>`__).

The left tree mesh has unmodified normals, while on the right one a *Normal Edit* modifier is used to bend them
towards the camera. This shading trick is often used in games to fake scattering in trees and other vegetation.
