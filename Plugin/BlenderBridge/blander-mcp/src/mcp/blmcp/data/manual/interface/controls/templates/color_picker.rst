.. _ui-color-picker:

************
Color Picker
************

.. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png
   :align: right

   Circle HSV color picker.

The *Color Picker* is a pop-up control that allows you to define and adjust color values.
It appears when editing any color property in Blender, such as materials, lights, brushes, or interface themes.

The color picker provides multiple color models and interaction modes to suit different workflows,
and can display or edit colors in both *linear* and *perceptual* (display-referred) color spaces.


Interface
=========

Color Picker
   The large color field lets you pick two color components at once, depending on the selected picker type.
   The third component (such as value or saturation) is controlled with a slider next to the color field.

   The picker's appearance and behavior depend on the type chosen in the Preferences; see `Types`_ below.

Value/Lightness
   The vertical slider with a gradient background defines the brightness or lightness of the selected color.
   You can scroll the :kbd:`Wheel` for fine adjustments or click and drag the handle.


Below the color picking widget are a few options, the first affects how the color component's values are computed.

:Linear:
   Displays color component values in the scene's :ref:`linear working <bpy.types.BlendFileColorspace.working_space>`
   color space used internally for rendering and compositing.
:Perceptual:
   Displays color component values in the color picking space (*sRGB* by default),
   which matches the visual appearance of the color widgets and is more intuitive for user selection.

The next set of options change the :term:`Color Model` that is used.
The available options depend on the :ref:`Color Picker Type <bpy.types.PreferencesView.color_picker_type>`.

:RGB:
   Defines a color by directly mixing *Red*, *Green*, and *Blue* components.
:HSV/HSL:
   Defines a color by adjusting *Hue*, *Saturation*, and *Value* (or Lightness).
   Useful for adjusting color tone and intensity independently.

Component Values
   The numeric fields below the picker show the component values (RGB or HSV/HSL).
   Blender expresses these in the range **0.0 to 1.0**.
   For color inputs that include an :term:`Alpha Channel`, an additional slider and field are shown.

Hex
   Displays or accepts the color's hexadecimal (hex) representation.
   Hex shorthand notation can be used (for example, ``FC0`` for ``FFCC00``).

   .. note::

      Hex values are automatically :term:`Gamma`-corrected for the :term:`sRGB Color Space <Color Space>`.
      For more information, see :doc:`Color Management </render/color_management/index>`.

.. _bpy.ops.ui.eyedropper_color:

:bl-icon:`eyedropper` Eyedropper
   Samples a color from anywhere inside the Blender window using the :ref:`ui-eyedropper`.

   The sampled colors are read in **linear color space**, so they do not account for display transformations
   such as view or exposure adjustments.
   Sampling colors from overlays, reference images, or video preview regions may be inaccurate
   since those may be drawn after color management transforms.


Shortcuts
=========

- :kbd:`Ctrl-LMB` (drag): Snap hue to 30° intervals.
- :kbd:`Shift-LMB` (drag): Fine-tune color movement for precise adjustments.
- :kbd:`Wheel`: Adjust value or lightness.
- :kbd:`Backspace`: Reset the current value to its default.


Types
=====

The *Color Picker Type* determines how colors are visualized and selected.
Different picker types offer alternative layouts for adjusting hue, saturation, and value components.
The choice is a matter of personal preference and workflow.

You can choose the default picker type in the Preferences under
:ref:`Interface Preferences <bpy.types.PreferencesView.color_picker_type>`.

.. list-table:: Color Picker Types
   :header-rows: 0
   :widths: 33 33 33
   :class: valign

   * - .. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png

          Circle HSV

     - .. figure:: /images/interface_controls_templates_color-picker_circle-hsl.png

          Circle HSL

     - ..

   * - .. figure:: /images/interface_controls_templates_color-picker_square-sv-h.png

          Square (SV + H)

     - .. figure:: /images/interface_controls_templates_color-picker_square-hs-v.png

          Square (HS + V)

     - .. figure:: /images/interface_controls_templates_color-picker_square-hv-s.png

          Square (HV + S)


Notes
=====

- Blender internally works in *linear color space*; conversions from sRGB or other spaces happen automatically.
- The color picker displays the color as it appears in the current view transform, but the stored value remains
  linear.
- For consistent results across renders and display devices, see
  :doc:`Color Management </render/color_management/index>`.
