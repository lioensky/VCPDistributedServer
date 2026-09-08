
*********
Selecting
*********

By default, Blender uses :kbd:`LMB` to select items.
This can be changed to :kbd:`RMB` in the :doc:`Preferences </editors/preferences/keymap>`.

Blender has several selection tools that can be used across the different editors.

.. note::

   Some editors deviate from the keyboard shortcuts shown below. For example, most editors
   use :kbd:`Shift-LMB` to add a single item to the selection, but the
   :doc:`Outliner </editors/outliner/introduction>` uses :kbd:`Ctrl-LMB`.
   Similarly, most editors use :kbd:`Ctrl-RMB` for performing a *Lasso Select*,
   but :doc:`node editors </interface/controls/nodes/index>` use :kbd:`Ctrl-Alt-LMB`.

Most selection tools come in two variants, where one variant is available in the Toolbar
and the other in the *Select* menu. While the variants' names are almost identical
(such as *Select Box* in the Toolbar versus *Box Select* in the menu),
the way they work is a bit different. New users coming from other applications
will find the Toolbar variants to be the most familiar.


Toolbar Selection Tools
=======================

All the Toolbar selection tools behave the same when clicking an item: they select it
(and deselect any previously selected items). If you hold :kbd:`Shift` while clicking,
the item will be added to the selection (if it's not selected) or removed from the selection
(if it is selected).

What makes the tools different is what happens when you drag.


.. _tool-select-tweak:

Tweak
-----

.. reference::

   :Tool:      :menuselection:`Toolbar --> Tweak`
   :Shortcut:  :kbd:`W`

Dragging an item will move it around.


.. _tool-select-box:

Select Box
----------

.. reference::

   :Tool:      :menuselection:`Toolbar --> Select Box`
   :Shortcut:  :kbd:`W`

Dragging will create a rectangle, and select all the items that are partially or completely inside it
once you release. (Any other items will be deselected.)

Holding :kbd:`Shift` while dragging will add the items to the selection.
Holding :kbd:`Ctrl` will remove them.

While dragging, you can additionally hold :kbd:`Spacebar` to move the rectangle around with the mouse.

.. list-table:: Select Box example (Edit Mode).

   * - .. _fig-mesh-select-basics-start:

       .. figure:: /images/interface_selecting_border-select1.png
          :width: 200px

          Start.

     - .. _fig-mesh-select-basics-selecting:

       .. figure:: /images/interface_selecting_border-select2.png
          :width: 200px

          Selecting vertices.

     - .. _fig-mesh-select-basics-complete:

       .. figure:: /images/interface_selecting_border-select3.png
          :width: 200px

          Complete.


.. _tool-select-circle:

Select Circle
-------------

.. reference::

   :Tool:      :menuselection:`Toolbar --> Select Circle`
   :Shortcut:  :kbd:`W`

Dragging will select all the items which the circle passed over.
Items which you didn't pass over will be deselected.

Holding :kbd:`Shift` while dragging will add the items to the selection.
Holding :kbd:`Ctrl` will remove them.

You can change the radius of the circle in the tool settings (which can be found
in the area header, the Tool tab of the Sidebar :kbd:`N`, or the Active Tool tab
of the :doc:`Properties editor </editors/properties_editor>`).

.. note::

   In :doc:`Object Mode </editors/3dview/modes>`: unlike *Select Box*,
   which selects objects as soon as the box covers any part of their geometry,
   *Select Circle* only selects objects if the circle passes over their origin point.
   The origin is shown as an orange dot for selected objects but is invisible for unselected ones,
   unless "Origins (All)" is enabled in the :doc:`/editors/3dview/display/overlays`.

   This difference in behavior does not apply to the other modes
   (like Edit Mode and Pose Mode).

.. list-table:: Select Circle example (Edit Mode).

   * - .. figure:: /images/interface_selecting_circle-select1.png
          :width: 320px

          Start.

     - .. figure:: /images/interface_selecting_circle-select2.png
          :width: 320px

          Selecting vertices.

     - .. figure:: /images/interface_selecting_circle-select3.png
          :width: 320px

          Complete.


.. _tool-select-lasso:

Select Lasso
------------

.. reference::

   :Tool:      :menuselection:`Toolbar --> Select Lasso`
   :Shortcut:  :kbd:`W`

Dragging will create a freeform shape, and select all the items inside it once you release.
(Any other items will be deselected.)

Holding :kbd:`Shift` while dragging will add the items to the selection.
Holding :kbd:`Ctrl` will remove them.

While dragging, you can additionally hold :kbd:`Spacebar` to move the shape around with the mouse.

.. note::

   *Select Lasso* behaves the same as *Select Circle* in that
   it only looks at origin points in Object Mode.

.. list-table:: Select Lasso example (Edit Mode).

   * - .. figure:: /images/interface_selecting_lasso-select1.png
          :width: 200px

          Start.

     - .. figure:: /images/interface_selecting_lasso-select2.png
          :width: 200px

          Selecting vertices.

     - .. figure:: /images/interface_selecting_lasso-select3.png
          :width: 200px

          Complete.


Selection Modes
---------------

.. reference::

   :Tool:      Select Tools
   :Panel:     :menuselection:`Tool Settings --> Mode`

Each of the Toolbar selection tools has a mode to configure
how it interacts with existing selections.
Note that not every tool supports all of these modes.

Set
   Sets a new selection (the previous selection is discarded).
   This is the default.
Extend
   Adds newly selected items to the existing selection.
Subtract
   Removes newly selected items from the existing selection.
Invert :kbd:`Ctrl-I`
   Inverts the selection (unselected items become selected and vice versa).
Intersect
   Selects items that intersect with the existing selection.


Menu Selection Tools
====================

These tools are variants of the previously described ones.
They're available in the menu rather than the Toolbar
and work slightly differently.


.. _bpy.ops.*.select_box:

Box Select
----------

.. reference::

   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`

To use this tool, you first activate the menu item or keyboard shortcut
and then drag a box as usual. Unlike *Select Box*, the default behavior
here is to add the items inside the box to the selection.
(The ones outside the box are not deselected.)

To remove the items inside the box from the selection,
hold :kbd:`Shift`, or drag with :kbd:`MMB` instead.

While dragging, you can additionally hold :kbd:`Spacebar` to move the box around with the mouse.


.. _bpy.ops.*.select_circle:

Circle Select
-------------

.. reference::

   :Menu:      :menuselection:`Select --> Circle Select`
   :Shortcut:  :kbd:`C`

To use this tool, you first activate the menu item or keyboard shortcut
and then drag a circle around as usual. Unlike *Select Circle*, the default
behavior here is to add the items inside the circle to the selection.
(The ones outside the circle are not deselected.)

To remove the items inside the circle from the selection,
hold :kbd:`Shift`, or drag with :kbd:`MMB` instead.

You can change the radius of the circle by scrolling with the :kbd:`Wheel`
or using the :kbd:`NumpadPlus` and :kbd:`NumpadMinus` keys.

Once activated, *Circle Select* stays active: you can release the mouse button
and start dragging somewhere else without having to press :kbd:`C` again.
At the same time, however, it blocks all other parts of Blender while it's active.
To deactivate the tool again, press :kbd:`RMB`, :kbd:`Return`, or :kbd:`Esc`.


.. _bpy.ops.*.select_lasso:

Lasso Select
------------

.. reference::

   :Menu:      :menuselection:`Select --> Lasso Select`
   :Shortcut:  :kbd:`Ctrl-RMB`

To use this tool, you first activate the menu item and drag a freeform shape
around the item(s) you want to select with :kbd:`LMB`. The menu lets you choose
whether to set, extend or reduce the selection.

Alternatively, you can immediately start dragging with :kbd:`Ctrl-RMB`.
Unlike *Select Lasso*, the default behavior then is to add the items inside
the lasso to the selection. (The ones outside the lasso are not deselected.)

To remove the items inside the lasso from the selection,
drag with :kbd:`Shift-Ctrl-RMB` instead.

While dragging, you can additionally hold :kbd:`Spacebar` to move the lasso
around with the mouse.
