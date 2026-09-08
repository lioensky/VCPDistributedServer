
**********************
Selection & Visibility
**********************

Selection Masking
=================

If you have a complex mesh, it is sometimes not easy to paint on the intended vertices.
Suppose you only want to paint on a small area of the Mesh and keep the rest untouched.
This is where "selection masking" comes into play. When this mode is enabled,
a brush will only paint on the selected vertices or faces.
The option is available from the header of the 3D Viewport
(see icons surrounded by the yellow frame):

.. figure:: /images/sculpt-paint_brush_introduction_select.webp

   You can choose between *Face Selection masking* (left button), *Vertex
   selection masking* (middle button), and *Bone selection* (right button). The
   latter is only available when the mesh has an Armature modifier.

Selection masking has some advantages over the default paint mode:

- The original mesh edges are shown, even when modifiers are active.
- You can select and deselect faces instead without the need to switch to Edit Mode.


Details About Selecting
-----------------------

The following standard selection operations are supported:

- :kbd:`Alt-LMB` -- Single faces
- :kbd:`Shift-Alt-LMB` -- Select more or remove them from the selection.
- :kbd:`A` -- All faces, :kbd:`A A` to deselect.
- :kbd:`B` -- Box selection.
- :kbd:`C` -- Circle select with brush.
- :kbd:`Ctrl-I` -- Invert selection.
- :kbd:`L` -- Pick linked (under the mouse cursor).
- :kbd:`Ctrl-L` -- Select linked.
- :kbd:`Ctrl-NumpadPlus` -- Extend Selection
- :kbd:`Ctrl-NumpadMinus` -- Shrink Selection
- :kbd:`Alt-LMB` -- Loop Select


Vertex Selection Masking
------------------------

.. reference::

   :Mode:      Vertex and Weight Paint Modes
   :Header:    :menuselection:`Vertex Selection`
   :Shortcut:  :kbd:`2`

In this mode you can select one or more vertices and then paint only on the selection.
All unselected vertices are protected from unintentional changes.

.. figure:: /images/sculpt-paint_brush_introduction_vertex-select.png

   Vertex Selection masking.


.. _bpy.types.Mesh.use_paint_mask:

Face Selection Masking
----------------------

.. reference::

   :Mode:      Texture, Vertex, and Weight Paint Modes
   :Header:    :menuselection:`Paint Mask`
   :Shortcut:  :kbd:`1`

The *Face Selection masking* allows you to select faces and limit the paint
tool to those faces, very similar to Vertex selection masking.

.. figure:: /images/sculpt-paint_brush_introduction_face-select.png

   Face Selection masking.

.. The visual example needs to be updated. Ideally show hard edges on painted face corners.

Hide/Unhide Faces
-----------------

.. figure:: /images/sculpt-paint_brush_introduction_face-select-hidden.png

   Hidden faces.

You also can hide selected faces as in Edit Mode with the keyboard Shortcut :kbd:`H`,
then paint on the remaining visible faces and finally unhide the hidden faces again by using
:kbd:`Alt-H`.


Hide/Unhide Vertices
--------------------

You cannot specifically hide only selected faces in vertex mask selection mode.
However, the selection is converted when switching selection modes.
So a common trick is to:

#. Switch to Face selection mask mode to have the selection converted to faces.
#. Refine your selection next or just hide the faces.
#. Switch back to Vertex Selection mask mode.

Hiding faces will make sure that vertices that belong to visible faces remain visible.


.. _clipping_region:

The Clipping Region
-------------------

To constrain the paint area further you can use the *Clipping Region*.
Press :kbd:`Alt-B` and :kbd:`LMB`-drag a rectangular area.
The selected area will be "cut out" as the area of interest.
The rest of the 3D Viewport gets hidden.

.. figure:: /images/sculpt-paint_brush_introduction_border-select.png

   The Clipping Region is used to select interesting parts for local painting.

.. This visual example could include the (Clipped) text info overlay

You make the entire mesh visible again by pressing :kbd:`Alt-B` a second time.

All paint tools that use the view respect this clipping, including box select, and of course brush strokes.

There are two helpful reminders that a Clipping Region is used:

#. The clipping region is drawn as a gray box in the 3D Viewport
#. The Text Info overlay will state that the perspective is "Clipped"


.. _bpy.ops.paint.vert_select_linked:

Select Linked
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Linked --> Linked`
   :Shortcut:  :kbd:`Ctrl-L`, :kbd:`Shift-L`

Select geometry connected to already selected elements.
This is often useful when a mesh has disconnected, overlapping parts,
where isolating it any other way would be tedious.
Pressing :kbd:`Shift-L` will deselect linked any linked elements.

With :kbd:`L` you can also select connected geometry directly under the cursor.
