Scene Operators
===============

.. module:: bpy.ops.scene

.. function:: delete()

   Delete active scene

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: drop_scene_asset(*, session_uid=0)

   Import scene and set it as the active one in the window

   :param session_uid: Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
   :type session_uid: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: gltf2_action_filter_refresh()

   Refresh list of actions

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py\:615 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py#L615>`__

.. function:: gpencil_brush_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove Grease Pencil brush preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: gpencil_material_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove Grease Pencil material preset

   :param name: Name, Name of the preset, used to make the path name (optional, never None)
   :type name: str
   :param remove_name: remove_name, (optional)
   :type remove_name: bool
   :param remove_active: remove_active, (optional)
   :type remove_active: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119>`__


.. function:: new(*, type='NEW')

   Add new scene by type

   :param type: Type, (optional)

      - ``NEW``
        New -- Add a new, empty scene with default settings.
      - ``EMPTY``
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.
      - ``LINK_COPY``
        Linked Copy -- Link in the collections from the current scene (shallow copy).
      - ``FULL_COPY``
        Full Copy -- Make a full copy of the current scene.
   :type type: Literal['NEW', 'EMPTY', 'LINK_COPY', 'FULL_COPY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new_sequencer(*, type='NEW')

   Add new scene by type in the sequence editor and assign to active strip

   :param type: Type, (optional)

      - ``NEW``
        New -- Add a new, empty scene with default settings.
      - ``EMPTY``
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.
      - ``LINK_COPY``
        Linked Copy -- Link in the collections from the current scene (shallow copy).
      - ``FULL_COPY``
        Full Copy -- Make a full copy of the current scene.
   :type type: Literal['NEW', 'EMPTY', 'LINK_COPY', 'FULL_COPY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: new_sequencer_scene(*, type='NEW')

   Add new scene to be used by the sequencer

   :param type: Type, (optional)

      - ``NEW``
        New -- Add a new, empty scene with default settings.
      - ``EMPTY``
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.
      - ``LINK_COPY``
        Linked Copy -- Link in the collections from the current scene (shallow copy).
      - ``FULL_COPY``
        Full Copy -- Make a full copy of the current scene.
   :type type: Literal['NEW', 'EMPTY', 'LINK_COPY', 'FULL_COPY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: render_view_add()

   Add a render view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: render_view_remove()

   Remove the selected render view

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_layer_add(*, type='NEW')

   Add a view layer

   :param type: Type, (optional)

      - ``NEW``
        New -- Add a new view layer.
      - ``COPY``
        Copy Settings -- Copy settings of current view layer.
      - ``EMPTY``
        Blank -- Add a new view layer with all collections disabled.
   :type type: Literal['NEW', 'COPY', 'EMPTY']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_layer_add_aov()

   Add a Shader AOV

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_layer_add_lightgroup(*, name="")

   Add a Light Group

   :param name: Name, Name of newly created lightgroup (optional, never None)
   :type name: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: view_layer_add_used_lightgroups()

   Add all used Light Groups

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_layer_remove()

   Remove the selected view layer

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_layer_remove_aov()

   Remove Active AOV

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_layer_remove_lightgroup()

   Remove Active Lightgroup

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: view_layer_remove_unused_lightgroups()

   Remove all unused Light Groups

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
