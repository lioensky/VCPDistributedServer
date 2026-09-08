Rigidbody Operators
===================

.. module:: bpy.ops.rigidbody

.. function:: bake_to_keyframes(*, frame_start=1, frame_end=250, step=1)

   Bake rigid body transformations of selected objects to keyframes

   :param frame_start: Start Frame, Start frame for baking (in [0, 300000], optional)
   :type frame_start: int
   :param frame_end: End Frame, End frame for baking (in [1, 300000], optional)
   :type frame_end: int
   :param step: Frame Step, Frame Step (in [1, 120], optional)
   :type step: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/rigidbody.py\:108 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L108>`__


.. function:: connect(*, con_type='FIXED', pivot_type='CENTER', connection_pattern='SELECTED_TO_ACTIVE')

   Create rigid body constraints between selected rigid bodies

   :param con_type: Type, Type of generated constraint (optional)

      - ``FIXED``
        Fixed -- Glue rigid bodies together.
      - ``POINT``
        Point -- Constrain rigid bodies to move around common pivot point.
      - ``HINGE``
        Hinge -- Restrict rigid body rotation to one axis.
      - ``SLIDER``
        Slider -- Restrict rigid body translation to one axis.
      - ``PISTON``
        Piston -- Restrict rigid body translation and rotation to one axis.
      - ``GENERIC``
        Generic -- Restrict translation and rotation to specified axes.
      - ``GENERIC_SPRING``
        Generic Spring -- Restrict translation and rotation to specified axes with springs.
      - ``MOTOR``
        Motor -- Drive rigid body around or along an axis.
   :type con_type: Literal['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR']
   :param pivot_type: Location, Constraint pivot location (optional)

      - ``CENTER``
        Center -- Pivot location is between the constrained rigid bodies.
      - ``ACTIVE``
        Active -- Pivot location is at the active object position.
      - ``SELECTED``
        Selected -- Pivot location is at the selected object position.
   :type pivot_type: Literal['CENTER', 'ACTIVE', 'SELECTED']
   :param connection_pattern: Connection Pattern, Pattern used to connect objects (optional)

      - ``SELECTED_TO_ACTIVE``
        Selected to Active -- Connect selected objects to the active object.
      - ``CHAIN_DISTANCE``
        Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
   :type connection_pattern: Literal['SELECTED_TO_ACTIVE', 'CHAIN_DISTANCE']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/rigidbody.py\:277 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L277>`__


.. function:: constraint_add(*, type='FIXED')

   Add Rigid Body Constraint to active object

   :param type: Rigid Body Constraint Type, (optional)
   :type type: Literal[:ref:`rna_enum_rigidbody_constraint_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: constraint_remove()

   Remove Rigid Body Constraint from Object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: mass_calculate(*, material='DEFAULT', density=1.0)

   Automatically calculate mass values for Rigid Body Objects based on volume

   :param material: Material Preset, Type of material that objects are made of (determines material density) (optional)
   :type material: Literal['DEFAULT']
   :param density: Density, Density value (kg/m^3), allows custom value if the 'Custom' preset is used (in [1.17549e-38, inf], optional)
   :type density: float
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: object_add(*, type='ACTIVE')

   Add active object as Rigid Body

   :param type: Rigid Body Type, (optional)
   :type type: Literal[:ref:`rna_enum_rigidbody_object_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: object_remove()

   Remove Rigid Body settings from Object

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: object_settings_copy()

   Copy Rigid Body settings from active object to selected

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/rigidbody.py\:45 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/rigidbody.py#L45>`__

.. function:: objects_add(*, type='ACTIVE')

   Add selected objects as Rigid Bodies

   :param type: Rigid Body Type, (optional)
   :type type: Literal[:ref:`rna_enum_rigidbody_object_type_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: objects_remove()

   Remove selected objects from Rigid Body simulation

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: shape_change(*, type='MESH')

   Change collision shapes for selected Rigid Body Objects

   :param type: Rigid Body Shape, (optional)
   :type type: Literal[:ref:`rna_enum_rigidbody_object_shape_items`]
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: world_add()

   Add Rigid Body simulation world to the current scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: world_remove()

   Remove Rigid Body simulation world from the current scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
