Node(bpy_struct)
================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`NodeCustomGroup`, :class:`NodeInternal`

.. class:: Node(bpy_struct)

   Node in a node tree

   .. attribute:: bl_description

      (default "", never None)

      :type: str

   .. attribute:: bl_height_default

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: bl_height_max

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: bl_height_min

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: bl_icon

      The node icon (default ``'NODE'``)

      :type: Literal[:ref:`rna_enum_icon_items`]

   .. attribute:: bl_idname

      (default "", never None)

      :type: str

   .. attribute:: bl_label

      The node label (default "", never None)

      :type: str

   .. data:: bl_static_type

      Legacy unique node type identifier, redundant with bl_idname property (default "", readonly, never None)

      :type: str

   .. attribute:: bl_width_default

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: bl_width_max

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: bl_width_min

      (in [0, inf], default 0.0)

      :type: float

   .. attribute:: color

      Custom color of the node body (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. data:: color_tag

      Node header color tag (default ``'NONE'``, readonly)

      - ``NONE``
        None -- Default color tag for new nodes and node groups.
      - ``ATTRIBUTE``
        Attribute.
      - ``COLOR``
        Color.
      - ``CONVERTER``
        Converter.
      - ``DISTORT``
        Distort.
      - ``FILTER``
        Filter.
      - ``GEOMETRY``
        Geometry.
      - ``INPUT``
        Input.
      - ``MATTE``
        Matte.
      - ``OUTPUT``
        Output.
      - ``SCRIPT``
        Script.
      - ``SHADER``
        Shader.
      - ``TEXTURE``
        Texture.
      - ``VECTOR``
        Vector.
      - ``PATTERN``
        Pattern.
      - ``INTERFACE``
        Interface.
      - ``GROUP``
        Group.

      :type: Literal['NONE', 'ATTRIBUTE', 'COLOR', 'CONVERTER', 'DISTORT', 'FILTER', 'GEOMETRY', 'INPUT', 'MATTE', 'OUTPUT', 'SCRIPT', 'SHADER', 'TEXTURE', 'VECTOR', 'PATTERN', 'INTERFACE', 'GROUP']

   .. data:: dimensions

      Absolute bounding box dimensions of the node (array of 2 items, in [-inf, inf], default (0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. attribute:: height

      Height of the node (in [-inf, inf], default 0.0)

      :type: float

   .. attribute:: hide

      (default False)

      :type: bool

   .. data:: inputs

      (default None, readonly)

      :type: :class:`NodeInputs`\ [:class:`NodeSocket`]

   .. data:: internal_links

      Internal input-to-output connections for muting (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`NodeLink`]

   .. attribute:: label

      Optional custom node label (default "", never None)

      :type: str

   .. attribute:: location

      Location of the node within its parent frame (array of 2 items, in [-1e+06, 1e+06], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: location_absolute

      Location of the node in the entire canvas (array of 2 items, in [-1e+06, 1e+06], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: mute

      (default False)

      :type: bool

   .. attribute:: name

      Unique node identifier (default "", never None)

      :type: str

   .. data:: outputs

      (default None, readonly)

      :type: :class:`NodeOutputs`\ [:class:`NodeSocket`]

   .. attribute:: parent

      Parent this node is attached to

      :type: :class:`Node` | None

   .. attribute:: select

      Node selection state (default False)

      :type: bool

   .. attribute:: show_options

      (default False)

      :type: bool

   .. attribute:: show_preview

      (default False)

      :type: bool

   .. attribute:: show_texture

      Display node in viewport textured shading mode (default False)

      :type: bool

   .. data:: type

      Legacy unique node type identifier, redundant with bl_idname property (default "", readonly, never None)

      :type: str

   .. attribute:: use_custom_color

      Use custom color for the node (default False)

      :type: bool

   .. attribute:: warning_propagation

      The kinds of messages that should be propagated from this node to the parent group node (default ``'ALL'``)

      - ``ALL``
        All Messages -- Propagate every info, error, and warning message upstream.
      - ``ERRORS_AND_WARNINGS``
        Errors and Warnings -- Propagate only error and warning messages upstream.
      - ``ERRORS``
        Errors -- Propagate only error messages upstream.
      - ``NONE``
        None -- Do not propagate any messages upstream.

      :type: Literal['ALL', 'ERRORS_AND_WARNINGS', 'ERRORS', 'NONE']

   .. attribute:: width

      Width of the node (in [-inf, inf], default 0.0)

      :type: float

   .. method:: bl_system_properties_get(*, do_create=False)

      DEBUG ONLY. Internal access to runtime-defined RNA data storage, intended solely for testing and debugging purposes. Do not access it in regular scripting work, and in particular, do not assume that it contains writable data

      :param do_create: Ensure that system properties are created if they do not exist yet (optional)
      :type do_create: bool
      :return: The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested
      :rtype: :class:`PropertyGroup`

   .. method:: socket_value_update(context)

      Update after property changes

      :param context: (never None)
      :type context: :class:`Context` | None

   .. classmethod:: is_registered_node_type()

      True if a registered node type

      :return: Result
      :rtype: bool

   .. classmethod:: poll(node_tree)

      If non-null output is returned, the node type can be added to the tree

      :param node_tree: Node Tree
      :type node_tree: :class:`NodeTree` | None
      :rtype: bool

   .. method:: poll_instance(node_tree)

      If non-null output is returned, the node can be added to the tree

      :param node_tree: Node Tree
      :type node_tree: :class:`NodeTree` | None
      :rtype: bool

   .. method:: update()

      Update on node graph topology changes (adding or removing nodes and links)


   .. method:: insert_link(link)

      Handle creation of a link to or from the node

      :param link: Link, Node link that will be inserted (never None)
      :type link: :class:`NodeLink` | None

   .. method:: init(context)

      Initialize a new instance of this node

      :param context: (never None)
      :type context: :class:`Context` | None

   .. method:: copy(node)

      Initialize a new instance of this node from an existing node

      :param node: Node, Existing node to copy (never None)
      :type node: :class:`Node` | None

   .. method:: free()

      Clean up node on removal


   .. method:: draw_buttons(context, layout)

      Draw node buttons

      :param context: (never None)
      :type context: :class:`Context` | None
      :param layout: Layout, Layout in the UI (never None)
      :type layout: :class:`UILayout` | None

   .. method:: draw_buttons_ext(context, layout)

      Draw node buttons in the sidebar

      :param context: (never None)
      :type context: :class:`Context` | None
      :param layout: Layout, Layout in the UI (never None)
      :type layout: :class:`UILayout` | None

   .. method:: draw_label()

      Returns a dynamic label string

      :return: Label, (never None)
      :rtype: str

   .. method:: debug_zone_body_lazy_function_graph()

      Get the internal lazy-function graph for the body of this zone

      :return: Dot Graph, Graph in dot format
      :rtype: str

   .. method:: debug_zone_lazy_function_graph()

      Get the internal lazy-function graph for this zone

      :return: Dot Graph, Graph in dot format
      :rtype: str

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

   - :mod:`bpy.context.active_node`
   - :mod:`bpy.context.selected_nodes`
   - :mod:`bpy.context.texture_node`
   - :class:`GeometryNodeForeachGeometryElementInput.paired_output`
   - :class:`GeometryNodeMenuSwitch.enum_definition`
   - :class:`GeometryNodeRepeatInput.paired_output`
   - :class:`GeometryNodeSimulationInput.paired_output`
   - :class:`Node.copy`
   - :class:`Node.parent`
   - :class:`NodeClosureInput.paired_output`
   - :class:`NodeLink.from_node`
   - :class:`NodeLink.to_node`
   - :class:`NodeSocket.draw`
   - :class:`NodeSocket.draw_color`
   - :class:`NodeSocket.node`
   - :class:`NodeSocketStandard.draw`
   - :class:`NodeSocketStandard.draw_color`
   - :class:`NodeTree.nodes`
   - :class:`NodeTreeInterfaceSocket.from_socket`
   - :class:`NodeTreeInterfaceSocket.init_socket`
   - :class:`NodeTreeInterfaceSocketBool.from_socket`
   - :class:`NodeTreeInterfaceSocketBool.init_socket`
   - :class:`NodeTreeInterfaceSocketBundle.from_socket`
   - :class:`NodeTreeInterfaceSocketBundle.init_socket`
   - :class:`NodeTreeInterfaceSocketClosure.from_socket`
   - :class:`NodeTreeInterfaceSocketClosure.init_socket`
   - :class:`NodeTreeInterfaceSocketCollection.from_socket`
   - :class:`NodeTreeInterfaceSocketCollection.init_socket`
   - :class:`NodeTreeInterfaceSocketColor.from_socket`
   - :class:`NodeTreeInterfaceSocketColor.init_socket`
   - :class:`NodeTreeInterfaceSocketFloat.from_socket`
   - :class:`NodeTreeInterfaceSocketFloat.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatAngle.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatAngle.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatColorTemperature.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatColorTemperature.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatDistance.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatDistance.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatFactor.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatFactor.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatFrequency.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatFrequency.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatMass.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatMass.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatPercentage.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatPercentage.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatTime.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatTime.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatUnsigned.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatUnsigned.init_socket`
   - :class:`NodeTreeInterfaceSocketFloatWavelength.from_socket`
   - :class:`NodeTreeInterfaceSocketFloatWavelength.init_socket`
   - :class:`NodeTreeInterfaceSocketGeometry.from_socket`
   - :class:`NodeTreeInterfaceSocketGeometry.init_socket`
   - :class:`NodeTreeInterfaceSocketImage.from_socket`
   - :class:`NodeTreeInterfaceSocketImage.init_socket`
   - :class:`NodeTreeInterfaceSocketInt.from_socket`
   - :class:`NodeTreeInterfaceSocketInt.init_socket`
   - :class:`NodeTreeInterfaceSocketIntFactor.from_socket`
   - :class:`NodeTreeInterfaceSocketIntFactor.init_socket`
   - :class:`NodeTreeInterfaceSocketIntPercentage.from_socket`
   - :class:`NodeTreeInterfaceSocketIntPercentage.init_socket`
   - :class:`NodeTreeInterfaceSocketIntUnsigned.from_socket`
   - :class:`NodeTreeInterfaceSocketIntUnsigned.init_socket`
   - :class:`NodeTreeInterfaceSocketMaterial.from_socket`
   - :class:`NodeTreeInterfaceSocketMaterial.init_socket`
   - :class:`NodeTreeInterfaceSocketMatrix.from_socket`
   - :class:`NodeTreeInterfaceSocketMatrix.init_socket`
   - :class:`NodeTreeInterfaceSocketMenu.from_socket`
   - :class:`NodeTreeInterfaceSocketMenu.init_socket`
   - :class:`NodeTreeInterfaceSocketObject.from_socket`
   - :class:`NodeTreeInterfaceSocketObject.init_socket`
   - :class:`NodeTreeInterfaceSocketRotation.from_socket`
   - :class:`NodeTreeInterfaceSocketRotation.init_socket`
   - :class:`NodeTreeInterfaceSocketShader.from_socket`
   - :class:`NodeTreeInterfaceSocketShader.init_socket`
   - :class:`NodeTreeInterfaceSocketString.from_socket`
   - :class:`NodeTreeInterfaceSocketString.init_socket`
   - :class:`NodeTreeInterfaceSocketStringFilePath.from_socket`
   - :class:`NodeTreeInterfaceSocketStringFilePath.init_socket`
   - :class:`NodeTreeInterfaceSocketTexture.from_socket`
   - :class:`NodeTreeInterfaceSocketTexture.init_socket`
   - :class:`NodeTreeInterfaceSocketVector.from_socket`
   - :class:`NodeTreeInterfaceSocketVector.init_socket`
   - :class:`NodeTreeInterfaceSocketVector2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVector2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVector4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVector4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorAcceleration4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorDirection.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorDirection.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorDirection2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorDirection2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorDirection4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorDirection4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorEuler.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorEuler.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorEuler2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorEuler2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorEuler4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorEuler4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorFactor.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorFactor.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorFactor2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorFactor2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorFactor4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorFactor4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorPercentage.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorPercentage.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorPercentage2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorPercentage2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorPercentage4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorPercentage4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorTranslation.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorTranslation.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorTranslation2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorTranslation2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorTranslation4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorTranslation4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorVelocity.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorVelocity.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorVelocity2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorVelocity2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorVelocity4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorVelocity4D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorXYZ.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorXYZ.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorXYZ2D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorXYZ2D.init_socket`
   - :class:`NodeTreeInterfaceSocketVectorXYZ4D.from_socket`
   - :class:`NodeTreeInterfaceSocketVectorXYZ4D.init_socket`
   - :class:`Nodes.active`
   - :class:`Nodes.new`
   - :class:`Nodes.remove`
   - :class:`NodesModifierBake.node`
   - :class:`RenderEngine.update_script_node`
   - :class:`SpaceNodeEditorPath.append`
   - :class:`UILayout.template_node_inputs`
   - :class:`UILayout.template_node_link`
   - :class:`UILayout.template_node_view`

