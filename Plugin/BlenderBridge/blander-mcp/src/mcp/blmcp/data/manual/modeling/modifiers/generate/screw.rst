.. index:: Modeling Modifiers; Screw Modifier
.. _bpy.types.ScrewModifier:

**************
Screw Modifier
**************

The *Screw* modifier is similar to the :doc:`Screw </modeling/meshes/editing/edge/screw>` tool
in the Toolbar, in that it takes a profile object, a mesh or a curve, to create a helix-like shape.

.. figure:: /images/modeling_modifiers_generate_screw_align.png
   :width: 540px

   Properly aligning the profile object is important.

The profile should be properly aligned to the cardinal direction of the object rather than to the screw axis.


Options
=======

.. figure:: /images/modeling_modifiers_generate_screw_panel.png
   :align: right
   :width: 300px

   The Screw modifier.

Angle
   Degrees for a single helix revolution.

Screw
   The height of one helix iteration.

Iterations
   Number of revolutions.

Axis
   The axis along which the helix will be built.

Axis Object
   The name of an object to define the axis direction.

   Object Screw
      Use the distance from the *Axis Object* to define the height of one helix iteration.

Steps Viewport
   Number of steps used for a single revolution displayed in the 3D Viewport.
Render
   As above, but used during render time. Increase to improve quality.

Merge
   Merge vertices that lie on the axis of rotation.
   Use this to close off end points with a triangle fan.

   Merge Distance
      Vertices under this distance to the axis are merged.

Stretch UVs
   Stretch the UV coordinates from (0.0 to 1.0) when UVs are present.


Normals
-------

Smooth Shading
   Output faces with smooth shading rather than flat shading.
   The smooth/flat shading of the input geometry is not preserved.

Calculate Order
   Order of edges is calculated to avoid problems with normals and shading. Only needed for meshes, not curves.

Flip
   Flip normals direction.
