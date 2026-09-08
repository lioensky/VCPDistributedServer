.. _bpy.types.Region:
.. _ui-region:

*******
Regions
*******

Every Editor in Blender is divided into Regions.
Regions can have smaller structuring elements like
:doc:`tabs and panels </interface/window_system/tabs_panels>`
with buttons, controls and widgets placed within them.

.. figure:: /images/interface_window-system_regions_3d-view.png

   The regions of the 3D Viewport showing the Sidebar and
   the Adjust Last Operation panel after adding a Cube.

   Header (green), Main region (yellow), Toolbar (blue),
   Sidebar (red) and Adjust Last Operation panel (pink).


.. _ui-region-window:

Main Region
===========

At least one region is always visible.
It is called the Main region and is the most prominent part of the editor.

Each editor has a specific purpose, so the main region and
the availability of additional regions are different between editors.
See specific documentation about each editor in the :doc:`Editors </editors/index>` chapter.


.. _bpy.types.Header:
.. _ui-region-header:

Header
======

A header is a small horizontal strip, which sits either at the top or bottom of an area.
All editors have a header acting as a container for menus and commonly used tools.
:ref:`Menus <bpy.types.UIPopupMenu>` and buttons will change with the editor type and
the selected object and mode.

.. figure:: /images/editors_3dview_introduction_3d-view-header-object-mode.png

   The Header of the 3D Viewport.


.. _bpy.ops.screen.header:

Context Menu
------------

:kbd:`RMB` on a header reveals a context menu with a couple options:

Show Header
   Toggles the visibility of the header.
   If a header is hidden, it can be made visible again by clicking or dragging
   the small arrow that appears at the top/bottom right of the editor.
Show Tool Settings
   Toggles the visibility of the `Tool Settings`_.
Show Menus
   Toggles whether the :ref:`Menus <bpy.types.UIPopupMenu>` are collapsed or not.

.. _bpy.ops.screen.region_flip:

Flip to Bottom/Top
   Toggles whether the header or Tool Settings appear on the top or bottom of the editor.
Vertical/Horizontal Split
   Shows an indicator line that lets you select the area and position where to split.
   :kbd:`Tab` switches between vertical/horizontal.
Maximize Area / Focus Mode
   See :ref:`bpy.ops.screen.screen_full_area`.
Duplicate Area into New Window
   See :ref:`bpy.ops.screen.area_dupli`.
Close Area
   Closes the area and replaces it with the expansion of a neighboring area.


Toolbar
=======

The :ref:`Toolbar <ui-region-toolbar>` (on the left side of the editor area)
contains a set of interactive tools. :kbd:`T` toggles the visibility of the Toolbar.


.. _ui-region-tool-settings:

Tool Settings
=============

A horizontal strip at the top or bottom of the editor (similar to the header)
containing settings for the currently selected tool. Just like the header,
it can be hidden and moved through its context menu.


Adjust Last Operation
=====================

:ref:`Adjust Last Operation <bpy.ops.screen.redo_last>` is a region that allows
tweaking an operator after running it. For example, if you just added a cube,
you can use this region to tweak its size.


.. _ui-region-sidebar:

Sidebar
=======

The *Sidebar* (on the right side of the editor area)
contains :ref:`Panels <ui-panels>`
with settings of objects within the editor and the editor itself.
:kbd:`N` toggles the visibility of the Sidebar.


.. _ui-region-footer:

Footer
======

Some editors show a bar (on top/bottom of the editor area)
that displays information about for example the active tool or operator.

In animation editors, the footer contains controls and options related to playback, keying, auto keyframing, and
transport.

These settings allow you to:

- Control how animations are previewed and synchronized with audio.
- Insert and manage keyframes through keying sets and auto keying.
- Navigate the timeline using playback and transport controls.
- Adjust frame ranges and preview specific segments of the animation.

.. seealso::

   For a detailed description of all properties and controls commonly found in the footer,
   see the :ref:`Playback Controls <animation-editors-footer>` documentation.


Arranging
=========

Scrolling
---------

A region can be scrolled vertically and/or horizontally by dragging it with the :kbd:`MMB`.
If the region has no zoom level, it can also be scrolled by using the :kbd:`Wheel`
while the mouse hovers over it.

.. _interface_window-system_regions_scroll_range:

Some regions, in particular animation timelines, have scrollbars with added control points
to adjust the vertical or horizontal range of the region.
These special scrollbars will have added widgets at the ends, as shown in the following image:

.. figure:: /images/interface_window-system_regions_scrollbar_widget.png
   :align: center

   Scrollbars with zoom widgets.

This can be used to stretch or compress the range to show more or less detail within the available screen space.
Simply drag one of the dots to either increase or decrease the displayed range.
You can also quickly adjust both the horizontal and vertical range by dragging in the editor with :kbd:`Ctrl-MMB`.


.. _bpy.ops.screen.region_blend:

Changing the Size and Hiding Regions
------------------------------------

Resizing regions works by dragging their border, the same way as
:doc:`/interface/window_system/areas`.

To hide a region, resize it down to nothing.
A hidden region leaves a little arrow sign.
:kbd:`LMB` on this icon to make the region reappear.

.. list-table:: Hiding and showing the Sidebar.

   * - .. figure:: /images/interface_window-system_regions_sidebar-hide.png

     - .. figure:: /images/interface_window-system_regions_sidebar-show.png


.. _bpy.ops.screen.region_scale:

Scaling
-------

The scale of certain regions (such as the Toolbar) can be changed by dragging inside them
with :kbd:`Ctrl-MMB`, or using :kbd:`NumpadPlus` and :kbd:`NumpadMinus` while hovering the
mouse cursor over them. Press :kbd:`Home` to reset the scale to the default.


.. _ui-region-asset_shelf:

Asset Shelf
===========

.. figure:: /images/interface_window-system_regions_asset-shelf.png
   :align: center

   The Asset Shelf of the 3D View, showing material assets.

Search
------

To search for assets, hover your mouse over the Asset Shelf, then press Ctrl-F and type a search query.
This will filter the poses to match what you typed.


Tabs
----

.. figure:: /images/asset_shelf-tabs.png

   The usage of catalogs as tabs.

Catalogs can be shown as individual tabs. Each tab will only show its content, and the content of its children.
That makes it easy to filter down to a certain set of assets.


Display Options
---------------

.. figure:: /images/asset_shelf-options.png

   Display options available for the asset shelf.

It is possible to change the size of items on the shelf by using the size property.

By toggling on the "Names" checkbox, the asset names will be shown in the shelf. Alternatively it is also
possible to hover over an item to show its name.

By default the shelf only has a height for one item row. To allow for more rows, drag it on the upper edge to increase
its size.


Filter
------

.. _bpy.types.PreferencesView.use_filter_brushes_by_tool:

By Active Tool
   Only show brushes applicable for the currently active tool in the asset shelf.

   .. note::

      The value of this property is stored in the :doc:`/editors/preferences/index`,
      which may have to be saved manually if *Auto-Save Preferences* is disabled.
