
*******************
Bounding Box Center
*******************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Location:  :menuselection:`Header --> Transform Pivot Point --> Bounding Box Center` (:bl-icon:`pivot_boundbox`)
   :Shortcut:  :kbd:`Period`

In this mode, the pivot point lies at the center of the bounding box, which is a box that's
wrapped as tightly as possible around the selection while still being aligned to the world axes.


In Object Mode
==============

The pivot point becomes the center of the bounding box *around the selected objects'
origin points*, not their geometry.

This means that, if you have a single object selected, the pivot point is the same
as the object's :doc:`origin point </scene_layout/object/origin>` -- which can be customized
and doesn't have to be in the center. In the example below, the orange rectangle
has it in a corner instead.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_object-mode_single.png
   :align: center

   Single object rotation.

If you have multiple objects selected, the pivot point becomes the center
of an imaginary box around their origins.

The image below shows the difference between Bounding Box Center
and :doc:`/editors/3dview/controls/pivot_point/median_point`.
The latter calculates the average position of the origins,
meaning that the pivot point shifts towards the area with the most objects.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_object-mode_multiple.png
   :align: center

   Difference between "Bounding Box Center" (left) and "Median Point" (right).


In Edit Mode
============

The pivot point becomes the center of the bounding box around the selected mesh elements.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_edit-mode-rotation.png
   :align: center

   The effects of rotation in different mesh selection modes.
   The pivot point is shown by a yellow circle.

Median Point may again give a different result.

.. figure:: /images/editors_3dview_controls_pivot-point_bounding-box-center_median-point.png
   :align: center

   Difference between "Bounding Box Center" (left) and "Median Point" (right).
