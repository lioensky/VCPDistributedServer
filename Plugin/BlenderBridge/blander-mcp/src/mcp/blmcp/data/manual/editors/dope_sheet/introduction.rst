.. index:: Editors; Dope Sheet

************
Introduction
************

The Dope Sheet offers a bird's-eye view of the keyframes inside the scene.
It's inspired by classical hand-drawn animation, where animators make use of a chart
showing exactly when each drawing, sound, and camera move will occur, and for how long.
It is also possible to show :ref:`Playback Controls <animation-editors-footer>` to control the playhead.

.. figure:: /images/editors_dope-sheet_introduction_overview.png
   :width: 620px

   The Dope Sheet.


Dope Sheet Modes
================

The editor has several different modes that can be selected from a dropdown in the header.
The default *Dope Sheet* mode gives an overview of most types of animatable data.
For others, such as masks, you need to switch to a more specific mode.

.. figure:: /images/editors_dope-sheet_introduction_modes.png

   Dope Sheet modes.

The modes are as follows:

- Dope Sheet
- :doc:`Action Editor </editors/dope_sheet/modes/action>`
- :doc:`Shape Key Editor </editors/dope_sheet/modes/shape_key>`
- :doc:`Grease Pencil </editors/dope_sheet/modes/grease_pencil>`
- :doc:`Mask </editors/dope_sheet/modes/mask>`
- Cache File: originally meant to show the baked animation data in :doc:`/files/import_export/alembic`
  files, but never implemented.


Main Region
===========

The Dope Sheet Editor shows a stack of :doc:`channels </editors/graph_editor/channels/index>`
(animatable properties), and for each channel, a series of keyframes laid out along the time axis.

.. figure:: /images/editors_dope-sheet_introduction_types.png

   The Dope Sheet Editor with object channels.

Keyframes can take on various colors and shapes:

.. list-table::
   :widths: 20 80

   * - Gray
     - Unselected
   * - Yellow
     - Selected
   * - Other colors
     - Custom keyframe tag set by the user (:menuselection:`Key --> Keyframe Type`)
   * - Diamond
     - Free Keyframe Handle (:menuselection:`Key --> Handle Type`)
   * - Round
     - Auto-Clamped Keyframe Handle
   * - Circle
     - Automatic Keyframe Handle
   * - Square
     - Vector Keyframe Handle
   * - Rhombus
     - Aligned Keyframe Handle
   * - Gray bar between keys
     - Held key (the two keyframes are identical)
   * - Green line between keys
     - The curve segment uses custom interpolation (:menuselection:`Key --> Interpolation Mode`)
   * - Upwards arrow
     - Local maximum in curve (visible if :menuselection:`View --> Show Curve Extremes` is enabled)
   * - Downwards arrow
     - Local minimum in curve

Keyframes can be selected by clicking and moved by dragging. See the :ref:`Select <dopesheet-select-menu>`
and :ref:`Key <dopesheet-key-menu>` menus for more options.
