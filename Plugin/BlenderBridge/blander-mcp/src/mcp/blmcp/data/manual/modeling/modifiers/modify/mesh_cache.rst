.. index:: Modeling Modifiers; Mesh Cache Modifier
.. _bpy.types.MeshCacheModifier:

*******************
Mesh Cache Modifier
*******************

The *Mesh Cache* modifier applies animated mesh data from an external file to a mesh, allowing it to deform over time.
It is commonly used for importing animations from other applications, enabling smooth playback of cached deformations.

This modifier functions similarly to :doc:`shape keys </animation/shape_keys/introduction>`,
but is specifically designed for playback of externally stored animations rather than keyframe-based deformations.

.. important::

   Both ``.mdd`` and ``.pc2`` file formats rely on a consistent vertex order throughout the animation.
   Adding, removing, or reordering vertices after this modifier may cause unintended results.


Options
=======

.. figure:: /images/modeling_modifiers_modify_mesh-cache_panel.png
   :align: right
   :width: 300px

   Mesh Cache Modifier.

Format
   Specifies the input file format. The modifier currently supports ``.mdd`` and ``.pc2``.

File Path
   Path to the external cache file containing the animation data.

Influence
   Controls the strength of the deformation. Lower values blend the cached animation with the original mesh shape.

Deform Mode
   Determines how the cache data influences the mesh:

   :Overwrite:
      Replaces vertex positions with those from the cache file.
   :Integrate:
      Blends the cache deformation with existing deformations, such as shape keys or modifiers.

      .. note::

         This mode is best suited for minor, localized adjustments.
         Large transformations, such as reposing limbs, may not work as expected.

Interpolation
   Controls how frames between cache data are handled:

   :None:
      Uses only the raw frame data from the cache without interpolation.
   :Linear:
      Blends between frames for smoother transitions, useful when cache frames do not align perfectly with the scene
      frames.

Vertex Group
   If set, restrict the effect to the only vertices in that vertex group.

   :bl-icon:`arrow_leftright` Invert
      Inverts the influence of the selected vertex group, meaning that the group
      now represents vertices that will not be deformed by the modifier.

      The setting reverses the weight values of the group.


Time Remapping
--------------

Time Mode
   Defines how animation time is interpreted:

   :Frame:
      Ignores timing data from the cache and plays back frames directly.
      This mode provides direct control over playback speed.
   :Time:
      Uses the cache's timing data, including offsets and frame durations.
   :Factor:
      Maps the entire animation to a range between ``0`` and ``1`` for precise control.

Play Mode
   Specifies how playback timing is determined:

   :Scene:
      Uses the scene's current frame for playback.

      Frame Start
         Defines the starting frame for playback.
      Frame Scale
         Adjusts the playback speed by scaling time.

   :Custom:
      Allows manual control of animation timing.

      Evaluation Value
         Determines animation playback position, which can be animated for precise control.


Axis Mapping
------------

Forward/Up Axis
   Specifies the forward and up axes of the imported animation, ensuring proper orientation.

Flip Axis
   Flips the animation along a chosen axis if the imported data requires correction.
