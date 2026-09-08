
***
STL
***

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Stl (.stl)`

The STL-file format is useful if you intend to import/export the files for CAD software.
It is also commonly used for loading into 3D printing software.


.. _bpy.ops.wm.stl_import:

Importing
=========

General
-------

Scale
   Value by which to scale the imported objects in relation to the world's origin.
Scene Unit
   Apply current scene's unit (as defined by unit scale) to imported data.
Forward / Up Axis
   Since many applications use a different axis for pointing upwards, these are axis conversion for these settings,
   Forward and up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y forward, Z up (since the front view looks along the +Y direction).
   For example, it is common for applications to use Y as the up axis, in that case -Z forward, Y up is needed.


Options
-------

Facet Normals
   Use (import) facet normals (note that this will still give flat shading).
Validate Mesh
   Check the imported mesh for corrupt data and fix it if necessary.
   When disabled, erroneous data may cause crashes displaying or editing the meshes.
   This option will make the importing slower but is recommended, as data errors are not always obvious.


Exporting
=========

General
-------

Format: ASCII
   Exports the stl-file in ASCII format rather than as a binary format
Batch
   Export each object as a separate STL file.
Include: Selection Only
      When checked, only selected objects are exported.
      Instanced objects, for example collections that are instanced in the scene,
      are considered 'selected' when their instancer is selected.
Scale
   Value by which to scale the exported objects in relation to the world's origin.
Scene Unit
   Apply current scene's unit (as defined by unit scale) to exported data.
Forward, Up
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry
--------

Apply Modifiers
   Export objects using the evaluated mesh, meaning the resulting mesh after all
   :doc:`Modifiers </modeling/modifiers/index>` have been calculated.
