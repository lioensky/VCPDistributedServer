
***********
Relax Slide
***********

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

This brush deforms the topology of the mesh
while minimizing changes to the geometrical shape of the mesh.
By default it will drag geometry, but this can be changed in the *Deformation* settings.

This brush is especially useful for redistributing topology to areas that require more detail,
or sliding geometry to somewhere where they should be.

Holding :kbd:`Shift` changes the brush effect to Relax geometry,
creating an even distribution of topology.


Brush Settings
==============

General
-------

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.


Unique
------

.. _bpy.types.Brush.slide_deform_type:

Deformation
   Deformation type that is used by the brush.

   :Drag: Slides the topology of the mesh in the direction of the stroke.
   :Pinch: Slides the topology of the mesh towards the center of the stroke.
   :Expand: Slides the topology of the mesh away from the center of the stroke.
