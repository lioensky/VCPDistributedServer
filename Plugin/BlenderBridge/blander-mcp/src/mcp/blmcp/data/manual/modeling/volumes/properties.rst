
*****************
Volume Properties
*****************

.. _bpy.types.VolumeGrids:

Grids
=====

The :ref:`ui-list-view` shows the grids in the OpenVDB-file, listing their name and data type.
A "grid" is a set of volumetric data, which typically stores the density of each voxel
but can also contain temperatures, velocities and so on.

Click a grid to make the volume object display it.


OpenVDB File
============

.. _bpy.types.Volume.filepath:

File Path
   The VDB file to use.

.. _bpy.types.Volume.is_sequence:

Sequence
   Loads further VDB files, one for each frame in an animation. Much like with image sequences,
   all the files should have a numerical suffix in their name; so if you selected smoke-000.vdb
   in the *File Path*, there should be a smoke-001.vdb, a smoke-002.vdb and so on.

   .. _bpy.types.Volume.frame_duration:

   Frames
      How many frames of the sequence to use.

   .. _bpy.types.Volume.frame_start:

   Start
      Scene frame at which the sequence should start.

   .. _bpy.types.Volume.frame_offset:

   Offset
      How many frames of the sequence to skip at the beginning.

   .. _bpy.types.Volume.sequence_mode:

   Mode
      How the volume should behave before the sequence's first frame (*Start*) and after its
      last (*Start* + *Frames*).

      :Clip:
         Show nothing.
      :Extend:
         Keep showing the first/last frame of the sequence.
      :Repeat:
         Play the sequence again (and again, and again...).
      :Ping-Pong:
         Play the sequence forwards, then backwards, then forwards again and so on.


.. _bpy.types.VolumeDisplay:

Viewport Display
================

.. _bpy.types.VolumeDisplay.wireframe_type:

Wireframe
   Method used to represent volumes in :ref:`wireframe <3dview-shading-rendered>` shading mode.
   For heavy volume data sets, it can be useful to set the object to always display as wireframe.
   This way, the 3D Viewport remains responsive but the volume still appears in the final render.

   :None:
      The volume is not displayed in wireframe mode.
   :Bounds:
      Displays the volume as a :term:`Bounding Box` for the entire grid.
   :Boxes:
      Displays bounding boxes for nodes in the volume tree.
   :Points:
      Displays points for nodes in the volume tree.

.. _bpy.types.VolumeDisplay.wireframe_detail:

Detail
   The amount of detail to display for *Boxes* or *Points* wireframe mode.

   :Coarse:
      Display one box or point for each intermediate tree node.
   :Fine:
      Display a box or point for each leaf node containing 8×8 voxels.

.. _bpy.types.VolumeDisplay.density:

Density
   Thickness of the volume in the 3D Viewport.
   The density of the volume in the render is adjusted via
   :doc:`Volume Shading </render/shader_nodes/shader/volume_principled>`.

.. _bpy.types.VolumeDisplay.interpolation_method:

Interpolation
   Interpolation method to use for the visualization of the fluid grid.

   :Linear:
      Linear interpolation between voxels. Gives good smoothness and speed.
   :Cubic:
      Cubic interpolation between voxels. Gives smoothed high quality interpolation, but is slower.
   :Closest:
      No interpolation between voxels. Gives raw voxels.


.. _bpy.types.VolumeDisplay.use_slice:

Slice
-----

Renders only a single 2D section of the domain object.

.. _bpy.types.VolumeDisplay.slice_axis:

Axis
   :Auto:
      Adjust slice direction according to the view direction.
   :X/Y/Z:
      Slice along the X, Y, or Z axis.

.. _bpy.types.VolumeDisplay.slice_depth:

Position
   Position of the slice relative to the length of the respective domain side.


.. _bpy.types.VolumeRender:

Render
======

.. _bpy.types.VolumeRender.space:

Space
   Specifies how volume density and step size are computed.

   :Object:
      Keeps volume *Density* and *Detail* the same regardless of object scale.
   :World:
      Specify *Step Size* and *Density* in world space.

.. _bpy.types.VolumeRender.clipping:

Clipping :guilabel:`Cycles Only`
   Value under which voxels are considered empty space to optimize rendering.

.. _bpy.types.VolumeRender.precision:

Precision :guilabel:`Cycles Only`
   Specifies volume data precision. Lower values reduce memory consumption at the cost of detail.

   :Full: Full float (Use 32 bit for all data).
   :Half: Half float (Use 16 bit for all data).
   :Variable: Automatically use less precision for less noticeable areas.

.. _bpy.types.Volume.velocity_grid:

Velocity Grid :guilabel:`Cycles Only`
   The name of the grid that contains voxel velocities, for calculating motion blur.
   This can be the name of a single grid containing 3D vectors,
   or a prefix of three separate grids containing scalar values.
   In the latter case, the X grid should have a name suffix of ``x``, ``.x`` or ``_x``,
   with similar conventions for the Y and Z grids.

.. _bpy.types.Volume.velocity_unit:

Velocity Unit :guilabel:`Cycles Only`
   Whether the velocity grid(s) specify distances per frame or per second.

.. _bpy.types.Volume.velocity_scale:

Velocity Scale :guilabel:`Cycles Only`
   A custom multiplier to apply to the velocities in the VDB.
