Window(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Window(bpy_struct)

   Open window

   .. data:: height

      Window height (in [0, 32767], default 0, readonly)

      :type: int

   .. data:: modal_operators

      A list of currently running modal operators (default None, readonly)

      :type: :class:`bpy_prop_collection`\ [:class:`Operator`]

   .. data:: parent

      Active workspace and scene follow this window (readonly)

      :type: :class:`Window` | None

   .. attribute:: scene

      Active scene to be edited in the window (never None)

      :type: :class:`Scene`

   .. attribute:: screen

      Active workspace screen showing in the window (never None)

      :type: :class:`Screen`

   .. data:: stereo_3d_display

      Settings for stereo 3D display (readonly, never None)

      :type: :class:`Stereo3dDisplay`

   .. data:: support_hdr_color

      The window has a HDR graphics buffer that wide gamut and high dynamic range colors can be written to, in extended sRGB color space. (default False, readonly)

      :type: bool

   .. attribute:: view_layer

      The active workspace view layer showing in the window (never None)

      :type: :class:`ViewLayer`

   .. data:: width

      Window width (in [0, 32767], default 0, readonly)

      :type: int

   .. attribute:: workspace

      Active workspace showing in the window (never None)

      :type: :class:`WorkSpace`

   .. data:: x

      Horizontal location of the window (in [-32768, 32767], default 0, readonly)

      :type: int

   .. data:: y

      Vertical location of the window (in [-32768, 32767], default 0, readonly)

      :type: int

   .. method:: cursor_warp(x, y)

      Set the cursor position

      :param x: (in [-inf, inf])
      :type x: int
      :param y: (in [-inf, inf])
      :type y: int

   .. method:: cursor_set(cursor)

      Set the cursor

      :param cursor: cursor
      :type cursor: Literal[:ref:`rna_enum_window_cursor_items`]

   .. method:: cursor_modal_set(cursor)

      Set the cursor, so the previous cursor can be restored

      :param cursor: cursor
      :type cursor: Literal[:ref:`rna_enum_window_cursor_items`]

   .. method:: cursor_modal_restore()

      Restore the previous cursor after calling ``cursor_modal_set``


   .. method:: event_simulate(type, value, *, unicode="", x=0, y=0, shift=False, ctrl=False, alt=False, oskey=False, hyper=False)

      event_simulate

      :param type: Type
      :type type: Literal[:ref:`rna_enum_event_type_items`]
      :param value: Value
      :type value: Literal[:ref:`rna_enum_event_value_items`]
      :param unicode: (optional)
      :type unicode: str
      :param x: (in [-inf, inf], optional)
      :type x: int
      :param y: (in [-inf, inf], optional)
      :type y: int
      :param shift: Shift, (optional)
      :type shift: bool
      :param ctrl: Ctrl, (optional)
      :type ctrl: bool
      :param alt: Alt, (optional)
      :type alt: bool
      :param oskey: OS Key, (optional)
      :type oskey: bool
      :param hyper: Hyper, (optional)
      :type hyper: bool
      :return: Item, Added key map item
      :rtype: :class:`Event`

   .. method:: find_playing_scene(*, scrub=False)

      find_playing_scene

      :param scrub: Scrubbing, Check if time in the scene is being scrubbed (optional)
      :type scrub: bool
      :return: Scene, Scene that is currently playing
      :rtype: :class:`Scene`

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

   - :class:`Context.window`
   - :class:`Window.parent`
   - :class:`WindowManager.event_timer_add`
   - :class:`WindowManager.windows`
   - :class:`Windows.find_playing`

