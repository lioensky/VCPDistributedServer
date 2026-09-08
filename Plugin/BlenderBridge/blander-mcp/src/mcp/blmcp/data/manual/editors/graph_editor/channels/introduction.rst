
************
Introduction
************

.. _editors-graph_editor-channels_region:

Channels Region
===============

.. figure:: /images/editors_graph-editor_channels_region.png

   The Channels region.

This region is found on the left side of time-based editors like
the :doc:`Dope Sheet Editor </editors/dope_sheet/introduction>` and the Graph Editor.
It shows a tree of items (objects, bones...) and their animated properties,
with the latter also being called "channels." Each channel has an associated F-curve
describing how its value changes over time.

The rows are color-coded as follows:

- Dark blue: scenes, objects
- Light blue: :doc:`actions </animation/actions>`, :doc:`shape keys </animation/shape_keys/index>` etc.
- Green: channel groups
- Gray: channels

.. _bpy.types.DopeSheet.use_filter_invert:
.. _bpy.types.DopeSheet.filter_text:

Search :kbd:`Ctrl-F`
   Lets you filter the channels by typing a part of their name. Click the Invert button to instead
   show channels that *don't* include the search text.


Channels
--------

The headers contain the following toggle buttons:

:bl-icon:`unpinned` / :bl-icon:`pinned` Pin
   Keep the row and its children visible even when selecting a different object.
:bl-icon:`hide_off` / :bl-icon:`hide_on` Hide
   Hides the keyframes and curve associated with the channel.
:bl-icon:`modifier_on` / :bl-icon:`modifier_off` Modifiers
   Deactivates the modifiers of the curve.
:bl-icon:`checkbox_hlt` / :bl-icon:`checkbox_dehlt` Mute
   Deactivates the curve, making the animation behave as though it doesn't exist.
:bl-icon:`unlock` / :bl-icon:`locked` Lock :kbd:`Tab`
   Prevent the curve from being edited.

   .. note::

      This also works in the :doc:`Nonlinear Animation Editor </editors/nla/introduction>`,
      but note that it only locks the strips there, not the underlying F-curves.


Selection
---------

- Select single header: click :kbd:`LMB`
- Add/Remove single header to/from selection: click :kbd:`Ctrl-LMB`
- Select range: click :kbd:`Shift-LMB`
- Select All: :kbd:`A`
- Deselect All: press :kbd:`Alt-A` or double-tap :kbd:`A`
- Box Select: drag :kbd:`LMB`
- Box Add: drag :kbd:`Shift-LMB`
- Box Remove: drag :kbd:`Ctrl-LMB`
- Select all keyframes in the channel: double-click :kbd:`LMB` on its header.


Editing
-------

- Rename (anything but a channel): double-click :kbd:`LMB`
- Delete selected: :kbd:`X` or :kbd:`Delete`
- Lock selected: :kbd:`Tab`

Sliders
^^^^^^^

.. figure:: /images/editors_dope-sheet_introduction_action-editor-sliders.png

   The Action editor showing sliders.

If you enable :menuselection:`View --> Show Sliders`, the region will show a
value slider next to each channel. Changing such a slider will change the value
of the curve at the current frame, creating a keyframe if one doesn't already exist.
