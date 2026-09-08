
************
Input Fields
************

.. _bpy.ops.buttons.start_filter:
.. _bpy.ops.buttons.clear_filter:

Text & Search Fields
====================

.. figure:: /images/interface_controls_buttons_fields_text-search.png
   :align: center

   A text and a search field.

Text fields show a rounded rectangular border, and optionally an icon and/or text inside the border.
Text fields store text strings, and provide the means to edit text by standard text editing shortcuts:

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Home`
     - Go to the start of the line.
   * - :kbd:`End`
     - Go to the end of the line.
   * - :kbd:`Left`, :kbd:`Right`
     - Move the cursor a single character.
   * - :kbd:`Ctrl-Left`, :kbd:`Ctrl-Right`
     - Move the cursor an entire word.
   * - :kbd:`Backspace`, :kbd:`Delete`
     - Delete characters.
   * - :kbd:`Ctrl-Backspace`, :kbd:`Ctrl-Delete`
     - Delete words.
   * - :kbd:`Shift`
     - Select while holding the key and moving the cursor.
   * - :kbd:`Ctrl-A`
     - Select all text.
   * - :kbd:`Ctrl-C`
     - Copy the selected text.
   * - :kbd:`Ctrl-X`
     - Cut the selected text.
   * - :kbd:`Ctrl-V`
     - Paste text at the cursor position.

For text fields with an icon and pop-ups, see :ref:`ui-data-id`.


Number Fields
=============

.. figure:: /images/interface_controls_buttons_fields_number-button.png
   :align: right

   Number fields.

Number fields store values and units.

The first type of number field shows triangles pointing left (<) and right (>)
on the sides of the field when mouse pointer is over the field.

Sliders, a second type of number field, have a colored bar in the background
to display values over a range, e.g. percentage values.

The value can be edited in several ways:

Incremental Steps
   To change the value in unit steps, click :kbd:`LMB` on the small triangles (not available for sliders).
   You can also use :kbd:`Ctrl-Wheel` while hovering over the field to edit the value.
Dragging
   To change the value with the mouse, hold down :kbd:`LMB` and drag to left or right.

   Hold :kbd:`Ctrl` to snap to the discrete steps while dragging or :kbd:`Shift` for precision input.
Keyboard Input
   Press :kbd:`LMB` or :kbd:`Return` to enter value by typing it with keyboard.

   When entering values by keyboard, number fields work like text fields:

   - Press :kbd:`Return` or :kbd:`LMB` outside the field to apply the change.
   - Press :kbd:`Esc` or :kbd:`RMB` to cancel.
   - Press :kbd:`Tab` to jump to the next field or :kbd:`Shift-Tab` to go to the previous field.
   - Press :kbd:`Minus` while hovering over a number field to negate the value.


Multi-Value Editing
-------------------

.. figure:: /images/interface_controls_buttons_fields_multi-value-edit.png
   :align: right

   Multi-value editing.

You can edit multiple number fields at once by pressing down
:kbd:`LMB` on the first field, and then dragging vertically over
the fields you want to edit. Finally you can either drag left or right to
adjust value with the mouse, or release the :kbd:`LMB` and type in a value.


Value Limits
------------

Most numerical values are restricted by "soft limit" and "hard limit" value ranges.
Changing values by dragging with the mouse is restricted to the "soft limit" value range.
Input via keyboard will allow the use of wider value ranges, but never wider than the "hard limit".


Expressions
-----------

.. Do not use mathjax here

You can enter mathematical expressions into any number field.
For example, enter ``3*2`` or ``10/5+4`` instead of ``6``.
Even constants like ``pi`` (3.142) or functions like ``sqrt(2)`` (square root of 2)
may be used.

.. seealso::

   These expressions are evaluated by Python; for all available math expressions see:
   `Math module reference <https://docs.python.org/3/library/math.html>`__.


Expressions as Drivers
^^^^^^^^^^^^^^^^^^^^^^

You may want your expression to be re-evaluated after it is entered.
Blender supports this using :doc:`Drivers </animation/drivers/index>` (a feature of the animation system).

Expressions beginning with ``#`` have a special use.
Instead of evaluating the value and discarding the expression,
a driver is added to the property with the expression entered.

The expression ``#frame`` is a quick way to map a value to the current frame,
but more complex expressions like ``#fmod(frame, 24) / 24`` are also supported.

This is simply a convenient shortcut to add drivers which can also be added via the :kbd:`RMB` menu.


Units
-----

As well as expressions, you can specify numbers and units.
If no unit is given, then a default unit is applied.
The unit system can be changed in :ref:`scene settings <bpy.types.UnitSettings>`.

You can use either the unit abbreviation or the full name after the value.

Examples of valid usage of length units include:

.. hlist::
   :columns: 2

   - ``1cm``
   - ``1m 3mm``
   - ``1m, 3mm``
   - ``2ft``
   - ``3ft/0.5km``
   - ``2.2mm + 5' / 3" - 2yards``

.. note:: Using Units

   - Decimal separator is optional.
   - You can mix units, e.g. metric and imperial even though you can only show one at a time.
   - Plurals of the names are recognized too, so ``meter`` and ``meters`` can both be used.


Color Fields
============

.. figure:: /images/interface_controls_buttons_fields_color.png
   :align: right
   :figwidth: 129px

   Color fields. With and without alpha.

The color field stores a color value.
Clicking on it with :kbd:`LMB` opens the :doc:`/interface/controls/templates/color_picker`.

Color fields with an alpha channel are divided in half: on the left, the color is shown without an alpha channel,
and on the right, it's shown with an alpha channel over a checker pattern.

Colors can be copied to other color fields by dragging and dropping.

Hovering over a color property will display a large swatch preview of the color
and the color's hexadecimal, RGBA, and HSVA values.
