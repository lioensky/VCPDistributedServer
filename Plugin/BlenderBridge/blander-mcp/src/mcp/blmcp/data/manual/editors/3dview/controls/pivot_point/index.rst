.. _bpy.types.ToolSettings.transform_pivot_point:
.. _pivot-point-index:

#########################
  Transform Pivot Point
#########################

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Location:  :menuselection:`Header --> Transform Pivot Point`
   :Shortcut:  :kbd:`Period`

The *Pivot Point* determines the location of the
:doc:`Object Gizmo </editors/3dview/display/gizmo>`.
Changing this location can make it easier to perform
transformations around the point you want.

.. figure:: /images/editors_3dview_controls_pivot-point_index_demo.png
   :align: center

   With the default "Median Point" pivot point (left) it's tricky to
   bring the second wheel spoke into place, but with "3D Cursor" (right)
   it's easy.


The Pivot Point can be changed using a selector in the 3D Viewport's header:

.. figure:: /images/editors_3dview_controls_pivot-point_index_popover.png


Pivot Types
===========

.. toctree::
   :maxdepth: 2

   bounding_box_center.rst
   3d_cursor.rst
   individual_origins.rst
   median_point.rst
   active_element.rst
