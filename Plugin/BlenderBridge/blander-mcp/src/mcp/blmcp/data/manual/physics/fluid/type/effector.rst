
********
Effector
********

Effector objects are used to deflect fluids and influence the fluid flow. To define any mesh object
as an effector object, add fluid physics by clicking *Fluid* in :menuselection:`Properties --> Physics`.
Then select *Effector* as the fluid *Type*.

.. tip::

   :doc:`Force Fields </physics/forces/force_fields/index>`
   (such as wind or vortex) are supported, like in most physics systems.
   The influence individual force types have can be
   :doc:`controlled </physics/fluid/type/domain/field_weights>` per domain object.


.. _bpy.types.FluidEffectorSettings:

Settings
========

.. reference::

   :Panel:     :menuselection:`Physics --> Fluid --> Settings`
   :Type:      Effector

.. _bpy.types.FluidEffectorSettings.effector_type:

Effector Type
   :Collision:
      Objects of this type will collide with fluid.
   :Guide:
      The velocity of objects of this type will be used when baking the guiding.
      So fluid guiding objects should move and have some velocity.

      .. _bpy.types.FluidEffectorSettings.velocity_factor:

      Velocity Factor
         Multiply the guiding object velocities by this factor. This is useful when working with
         multiple guiding objects and some of them should have higher or smaller velocities.

      .. _bpy.types.FluidEffectorSettings.guide_mode:

      Guide Mode
         The mode describes how guiding velocities should be written into the global guiding velocity
         field of the domain.

         :Maximize:
            The guiding object will compare the existing velocity in the global velocity field with
            its own velocity. If its absolute value is greater than the absolute value in the velocity
            field the guiding velocity will be kept.
         :Minimize:
            A guiding object will compare the existing velocity in the global velocity field with its
            own velocity. If its absolute value is smaller than the absolute value in the velocity
            field the guiding velocity will be kept.
         :Override:
            The most intuitive option. A guiding object will always
            write its own current velocity into the global guiding velocity field.
            Values in the velocity field from a previous frame or guiding object
            will be overridden.
         :Averaged:
            A guiding object will write the average of its own current velocity and the existing
            guiding velocity at that cell into the global guiding velocity field.

.. _bpy.types.FluidEffectorSettings.subframes:

Sampling Substeps
   Number of substeps used to reduce gaps in collision of fluid from fast-moving effectors.

.. _bpy.types.FluidEffectorSettings.surface_distance:

Surface Thickness
   Additional area around the effector that will be considered as an effector.

.. _bpy.types.FluidEffectorSettings.use_effector:

Use Effector
   Enables or disables the effector object effect on the fluid,
   this property is useful for animations to selectively enable and disable
   when the effector affects the fluid.

.. _bpy.types.FluidEffectorSettings.use_plane_init:

Is Planar
   Defines the effector as either a single dimension object i.e. a plane or the mesh is :term:`Non-manifold`.
   This ensures that the fluid simulator will give the most accurate results for these types of meshes.

   A :term:`Manifold` mesh can also be declared as planar. The fluid solver will then ignore the volume
   inside the mesh and just emit fluid from the mesh sides.
