.. _bpy.types.PreferencesView:

*********
Interface
*********

Interface configuration lets you change how UI elements are displayed and how they react.

.. figure:: /images/editors_preferences_section_interface.webp


Display
=======

.. _bpy.types.PreferencesView.ui_scale:

Resolution Scale
   Adjusts the size of fonts and buttons relative to the automatically detected DPI.
   During typical usage, you may prefer to use zoom which is available in many parts of Blender interface.

.. _bpy.types.PreferencesView.ui_line_width:

Line Width
   Scale of lines and points in the interface e.g. button outlines, edges and vertex points in the 3D Viewport.

   Thin, Default, Thick

.. _bpy.types.PreferencesView.show_splash:

Splash Screen
   Display the :ref:`splash` when starting Blender.

.. _bpy.types.PreferencesView.show_developer_ui:

Developer Extras
   Show settings and menu items which are intended to help developers, this includes:

   - :ref:`Operator Search <bpy.ops.wm.search_operator>`
   - :doc:`Sequencer Cache Settings </editors/video_sequencer/sequencer/sidebar/cache>`

   Button Context Menu
      Online Python Reference
         To open the Python reference manual.
      Copy Python Command
         To copy the expression used when pressing the button.
      Edit Source
         To edit Python source code that defines the button.
      Edit Translation
         The option to edit UI translations
         (only available when the *Manage UI translations* add-on is also enabled).
   Preferences
      Experimental Tab
         Work in progress features can be enabled here which are currently being tested.

.. _bpy.types.PreferencesView.show_tooltips:

Tooltips
   User Tooltips
      When enabled, a tooltip will appear when your mouse pointer is over a control.
      This tip explains the function of what is under the pointer,
      shows the associated hotkey (if any).
      When disabled, you can still force the tooltip display by holding :kbd:`Alt` then hovering the control.

   .. _bpy.types.PreferencesView.show_tooltips_python:

   Python Tooltips
      Displays a property's Python information below the tooltip.

.. _bpy.types.Preferences.use_recent_searches:

Search -- Sort by Most Recent
   Show most recently selected items at the top of search results,
   otherwise search results are sorted alphabetically.

.. _bpy.types.Preferences.show_hidden_ids:

Search -- Show Hidden
   Display data-blocks with dot-prefixed names in search menus.
   This affects search pop-ups and data-block selectors that use filtering.

   By default, dot-prefixed names are hidden to prevent accidental use
   of internal or helper data-blocks. See :ref:`data-system-datablock-name-hidden`
   for more information about this naming convention.


Editors
=======

.. _bpy.types.PreferencesSystem.use_region_overlap:

Region Overlap
   This makes regions overlap the viewport. It means that the *Toolbar* and *Sidebar* regions,
   will be displayed overlapping the main area.

.. _bpy.types.PreferencesView.show_area_handle:

Show -- Corner Handles:
   Displays small handles in the corners of each :doc:`/interface/window_system/areas`.
   These can be used to split or join areas with a click-and-drag action.

   This option is especially useful on touch-enabled devices,
   where precise right-click or edge selection is more difficult.

.. _bpy.types.PreferencesView.show_number_arrows:

Show -- Numeric Input Arrows
   - When enabled always display arrows in numeric input fields for increasing or decreasing values.
   - When disabled, arrows are shown when hovering over the property.

.. _bpy.types.PreferencesView.show_navigate_ui:

Show -- Navigation Controls
   Show navigation controls at top right of the area.
   This impacts the 3D Viewport as well as image spaces.

   .. note::

      If you are familiar with navigation key shortcuts, this can be disabled.

.. _bpy.types.PreferencesView.border_width:

Border Width
   Sets the padding around each editor area.
   A larger value increases the hit zone for :doc:`area controls </interface/window_system/areas>`,
   which can improve usability on pen tablets, touch screens,
   or for users with visual or physical accessibility issues.

.. _bpy.types.PreferencesView.color_picker_type:

Color Picker Type
   Choose which type of :term:`Color Space` you prefer for the
   :doc:`Color picker </interface/controls/templates/color_picker>`.
   It will show when clicking :kbd:`LMB` on any color field.

   .. list-table:: Color Picker types.

      * - .. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png

             Circle HSV.

        - .. figure:: /images/interface_controls_templates_color-picker_circle-hsl.png

             Circle HSL.

        - ..

      * - .. figure:: /images/interface_controls_templates_color-picker_square-sv-h.png

             Square (SV + H).

        - .. figure:: /images/interface_controls_templates_color-picker_square-hs-v.png

             Square (HS + V).

        - .. figure:: /images/interface_controls_templates_color-picker_square-hv-s.png

             Square (HV + S).

.. _bpy.types.PreferencesView.header_align:

Header Position
   The default header position when opening a new editor.

   :Keep Existing:
      Uses top for most editor types and the positions saved in the start-up file.
   :Top/Bottom:
      Always positions the header at the top or the bottom of the editor.

.. _bpy.types.PreferencesView.factor_display_type:

Factor Display Type
   How factor value types are displayed in the user interface.

   :Factor: Values are displayed as float numbers between 0.0 and 1.0.
   :Percentage: Values are expressed as a percentage between 0 and 100.


Temporary Editors
-----------------

When performing certain operations, Blender will open a new window.
The behavior of these operations can be configured here.

.. _bpy.types.PreferencesView.render_display_type:

Render In
   When rendering, the user interface can do any of:

   :Keep User Interface: The user interface does not change and the render is computed in the background.
   :Maximize Area: A new Image editor is opened as a temporary window in full screen mode.
   :Image Editor: The area that is the largest on screen is replaced placed by a temporary Image editor.
   :New Window: A new Image editor is opened as a regularly sized temporary window.

.. _bpy.types.PreferencesView.filebrowser_display_type:

File Browser
   When opening files from the computer, the user interface can do any of:

   :Maximize Area: A new File Browser editor is opened as a temporary window in full screen mode.
   :New Window: A new File Browser editor is opened as a regularly sized temporary window.

.. _bpy.types.PreferencesView.preferences_display_type:

Preferences
   Controls how the :ref:`User Preferences <bpy.ops.screen.userpref_show>` editor is displayed when opened.

   :Maximize Area: Opens the Preferences as a temporary full-screen editor within the current window.
   :New Window: Opens the Preferences in a new, separate window of regular size.


.. _prefs-interface-status_bar:

Status Bar
----------

Preferences that affect the :doc:`/interface/window_system/status_bar`.

.. _bpy.types.PreferencesView.show_statusbar:

.. rubric:: Show

Scene Statistics
   Shows information about the data in the active scene.

   - **Collection**: The name of the active :doc:`Collection </scene_layout/collections/index>`.
   - **Active Object**: The name of the active selected object.
   - **Geometry**: Information about the current scene depending on the mode and object type.
     This can be the number of vertices, faces, triangles, or bones.
   - **Objects**: The number of selected objects and the total count of objects.

Scene Duration
   Shows the total amount of time of the playback along with the current frame number and total frame count.
   The format of the duration text is determined by the
   :ref:`Timecode Style <bpy.types.PreferencesView.timecode_style>`.

System Memory
   Shows an estimate of Blender's RAM consumption. On a single-instance single-machine scenario,
   this estimate provides a measurement against the hardware limit of the machine.

Extensions Updates
   Shows the number of :doc:`extensions </advanced/extensions/index>` with available updates.

Blender Version
   Shows the version number of Blender that is currently running.


.. _prefs-interface-translation:

Language
========

.. _bpy.types.PreferencesView.language:

Language
   The language used for translating the user interface (UI).
   The list is broken up into categories determining how complete the translations are.

.. _bpy.types.PreferencesView.use_translate:

Translate
   Tooltips
      Translates the descriptions when hovering over UI elements.
   Interface
      Translates all labels in menus, buttons, and panels.
   New Data
      Translates the names of new data-blocks.


Accessibility
=============

.. _bpy.types.PreferencesView.use_reduce_motion:

Reduce Motion
   Avoids interface animations and motion effects.
   This option helps reduce visual distractions and can improve comfort for
   users sensitive to motion or those who prefer a more static interface.


Text Rendering
==============

.. _bpy.types.PreferencesView.use_text_antialiasing:

Anti-Aliasing
   Enable interface text :term:`Anti-Aliasing`.
   When disabled, texts are rendered using straight text rendering (filling only absolute pixels).

.. _bpy.types.PreferencesView.use_text_render_subpixelaa:

Subpixel Anti-Aliasing
   Render text for optimal horizontal placement.

.. _bpy.types.PreferencesView.text_hinting:

Hinting
   Adjust `font hinting <https://en.wikipedia.org/wiki/Font_hinting>`__,
   controls the spacing and crispness of text display.

.. _bpy.types.PreferencesView.font_path_ui:

Interface Font
   Replacement for the default user interface font.

.. _bpy.types.PreferencesView.font_path_ui_mono:

Mono-space Font
   Replacement for the default mono-space interface font
   *(used in the Text editor and Python Console)*.


Menus
=====

.. _bpy.types.PreferencesView.menu_close_leave:

Close Menu on Leave
   Close menus when the mouse is moved out of the region.


.. _bpy.types.PreferencesView.use_mouse_over_open:

Open on Mouse Over
------------------

Select this to have the menu open by placing the mouse pointer over the entry instead of clicking on it.

.. _bpy.types.PreferencesView.open_toplevel_delay:

Top Level
   Time delay in 1/10 second before a menu opens (*Open on Mouse Over* needs to be enabled).

.. _bpy.types.PreferencesView.open_sublevel_delay:

Sub Level
   Same as above for sub menus (for example: :menuselection:`File --> Open Recent`).


.. _prefs-pie-menu:

Pie Menus
---------

.. _bpy.types.PreferencesView.pie_animation_timeout:

Animation Timeout
   Length of animation when opening Pie Menus.

.. _bpy.types.PreferencesView.pie_tap_timeout:

Tap Key Timeout
   Keystrokes held longer than this will dismiss the menu on release (in 1/100ths of a second).

.. _bpy.types.PreferencesView.pie_initial_timeout:

Recenter Timeout
   The window system tries to keep the pie menu within the window borders.
   Pie menus will use the initial mouse position as center for this amount of time, measured in 1/100ths of a second.
   This allows for fast dragged selections.

.. _bpy.types.PreferencesView.pie_menu_radius:

Radius
   The size of the Pie Menu set with the distance (in pixels) of the menu items from the center of the pie menu.

.. _bpy.types.PreferencesView.pie_menu_threshold:

Threshold
   Distance from center before a selection can be made.

.. _bpy.types.PreferencesView.pie_menu_confirm:

Confirm Threshold
   Distance threshold after which selection is made (zero disables).
