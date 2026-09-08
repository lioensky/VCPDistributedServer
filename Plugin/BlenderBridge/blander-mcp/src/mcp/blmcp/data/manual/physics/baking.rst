.. _bpy.types.PointCache:
.. _bpy.ops.ptcache:

**************************
Baking Physics Simulations
**************************

:term:`Baking` refers to the act of storing or caching the results of a calculation.
The result of a simulation is automatically cached to memory when the animation is played,
so that the next time it runs, it can be replayed more quickly by reading the results from the memory.

If you bake the simulation the cache is protected,
and you will be unable to change the simulation settings
until you clear the baked frames by clicking *Delete Bake*.

It is generally recommended to bake your physics simulations before rendering.
Aside from no longer needing to go through the time-consuming process of simulating again,
baking can help prevent potential glitches and ensure that the outcome of the simulation
remains exactly the same every time.

.. A screenshot of the baking interface is intentionally omitted, as it
   the available options vary slightly between different physics systems.

.. note::

   Most physics simulators in Blender use a similar system,
   but not all have exactly the same settings available. All the settings are covered here,
   but individual physics types may not provide all these options.


Options
=======

.. figure:: /images/physics_baking_multi-cache-interface.png
   :align: right

   Two different caches stored simultaneously.

Caches List
   Blender allows for storing and managing multiple caches at once for the same physics object.
   You can manage the caches with this :ref:`list view <ui-list-view>`.
   Double-click the cache entry to give it a name.

   Each cache can have a name. Double-click the cache entry to give it a name.
   If this name is given, any disk cache will be stored in files starting with that name.
   For example, a cache named ``MyCache`` will be stored in ``MyCache_xxxxxx_yy.bphys``.

   If the cache does not have a name (which is the default),
   the filename of the cache will depend on the object it is attached to,
   although this is not immediately obvious. For example, a cache on
   an object ``Cube`` will be stored in ``43756265_xxxxxx_yy.bphys``,
   where ``43756265`` is determined by the object name.

   .. warning::

      When there are multiple caches on one object, **always specify a Cache Name**. As described above,
      the filename of an unnamed cache is determined by the name of the object it is attached to.
      As a result, an object with multiple physics systems that all have an unnamed cache will cause
      conflict and **can result in losing cache files**.

External
   Allows you to read the cache from a drive using a user-specified file path.

   .. note::

      The cache name in *Caches List* and the *Index*
      has to exactly match the external cache files name in order to work.
      The cache files name format is ``name_frame_index.bphys``.

   Index
      The index number of cache files. (The last two digits of the files name.)
   Path
      Select the directory path to the cache files.

Disk Cache
   The cache of a baked simulation will be stored inside the blend-file when you save it.
   When *Disk Cache* is checked, Blender will save the cache separately to
   the drive in a folder named ``blendcache_[filename]`` alongside the blend-file.
   (The blend-file must be saved first.)

   .. note::

      When using :doc:`/files/linked_libraries/library_overrides`,
      data-blocks only support *Disk Cache* storage.

Use Library Path
   Share the disk cache when the physics object is
   :doc:`linked </files/linked_libraries/index>` into another blend-file.
   When this option is enabled, linked versions of the object will reference the same disk cache.
   Otherwise linked versions of the object will use independent caches.

Start
   Frame on which to start the simulation.
End
   Frame on which to stop the simulation.

   .. note::

      The simulation is only calculated for positive frames
      in between the *Start* and *End* frames of the *Cache* panel, whether you bake or not.
      So if you want a simulation that is longer than the default frame range you have to change the *End* frame.

Cache Step
   Interval for storing simulation data.

   .. note::

      Some physics systems (such as particles)
      allow for positions to be stored only on every nth frame,
      letting the positions for in-between frames be interpolated.
      Using a cache step greater than one will result in a smaller cache,
      but the result may differ from the original simulation.


.. _physics-bake:

Baking
======

Bake
   Start baking.
   Blender will become unresponsive during most baking operations.
   The cursor will display as a number representing the progress of the baking.
   You need to be in Object Mode to bake.

.. _delete-physics-bake:

Delete Bake
   Mark the baked cache as temporary. The data will still exist,
   but will be removed with the next object modification and frame change.
   This button is only available when the physics system has been baked.

.. _calc-physics-bake-to-frame:

Calculate to Frame
   Bake only up to the current frame. Limited by *End* frame set in the cache settings.
Current Cache to Bake
   Store any temporarily cached simulation data as a bake.
   Note that playing the animation will try to simulate any visible physics simulations.
   Depending on the physics type, this data may be temporarily cached.
   Normally such temporary caches are cleared when an object or setting is
   modified, but converting it to a bake will "save" it.

Bake All Dynamics
   Bake all physics systems in the scene, even those of different types.
   Useful for baking complex setups involving interactions between different physics types.

   See :ref:`Bake <physics-bake>`.
Delete All Bakes
   Delete bakes of all physics systems in the scene, even those of different types.

   See :ref:`Delete Bake <delete-physics-bake>` for more information.
Update All to Frame
   Bake all physics systems in the scene to the current frame.

   See :ref:`Calculate To Frame <calc-physics-bake-to-frame>`.
