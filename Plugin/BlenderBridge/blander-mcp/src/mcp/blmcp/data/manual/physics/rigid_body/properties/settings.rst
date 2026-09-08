
********
Settings
********

.. reference::

   :Panel:     :menuselection:`Physics --> Rigid Body --> Settings`

.. figure:: /images/physics_rigid-body_properties_settings_panel.png

   Default rigid body panel.

.. _bpy.types.RigidBodyObject.mass:

Mass
   Specifies how heavy the object is and "weights" irrespective of gravity.

   .. tip::

      There are predefined mass presets available with the :ref:`bpy.ops.rigidbody.mass_calculate` operator.

.. _bpy.types.RigidBodyObject.enabled:

Dynamic
   Enables/disables rigid body simulation for the object.

.. _bpy.types.RigidBodyObject.kinematic:

Animated
   Allows the rigid body to additionally be controlled by the animation system.
