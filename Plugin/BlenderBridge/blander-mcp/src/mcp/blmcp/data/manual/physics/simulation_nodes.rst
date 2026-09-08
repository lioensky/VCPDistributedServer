
****************
Simulation Nodes
****************

Through the use of :doc:`Simulation Zones </modeling/geometry_nodes/simulation/simulation_zone>`,
:doc:`/modeling/geometry_nodes/index` can be used to create custom physic simulations through nodes.
Simulation zones allow the result of one frame to influence the next one.
That way even a set of simple rules can lead to complex results, with the passing of time.
The most common type of them is physics simulation, with specific solvers for physical phenomena.

.. seealso::

   Read more about :doc:`Simulation Zones </modeling/geometry_nodes/simulation/simulation_zone>`


Baking
======

The simulation is automatically cached during playback.
The valid cache can be seen as a strong yellow line in the timeline editor.
This allows for animators to quickly inspect all the previous frames of a simulation.

.. figure:: /images/modeling_geometry-nodes_simulation_baking_timeline.png
   :align: center

   Cached frames in the Timeline.

When the result is ready to be sent to a render-farm, it can be baked to disk.
This allows for the simulation to be rendered in a non-sequential order.

.. figure:: /images/modeling_geometry-nodes_simulation_baking.png
   :align: center

   Simulation and Physics, Geometry Nodes user interface.

.. note::

   Baking the simulation will bake all the simulations in all modifiers for the selected objects.

.. _bpy.ops.object.simulation_nodes_cache_calculate_to_frame:

Calculate to Frame
   Calculate simulations in geometry nodes modifiers from the start to current frame.

.. _bpy.ops.object.simulation_nodes_cache_bake:

Bake
   Bake simulations in geometry nodes modifiers.
   In order to bake the simulation, the blend-file must be saved to your computer.
   The location the file is saved determines where the baked data is also saved.
   The directory the baked data is saved to can be changed per modifier in the
   :ref:`Internal Dependencies <bpy.types.NodesModifier.bake_directory>`.

   .. _bpy.ops.object.simulation_nodes_cache_delete:

   Delete Cached Simulation
      Delete cached/baked simulations in geometry nodes modifiers

.. _bpy.types.Object.use_simulation_cache:

Cache
   For the cases where the current frame is the only one relevant,
   users can opt-out of caching the results to save memory.


Examples
========

Combined with the :doc:`/modeling/geometry_nodes/geometry/sample/index_of_nearest`,
this can be used for a number of sphere-based simulations.

.. figure:: /images/modeling_geometry-nodes_simulation_example.png
   :align: center

   Index of Nearest sample file CC-BY Sean Christofferson.
