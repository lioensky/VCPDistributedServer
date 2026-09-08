NodeTree(ID)
============

.. currentmodule:: bpy.types


Poll Function
+++++++++++++++

The :class:`NodeTree.poll` function determines if a node tree is visible
in the given context (similar to how :class:`Panel.poll`
and :class:`Menu.poll` define visibility). If it returns False,
the node tree type will not be selectable in the node editor.

A typical condition for shader nodes would be to check the active render engine
of the scene and only show nodes of the renderer they are designed for.

.. literalinclude:: ./examples/bpy.types.NodeTree.0.py
   :lines: 13-

base classes --- :class:`bpy_struct`, :class:`ID`

subclasses --- 
:class:`CompositorNodeTree`, :class:`GeometryNodeTree`, :class:`ShaderNodeTree`, :class:`TextureNodeTree`

.. class:: NodeTree(ID)

   Node tree consisting of linked nodes used for shading, textures and compositing

   .. data:: animation_data

      Animation data for this data-block (readonly)

      :type: :class:`AnimData` | None

   .. attribute:: annotation

      Annotation data

      :type: :class:`Annotation` | None

   .. attribute:: bl_description

      (default "", never None)

      :type: str

   .. attribute:: bl_icon

      The node tree icon (default ``'NODETREE'``)

      :type: Literal[:ref:`rna_enum_icon_items`]

   .. attribute:: bl_idname

      (default "", never None)

      :type: str

   .. attribute:: bl_label

      The node tree label (default "", never None)

      :type: str

   .. attribute:: bl_use_group_interface

      Determines the visibility of some UI elements related to node groups (default True)

      :type: bool

   .. attribute:: color_tag

      Color tag of the node group which influences the header color (default ``'NONE'``)

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

   .. attribute:: default_group_node_width

      The width for newly created group nodes (in [60, 700], default 140)

      :type: int

   .. attribute:: description

      Description of the node tree (default "", never None)

      :type: str

   .. data:: interface

      Interface declaration for this node tree (readonly)

      :type: :class:`NodeTreeInterface` | None

   .. data:: links

      (default None, readonly)

      :type: :class:`NodeLinks`\ [:class:`NodeLink`]

   .. data:: nodes

      (default None, readonly)

      :type: :class:`Nodes`\ [:class:`Node`]

   .. data:: type

      Node Tree type (deprecated, bl_idname is the actual node tree type identifier) (default ``'SHADER'``, readonly)

      - ``UNDEFINED``
        Undefined -- Undefined type of nodes (can happen e.g. when a linked node tree goes missing).
      - ``CUSTOM``
        Custom -- Custom nodes.
      - ``SHADER``
        Shader -- Shader nodes.
      - ``TEXTURE``
        Texture -- Texture nodes.
      - ``COMPOSITING``
        Compositing -- Compositing nodes.
      - ``GEOMETRY``
        Geometry -- Geometry nodes.

      :type: Literal['UNDEFINED', 'CUSTOM', 'SHADER', 'TEXTURE', 'COMPOSITING', 'GEOMETRY']

   .. data:: view_center

      The current location (offset) of the view for this Node Tree (array of 2 items, in [-inf, inf], default (0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. method:: interface_update(context)

      Updated node group interface

      :param context: (never None)
      :type context: :class:`Context` | None

   .. method:: contains_tree(sub_tree)

      Check if the node tree contains another. Used to avoid creating recursive node groups.

      :param sub_tree: Node Tree, Node tree for recursive check (never None)
      :type sub_tree: :class:`NodeTree` | None
      :return: contained
      :rtype: bool

   .. classmethod:: poll(context)

      Check visibility in the editor

      :param context: (never None)
      :type context: :class:`Context` | None
      :rtype: bool

   .. method:: update()

      Update on editor changes


   .. classmethod:: get_from_context(context)

      Get a node tree from the context

      :param context: (never None)
      :type context: :class:`Context` | None
      :return:
         ``result_1``, Active node tree from context, :class:`NodeTree`

         ``result_2``, ID data-block that owns the node tree, :class:`ID`

         ``result_3``, Original ID data-block selected from the context, :class:`ID`

      :rtype: tuple[:class:`NodeTree`, :class:`ID`, :class:`ID`]

   .. classmethod:: valid_socket_type(idname)

      Check if the socket type is valid for the node tree

      :param idname: Socket Type, Identifier of the socket type (never None)
      :type idname: str
      :rtype: bool

   .. method:: debug_lazy_function_graph()

      Get the internal lazy-function graph for this node tree

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
   - :class:`ID.name`
   - :class:`ID.name_full`
   - :class:`ID.id_type`
   - :class:`ID.session_uid`
   - :class:`ID.is_evaluated`
   - :class:`ID.original`
   - :class:`ID.users`
   - :class:`ID.use_fake_user`
   - :class:`ID.use_extra_user`
   - :class:`ID.is_embedded_data`
   - :class:`ID.is_linked_packed`
   - :class:`ID.is_missing`
   - :class:`ID.is_runtime_data`
   - :class:`ID.is_editable`
   - :class:`ID.tag`
   - :class:`ID.is_library_indirect`
   - :class:`ID.library`
   - :class:`ID.library_weak_reference`
   - :class:`ID.asset_data`
   - :class:`ID.override_library`
   - :class:`ID.preview`

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
   - :class:`ID.bl_system_properties_get`
   - :class:`ID.rename`
   - :class:`ID.evaluated_get`
   - :class:`ID.copy`
   - :class:`ID.asset_mark`
   - :class:`ID.asset_clear`
   - :class:`ID.asset_generate_preview`
   - :class:`ID.override_create`
   - :class:`ID.override_hierarchy_create`
   - :class:`ID.user_clear`
   - :class:`ID.user_remap`
   - :class:`ID.make_local`
   - :class:`ID.user_of_id`
   - :class:`ID.animation_data_create`
   - :class:`ID.animation_data_clear`
   - :class:`ID.update_tag`
   - :class:`ID.preview_ensure`
   - :class:`ID.bl_rna_get_subclass`
   - :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   - :class:`BlendData.node_groups`
   - :class:`BlendDataNodeTrees.new`
   - :class:`BlendDataNodeTrees.remove`
   - :class:`CompositorNodeCustomGroup.node_tree`
   - :class:`CompositorNodeGroup.node_tree`
   - :class:`EvaluateClosureNodeViewerPathElem.source_node_tree`
   - :class:`FreestyleLineStyle.node_tree`
   - :class:`GeometryNodeCustomGroup.node_tree`
   - :class:`GeometryNodeGroup.node_tree`
   - :class:`Light.node_tree`
   - :class:`Material.node_tree`
   - :class:`Node.poll`
   - :class:`Node.poll_instance`
   - :class:`NodeCustomGroup.node_tree`
   - :class:`NodeGroup.node_tree`
   - :class:`NodeInternal.poll`
   - :class:`NodeInternal.poll_instance`
   - :class:`NodeTree.contains_tree`
   - :class:`NodeTree.get_from_context`
   - :class:`NodeTreePath.node_tree`
   - :class:`NodesModifier.node_group`
   - :class:`Scene.compositing_node_group`
   - :class:`SequencerCompositorModifierData.node_group`
   - :class:`ShaderNodeCustomGroup.node_tree`
   - :class:`ShaderNodeGroup.node_tree`
   - :class:`SpaceNodeEditor.edit_tree`
   - :class:`SpaceNodeEditor.node_tree`
   - :class:`SpaceNodeEditor.selected_node_group`
   - :class:`SpaceNodeEditorPath.append`
   - :class:`SpaceNodeEditorPath.start`
   - :class:`Texture.node_tree`
   - :class:`TextureNodeGroup.node_tree`
   - :class:`UILayout.template_node_link`
   - :class:`UILayout.template_node_view`
   - :class:`World.node_tree`

