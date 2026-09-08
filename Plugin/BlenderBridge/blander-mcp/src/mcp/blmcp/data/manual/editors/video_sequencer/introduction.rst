.. index:: Editors; Video Sequencer

************
Introduction
************

The Video Sequencer allows you to place images, videos, sounds, and scenes
on a timeline and combine them into a new video. This section only describes its UI;
to read more about its usage, see the :doc:`Video Editing </video_editing/index>` section.


Editor Layout
=============

The Video Sequencer is composed of multiple regions.
They are described in more detail in the next sections.
Figure 1 shows the combined *Sequencer & Preview* view type:

.. figure:: /images/editors_vse_overview.svg

   Figure 1: The Video Sequencer Editor shown in the Sequencer & Preview view type.

Header
   Contains menus and buttons for interacting with the editor.
   The header changes slightly depending on the selected view type (see below).
Footer
   Contains menus and buttons for interacting with animation playback.
Preview
   Shows the output of the Sequencer at the time of the Playhead.
Sequencer
   Shows a timeline for managing the montage of strips.
Sidebar
   Shows the properties of the active strip.
   It's divided into panels and tabs. Toggle on or off with :kbd:`N`.
Toolbar
   Shows a list of tools. Toggle on or off with :kbd:`T`.


.. _bpy.types.SpaceSequenceEditor.view_type:

View Types
==========

The Video Sequencer has three view types which can be
changed using the View Type selector (see figure 1; top left).

.. figure:: /images/editors_vse_view_types.svg

   Figure 2: Three view types for the Video Sequence Editor

Sequencer
   View timeline and strip properties.
Preview
   View preview window and preview properties.
Sequencer & Preview
   Combined view of preview and timeline and their properties.

.. tip::

   Rather than having one Video Sequencer in the *Sequencer & Preview* mode, it can be more
   useful to have one in the *Sequencer* mode and another in the *Preview* mode,
   the reason being that *Sequencer & Preview* lacks most of the *Preview* tools.
   Blender's default *Video Editing* workspace offers this layout.


Performance
===========

Playback performance can be improved in several ways.

The method with the most impact is to allow the Video Sequencer to cache generated frames.
There are two levels of cache: a memory cache, which is enabled by default
(and can be enlarged if RAM allows), and a disk cache, which is slower but has more capacity.
Both of these can be configured in the :ref:`Preferences <prefs-system-video-sequencer>`.

Another way to improve performance is by using :ref:`Strip Proxies <bpy.types.StripProxy>`.
These are copies of source images and videos with a lower resolution and/or quality,
making them faster to load than the originals.
