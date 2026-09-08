
***
FBX
***

The *FBX* (Filmbox) format is widely used for exchanging 3D data between applications,
especially for animated characters and complex scene data. It is supported by software
such as Autodesk Maya, 3ds Max, Cinema 4D, and game engines like Unity and Unreal Engine.

The exporter can bake mesh modifiers and animation into the FBX so the final result looks the same as in Blender.

.. note::

   - Bones would need to get a correction to their orientation
     (FBX bones seems to be -X aligned, Blender's are Y aligned),
     this does not affect skinning or animation, but imported bones in other applications will look wrong.
   - Animations (FBX AnimStacks, Blender actions) **are not linked** to their object,
     because there is no real way to know which stack to use as 'active' action for a given object, mesh or bone.
     This may be enhanced to be smarter in the future, but it's not really considered urgent,
     so for now you'll have to link actions to objects manually.
   - Armature instances **are not supported**.

.. note::

   - Bones' orientation importing is complex, you may have to play a bit with
     related settings until you get the expected results.
   - Animation support is minimal currently, we read all curves as if they were 'baked' ones
     (i.e. a set of close keyframes with linear interpolation).
   - Imported actions are linked to their related object, bone or shape key, on a 'first one wins' basis.
     If you export a set of them for a single object, you'll have to reassign them yourself.

.. note:: Saving Just Animations

   The FBX file format supports files that only contain takes.
   It is up to you to keep track of which animation belongs to which model.
   The animation that will be exported is the currently selected action within the Action editor.
   To reduce the file size, turn off the exporting of any parts you do not want and disable *All Actions*.
   For armature animations typically you just leave the armature enabled which is necessary for
   that type of animation. Reducing what is output makes the export and future import much faster.
   Normally each action will have its own name but the current or
   only take can be forced to be named "Default Take". Typically, this option can remain off.

.. note::

   Blender now only supports complex node-based shading.
   FBX having a fixed pipeline-like support of materials, this add-on converts between them.


Enabling Add-on
===============

This add-on is enabled by default, in case it is not:

#. Open Blender and go to :doc:`/editors/preferences/addons` section of the :doc:`/editors/preferences/index`.
#. Search "FBX" and check the *Enable Add-on* checkbox.


Import (Legacy)
===============

.. reference::

   :Menu:      :menuselection:`File --> Import --> FBX (.fbx) (Legacy)`

.. important::

   The importing functionality of add-on is deprecated,
   use the official :ref:`FBX Importer <bpy.ops.wm.fbx_import>` instead.


Include
-------

Import Normals
   .. todo:: Add this information.
Import Subdivision Surface
   Import FBX subdivision information as subdivision surface modifiers.
Import User Properties
   Import user properties as custom properties.
Import Enums as Strings
   Store custom property enumeration values as strings.
Image Search
   .. todo:: Add this information.


Transform
---------

Scale
   Value by which to scale the imported objects in relation to the world's origin.
Decal Offset
   .. todo:: Add this information.
Manual Orientation
   .. todo:: Add this information.
Forward / Up Axis.. todo:: Add this information.
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.

Apply Transform
   Bake space transform into object data, avoids getting unwanted rotations
   to objects when target space is not aligned with Blender's space.

   .. warning::

      Experimental option, use at own risk, known to be broken with armatures/animations.

Use Pre/Post Rotation
   .. todo:: Add this information.


Materials
---------

Material Name Collision
   Behavior when the name of an imported material conflicts with an existing material.

   :Make Unique: Import each USD material as a unique Blender material.
   :Reference Existing: If a material with the same name already exists, reference that instead of importing.


Animation
---------

Animation Offset
   Offset to apply to animation timestamps, in frames.


Armature
--------

Ignore Leaf Bones
   Ignore the last bone at the end of each chain (used to mark the length of the previous bone).
Force Connect Children
   .. todo:: Add this information.
Automatic Bone Orientation
   .. todo:: Add this information.
Primary/Secondary Bone Axis
   .. todo:: Add this information.


.. _bpy.ops.export_scene.fbx:

Export
======

.. reference::

   :Menu:      :menuselection:`File --> Export --> FBX (.fbx)`

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

   Embed Textures
      .. todo:: Add this information.

Batch Mode
   When enabled, export each group or scene to a file.

   Group/Scene
      Choose whether to batch export groups or scenes to files.
      Note, when Group/Scene is enabled, you cannot use the animation option *Current Action*
      since it uses scene data and groups are not attached to any scenes.
      Also note, when Group/Scene is enabled you must include the armature objects
      in the group for animated actions to work.
   Batch Own Directory
      When enabled, each file is exported into its own directory,
      this is useful when using the *Copy Images* option. So each directory contains
      one model with all the images it uses. Note, this requires a full Python installation.
      If you do not have a full Python installation, this button will not be shown.


Include
-------

Selected Objects
   Only export the selected objects. Otherwise export all objects in the scene.
   Note, this does not apply when batch exporting.
Active Collection
   .. todo:: Add this information.
Object Types
   Enable/Disable exporting of respective object types.
Custom Properties
   .. todo:: Add this information.


Transform
---------

Scale
   Scale the exported data by this value. 10 is the default
   because this fits best with the scale most applications import FBX to.
Apply Scaling
   .. todo:: Add this information.
Forward / Up
   Since many applications use a different axis for 'Up', these are axis conversions for Forward and
   Up axes -- By mapping these to different axes you can convert rotations between applications
   default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.
Apply Unit
   .. todo:: Add this information.
Apply Transform
   Applies object *Location*, *Rotation*, and *Scale* to the mesh before export, writing vertices in world space.
   When disabled, vertices are exported in local object space without applying transforms.
   See :ref:`bpy.ops.object.transform_apply` for more information on applying transforms.


Geometry
--------

Smoothing
   Export smoothing information.

   If the importer supports custom split normals, using *Normals Only* is generally the most accurate.

   :Normals Only: Export only custom split normals, without writing any face or edge smoothing flags.
   :Face: Export smoothing using the face smoothing flags (Blender's "smooth" shading per face).
   :Edge: Export smoothing using edge sharpness. Sharp edges are used to define smoothing boundaries.
   :Smoothing Groups:
      Write face smoothing groups,
      which defines shading by grouping faces together—faces in the same group are shaded smoothly,
      while faces in different groups create hard edges.
      Useful for preserving shading in applications that rely on this method.
Export Subdivision Surface
   .. todo:: Add this information.
Apply Modifiers
   Export objects using the evaluated mesh, meaning the resulting mesh after all
   :doc:`Modifiers </modeling/modifiers/index>` have been calculated.
Loose Edges
   .. todo:: Add this information.
Tangent Space
   .. todo:: Add this information.


Armatures
---------

Primary/Secondary Bone Axis
   .. todo:: Add this information.
Armature FBXNode Type
   .. todo:: Add this information.
Only Deform Bones
   .. todo:: Add this information.
Add Leaf Bones
   .. todo:: Add this information.


Bake Animation
--------------

.. todo:: Add this information.

Key All Bones
   .. todo:: Add this information.
NLA Strips
   .. todo:: Add this information.
All Actions
   Export all actions compatible with the selected armatures
   start/end times which are derived from the keyframe range of each action.
   When disabled only the currently assigned action is exported.
Force Start/End Keying
   .. todo:: Add this information.
Sampling Rate
   .. todo:: Add this information.
Simplify
   .. todo:: Add this information.


Compatibility
=============

Import
------

Note that the importer is a new addition and lacks many features the exporter supports.

- binary FBX files only.
- Version 7.1 or newer.


Missing
^^^^^^^

- Mesh: shape keys.


Export
------

NURBS surfaces, text3D and metaballs are converted to meshes at export time.


Missing
^^^^^^^

Some of the following features are missing because they
are not supported by the FBX format, others may be added later.

- Object instancing -- exported objects do not share data,
  instanced objects will each be written with their own data.
- Material textures
- Vertex shape keys -- FBX supports them but this exporter does not write them yet.
- Animated fluid simulation -- FBX does not support this kind of animation.
  You can however use the OBJ exporter to write a sequence of files.
- Constraints -- The result of using constraints is exported as a keyframe animation
  however the constraints themselves are not saved in the FBX.
- Instanced objects -- At the moment instanced objects are only written in static scenes
  (when animation is disabled).
