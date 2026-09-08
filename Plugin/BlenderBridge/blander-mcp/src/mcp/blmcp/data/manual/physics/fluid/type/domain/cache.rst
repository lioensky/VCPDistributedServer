
*****
Cache
*****

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Cache`
   :Type:      Domain

The *Cache* panel is used to :term:`Bake <Baking>` the fluid simulation and stores the outcome of
a simulation so it does not need to be recalculated.

Baking takes a **lot** of compute power (hence time). Depending on the scene, it is recommended
to allocate enough time for the baking process.

If the mesh has modifiers, the rendering settings are used for exporting the mesh to the fluid solver.
Depending on the setting, calculation times and memory use might exponentially increase. For example,
when using a moving mesh with *Subdivision Surface* as an obstacle, it might help to decrease simulation
time by switching it off, or to a low subdivision level. When the setup/rig is correct, you can always
increase settings to yield a more realistic result.

.. note::

   Fluid simulations use their own cache. All other physics simulations make use of
   the :doc:`General Baking </physics/baking>` operators.

.. _bpy.types.FluidDomainSettings.cache_directory:

Cache Directory
   Directory to store baked simulation files in. Inside this directory each simulation type
   (i.e. mesh, particles, noise) will have its own directory containing the simulation data.

.. _bpy.types.FluidDomainSettings.cache_frame_start:

Frame Start
   The simulation starts on this frame, and this is the first one that is baked.

.. _bpy.types.FluidDomainSettings.cache_frame_end:

End
   The simulation ends on this frame, and this is the last one to be baked.

   .. note::

      The simulation is only calculated for positive frames between the *Start* and *End* frames
      of the *Cache* panel. So if you want a simulation that is longer than the default frame range
      you have to change the *End* frame.

.. _bpy.types.FluidDomainSettings.cache_frame_offset:

Offset
   Frame offset that is used when loading the simulation from the cache.
   It is not considered when baking the simulation, only when loading it.

.. _bpy.types.FluidDomainSettings.cache_type:

Type
   The type of the cache determines how the cache can be baked.

   :Replay:
      The cache will be baked as the simulation is being played in the viewport.
   :Modular:
      The cache will be baked step by step: The bake operators for this type are spread across various panels within
      the domain settings (e.g. the bake tool for the mesh can be found in the Mesh panel).
   :All:
      The cache will be baked with a single tool. All selected settings will be considered during this bake.
      The bake tool for this type can be found in the Cache panel.

   .. important::

      "Replay" only works when the :ref:`Playback Sync mode <bpy.types.Scene.sync_mode>` is set to "Play Every Frame".
      If you need to use "Frame Dropping" or "Sync to Audio", consider using the "Modular" or "All" options below.

.. _bpy.types.FluidDomainSettings.cache_resumable:

Resumable
   Extra data will be saved so that you can resumed baking after pausing. Since more data will be written
   to drive it is recommended to avoid enabling this option when baking at high resolutions.

.. _bpy.ops.fluid.bake_all:
.. _bpy.ops.fluid.free_all:

Bake All, Free All
   This option is only available when using the :ref:`Final <bpy.types.FluidDomainSettings.cache_type>` cache type.
   *Bake All* will run the simulation considering all parameters from
   the settings (i.e. it will bake all steps that can be baked individually with
   the :ref:`Modular <bpy.types.FluidDomainSettings.cache_type>` cache type at once).

   The progress will be displayed in the status bar. Pressing :kbd:`Esc` will abort the simulation.

   Once the simulation has been baked, the cache can be deleted by pressing *Free All*.
   It is not possible to pause or resume a *Bake All* process as
   only the most essential cache files are stored on drive.


Volumetric Data
===============

.. _bpy.types.FluidDomainSettings.cache_data_format:

Format
   File format for volume based simulation data (i.e. grids and particles).

   :Uni Cache:
      Blender's own caching format with some compression.
      Each simulation object is stored in its own ``.uni`` cache file.
   :OpenVDB:
      Advanced and efficient storage format.
      All simulation objects (i.e. grids and particles) are stored in a single ``.vdb`` file per frame.

.. _bpy.types.FluidDomainSettings.openvdb_cache_compress_type:

Compression :guilabel:`OpenVDB Only`
   Compression method that is used when writing OpenVDB cache files.

   :Zip:
      Cache files will be written with ``Zip`` compression. Effective but slower than ``Blosc``.
   :Blosc:
      Cache files will be written with ``Blosc`` compression. Multithreaded compression,
      similar in size and quality to ``Zip`` compression.
   :None:
      Cache files will be written without any compression.

.. _bpy.types.FluidDomainSettings.openvdb_data_depth:

Precision :guilabel:`OpenVDB Only`
   Precision level that is used when writing OpenVDB cache files.

   :Full:
      Volumetric data (e.g. grids, particles) will be written with full precision (32-bit).
   :Half:
      Volumetric data (e.g. grids, particles) will be written with half precision (16-bit).
   :Mini:
      Volumetric data (e.g. grids, particles) will be written with mini float precision (8-bit) where possible.
      For cache data where this is not possible, 16-bit floats will be used instead.

.. _bpy.types.FluidDomainSettings.cache_mesh_format:

Meshes :guilabel:`Liquids Only`
   File format for the mesh cache files.

   Binary Object: Mesh data files with some compression.
   Object: Simple, standard data format for mesh data.

.. _bpy.types.FluidDomainSettings.export_manta_script:

Export Mantaflow Script
   Export the simulation as a standalone Mantaflow script when baking the scene (exported on "Bake Data").
   Usually, only developers and advanced users who know how to use the Mantaflow GUI will
   make use of this functionality. Use a :ref:`Debug Value <bpy.ops.wm.debug_menu>` of ``3001`` to enable.
