.. index:: Object Constraints; Transform Cache Constraint
.. _bpy.types.TransformCacheConstraint:

**************************
Transform Cache Constraint
**************************

The *Transform Cache Constraint* streams an animation from an
:doc:`Alembic </files/import_export/alembic>` or :doc:`USD </files/import_export/usd>`
file. For example, it can apply a baked rigid body simulation to an object.

The constraint is automatically added when importing such a file. However, it only applies
to transforms (location/rotation/scale of the whole object). For animations that cause
deformation, the :doc:`/modeling/modifiers/modify/mesh_sequence_cache` is used instead.


Options
=======

.. figure:: /images/animation_constraints_transform_transform-cache_panel.png

   Transform Cache Constraint.

Cache File
   Data-block menu to select the Alembic or USD file.

File Path
   Path to the Alembic or USD file.

Sequence
   Whether or not the cache is separated in a series of files.

Override Frame
   Whether to use a custom frame for looking up data in the cache file,
   instead of using the current scene frame.

   The *Frame* value is the time to use for looking up the data in the cache file,
   or to determine which to use in a file sequence.

Frame Offset
   Subtracted from the current frame to use for looking up the data in the cache file,
   or to determine which file to use in a file sequence.

Manual Scale
   Value by which to enlarge or shrink the object with respect to the world's origin.

Velocity Attribute
   The name of the Alembic attribute used for generating motion blur data;
   by default, this is ``.velocities`` which is standard for most Alembic files.

   .. note:: The *Velocity Attribute* option is currently for Alembic files only.

Velocity Unit
   Defines how the velocity vectors are interpreted with regard to time.

   :Frame:
      The velocity unit was encoded in frames and does not need to be scaled by scene FPS.
   :Second:
      The velocity unit was encoded in seconds and needs to be scaled by the scene FPS (1 / FPS).

   .. note:: The *Velocity Unit* option is currently for Alembic files only.

Object Path
   The path to the Alembic or USD object inside the archive or stage.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the object.
