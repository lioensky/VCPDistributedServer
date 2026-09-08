
*************
Grease Pencil
*************

This mode lets you adjust the timing of a :doc:`Grease Pencil object's </grease_pencil/introduction>`
animation frames. It is especially useful for blocking out shots.

.. figure:: /images/editors_dope-sheet_grease-pencil_view.png


Channels Region
===============

The Channels region shows the Grease Pencil object in light blue and its
:doc:`layers </grease_pencil/properties/layers>` in gray.
Layers have the following settings:

Opacity
   The layer's :ref:`opacity <bpy.types.GreasePencilLayer.opacity>`.
Use Mask
   Toggle the layer's :ref:`masks <bpy.types.GreasePencilTreeNode.use_masks>` on or off.
Onion Skinning
   Toggle :doc:`onion skinning </grease_pencil/properties/onion_skinning>`.
Visibility (eye icon)
   Toggle layer visibility in the viewport and in render.
Show all keyframes (checkbox)
   When unchecked, the layer gets frozen in its current state, and moving to
   a different keyframe will no longer change its appearance.
Lock (padlock)
   Locked layers can't be edited.


Header
======

Add New Layer
   Adds a layer.
Remove Layer
   Removes the active layer.
Move Layer
   Moves the active layer down/up.

.. _bpy.ops.grease_pencil.layer_isolate:

Isolate Layers (screen icon)
   Toggle whether the active layer is the only one that can be edited and is visible.
Isolate Layers (padlock icon)
   Toggle whether the active layer is the only one that can be edited.


Insert Keyframe
---------------

You can press :kbd:`I` while hovering over the Dope Sheet Editor to insert a keyframe.
It'll create a copy of the active frame if
:ref:`Additive Drawing <bpy.types.ToolSettings.use_gpencil_draw_onback>` is enabled,
and a blank frame otherwise.


Copying Frames
--------------

It is possible to copy frames from one layer to another,
or from object to object, using the *Copy* and *Paste* tools in the *Key* menu.
Note that keyframes will be pasted into selected layers, so make sure you have a destination layer selected.


Main Region
===========

The keyframes can be manipulated like any other data in the *Dope Sheet*.
Interpolated keyframes (alias breakdowns) are visualized as smaller light blue points.


Sidebar
=======

The Sidebar contains a copy of the Grease Pencil :doc:`Layer Properties </grease_pencil/properties/layers>`.
