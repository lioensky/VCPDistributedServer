
******************
Individual Origins
******************

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Location:  :menuselection:`Header --> Transform Pivot Point --> Individual Origins` (:bl-icon:`pivot_individual`)
   :Shortcut:  :kbd:`Period`

While the other pivot point modes transform the whole selection around one point,
Individual Origins transforms each item around itself.

In Object Mode
==============

Each object gets transformed around its :doc:`origin </scene_layout/object/origin>`,
which is a point that can be chosen freely and doesn't have to be in the center.
In the example below, the orange rectangle has it in a corner instead.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_rotation-around-center.png
   :align: center

   Rotation around individual origins.

The images below compare Individual Origins to :doc:`/editors/3dview/controls/pivot_point/median_point`.


.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_objects-rotate.png
   :align: center

   Starting situation, rotation around Individual Origins, rotation around Median Point.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_objects-scale.png
   :align: center

   Starting situation, scaling using Individual Origins, scaling using Median Point.


In Edit Mode
============

Each selected element is transformed around its own centerpoint.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_rotation-faces.png
   :align: center

   Starting situation, rotation around Individual Origins, rotation around Median Point.

.. figure:: /images/editors_3dview_controls_pivot-point_individual-origins_scale-individual-faces.png
   :align: center

   Starting situation, scaling using Individual Origins, scaling using Median Point.

When you transform adjacent faces or edges, they are treated as a single element
(meaning they don't become disconnected).
