SpaceImageEditor(Space)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceImageEditor(Space)

   Image and UV editor space data

   .. attribute:: annotation

      Annotation data for this space

      :type: :class:`Annotation` | None

   .. attribute:: blend_factor

      Overlay blending factor of rasterized mask (in [0, 1], default 0.7)

      :type: float

   .. attribute:: cursor_location

      2D cursor location for this view (array of 2 items, in [-inf, inf], default (0.0, 0.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: display_channels

      Channels of the image to display (default ``'COLOR'``)

      - ``COLOR_ALPHA``
        Color & Alpha -- Display image with RGB colors and alpha transparency.
      - ``COLOR``
        Color -- Display image with RGB colors.
      - ``ALPHA``
        Alpha -- Display alpha transparency channel.
      - ``Z_BUFFER``
        Z-Buffer -- Display Z-buffer associated with image (mapped from camera clip start to end).
      - ``RED``
        Red.
      - ``GREEN``
        Green.
      - ``BLUE``
        Blue.

      :type: Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'Z_BUFFER', 'RED', 'GREEN', 'BLUE']

   .. attribute:: image

      Image displayed and edited in this space

      :type: :class:`Image` | None

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed (readonly, never None)

      :type: :class:`ImageUser`

   .. attribute:: mask

      Mask displayed and edited in this space

      :type: :class:`Mask` | None

   .. attribute:: mask_display_type

      Display type for mask splines (default ``'OUTLINE'``)

      - ``OUTLINE``
        Outline -- Display white edges with black outline.
      - ``DASH``
        Dash -- Display dashed black-white edges.
      - ``BLACK``
        Black -- Display black edges.
      - ``WHITE``
        White -- Display white edges.

      :type: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']

   .. attribute:: mask_overlay_mode

      Overlay mode of rasterized mask (default ``'ALPHACHANNEL'``)

      - ``ALPHACHANNEL``
        Alpha Channel -- Show alpha channel of the mask.
      - ``COMBINED``
        Combined -- Combine space background image with the mask.

      :type: Literal['ALPHACHANNEL', 'COMBINED']

   .. attribute:: mode

      Editing context being displayed (default ``'VIEW'``)

      :type: Literal[:ref:`rna_enum_space_image_mode_all_items`]

   .. data:: overlay

      Settings for display of overlays in the UV/Image editor (readonly, never None)

      :type: :class:`SpaceImageOverlay`

   .. attribute:: pivot_point

      Rotation/Scaling Pivot (default ``'BOUNDING_BOX_CENTER'``)

      - ``BOUNDING_BOX_CENTER``
        Bounding Box Center -- Pivot around bounding box center of selected object(s).
      - ``CURSOR``
        3D Cursor -- Pivot around the 3D cursor.
      - ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each object's own origin.
      - ``MEDIAN_POINT``
        Median Point -- Pivot around the median point of selected objects.
      - ``ACTIVE_ELEMENT``
        Active Element -- Pivot around active object.

      :type: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT']

   .. data:: sample_histogram

      Sampled colors along line (readonly)

      :type: :class:`Histogram` | None

   .. data:: scopes

      Scopes to visualize image statistics (readonly)

      :type: :class:`Scopes` | None

   .. attribute:: show_annotation

      Show annotations for this view (default False)

      :type: bool

   .. attribute:: show_gizmo

      Show gizmos of all types (default True)

      :type: bool

   .. attribute:: show_gizmo_navigate

      Viewport navigation gizmo (default True)

      :type: bool

   .. attribute:: show_mask_overlay

      (default False)

      :type: bool

   .. attribute:: show_mask_spline

      (default True)

      :type: bool

   .. data:: show_maskedit

      Show Mask editing related properties (default False, readonly)

      :type: bool

   .. data:: show_paint

      Show paint related properties (default False, readonly)

      :type: bool

   .. attribute:: show_region_asset_shelf

      Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode) (default False)

      :type: bool

   .. attribute:: show_region_hud

      (default False)

      :type: bool

   .. attribute:: show_region_tool_header

      (default False)

      :type: bool

   .. attribute:: show_region_toolbar

      (default False)

      :type: bool

   .. attribute:: show_region_ui

      (default False)

      :type: bool

   .. data:: show_render

      Show render related properties (default False, readonly)

      :type: bool

   .. attribute:: show_repeat

      Display the image repeated outside of the main view (default False)

      :type: bool

   .. attribute:: show_sequencer_scene

      Display the render result for the sequencer scene instead of the active scene (default False)

      :type: bool

   .. attribute:: show_stereo_3d

      Display the image in Stereo 3D (default False)

      :type: bool

   .. data:: show_uvedit

      Show UV editing related properties (default False, readonly)

      :type: bool

   .. attribute:: ui_mode

      Editing context being displayed (default ``'VIEW'``)

      - ``VIEW``
        View -- Inspect images or render results.
      - ``PAINT``
        Paint -- Paint images in 2D.
      - ``MASK``
        Mask -- View and edit masks.

      :type: Literal['VIEW', 'PAINT', 'MASK']

   .. attribute:: use_image_pin

      Display current image regardless of object selection (default False)

      :type: bool

   .. attribute:: use_realtime_update

      Update other affected window spaces automatically to reflect changes during interactive operations such as transform (default False)

      :type: bool

   .. data:: uv_editor

      UV editor settings (readonly, never None)

      :type: :class:`SpaceUVEditor`

   .. data:: zoom

      Zoom factor (array of 2 items, in [-inf, inf], default (0.0, 0.0), readonly)

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: zoom_percentage

      Zoom percentage (in [0.4, 80000], default 100.0)

      :type: float

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

