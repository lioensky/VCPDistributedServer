
*************
Wavefront OBJ
*************

.. reference::

   :Menu:      :menuselection:`File --> Import/Export --> Wavefront (.obj)`

OBJ format is a popular plain text format, however, it has only basic geometry and material support.

.. note::

   There is no support for armatures, lights, cameras, empty objects, parenting, or transformations.
   See `Compatibility`_ for more information.


.. _bpy.ops.wm.obj_import:

Importing
=========

Import geometry and curves to the OBJ format.

If there is a matching ``.MTL`` for the OBJ then its materials will be imported too.


General
-------

Scale
   Value by which to scale the imported objects in relation to the world's origin.
Clamp Bounding Box
   OBJ-files often vary greatly in scale, this setting clamps the imported file to a fixed size.
Forward Axis, Up Axis
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Options
-------

Split By Object
   Import each OBJ "object name" group (``o``) as a separate object.
Split By Group
   Import each OBJ "object name" group (``g``) as a separate object.
Vertex Groups
   Import OBJ groups as vertex groups.
Validate Meshes
   Check the imported mesh for corrupt data and fix it if necessary.
   When disabled, erroneous data may cause crashes displaying or editing the meshes.
   This option will make the importing slower but is recommended, as data errors are not always obvious.
Detect Cyclic Curves
   Joins curve endpoints if overlapping control points are detected (if disabled, no curves will be cyclic).
Path Separator
   Character used to separate an object's name into a hierarchical
   structure using :doc:`/scene_layout/collections/index`.


Materials
---------

Material Name Collision
   Behavior when the name of an imported material conflicts with an existing material.

   :Make Unique: Import each USD material as a unique Blender material.
   :Reference Existing: If a material with the same name already exists, reference that instead of importing.


.. _bpy.ops.wm.obj_export:

Exporting
=========

Export geometry and curves to the OBJ format.


General
-------

Include: Selected Only
   Only export the selected objects. Otherwise export all objects in the scene.
Scale
   Global scale to use on export.
Forward Axis, Up Axis
   Since many applications use a different axis for 'Up', there are axis conversion settings,
   Forward and Up axis -- By mapping these to different axis you can convert rotations
   between applications default up and forward axis.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry Properties
^^^^^^^^^^^^^^^^^^^

UV Coordinates
   Write out the active UV layers coordinates from Blender.
Normals
   Write out Blender's face and vertex normals (depending on the faces smooth setting).

   Mostly this isn't needed since most applications will calculate their
   own normals but to match Blender's normal map textures you will need to write these too.
Colors
   Write out the active vertex colors attribute layer, if present. Colors are exported in
   "xyzrgb" OBJ extension format.
Curves as NURBS
   Write out NURBS curves as OBJ NURBS rather than converting to geometry.
Triangulated Mesh
   Write out quads as two triangles. Some programs only have very basic OBJ support and only support triangles.
Apply Modifiers
   Export objects using the evaluated mesh, meaning the resulting mesh after all
   :doc:`Modifiers </modeling/modifiers/index>` have been calculated.
Apply Transform
   Applies object *Location*, *Rotation*, and *Scale* to the mesh before export, writing vertices in world space.
   When disabled, vertices are exported in local object space without applying transforms.
   See :ref:`bpy.ops.object.transform_apply` for more information on applying transforms.
Properties
   For properties that have different settings for the viewport/final render pick which is used for output.
   One example where this is important is the :doc:`/modeling/modifiers/generate/subdivision_surface`.

   :Viewport: Use viewport properties.
   :Render: Use final render properties.


Grouping
--------

Object Groups
   Write out each Blender object as an OBJ object.

   .. note::

      Note that as far as Blender is concerned there is no difference between OBJ Groups and Objects,
      this option is only included for applications that treat them differently.
Material Groups
   Generate an OBJ group for each part of a geometry using a different material.
Vertex Groups
   Export the name of the vertex group of a face.
   It is approximated by choosing the vertex group with the most members among the vertices of a face.
Smooth Groups
   Write Blender's sharp edges as smooth groups.
Smooth Group Bitflags
   Generate Bitflags for smooth Groups.


Materials
---------

Write out the MTL-file along with the OBJ. Most importers that support OBJ will also read the MTL-file.

PBR Extensions
   Export MTL library using PBR extensions (roughness, metallic, sheen, clearcoat, anisotropy, transmission).
Path Mode
   When referencing paths in exported files you may want some control as to the method used since absolute paths
   may only be correct on your own system. Relative paths, on the other hand, are more portable
   but mean that you have to keep your files grouped when moving about on your local file system.
   In some cases, the path doesn't matter since the target application will search
   a set of predefined paths anyway so you have the option to strip the path too.

   :Auto: Uses relative paths for files which are in a subdirectory of the exported location,
          absolute for any directories outside that.
   :Absolute: Uses full paths.
   :Relative: Uses relative paths in every case (except when on a different drive on Windows).
   :Match: Uses relative / absolute paths based on the paths used in Blender.
   :Strip Path: Only write the filename and omit the path component.
   :Copy: Copy the file on exporting and reference it with a relative path.


Animation
---------

Exports a numbered OBJ for each frame from the start to the end frame.
Please be aware that this can take quite a long time.

Frame Start, End
   The first and last frame to export, used to determine the range of exported frames.


Compatibility
-------------

NURBS surfaces, text3D and metaballs are converted to meshes at export time.
