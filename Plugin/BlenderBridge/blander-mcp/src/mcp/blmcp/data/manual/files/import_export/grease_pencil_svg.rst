**********************************
Import/Export SVG as Grease Pencil
**********************************

The Scalable Vector Graphics (SVG) format is used for interchanging vector-based illustrations between applications
and is supported by vector graphics editors such as Inkscape and modern browsers, among others.

.. warning:: The exporter only works in Object Mode.


.. _bpy.ops.wm.grease_pencil_import_svg:

Import
======

.. reference::

   :menu: :menuselection:`File --> Import --> SVG as Grease Pencil`

Resolution
   Resolution for generated strokes.

Scale
   Generated strokes scale.


.. _bpy.ops.wm.grease_pencil_export_svg:

Export
======

.. reference::

   :menu: :menuselection:`File --> Export --> Grease Pencil as SVG`


Scene Options
-------------

Object
   Determine which objects will be included in the export.

   :Active: Export only the active Grease Pencil object.
   :Selected: Export all selected Grease Pencil objects.
   :Visible: Export all visible Grease Pencil object in the scene.


Export Options
--------------

Frame
   Determine which frames will be included in the export.

   :Active: Export only the active keyframe.
   :Selected: Export all selected keyframes as SVG animation.
   :Scene: Export all frames as SVG animation.

Sampling
   Precision for the stroke sampling. Low values mean a more accurate result.

Fill
   When enabled, export the Grease Pencil strokes fill.

Uniform Width
   When enabled, export strokes with constant thickness.

Clip Camera
   When enabled and camera view is active, export only the strokes clipped from camera view.

.. note:: The export of the Grease Pencil strokes is always from the view of the largest 3D Viewport in the current 
    workspace.