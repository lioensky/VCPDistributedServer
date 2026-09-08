.. _bpy.types.LineStyleGeometryModifier_Simplification:

**************
Simplification
**************

The *Simplification* modifier merges stroke vertices that lie close to one another,
like the *Decimate* modifier for meshes.

Tolerance
   Measure for how close points have to be to each other to be merged.
   A higher tolerance means more vertices are merged.

.. figure:: /images/render_freestyle_parameter-editor_line-style_modifiers_geometry_simplification_example.png
   :width: 50%
   :align: center
