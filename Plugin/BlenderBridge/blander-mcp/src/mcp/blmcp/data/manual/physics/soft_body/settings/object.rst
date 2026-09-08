
******
Object
******

.. _bpy.types.SoftBodySettings.friction:

Friction
   The friction of the surrounding medium. Generally friction dampens a movement.
   The larger the friction, the more viscous is the medium.
   Friction always appears when a vertex moves relative to its surround medium.

.. _bpy.types.SoftBodySettings.mass:

Mass
   Mass value for vertices.
   Larger mass slows down acceleration, except for gravity where the motion is constant regardless of mass.
   Larger mass means larger inertia, so also braking a soft body is more difficult.

.. _bpy.types.SoftBodySettings.vertex_group_mass:

Control Point
   You can paint weights and use a specified vertex group for mass values.
