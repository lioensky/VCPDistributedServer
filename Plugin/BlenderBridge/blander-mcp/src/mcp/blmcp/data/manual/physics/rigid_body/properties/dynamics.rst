
********
Dynamics
********

.. reference::

   :Panel:     :menuselection:`Physics --> Rigid Body --> Dynamics`

.. figure:: /images/physics_rigid-body_properties_dynamics_panel.png

   Rigid Body Dynamics panel.

Used to control the physics of the rigid body simulation.
This panel is available only for *Active* type of rigid bodies.

Damping Translation
   Amount of linear velocity that is lost over time.

Rotation
   Amount of angular velocity that is lost over time.


Deactivation
============

Enable deactivation of resting rigid bodies. Allows the object to be deactivated during the simulation
(improves the performance and stability, but can cause glitches).

Start Deactivated
   The rigid body starts deactivated. It will be activated when in proximity of
   moving active rigid body objects. The proximity check uses the object's
   bounding box to determine if a moving object is close enough to activate it.

Linear Velocity
   Specifies the linear deactivation velocity below which the rigid body
   is deactivated and the simulation stops simulating the object.

Angular Velocity
   Specifies the angular deactivation velocity below which the rigid body
   is deactivated and the simulation stops simulating the object.
