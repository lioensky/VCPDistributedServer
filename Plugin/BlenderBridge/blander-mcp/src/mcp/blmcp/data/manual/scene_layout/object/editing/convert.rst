.. _object-convert-to:
.. _bpy.ops.object.convert:

*******
Convert
*******

Curve
=====

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Curve`

Converts the selected mesh or text object into a curve object.

- **For mesh objects**: Only loose edges (edges not part of any faces) will be included in the conversion.
- **For text objects**: The text is converted into curve outlines, preserving its shape.

The resulting curve will be :ref:`Poly Curve <curve-poly>` by default.
To create smooth segments, convert the curve to a :ref:`Bézier Curve <curve-bezier>`
using :ref:`bpy.ops.curve.spline_type_set`.


Mesh
====

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Mesh`

Converts the selected curve, metaball, surface, or text object to a mesh object.
The actual defined resolution of these objects will be taken into account for the conversion.
Note that it also keeps the faces and volumes created by closed and extruded curves.


Grease Pencil
=============

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Grease Pencil`

Converts the selected curve, mesh, or text object to a Grease Pencil object, generating strokes
that follow the original shape. Basic materials are also created.
When multiple objects are selected, they are combined into a single Grease Pencil object.

Keep Original
   Keeps the original object by creating a duplicate before conversion.
Thickness
   Defines the stroke thickness.
Stroke Offset
   Adjusts the offset to separate strokes from filled areas.
Export Faces
   Converts mesh faces into filled strokes.


Trace Image to Grease Pencil
============================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Trace Image to Grease Pencil`

See :doc:`/grease_pencil/modes/object/trace_image`.


.. _bpy.ops.image.convert_to_mesh_plane:

Convert to Mesh Plane
=====================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Convert to Mesh Plane`

Converts the selected :ref:`image empty <bpy.types.Object.empty_image>` to a textured mesh plane.

For a description of the options see :doc:`/modeling/meshes/import_images_as_planes`.
