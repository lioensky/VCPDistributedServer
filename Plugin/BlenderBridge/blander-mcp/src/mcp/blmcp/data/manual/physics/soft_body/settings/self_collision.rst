.. _bpy.types.SoftBodySettings.use_self_collision:

**************
Self Collision
**************

.. reference::

   :Panel:     :menuselection:`Physics --> Soft Body --> Self Collision`

.. note::

   *Self-Collision* is working only if you have activated *Use Edges*.

When enabled, allows you to control how Blender will prevent the soft body from intersecting with itself.
Every vertex is surrounded with an elastic virtual ball.
Vertices may not penetrate the balls of other vertices.
If you want a good result you may have to adjust the size of these balls.
Normally it works pretty well with the default options.

.. _bpy.types.SoftBodySettings.collision_type:

Calculation Type
   :Manual:
      The *Ball Size* directly sets the ball size.
   :Average:
      The average length of all edges attached to the vertex is calculated and then multiplied
      with the *Ball Size* setting. Works well with evenly distributed vertices.
   :Minimal/Maximal:
      The ball size is as large as the smallest/largest spring length of the vertex multiplied with the *Ball Size*.
   :Average Min Max:
      Size = ((Min + Max)/2) × *Ball Size*.

.. _bpy.types.SoftBodySettings.ball_size:

Ball Size
   Fraction of the length of attached edges.
   The edge length is computed based on the chosen algorithm.
   This setting is the factor that is multiplied by the spring length.
   It is a spherical distance (radius) within which, if another vertex of the same mesh enters,
   the vertex starts to deflect in order to avoid a self-collision.

   Set this value to the fractional distance between vertices that you want them to have their own "space".
   Too high of a value will include too many vertices at all times and slow down the calculation.
   Too low of a level will let other vertices get too close and thus possibly intersect because
   there will not be enough time to slow them down.

.. _bpy.types.SoftBodySettings.ball_stiff:

Stiffness
   How elastic that ball of personal space is.
   A high stiffness means that the vertex reacts immediately to another vertex enters their space.

.. _bpy.types.SoftBodySettings.ball_damp:

Dampening
   How the vertex reacts.
   A low value just slows down the vertex as it gets too close. A high value repulses it.

.. note::

   Collisions with other objects are set in the (other) :doc:`Collision panel </physics/collision>`.
   To collide with another object they have to share at least one common layer.
