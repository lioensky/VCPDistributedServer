.. _bpy.types.Brush.cloth:

*****
Cloth
*****

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

This brush simulates cloth physics on the mesh under the brush cursor.
There are various deformation types and settings to customize the brush.

It's also easy to sculpt the mesh with other brushes and tools
in between using the cloth brushes.

.. note::

   Using a relatively small brush size makes the calculations much faster,
   while larger brush sizes might be too slow to get a usable brush.


Brush Settings
==============

General
-------

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

Persistent
   Allows the cloth brush to not accumulate deformation after each stroke.
   This is convenient to always simulate the cloth based on the same initial shape,
   but applying different forces to it.

   When disabled, deformations accumulate after each stroke.

Set Persistent Base
   Resets the base mesh so that you can add another layer of deformations.

.. _bpy.types.Brush.cloth_simulation_area_type:

Simulation Area
   Selects the part of the mesh that is going to be simulated when the stroke is active.
   This can greatly affect performance depending on the complexity of the mesh.

   Local
      Simulates only a specific area around the brush limited by a fixed radius.
   Global
      Simulates the entire mesh.
   Dynamic
      The active simulation area moves with the brush while still being limited by a fixed radius.

.. _bpy.types.Brush.cloth_sim_limit:

Simulation Limit
   The Factor added relative to the size of the radius to limit the cloth simulation effects.

.. _bpy.types.Brush.cloth_sim_falloff:

Simulation Falloff
   The area to apply deformation falloff to the effects of the simulation.
   This setting is a factor of the *Simulation Limit* and is shown as a dashed line around the cursor.

.. _bpy.types.Brush.use_cloth_pin_simulation_boundary:

Pin Simulation Boundary
   Lock the position of the vertices in the simulation falloff area to avoid artifacts
   and create a softer transition with unaffected areas.

.. _bpy.types.Brush.cloth_deform_type:

Deformation
   The type of cloth deformation that is used by the brush.

   :Drag:
      Simulates pulling the cloth to the cursor,
      similar to placing a finger on a table cloth and pulling.
   :Push:
      Simulates pushing the cloth away from the cursor,
      similar to placing a finger on a table cloth and pushing.
   :Pinch Point:
      Simulates pulling the cloth into a point.
   :Pinch Perpendicular:
      Simulates pulling the brush into a line.
   :Inflate:
      Simulates air being blown under the cloth so that the cloth lifts up.
   :Grab:
      Simulates picking up and moving the cloth.
   :Expand:
      Simulates stretching the cloth out.
   :Snake Hook:
      Simulates moving the cloth without producing any artifacts in the surface
      and creates more natural looking folds than any of the other deformation modes.
      This is accomplished by adjusting the strength of the deformation constraints per brush step
      to avoid affecting the results of the simulation as much as possible.

.. _bpy.types.Brush.cloth_force_falloff_type:

Force Falloff
   Shape used in the brush to apply force to the cloth.

   :Radial: Applies the force as a sphere.
   :Plane: Applies the force as a plane.

.. _bpy.types.Brush.cloth_mass:

Cloth Mass
   Mass of each simulation particle.

.. _bpy.types.Brush.cloth_damping:

Cloth Damping
   How much the applied forces are propagated through the cloth.

.. _bpy.types.Brush.cloth_constraint_softbody_strength:

Soft Body Plasticity
   The amount the cloth preserves its original shape,
   acting as a :doc:`Soft Body </physics/soft_body/index>`.

.. _bpy.types.Brush.use_cloth_collision:

Use Collisions
   Enables the detection of collisions with other objects during the simulation.
   In order for the sculpt object to collide with objects,
   the collision object must have :doc:`Collision Physics </physics/collision>` activated.
