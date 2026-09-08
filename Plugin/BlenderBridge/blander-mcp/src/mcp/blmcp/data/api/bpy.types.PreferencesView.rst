PreferencesView(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesView(bpy_struct)

   Preferences related to viewing data

   .. attribute:: border_width

      Size of the padding around each editor. (in [1, 10], default 2)

      :type: int

   .. attribute:: color_picker_type

      Different styles of displaying the color picker widget (default ``'CIRCLE_HSV'``)

      - ``CIRCLE_HSV``
        Circle (HSV) -- A circular Hue/Saturation color wheel, with Value slider.
      - ``CIRCLE_HSL``
        Circle (HSL) -- A circular Hue/Saturation color wheel, with Lightness slider.
      - ``SQUARE_SV``
        Square (SV + H) -- A square showing Saturation/Value, with Hue slider.
      - ``SQUARE_HS``
        Square (HS + V) -- A square showing Hue/Saturation, with Value slider.
      - ``SQUARE_HV``
        Square (HV + S) -- A square showing Hue/Value, with Saturation slider.

      :type: Literal['CIRCLE_HSV', 'CIRCLE_HSL', 'SQUARE_SV', 'SQUARE_HS', 'SQUARE_HV']

   .. attribute:: factor_display_type

      How factor values are displayed (default ``'FACTOR'``)

      - ``FACTOR``
        Factor -- Display factors as values between 0 and 1.
      - ``PERCENTAGE``
        Percentage -- Display factors as percentages.

      :type: Literal['FACTOR', 'PERCENTAGE']

   .. attribute:: filebrowser_display_type

      Default location where the File Editor will be displayed in (default ``'WINDOW'``)

      - ``SCREEN``
        Maximized Area -- Open the temporary editor in a maximized screen.
      - ``WINDOW``
        New Window -- Open the temporary editor in a new window.

      :type: Literal['SCREEN', 'WINDOW']

   .. attribute:: font_path_ui

      Path to interface font (default "", never None)

      :type: str

   .. attribute:: font_path_ui_mono

      Path to interface monospaced Font (default "", never None)

      :type: str

   .. attribute:: gizmo_size

      Diameter of the gizmo (in [10, 200], default 75)

      :type: int

   .. attribute:: gizmo_size_navigate_v3d

      The Navigate Gizmo size (in [30, 200], default 80)

      :type: int

   .. attribute:: header_align

      Default header position for new space-types (default ``'BOTTOM'``)

      - ``NONE``
        Keep Existing -- Keep existing header alignment.
      - ``TOP``
        Top -- Top aligned on load.
      - ``BOTTOM``
        Bottom -- Bottom align on load (except for property editors).

      :type: Literal['NONE', 'TOP', 'BOTTOM']

   .. attribute:: language

      Language used for translation (default ``'DEFAULT'``)

      - ``DEFAULT``
        Automatic (Automatic) -- Automatically choose the system-defined language if available, or fall-back to English (US).

      :type: Literal['DEFAULT']

   .. attribute:: lookdev_sphere_size

      Diameter of the HDRI reference spheres (in [50, 400], default 150)

      :type: int

   .. attribute:: menu_close_leave

      Close menus when the mouse is moved out of the region. (default False)

      :type: bool

   .. attribute:: mini_axis_brightness

      Brightness of the icon (in [0, 10], default 8)

      :type: int

   .. attribute:: mini_axis_size

      The axes icon's size (in [10, 64], default 25)

      :type: int

   .. attribute:: mini_axis_type

      Show small rotating 3D axes in the top right corner of the 3D viewport (default ``'GIZMO'``)

      :type: Literal['NONE', 'MINIMAL', 'GIZMO']

   .. attribute:: open_sublevel_delay

      Time delay in 1/10 seconds before automatically opening sub level menus (in [1, 40], default 2)

      :type: int

   .. attribute:: open_toplevel_delay

      Time delay in 1/10 seconds before automatically opening top level menus (in [1, 40], default 5)

      :type: int

   .. attribute:: pie_animation_timeout

      Time needed to fully animate the pie to unfolded state (in 1/100ths of sec) (in [0, 1000], default 6)

      :type: int

   .. attribute:: pie_initial_timeout

      Pie menus will use the initial mouse position as center for this amount of time (in 1/100ths of sec) (in [0, 1000], default 0)

      :type: int

   .. attribute:: pie_menu_confirm

      Distance threshold after which selection is made (zero to disable) (in [0, 1000], default 0)

      :type: int

   .. attribute:: pie_menu_radius

      Pie menu size in pixels (in [0, 1000], default 100)

      :type: int

   .. attribute:: pie_menu_threshold

      Distance from center needed before a selection can be made (in [0, 1000], default 12)

      :type: int

   .. attribute:: pie_tap_timeout

      Pie menu button held longer than this will dismiss menu on release (in 1/100ths of sec) (in [0, 1000], default 20)

      :type: int

   .. attribute:: playback_fps_samples

      The number of frames to use for calculating FPS average. Zero to calculate this automatically, where the number of samples matches the target FPS. (in [0, 5000], default 8)

      :type: int

   .. attribute:: preferences_display_type

      Default location where the Preferences will be displayed in (default ``'WINDOW'``)

      - ``SCREEN``
        Maximized Area -- Open the temporary editor in a maximized screen.
      - ``WINDOW``
        New Window -- Open the temporary editor in a new window.

      :type: Literal['SCREEN', 'WINDOW']

   .. attribute:: render_display_type

      Default location where rendered images will be displayed in (default ``'WINDOW'``)

      - ``NONE``
        Keep User Interface -- Images are rendered without changing the user interface.
      - ``SCREEN``
        Maximized Area -- Images are rendered in a maximized Image Editor.
      - ``AREA``
        Image Editor -- Images are rendered in an Image Editor.
      - ``WINDOW``
        New Window -- Images are rendered in a new window.

      :type: Literal['NONE', 'SCREEN', 'AREA', 'WINDOW']

   .. attribute:: rotation_angle

      Rotation step for numerical pad keys (2 4 6 8) (in [0, 90], default 15.0)

      :type: float

   .. attribute:: show_addons_enabled_only

      Only show enabled add-ons. Un-check to see all installed add-ons. (default False)

      :type: bool

   .. attribute:: show_area_handle

      Show visible area maintenance corner handles (default False)

      :type: bool

   .. attribute:: show_column_layout

      Use a column layout for toolbox (default True)

      :type: bool

   .. attribute:: show_developer_ui

      Display advanced settings and tools for developers (default False)

      :type: bool

   .. attribute:: show_extensions_updates

      Show Extensions Update Count (default True)

      :type: bool

   .. attribute:: show_gizmo

      Use transform gizmos by default (default True)

      :type: bool

   .. attribute:: show_navigate_ui

      Show navigation controls in 2D and 3D views which do not have scroll bars (default True)

      :type: bool

   .. attribute:: show_number_arrows

      Display arrows in numeric input fields for increasing or decreasing values (default False)

      :type: bool

   .. attribute:: show_object_info

      Include the name of the active object and the current frame number in the text info overlay (default True)

      :type: bool

   .. attribute:: show_playback_fps

      Include the number of frames displayed per second in the text info overlay while animation is played back (default True)

      :type: bool

   .. attribute:: show_splash

      Display splash screen on startup (default True)

      :type: bool

   .. attribute:: show_statusbar_memory

      Show Blender memory usage (default False)

      :type: bool

   .. attribute:: show_statusbar_scene_duration

      Show scene duration (default False)

      :type: bool

   .. attribute:: show_statusbar_stats

      Show scene statistics (default False)

      :type: bool

   .. attribute:: show_statusbar_version

      Show Blender version string (default True)

      :type: bool

   .. attribute:: show_statusbar_vram

      Show GPU video memory usage (default False)

      :type: bool

   .. attribute:: show_tooltips

      Display tooltips (when disabled, hold Alt then hover to force display) (default True)

      :type: bool

   .. attribute:: show_tooltips_python

      Show Python references in tooltips (default False)

      :type: bool

   .. attribute:: show_view_name

      Include the name of the view orientation in the text info overlay (default True)

      :type: bool

   .. attribute:: smooth_view

      Time to animate the view in milliseconds, zero to disable (in [0, 1000], default 200)

      :type: int

   .. attribute:: text_hinting

      Method for making user interface text render sharp (default ``'AUTO'``)

      :type: Literal['AUTO', 'NONE', 'SLIGHT', 'FULL']

   .. attribute:: timecode_style

      Format of timecode displayed when not displaying timing in terms of frames (default ``'MINIMAL'``)

      - ``MINIMAL``
        Minimal Info -- Most compact representation, uses '+' as separator for sub-second frame numbers, with left and right truncation of the timecode as necessary.
      - ``SMPTE``
        SMPTE (Full) -- Full SMPTE timecode (format is HH:MM:SS:FF).
      - ``SMPTE_COMPACT``
        SMPTE (Compact) -- SMPTE timecode showing minutes, seconds, and frames only - hours are also shown if necessary, but not by default.
      - ``MILLISECONDS``
        Compact with Decimals -- Similar to SMPTE (Compact), except that the decimal part of the second is shown instead of frames.
      - ``SECONDS_ONLY``
        Only Seconds -- Direct conversion of frame numbers to seconds.

      :type: Literal['MINIMAL', 'SMPTE', 'SMPTE_COMPACT', 'MILLISECONDS', 'SECONDS_ONLY']

   .. attribute:: ui_line_width

      Changes the thickness of widget outlines, lines and dots in the interface (default ``'AUTO'``)

      - ``THIN``
        Thin -- Thinner lines than the default.
      - ``AUTO``
        Default -- Automatic line width based on UI scale.
      - ``THICK``
        Thick -- Thicker lines than the default.

      :type: Literal['THIN', 'AUTO', 'THICK']

   .. attribute:: ui_scale

      Changes the size of the fonts and widgets in the interface (in [0.5, 6], default 1.0)

      :type: float

   .. attribute:: use_filter_brushes_by_tool

      Only show brushes applicable for the currently active tool in the asset shelf. Stored in the Preferences, which may have to be saved manually if Auto-Save Preferences is disabled (default False)

      :type: bool

   .. attribute:: use_fresnel_edit

      Enable a fresnel effect on edit mesh overlays.
      It improves shape readability of very dense meshes, but increases eye fatigue when modeling lower poly
      
      (default False)

      :type: bool

   .. attribute:: use_mouse_over_open

      Open menu buttons and pull-downs automatically when the mouse is hovering (default False)

      :type: bool

   .. attribute:: use_reduce_motion

      Avoid animations and other motion effects in the interface (default False)

      :type: bool

   .. attribute:: use_save_prompt

      Ask for confirmation when quitting with unsaved changes (default True)

      :type: bool

   .. attribute:: use_text_antialiasing

      Smooth jagged edges of user interface text (default True)

      :type: bool

   .. attribute:: use_text_render_subpixelaa

      Render text for optimal horizontal placement (default False)

      :type: bool

   .. attribute:: use_translate_interface

      Translate all labels in menus, buttons and panels (note that this might make it hard to follow tutorials or the manual) (default True)

      :type: bool

   .. attribute:: use_translate_new_dataname

      Translate the names of new data-blocks (objects, materials...) (default True)

      :type: bool

   .. attribute:: use_translate_reports

      Translate additional information, such as error messages (default True)

      :type: bool

   .. attribute:: use_translate_tooltips

      Translate the descriptions when hovering UI elements (recommended) (default True)

      :type: bool

   .. attribute:: use_weight_color_range

      Enable color range used for weight visualization in weight painting mode (default False)

      :type: bool

   .. attribute:: view2d_grid_spacing_min

      Minimum number of pixels between each gridline in 2D Viewports (in [1, 500], default 45)

      :type: int

   .. attribute:: view_frame_keyframes

      Keyframes around cursor that we zoom around (in [1, 500], default 0)

      :type: int

   .. attribute:: view_frame_seconds

      Seconds around cursor that we zoom around (in [0, 10000], default 0.0)

      :type: float

   .. attribute:: view_frame_type

      How zooming to frame focuses around current frame (default ``'KEEP_RANGE'``)

      :type: Literal['KEEP_RANGE', 'SECONDS', 'KEYFRAMES']

   .. data:: weight_color_range

      Color range used for weight visualization in weight painting mode (readonly, never None)

      :type: :class:`ColorRamp`

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

   - :class:`Preferences.view`

