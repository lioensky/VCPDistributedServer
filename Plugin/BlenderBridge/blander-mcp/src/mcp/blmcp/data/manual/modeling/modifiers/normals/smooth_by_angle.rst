.. index:: Modeling Modifiers; Smooth By Angle Modifier

************************
Smooth By Angle Modifier
************************

Sets the sharpness of mesh edges based on the angle between the neighboring faces.

.. note::

   This is a geometry nodes asset that is included in the bundled :ref:`"Essentials" asset library <assets-bundled>`.

.. tip::

   This modifier can easily be added to an object with :ref:`bpy.ops.object.shade_auto_smooth`
   or removed with :ref:`bpy.ops.object.shade_smooth` or :ref:`bpy.ops.object.shade_flat`.


Options
=======

Angle
   Maximum angle between face normals that will be considered as smooth.
Ignore Sharpness
   Smooth all edges, even if they have been marked as :ref:`Sharp <bpy.ops.mesh.mark_sharp>`.
