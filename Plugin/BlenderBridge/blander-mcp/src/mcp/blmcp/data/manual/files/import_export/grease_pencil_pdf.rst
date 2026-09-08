.. _bpy.ops.wm.grease_pencil_export_pdf:

***************************
Export Grease Pencil as PDF
***************************

The Portable Document Format (PDF) is used to exchange documents that can be viewed with many applications, such as
PDF readers and modern browsers. Exporting Grease Pencil animations will create a separate page in the PDF document
for each frame selected.

.. warning:: The exporter only works in Object Mode.


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
   :Selected: Export all selected keyframes as different PDF pages.
   :Scene: Export all frames as different PDF pages.

Sampling
   Precision for the stroke sampling. Low values mean a more accurate result.

Fill
   When enabled, export the Grease Pencil strokes fill.

Uniform Width
   When enabled, export strokes with constant thickness.

.. note:: The export of the Grease Pencil strokes is always from the view of the largest 3D Viewport in the current
    workspace.
