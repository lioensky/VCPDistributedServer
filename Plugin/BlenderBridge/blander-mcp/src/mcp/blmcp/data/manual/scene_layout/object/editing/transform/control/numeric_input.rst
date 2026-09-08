.. _transform-numeric-input:

*************
Numeric Input
*************

Using the mouse for transformations is convenient, but if you require more precise control,
you can also enter numeric values. After pressing the shortcut type a number
to indicate the magnitude of the transformation. Then confirm or cancel.
E.g. pressing :kbd:`S 2`, :kbd:`Return` will double the scale of an object.

Move :kbd:`G`
   By default and with no other key presses, the translation will occur along the X axis.
Rotation :kbd:`R`
   The rotation is in clockwise direction for positive values.
Scale :kbd:`S`
   Scaling works in almost identical fashion to translation.
   The primary difference is that by default, scaling applies equally to all three axes.

You can see the numbers you enter in the 3D Viewport footer.

.. figure:: /images/scene-layout_object_editing_transform_control_numeric-input_footer.png
   :align: center

   Numeric input displayed in the footer.

.. tip::

   Numeric input can also be inputted in
   the :doc:`Properties </scene_layout/object/properties/transforms>` region.


.. _transform-numeric-input-simple:

Simple Mode
===========

Blender has two "modes" a simple and an advanced one. Simple mode only accepts simple numbers.

Decimals :kbd:`Period`
   Decimals can be entered by pressing :kbd:`Period`.
Negate :kbd:`Minus`
   Negate the whole value by pressing :kbd:`Minus`.
Inverse :kbd:`Slash`
   Hitting :kbd:`Slash` during number entry switches the number being entered to
   its reciprocal, e.g. ``2 /`` results in 0.5 (1/2); ``20 /`` results in 0.05 (1/20).
Reset :kbd:`Backspace`
   Hitting :kbd:`Backspace` after having deleted all leading chars
   will first reset the edited value to initial state, and on second press,
   the whole number editing will be canceled, going back to usual transform with mouse.
Next/Previous Component :kbd:`Tab`, :kbd:`Ctrl-Tab`
   To enter numeric values for multiple axes, use :kbd:`Tab` or :kbd:`Ctrl-Tab`.
   E.g. To move an object, one unit on all three axes press: :kbd:`G 1`
   and :kbd:`Tab 1` and :kbd:`Tab 1`.

Non-number Inputs
   You can also combine numeric input with
   :doc:`Axis Locking </scene_layout/object/editing/transform/control/axis_locking>`
   to limit movement to a particular axis or tool specific shortcuts.


.. _transform-numeric-input-advanced:

Advanced Mode
=============

In advanced mode you can additionally enter expressions and units.

Use :kbd:`=` or :kbd:`NumpadAsterisk` to enable advanced mode,
and :kbd:`Ctrl-=` or :kbd:`Ctrl-NumpadAsterisk` to switch back to simple mode.

It features:

- Units (``cm``, ``"``, ``deg``, etc.).
  See :ref:`unit system <bpy.types.UnitSettings>`.
- Basic operations from Python (``+``, ``*``, ``/``, ``**``, etc.).
- Math constants and functions (``pi``, ``sin``, ``sqrt``, etc.).
  See Python's `math <https://docs.python.org/3.8/library/math.html>`__ module.

You can still use the negate and inverse shortcuts (:kbd:`Minus`, :kbd:`Slash`),
as well as non-number inputs, but you have to hold :kbd:`Ctrl` to activate them.
