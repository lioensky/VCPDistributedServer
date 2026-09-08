Particle Operators
==================

.. module:: bpy.ops.particle

.. function:: brush_edit(*, stroke=None, pen_flip=False)

   Apply a stroke of brush to the particles

   :param stroke: Stroke, (optional)
   :type stroke: :class:`bpy_prop_collection`\ [:class:`OperatorStrokeElement`] | None
   :param pen_flip: Pen Flip, Whether a tablet's eraser mode is being used (optional)
   :type pen_flip: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: connect_hair(*, all=False)

   Connect hair to the emitter mesh

   :param all: All Hair, Connect all hair systems to the emitter mesh (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy_particle_systems(*, space='OBJECT', remove_target_particles=True, use_active=False)

   Copy particle systems from the active object to selected objects

   :param space: Space, Space transform for copying from one object to another (optional)

      - ``OBJECT``
        Object -- Copy inside each object's local space.
      - ``WORLD``
        World -- Copy in world space.
   :type space: Literal['OBJECT', 'WORLD']
   :param remove_target_particles: Remove Target Particles, Remove particle systems on the target objects (optional)
   :type remove_target_particles: bool
   :param use_active: Use Active, Use the active particle system from the context (optional)
   :type use_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: delete(*, type='PARTICLE')

   Delete selected particles or keys

   :param type: Type, Delete a full particle or only keys (optional)
   :type type: Literal['PARTICLE', 'KEY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: disconnect_hair(*, all=False)

   Disconnect hair from the emitter mesh

   :param all: All Hair, Disconnect all hair systems from the emitter mesh (optional)
   :type all: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: duplicate_particle_system(*, use_duplicate_settings=False)

   Duplicate particle system within the active object

   :param use_duplicate_settings: Duplicate Settings, Duplicate settings as well, so the new particle system uses its own settings (optional)
   :type use_duplicate_settings: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: dupliob_copy()

   Duplicate the current instance object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: dupliob_move_down()

   Move instance object down in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: dupliob_move_up()

   Move instance object up in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: dupliob_refresh()

   Refresh list of instance objects and their weights

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: dupliob_remove()

   Remove the selected instance object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: edited_clear()

   Undo all edition performed on the particle system

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: hair_dynamics_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove a Hair Dynamics Preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: hide(*, unselected=False)

   Hide selected particles

   :param unselected: Unselected, Hide unselected rather than selected (optional)
   :type unselected: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: mirror()

   Duplicate and mirror the selected particles along the local X axis

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: new()

   Add new particle settings

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: new_target()

   Add a new particle target

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: particle_edit_toggle()

   Toggle particle edit mode

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: particle_system_remove_all()

   Remove all particle system within the active object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: rekey(*, keys_number=2)

   Change the number of keys of selected particles (root and tip keys included)

   :param keys_number: Number of Keys, (in [2, inf], optional)
   :type keys_number: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: remove_doubles(*, threshold=0.0002)

   Remove selected particles close enough to others

   :param threshold: Merge Distance, Threshold distance within which particles are removed (in [0, inf], optional)
   :type threshold: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: reveal(*, select=True)

   Show hidden particles

   :param select: Select, (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all(*, action='TOGGLE')

   (De)select all particles' keys

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_less()

   Deselect boundary selected keys of each particle

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked()

   Select all keys linked to already selected ones

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_linked_pick(*, deselect=False, location=(0, 0))

   Select nearest particle from mouse pointer

   :param deselect: Deselect, Deselect linked keys rather than selecting them (optional)
   :type deselect: bool
   :param location: Location, (array of 2 items, in [0, inf], optional)
   :type location: Sequence[int]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_more()

   Select keys linked to boundary selected keys of each particle

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT', type='HAIR')

   Select a randomly distributed set of hair or points

   :param ratio: Ratio, Portion of items to select randomly (in [0, 1], optional)
   :type ratio: float
   :param seed: Random Seed, Seed for the random number generator (in [0, inf], optional)
   :type seed: int
   :param action: Action, Selection action to execute (optional)

      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: Literal['SELECT', 'DESELECT']
   :param type: Type, Select either hair or points (optional)
   :type type: Literal['HAIR', 'POINTS']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_roots(*, action='SELECT')

   Select roots of all visible particles

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_tips(*, action='SELECT')

   Select tips of all visible particles

   :param action: Action, Selection action to execute (optional)

      - ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      - ``SELECT``
        Select -- Select all elements.
      - ``DESELECT``
        Deselect -- Deselect all elements.
      - ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: shape_cut()

   Cut hair to conform to the set shape object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: subdivide()

   Subdivide selected particles segments (adds keys)

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: target_move_down()

   Move particle target down in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: target_move_up()

   Move particle target up in the list

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: target_remove()

   Remove the selected particle target

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unify_length()

   Make selected hair the same length

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: weight_set(*, factor=1.0)

   Set the weight of selected keys

   :param factor: Factor, Interpolation factor between current brush weight, and keys' weights (in [0, 1], optional)
   :type factor: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

