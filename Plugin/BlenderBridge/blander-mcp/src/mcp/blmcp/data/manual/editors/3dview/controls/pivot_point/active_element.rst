
**************
Active Element
**************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Location:  :menuselection:`Header --> Transform Pivot Point --> Active Element` (:bl-icon:`pivot_active`)
   :Shortcut:  :kbd:`Period`

Places the pivot point at the active element, which is the element that was selected most recently.


In Object Mode
==============

When in Object Mode,
rotation and scaling happen around the origin of the active object,
which is the element with a lighter outline than the others.

The effect of the pivot point is shown in the image below, where the active object (the cube)
remains in the same location while the others move.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_object-mode-rotation.png
   :align: center

   Starting point, rotation, and scaling.


In Edit Mode
============

When in Edit Mode, rotation and scaling happen around the centerpoint of
the active element, which is the element with a white outline.
That centerpoint remains in the same location while everything else
is transformed around it.

The image below illustrates rotation around the active vertex,
edge, and face. Each time, the active element rotates in place,
while the others "orbit" around it. In the case of vertices,
the active vertex is not changed at all, as a vertex on its own
is just a point that has no concept of rotation.

.. figure:: /images/editors_3dview_controls_pivot-point_active-element_edit-mode-multiple.png
   :align: center

   Left column: starting situation, right column: after rotation.
