ThemeUserInterface(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeUserInterface(bpy_struct)

   Theme settings for user interface elements

   .. attribute:: axis_w

      W-axis for quaternion and axis-angle rotations (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: axis_x

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: axis_y

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: axis_z

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: editor_border

      Color of the border between editors (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: editor_outline

      Color of the outline of each editor, except the active one (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: editor_outline_active

      Color of the outline of the active editor (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: gizmo_a

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: gizmo_b

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: gizmo_hi

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: gizmo_primary

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: gizmo_secondary

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: gizmo_view_align

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: icon_alpha

      Transparency of icons in the interface, to reduce contrast (in [0, 1], default 0.0)

      :type: float

   .. attribute:: icon_autokey

      Color of Auto Keying indicator when enabled (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_border_intensity

      Control the intensity of the border around themes icons (in [0, 1], default 0.0)

      :type: float

   .. attribute:: icon_collection

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_folder

      Color of folders in the file browser (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_modifier

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_object

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_object_data

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_saturation

      Saturation of icons in the interface (in [0, 1], default 0.0)

      :type: float

   .. attribute:: icon_scene

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: icon_shading

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: menu_shadow_fac

      Blending factor for panel and menu shadows (in [0.01, 1], default 0.0)

      :type: float

   .. attribute:: menu_shadow_width

      Width of panel and menu shadows, set to zero to disable (in [0, 24], default 0)

      :type: int

   .. attribute:: panel_active

      Color of the outline of top-level panels that are active (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: panel_back

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: panel_header

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: panel_outline

      Color of the outline of top-level panels (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: panel_roundness

      Roundness of the corners of panels and sub-panels (in [0, 1], default 0.4)

      :type: float

   .. attribute:: panel_sub_back

      (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: panel_text

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: panel_title

      (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: transparent_checker_primary

      Primary color of checkerboard pattern indicating transparent areas (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: transparent_checker_secondary

      Secondary color of checkerboard pattern indicating transparent areas (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

   .. attribute:: transparent_checker_size

      Size of checkerboard pattern indicating transparent areas (in [2, 48], default 0)

      :type: int

   .. data:: wcol_box

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_curve

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_list_item

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_menu

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_menu_back

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_menu_item

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_num

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_numslider

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_option

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_pie_menu

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_progress

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_pulldown

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_radio

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_regular

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_scroll

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_state

      (readonly, never None)

      :type: :class:`ThemeWidgetStateColors`

   .. data:: wcol_tab

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_text

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_toggle

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_tool

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_toolbar_item

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. data:: wcol_tooltip

      (readonly, never None)

      :type: :class:`ThemeWidgetColors`

   .. attribute:: widget_emboss

      Color of the 1px shadow line underlying widgets (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

      :type: :class:`bpy_prop_array`\ [float]

   .. attribute:: widget_text_cursor

      Color of the text insertion cursor (caret) (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

      :type: :class:`mathutils.Color`

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

   - :class:`Theme.user_interface`

