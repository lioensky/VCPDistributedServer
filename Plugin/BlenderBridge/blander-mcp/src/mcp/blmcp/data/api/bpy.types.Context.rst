Context(bpy_struct)
===================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Context(bpy_struct)

   Current windowmanager and data context

   .. data:: area

      (readonly)

      :type: :class:`Area` | None

   .. data:: asset

      (readonly)

      :type: :class:`AssetRepresentation` | None

   .. data:: blend_data

      (readonly)

      :type: :class:`BlendData` | None

   .. data:: collection

      (readonly)

      :type: :class:`Collection` | None

   .. data:: engine

      (default "", readonly, never None)

      :type: str

   .. data:: gizmo_group

      (readonly)

      :type: :class:`GizmoGroup` | None

   .. data:: layer_collection

      (readonly)

      :type: :class:`LayerCollection` | None

   .. data:: mode

      (default ``'EDIT_MESH'``, readonly)

      :type: Literal[:ref:`rna_enum_context_mode_items`]

   .. data:: preferences

      (readonly)

      :type: :class:`Preferences` | None

   .. data:: region

      (readonly)

      :type: :class:`Region` | None

   .. data:: region_data

      (readonly)

      :type: :class:`RegionView3D` | None

   .. data:: region_popup

      The temporary region for pop-ups (including menus and pop-overs) (readonly)

      :type: :class:`Region` | None

   .. data:: scene

      (readonly)

      :type: :class:`Scene` | None

   .. data:: screen

      (readonly)

      :type: :class:`Screen` | None

   .. data:: space_data

      The current space, may be None in background-mode, when the cursor is outside the window or when using menu-search (readonly)

      :type: :class:`Space` | None

   .. data:: tool_settings

      (readonly)

      :type: :class:`ToolSettings` | None

   .. data:: view_layer

      (readonly)

      :type: :class:`ViewLayer` | None

   .. data:: window

      (readonly)

      :type: :class:`Window` | None

   .. data:: window_manager

      (readonly)

      :type: :class:`WindowManager` | None

   .. data:: workspace

      (readonly)

      :type: :class:`WorkSpace` | None


   .. rubric:: Buttons Context

   .. data:: texture_slot

      :type: :class:`TextureSlot`

   .. data:: scene
      :noindex:

      :type: :class:`Scene`

   .. data:: world

      :type: :class:`World`

   .. data:: object

      :type: :class:`Object`

   .. data:: mesh

      :type: :class:`Mesh`

   .. data:: armature

      :type: :class:`Armature`

   .. data:: lattice

      :type: :class:`Lattice`

   .. data:: curve

      :type: :class:`Curve`

   .. data:: meta_ball

      :type: :class:`MetaBall`

   .. data:: light

      :type: :class:`Light`

   .. data:: speaker

      :type: :class:`Speaker`

   .. data:: lightprobe

      :type: :class:`LightProbe`

   .. data:: camera

      :type: :class:`Camera`

   .. data:: material

      :type: :class:`Material`

   .. data:: material_slot

      :type: :class:`MaterialSlot`

   .. data:: texture

      :type: :class:`Texture`

   .. data:: texture_user

      :type: :class:`ID`

   .. data:: texture_user_property

      :type: :class:`Property`

   .. data:: texture_node

      :type: :class:`Node`

   .. data:: bone

      :type: :class:`Bone`

   .. data:: edit_bone

      :type: :class:`EditBone`

   .. data:: pose_bone

      :type: :class:`PoseBone`

   .. data:: particle_system

      :type: :class:`ParticleSystem`

   .. data:: particle_system_editable

      :type: :class:`ParticleSystem`

   .. data:: particle_settings

      :type: :class:`ParticleSettings`

   .. data:: cloth

      :type: :class:`ClothModifier`

   .. data:: soft_body

      :type: :class:`SoftBodyModifier`

   .. data:: fluid

      :type: :class:`FluidModifier`

   .. data:: collision

      :type: :class:`CollisionModifier`

   .. data:: brush

      :type: :class:`Brush`

   .. data:: dynamic_paint

      :type: :class:`DynamicPaintModifier`

   .. data:: line_style

      :type: :class:`FreestyleLineStyle`

   .. data:: collection
      :noindex:

      :type: :class:`LayerCollection`

   .. data:: gpencil

      :type: :class:`GreasePencil`

   .. data:: grease_pencil

      :type: :class:`GreasePencil`

   .. data:: curves

      :type: :class:`Curves`

   .. data:: pointcloud

      :type: :class:`PointCloud`

   .. data:: volume

      :type: :class:`Volume`

   .. data:: strip

      :type: :class:`Strip`

   .. data:: strip_modifier

      :type: :class:`StripModifier`


   .. rubric:: Clip Context

   .. data:: edit_movieclip

      :type: :class:`MovieClip`

   .. data:: edit_mask

      :type: :class:`Mask`


   .. rubric:: File Context

   .. data:: active_file

      :type: :class:`FileSelectEntry`

   .. data:: selected_files

      :type: Sequence[:class:`FileSelectEntry`]

   .. data:: asset_library_reference

      :type: :class:`AssetLibraryReference`

   .. data:: asset
      :noindex:

      :type: :class:`AssetRepresentation`

   .. data:: selected_assets

      :type: Sequence[:class:`AssetRepresentation`]

   .. data:: id

      :type: :class:`ID`

   .. data:: selected_ids

      :type: Sequence[:class:`ID`]


   .. rubric:: Image Context

   .. data:: edit_image

      :type: :class:`Image`

   .. data:: edit_mask
      :noindex:

      :type: :class:`Mask`


   .. rubric:: Node Context

   .. data:: selected_nodes

      :type: Sequence[:class:`Node`]

   .. data:: active_node

      :type: :class:`Node`

   .. data:: light
      :noindex:

      :type: :class:`Light`

   .. data:: material
      :noindex:

      :type: :class:`Material`

   .. data:: world
      :noindex:

      :type: :class:`World`


   .. rubric:: Screen Context

   .. data:: scene
      :noindex:

      :type: :class:`Scene`

   .. data:: view_layer
      :noindex:

      :type: :class:`ViewLayer`

   .. data:: visible_objects

      :type: Sequence[:class:`Object`]

   .. data:: selectable_objects

      :type: Sequence[:class:`Object`]

   .. data:: selected_objects

      :type: Sequence[:class:`Object`]

   .. data:: editable_objects

      :type: Sequence[:class:`Object`]

   .. data:: selected_editable_objects

      :type: Sequence[:class:`Object`]

   .. data:: objects_in_mode

      :type: Sequence[:class:`Object`]

   .. data:: objects_in_mode_unique_data

      :type: Sequence[:class:`Object`]

   .. data:: visible_bones

      :type: Sequence[:class:`EditBone`]

   .. data:: editable_bones

      :type: Sequence[:class:`EditBone`]

   .. data:: selected_bones

      :type: Sequence[:class:`EditBone`]

   .. data:: selected_editable_bones

      :type: Sequence[:class:`EditBone`]

   .. data:: visible_pose_bones

      :type: Sequence[:class:`PoseBone`]

   .. data:: selected_pose_bones

      :type: Sequence[:class:`PoseBone`]

   .. data:: selected_pose_bones_from_active_object

      :type: Sequence[:class:`PoseBone`]

   .. data:: active_bone

      :type: :class:`EditBone` | :class:`Bone`

   .. data:: active_pose_bone

      :type: :class:`PoseBone`

   .. data:: active_object

      :type: :class:`Object`

   .. data:: object
      :noindex:

      :type: :class:`Object`

   .. data:: edit_object

      :type: :class:`Object`

   .. data:: sculpt_object

      :type: :class:`Object`

   .. data:: vertex_paint_object

      :type: :class:`Object`

   .. data:: weight_paint_object

      :type: :class:`Object`

   .. data:: image_paint_object

      :type: :class:`Object`

   .. data:: particle_edit_object

      :type: :class:`Object`

   .. data:: pose_object

      :type: :class:`Object`

   .. data:: active_nla_track

      :type: :class:`NlaTrack`

   .. data:: active_nla_strip

      :type: :class:`NlaStrip`

   .. data:: selected_nla_strips

      :type: Sequence[:class:`NlaStrip`]

   .. data:: selected_movieclip_tracks

      :type: Sequence[:class:`MovieTrackingTrack`]

   .. data:: annotation_data

      :type: :class:`GreasePencil`

   .. data:: annotation_data_owner

      :type: :class:`ID`

   .. data:: active_annotation_layer

      :type: :class:`AnnotationLayer`

   .. data:: grease_pencil
      :noindex:

      :type: :class:`GreasePencil`

   .. data:: active_operator

      :type: :class:`Operator`

   .. data:: active_action

      :type: :class:`Action`

   .. data:: selected_visible_actions

      :type: Sequence[:class:`Action`]

   .. data:: selected_editable_actions

      :type: Sequence[:class:`Action`]

   .. data:: visible_fcurves

      :type: Sequence[:class:`FCurve`]

   .. data:: editable_fcurves

      :type: Sequence[:class:`FCurve`]

   .. data:: selected_visible_fcurves

      :type: Sequence[:class:`FCurve`]

   .. data:: selected_editable_fcurves

      :type: Sequence[:class:`FCurve`]

   .. data:: active_editable_fcurve

      :type: :class:`FCurve`

   .. data:: selected_editable_keyframes

      :type: Sequence[:class:`Keyframe`]

   .. data:: ui_list

      :type: :class:`UIList`

   .. data:: property

      :type: :class:`AnyType` | :class:`str` | :class:`int`


      Get the property associated with a hovered button.
      Returns a tuple of the data-block, data path to the property, and array index.

      .. note::

         When the property doesn't have an associated :class:`bpy.types.ID` non-ID data may be returned.
         This may occur when accessing windowing data, for example, operator properties.

      .. literalinclude:: ./examples/bpy.context.property.0.py
         :lines: 10-

   .. data:: asset_library_reference
      :noindex:

      :type: :class:`AssetLibraryReference`

   .. data:: active_strip

      :type: :class:`Strip`

   .. data:: strips

      :type: Sequence[:class:`Strip`]

   .. data:: selected_strips

      :type: Sequence[:class:`Strip`]

   .. data:: selected_editable_strips

      :type: Sequence[:class:`Strip`]

   .. data:: sequencer_scene

      :type: :class:`Scene`


   .. rubric:: Sequencer Context

   .. data:: edit_mask
      :noindex:

      :type: :class:`Mask`

   .. data:: tool_settings
      :noindex:

      :type: :class:`ToolSettings`


   .. rubric:: Text Context

   .. data:: edit_text

      :type: :class:`Text`


   .. rubric:: View3D Context

   .. data:: active_object
      :noindex:

      :type: :class:`Object`

   .. data:: selected_ids
      :noindex:

      :type: Sequence[:class:`ID`]


   .. rubric:: Methods

   .. method:: evaluated_depsgraph_get()

      Get the dependency graph for the current scene and view layer, to access to data-blocks with animation and modifiers applied. If any data-blocks have been edited, the dependency graph will be updated. This invalidates all references to evaluated data-blocks from the dependency graph.

      :return: Evaluated dependency graph
      :rtype: :class:`Depsgraph`

   .. method:: copy()

      Get context members as a dictionary.
      
      :rtype: dict[str, Any]

   .. method:: path_resolve(path, coerce=True)

      Returns the property from the path, raise an exception when not found.
      
      :param path: patch which this property resolves.
      :type path: str
      :param coerce: optional argument, when True, the property will be converted into its Python representation.
      :type coerce: bool
      :return: Property value or property object.
      :rtype: Any | :class:`bpy.types.bpy_prop`

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


   .. method:: temp_override(*, window=None, screen=None, area=None, region=None, **keywords)
   
      Context manager to temporarily override members in the context.
   
      :param window: Window override or None.
      :type window: :class:`bpy.types.Window` | None
      :param screen: Screen override or None.
   
         .. note:: Switching to or away from full-screen areas & temporary screens isn't supported. Passing in these screens will raise an exception, actions that leave the context such screens won't restore the prior screen.
   
         .. note:: Changing the screen has wider implications than other arguments as it will also change the works-space and potentially the scene (when pinned).
   
      :type screen: :class:`bpy.types.Screen` | None
      :param area: Area override or None.
      :type area: :class:`bpy.types.Area` | None
      :param region: Region override or None.
      :type region: :class:`bpy.types.Region` | None
      :param keywords: Additional keywords override context members.
      :return: The context manager.
      :rtype: ContextTempOverride


      Overriding the context can be used to temporarily activate another ``window`` / ``area`` & ``region``,
      as well as other members such as the ``active_object`` or ``bone``.

      Notes:

      - When overriding window, area and regions: the arguments must be consistent,
        so any region argument that's passed in must be contained by the current area or the area passed in.
        The same goes for the area needing to be contained in the current window.

      - Temporary context overrides may be nested, when this is done, members will be added to the existing overrides.

      - Context members are restored outside the scope of the context-manager.
        The only exception to this is when the data is no longer available.

        In the event windowing data was removed (for example), the state of the context is left as-is.
        While this isn't likely to happen, explicit window operation such as closing windows or loading a new file
        remove the windowing data that was set before the temporary context was created.


      Overriding the context can be useful to set the context after loading files
      (which would otherwise be None). For example:

      .. literalinclude:: ./examples/bpy.types.Context.temp_override.2.py
         :lines: 6-


      This example shows how it's possible to add an object to the scene in another window.

      .. literalinclude:: ./examples/bpy.types.Context.temp_override.3.py
         :lines: 4-


      **Logging Context Member Access**

      Context members can be logged by calling ``logging_set(True)`` on the "with" target of a temporary override.
      This will log the members that are being accessed during the operation and may
      assist in debugging when it is unclear which members need to be overridden.

      In the event an operator fails to execute because of a missing context member, logging may help
      identify which member is required.

      This example shows how to log which context members are being accessed.
      Log statements are printed to your system's console.

      .. important::

         Not all operators rely on Context Members and therefore will not be affected by
         :class:`bpy.types.Context.temp_override`, use logging to what members if any are accessed.

      .. literalinclude:: ./examples/bpy.types.Context.temp_override.4.py
         :lines: 20-


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`AssetShelf.draw_context_menu`
   - :class:`AssetShelf.poll`
   - :class:`FileHandler.poll_drop`
   - :class:`Gizmo.draw`
   - :class:`Gizmo.draw_select`
   - :class:`Gizmo.exit`
   - :class:`Gizmo.invoke`
   - :class:`Gizmo.modal`
   - :class:`Gizmo.test_select`
   - :class:`GizmoGroup.draw_prepare`
   - :class:`GizmoGroup.invoke_prepare`
   - :class:`GizmoGroup.poll`
   - :class:`GizmoGroup.refresh`
   - :class:`GizmoGroup.setup`
   - :class:`Header.draw`
   - :class:`KeyingSetInfo.generate`
   - :class:`KeyingSetInfo.iterator`
   - :class:`KeyingSetInfo.poll`
   - :class:`Macro.draw`
   - :class:`Macro.poll`
   - :class:`Menu.draw`
   - :class:`Menu.poll`
   - :class:`Node.draw_buttons`
   - :class:`Node.draw_buttons_ext`
   - :class:`Node.init`
   - :class:`Node.socket_value_update`
   - :class:`NodeInternal.draw_buttons`
   - :class:`NodeInternal.draw_buttons_ext`
   - :class:`NodeSocket.draw`
   - :class:`NodeSocket.draw_color`
   - :class:`NodeSocketStandard.draw`
   - :class:`NodeSocketStandard.draw_color`
   - :class:`NodeTree.get_from_context`
   - :class:`NodeTree.interface_update`
   - :class:`NodeTree.poll`
   - :class:`NodeTreeInterfaceSocket.draw`
   - :class:`NodeTreeInterfaceSocketBool.draw`
   - :class:`NodeTreeInterfaceSocketBundle.draw`
   - :class:`NodeTreeInterfaceSocketClosure.draw`
   - :class:`NodeTreeInterfaceSocketCollection.draw`
   - :class:`NodeTreeInterfaceSocketColor.draw`
   - :class:`NodeTreeInterfaceSocketFloat.draw`
   - :class:`NodeTreeInterfaceSocketFloatAngle.draw`
   - :class:`NodeTreeInterfaceSocketFloatColorTemperature.draw`
   - :class:`NodeTreeInterfaceSocketFloatDistance.draw`
   - :class:`NodeTreeInterfaceSocketFloatFactor.draw`
   - :class:`NodeTreeInterfaceSocketFloatFrequency.draw`
   - :class:`NodeTreeInterfaceSocketFloatMass.draw`
   - :class:`NodeTreeInterfaceSocketFloatPercentage.draw`
   - :class:`NodeTreeInterfaceSocketFloatTime.draw`
   - :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.draw`
   - :class:`NodeTreeInterfaceSocketFloatUnsigned.draw`
   - :class:`NodeTreeInterfaceSocketFloatWavelength.draw`
   - :class:`NodeTreeInterfaceSocketGeometry.draw`
   - :class:`NodeTreeInterfaceSocketImage.draw`
   - :class:`NodeTreeInterfaceSocketInt.draw`
   - :class:`NodeTreeInterfaceSocketIntFactor.draw`
   - :class:`NodeTreeInterfaceSocketIntPercentage.draw`
   - :class:`NodeTreeInterfaceSocketIntUnsigned.draw`
   - :class:`NodeTreeInterfaceSocketMaterial.draw`
   - :class:`NodeTreeInterfaceSocketMatrix.draw`
   - :class:`NodeTreeInterfaceSocketMenu.draw`
   - :class:`NodeTreeInterfaceSocketObject.draw`
   - :class:`NodeTreeInterfaceSocketRotation.draw`
   - :class:`NodeTreeInterfaceSocketShader.draw`
   - :class:`NodeTreeInterfaceSocketString.draw`
   - :class:`NodeTreeInterfaceSocketStringFilePath.draw`
   - :class:`NodeTreeInterfaceSocketTexture.draw`
   - :class:`NodeTreeInterfaceSocketVector.draw`
   - :class:`NodeTreeInterfaceSocketVector2D.draw`
   - :class:`NodeTreeInterfaceSocketVector4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration.draw`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorDirection.draw`
   - :class:`NodeTreeInterfaceSocketVectorDirection2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorDirection4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorEuler.draw`
   - :class:`NodeTreeInterfaceSocketVectorEuler2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorEuler4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorFactor.draw`
   - :class:`NodeTreeInterfaceSocketVectorFactor2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorFactor4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorPercentage.draw`
   - :class:`NodeTreeInterfaceSocketVectorPercentage2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorPercentage4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorTranslation.draw`
   - :class:`NodeTreeInterfaceSocketVectorTranslation2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorTranslation4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorVelocity.draw`
   - :class:`NodeTreeInterfaceSocketVectorVelocity2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorVelocity4D.draw`
   - :class:`NodeTreeInterfaceSocketVectorXYZ.draw`
   - :class:`NodeTreeInterfaceSocketVectorXYZ2D.draw`
   - :class:`NodeTreeInterfaceSocketVectorXYZ4D.draw`
   - :class:`Operator.cancel`
   - :class:`Operator.check`
   - :class:`Operator.description`
   - :class:`Operator.draw`
   - :class:`Operator.execute`
   - :class:`Operator.invoke`
   - :class:`Operator.modal`
   - :class:`Operator.poll`
   - :class:`Panel.draw`
   - :class:`Panel.draw_header`
   - :class:`Panel.draw_header_preset`
   - :class:`Panel.poll`
   - :class:`RenderEngine.draw`
   - :class:`RenderEngine.view_draw`
   - :class:`RenderEngine.view_update`
   - :class:`UIList.draw_filter`
   - :class:`UIList.draw_item`
   - :class:`UIList.filter_items`
   - :class:`XrSessionState.action_binding_create`
   - :class:`XrSessionState.action_create`
   - :class:`XrSessionState.action_set_create`
   - :class:`XrSessionState.action_state_get`
   - :class:`XrSessionState.active_action_set_set`
   - :class:`XrSessionState.controller_aim_location_get`
   - :class:`XrSessionState.controller_aim_rotation_get`
   - :class:`XrSessionState.controller_grip_location_get`
   - :class:`XrSessionState.controller_grip_rotation_get`
   - :class:`XrSessionState.controller_pose_actions_set`
   - :class:`XrSessionState.haptic_action_apply`
   - :class:`XrSessionState.haptic_action_stop`
   - :class:`XrSessionState.is_running`
   - :class:`XrSessionState.reset_to_base_pose`

