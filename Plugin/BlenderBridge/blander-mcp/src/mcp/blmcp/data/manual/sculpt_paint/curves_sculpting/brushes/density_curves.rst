
*************
Density Brush
*************

Create (or remove) curves based on a target distance.
It generates a high number of points and then rejects the
ones that are too close to existing points.


Brush Settings
==============

.. _bpy.types.BrushCurvesSculptSettings.density_mode:

Density Mode
   Determines whether the brush adds or removes curves.

   :Auto:
      Either add or remove curves depending on the distance between existing curve roots under the cursor.
   :Add:
      Add new curves between existing curves, taking the minimum distance into account.
   :Remove:
      Remove curves whose root points are too close.

.. _bpy.types.BrushCurvesSculptSettings.minimum_distance:

Distance Min
   Goal distance between the curve roots.

   .. _bpy.ops.sculpt_curves.min_distance_edit:

   Edit Minimum Distance :kbd:`R`
      Interactively sets the *Distance Min* value by displaying
      a graphic inside the brush cursor, giving a representation of the density.

      The density can be adjusted by moving the mouse cursor closer or farther from the paint cursor.
      The *Distance Min* will be changed once the operator is confirmed.

.. _bpy.types.BrushCurvesSculptSettings.density_add_attempts:

Count Max
   The maximum amount of points that the brush tries to sample in the surface.
