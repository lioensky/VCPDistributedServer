.. index:: Force Fields

************
Introduction
************

Force fields offer a way to influence a simulation, in example to add extra movement.
:doc:`Particles </physics/particles/index>`, :doc:`Soft Bodies </physics/soft_body/index>`,
:doc:`Rigid Bodies </physics/rigid_body/index>`, and :doc:`Cloth objects </physics/cloth/index>`
can all be affected by forces fields.
Force fields automatically affect everything.
To remove a simulation or particle system from their influence,
simply turn down the influence of that type of force field in its Field Weights panel.

- All types of objects and particles can generate fields,
  but only curve object can bear a :doc:`/physics/forces/force_fields/types/curve_guide` field.
- Force fields can also be generated from particles.
  See :doc:`Particle Physics </physics/particles/emitter/physics/index>`.
- The objects need to share at least one common layer to have an effect.

You may limit the effect on particles to a group of objects
(see the :doc:`Particle Physics </physics/particles/emitter/physics/index>` page).


Creating a Force Field
======================

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Add --> Force Field`
   :Panel:     :menuselection:`Physics --> Force Field`

To create a single force field,
you can select :menuselection:`Add --> Force Field` and select the desired force field.
This method creates an empty with the force field attached.

.. list-table:: Examples of an empty with the force field attached.

   * - .. figure:: /images/physics_forces_force-fields_types_vortex_visualzation.png

          Vortex: force field.

     - .. figure:: /images/physics_forces_force-fields_types_wind_visualzation.png

          Wind: force field.

     - .. figure:: /images/physics_forces_force-fields_types_force_visualzation.png

          Force: force field.

To create a field from an existing object you have to select the object and
change to the *Physics* tab. Select the field type in the *Fields* menu.

.. note::

   After changing the fields *Fields* panel or deflection *Collision* panel settings,
   you have to recalculate the particle, soft body or cloth system by *Free Cache*,
   this is not done automatically.

   Particles react to all kinds of force fields,
   soft bodies only to *Force*, *Wind*, *Vortex*
   (they react on *Harmonic* fields but not in a useful way).


.. _force-field-common-settings:

Common Field Settings
=====================

Most fields have the same settings, even though they act very differently.
Settings unique to a field type are described below.
Curve Guide and Texture fields have very different options.

.. _bpy.types.FieldSettings.shape:

Shape
   Sets the direction which is used to calculate the effector force.
   For force fields from an empty object only *Point*, *Line* and *Plane* shapes are available,
   as for a field from a 3D object there are additional *Surface* and *Every Point* options,
   and *Curve* for a field from a curve.

   :Point: Point with omnidirectional influence. Uses the object origin as the effector point.
   :Line:
      The force only acts in the local XY plane, using the Z axis line as the effector.
   :Plane:
      The force only acts in the local Z direction, using the XY axis plane as the effector.
   :Surface:
      The force field acts on a 3D object's surface.
      In this case, the Z axis is the surface normal.
   :Every Point: Uses every vertex in the mesh object as an effector point.

.. _bpy.types.FieldSettings.strength:

Strength
   The strength of the field effect.
   This can be positive or negative to change the direction that the force operates in.
   A force field's strength is scaled with the force object's scale,
   allowing you to scale up and down the scene, keeping the same effects.

.. _bpy.types.FieldSettings.flow:

Flow
   If nonzero, this adds a drag force proportional and opposite to the point velocity.

   This effectively re-interprets the force field so that the *Strength* to *Flow* ratio
   at a certain point defines the velocity of an "air flow" field, and objects are
   encouraged to follow the flow by the resistance caused by the *Flow* drag force.

.. _bpy.types.FieldSettings.apply_to_location:
.. _bpy.types.FieldSettings.apply_to_rotation:

Affect
   Location
      Influence the location of particles and other physics entities.
   Rotation
      Influence the rotation of particles with :doc:`Dynamic Rotation </physics/particles/emitter/rotation>`.
      The option is not relevant for other types of physics systems.

   Disabling both options completely deactivates the force field.

.. _bpy.types.FieldSettings.noise:

Noise Amount
   Adds noise to the strength of the force.

.. _bpy.types.FieldSettings.seed:

Seed
   Changes the seed of the random noise.

.. _bpy.types.FieldSettings.use_absorption:

Absorption
   Force gets absorbed by collision objects.

.. _bpy.types.FieldSettings.wind_factor:

Wind Factor
   Specifies how much the force is reduced when acting parallel to a surface, e.g. cloth.
   If set to 1, only the normal component of the force is taken into account.


Falloff
-------

Here you can specify the shape of the force field
(if the falloff *Power* is greater than 0).

.. _bpy.types.FieldSettings.falloff_type:

Shape
   :Cone:
      The falloff results in a cone-shaped force field. Additional options are the same as those of *Tube* options.
   :Sphere:
      The falloff is uniform in all directions, as in a sphere.
   :Tube:
      The falloff results in a tube-shaped force field.
      The field's *Radial Power* can be adjusted,
      as well as the *Minimum* and *Maximum* distances of the field.

.. _bpy.types.FieldSettings.z_direction:

Z Direction
   The direction the force affects on the Z axis.

   :+Z: The force only has an affect on the positive Z axis.
   :-Z: The force only has an affect on the negative Z axis.
   :Both Z: The force has an affect on the positive and negative Z axis.

.. _bpy.types.FieldSettings.falloff_power:

Power
   How the power of the force field changes with the distance from the force field.
   If *r* is the distance from the origin of the object, the force changes with 1/(*r* - *min* + 1)\ :sup:`power`.
   A falloff of 2 changes the force field with 1/(*r* - *min* + 1)\ :sup:`2`,
   which is similar to the falloff of gravitational pull.

.. _bpy.types.FieldSettings.use_min_distance:
.. _bpy.types.FieldSettings.distance_min:

Min Distance
   The distance from the object's origin, up to where the force field is effective with full strength.
   If you have a falloff of 0, this parameter will have no effect,
   because the field is effective with full strength up to *Max Distance* (or infinite).
   Shown by an additional circle around the object.

.. _bpy.types.FieldSettings.use_max_distance:
.. _bpy.types.FieldSettings.distance_max:

Max Distance
   Specifies the maximum radius in which the force field affects other objects
   (shown by an additional circle around the object).
