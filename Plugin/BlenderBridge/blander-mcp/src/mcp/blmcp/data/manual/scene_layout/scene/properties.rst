
****************
Scene Properties
****************

Scene
=====

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Scene`

.. _bpy.types.Scene.camera:

Camera
   Used to select which camera is used as the active camera.
   You can also set the active camera in the 3D Viewport with :kbd:`Ctrl-Numpad0`.

.. _bpy.types.Scene.background_set:

Background Scene
   Allows you to use a scene as a background,
   this is typically useful when you want to focus on animating the foreground for example,
   without background elements getting in the way.

   This scene can have its own animation, physics simulations, etc,
   but you will have to select it from the *Scene* data-block menu, if you want to edit any of its contents.

   Background Scenes can themselves have a Background Scene (they're recursively included).
   So you can always make additions to existing scenes by using them as a background
   to a newly created scene where your additions are made.

   .. tip::

      This can also be used in combination with :ref:`Linking to a Scene <bpy.ops.object.make_links_scene>`,
      where one blend-file contains the environment, which can be reused in many places.

.. _bpy.types.Scene.active_clip:

Active Clip
   Selects a :doc:`Movie Clip </movie_clip/index>` that can be used by
   :doc:`/animation/constraints/motion_tracking/index` or a camera's :ref:`bpy.types.CameraBackgroundImage`.


.. _bpy.types.UnitSettings:

Units
=====

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Units`

.. _bpy.types.UnitSettings.system:

Unit System
   The unit system to use for user interface controls.

   :None:
      Use units that have with no relation to the real world,
      practically this is the same as *Metric* just without unit names.
   :Metric: Use the metric unit system in this scene.
   :Imperial: Use the imperial unit system in this scene.

.. _bpy.types.UnitSettings.scale_length:

Unit Scale
   Scale factor to use when converting between internal units and values displayed in the user interface.
   This can be changed when modeling at microscopic or astronomical scales.

   .. note::

      This only influences the values displayed in the user interface
      and not how things behave internally. For example, physics simulations
      don't take the unit scale into account.

.. _bpy.types.UnitSettings.use_separate:

Separate Units
   When using *Metric* or *Imperial*, display properties as multiple values.
   For example, ``2.285m`` will become ``2m 28.5cm``.

.. _bpy.types.UnitSettings.system_rotation:

Rotation
   Unit to use for displaying/editing rotation values.

   :Degrees: Use degrees for angles in the user interface.
   :Radians: Use radians for angles in the user interface.

.. _bpy.types.UnitSettings.length_unit:

Length
   Unit that will be used to display length values.

   :Adaptive:
      The unit used for a specific value depends on the magnitude of the value.
      For example, some values might be displayed as ``23cm`` while others are
      displayed as ``10km``.
   :Meters/Centimeters/Feet:
      A fixed unit that will be used for all lengths in the user interface.

.. _bpy.types.UnitSettings.mass_unit:

Mass
   See *Length*.

.. _bpy.types.UnitSettings.time_unit:

Time
   See *Length*.

.. _bpy.types.UnitSettings.temperature_unit:

Temperature
   See *Length*.

.. Normally we would avoid documenting long lists of values
   however, this is not displayed anywhere else.

.. list-table:: Imperial Length Units
   :header-rows: 1
   :stub-columns: 1

   * - Full Name
     - Short Name(s)
     - Scale of a Meter
   * - thou
     - ``mil``
     - 0.0000254
   * - inch
     - ``"``, ``in``
     - 0.0254
   * - foot, feet
     - ``'``, ``ft``
     - 0.3048
   * - yard
     - ``yd``
     - 0.9144
   * - chain
     - ``ch``
     - 20.1168
   * - furlong
     - ``fur``
     - 201.168
   * - mile
     - ``mi``, ``m``
     - 1609.344

.. list-table:: Metric Length Units
   :header-rows: 1
   :stub-columns: 1

   * - Full Name
     - Short Name(s)
     - Scale of a Meter
   * - micrometer
     - ``um``
     - 0.000001
   * - millimeter
     - ``mm``
     - 0.001
   * - centimeter
     - ``cm``
     - 0.01
   * - decimeter
     - ``dm``
     - 0.1
   * - meter
     - ``m``
     - 1.0
   * - dekameter
     - ``dam``
     - 10.0
   * - hectometer
     - ``hm``
     - 100.0
   * - kilometer
     - ``km``
     - 1000.0


Gravity
=======

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Gravity`

Options to control global gravity used for physics effects.

See the :doc:`Physics chapter </physics/forces/gravity>` for more information.


Simulation
==========

.. _bpy.types.Scene.use_custom_simulation_range:

Simulation Range
   Use a simulation range that is different from the scene range for
   :doc:`Simulation Nodes </modeling/geometry_nodes/simulation/simulation_zone>`
   that do not override the frame range themselves.

Start, End
   The frame at which the simulation starts/ends.


Keying Sets
===========

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Keying Sets`

See :doc:`/animation/keyframes/keying_sets`.


.. _data-scenes-audio:

Audio
=====

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Audio`

Options to control global audio settings.
To control how sounds is played back from within Blender, see the audio settings
in the :ref:`Preferences <prefs-system-sound>`.

.. _bpy.types.Scene.audio_volume:

Volume
   Volume for the scene.

.. _bpy.types.Scene.audio_distance_model:

Distance Model
   Changes how the sound attenuation is calculated based on the distance.
   Most physically correct is the *Inverse* model,
   but it's also possible to choose a linear and an exponential falloff.
   The clamped modes limit the volume to be lower than 100% (1.0),
   that means if the distance is smaller than the reference distance, the volume is always 100%.
   For an exact description of each option
   see the `OpenAL documentation <https://www.openal.org/documentation/>`__.

.. _bpy.types.Scene.audio_doppler_speed:

Doppler Speed
   Speed of the sound for the Doppler effect calculations.
   The typical value is 343.3 m/s in air, in water for example this value is around 1560 m/s.

.. _bpy.types.Scene.audio_doppler_factor:

Doppler Factor
   Controls how strong the Doppler effect is.
   You can exaggerate or attenuate the change of pitch, but physically correct is a factor of 1.0.

.. _bpy.ops.sound.bake_animation:

Update Animation Cache
   Updates the audio animation cache. This is useful if you start noticing artifact in the audio.


Rigid Body World
================

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Rigid Body World`

The *Rigid Body World* is a group of rigid body objects,
which holds settings that apply to all rigid bodies in this simulation.

See :doc:`Rigid Body World </physics/rigid_body/world>` for more information.


.. _scene-properties-animation:

Animation
=========

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> Animation`

Controls animation data for scene-level properties, including active :doc:`Actions </animation/actions>`
and their assigned :ref:`Slot <animation-actions-slots>`.

See :ref:`animation-actions-slots-manual-assign` for more information.

Scene
   Specifies the action and slot where animation data for scene properties is stored/retrieved.


Custom Properties
=================

Create and manage your own properties to store data in the scene's data block.
See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.
