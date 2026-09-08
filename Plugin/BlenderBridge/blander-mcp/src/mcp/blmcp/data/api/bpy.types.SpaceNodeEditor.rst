SpaceNodeEditor(Space)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceNodeEditor(Space)

   Node editor space data

   .. attribute:: backdrop_channels

      Channels of the image to draw (default ``'COLOR'``)

      - ``COLOR_ALPHA``
        Color & Alpha -- Display image with RGB colors and alpha transparency.
      - ``COLOR``
        Color -- Display image with RGB colors.
      - ``ALPHA``
        Alpha -- Display alpha transparency channel.
      - ``RED``
        Red.
      - ``GREEN``
        Green.
      - ``BLUE``
        Blue.

      :type: Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'RED', 'GREEN', 'BLUE']

   .. attribute:: backdrop_offset

      Backdrop offset (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: backdrop_zoom

      Backdrop zoom factor (in [0.01, inf], default 1.0)

      :type: float

   .. attribute:: cursor_location

      Location for adding new nodes (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. data:: edit_tree

      Node tree being displayed and edited (readonly)

      :type: :class:`NodeTree` | None

   .. data:: id

      Data-block whose nodes are being edited (readonly)

      :type: :class:`ID` | None

   .. data:: id_from

      Data-block from which the edited data-block is linked (readonly)

      :type: :class:`ID` | None

   .. attribute:: insert_offset_direction

      Direction to offset nodes on insertion (default ``'RIGHT'``)

      :type: Literal['RIGHT', 'LEFT']

   .. attribute:: node_tree

      Base node tree from context

      :type: :class:`NodeTree` | None

   .. attribute:: node_tree_sub_type

      :type: str

   .. data:: overlay

      Settings for display of overlays in the Node Editor (readonly, never None)

      :type: :class:`SpaceNodeOverlay`

   .. data:: path

      Path from the data-block to the currently edited node tree (default None, readonly)

      :type: :class:`SpaceNodeEditorPath`\ [:class:`NodeTreePath`]

   .. attribute:: pin

      Use the pinned node tree (default False)

      :type: bool

   .. attribute:: selected_node_group

      Node group to edit

      :type: :class:`NodeTree` | None

   .. attribute:: shader_type

      Type of data to take shader from (default ``'OBJECT'``)

      - ``OBJECT``
        Object -- Edit shader nodes from Object.
      - ``WORLD``
        World -- Edit shader nodes from World.

      :type: Literal['OBJECT', 'WORLD']

   .. attribute:: show_annotation

      Show annotations for this view (default False)

      :type: bool

   .. attribute:: show_backdrop

      Use active Viewer Node output as backdrop for compositing nodes (default False)

      :type: bool

   .. attribute:: show_gizmo

      Show gizmos of all types (default True)

      :type: bool

   .. attribute:: show_gizmo_active_node

      Context sensitive gizmo for the active node (default True)

      :type: bool

   .. attribute:: show_region_asset_shelf

      Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode) (default False)

      :type: bool

   .. attribute:: show_region_toolbar

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. data:: supports_previews

      Whether the node editor's type supports displaying node previews (default False, readonly)

      :type: bool

   .. attribute:: texture_type

      Type of data to take texture from (default ``'WORLD'``)

      - ``WORLD``
        World -- Edit texture nodes from World.
      - ``BRUSH``
        Brush -- Edit texture nodes from Brush.

      :type: Literal['WORLD', 'BRUSH']

   .. attribute:: tree_type

      Node tree type to display and edit (default ``'DEFAULT'``)

      - ``GeometryNodeTree``
        Geometry Node Editor -- Advanced geometry editing and tools creation using nodes.
      - ``CompositorNodeTree``
        Compositor -- Create effects and post-process renders, images, and the 3D Viewport.
      - ``ShaderNodeTree``
        Shader Editor -- Edit materials, lights, and world shading using nodes.
      - ``TextureNodeTree``
        Texture Node Editor -- Edit textures using nodes.

      :type: Literal['GeometryNodeTree', 'CompositorNodeTree', 'ShaderNodeTree', 'TextureNodeTree']

   .. method:: cursor_location_from_region(x, y)

      Set the cursor location using region coordinates

      :param x: x, Region x coordinate (in [-inf, inf])
      :type x: int
      :param y: y, Region y coordinate (in [-inf, inf])
      :type y: int

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :param callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :param args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :param region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :param draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :param handler: The draw handler that should be removed.
      :type handler: object
      :param region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`
   - :class:`Space.type`
   - :class:`Space.show_locked_time`
   - :class:`Space.show_region_header`

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
   - :class:`Space.bl_rna_get_subclass`
   - :class:`Space.bl_rna_get_subclass_py`
   - :class:`Space.draw_handler_add`
   - :class:`Space.draw_handler_remove`

