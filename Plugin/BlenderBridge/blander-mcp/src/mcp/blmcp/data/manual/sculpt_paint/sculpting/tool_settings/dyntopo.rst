.. _bpy.ops.sculpt.dynamic_topology_toggle:

*******
Dyntopo
*******

.. reference::

   :Mode:      Sculpt Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Dyntopo`

Dynamic Topology (aka Dyntopo) can be toggled with the checkbox.
With dynamic topology active, most brushes will subdivide the mesh during the stroke.

For a general explanation of dynamic topology, visit
the :doc:`Introduction </sculpt_paint/sculpting/introduction/adaptive>`.

.. _bpy.types.Sculpt.detail_size:
.. _bpy.types.Sculpt.constant_detail_resolution:
.. _bpy.types.Sculpt.detail_percent:
.. _bpy.ops.sculpt.dyntopo_detail_size_edit:

Detail Size/Percentage, Resolution :kbd:`R`
   Each Detail Type's detail is set here. Depending on the Detail Type being used
   this property will rather show as a pixel count (px), or percentage.

   :kbd:`R` allows you to interactively set the detail, with a preview of the detail's density in the 3D Viewport.

   :bl-icon:`eyedropper` Sample Detail Size
      When using *Constant Detail*, it is possible to sample the detail value of a certain mesh area
      by clicking the pipette icon next to the detail setting and then clicking on the area.

      .. More on shortcut. Shift for precision. Ctrl for sampling. Only available for constant and manual size.

.. _bpy.types.Sculpt.detail_refine_method:

Refine Method
   Setting the option will determine which of the methods will be used when altering the topology.

   :Subdivide Edges:
      Just like the Subdivide tool, this method will only subdivide topology
      to match the detail given.
   :Collapse Edges:
      When topology is too dense, and is smaller than the detail given, edges will
      be collapsed to fit the detail size appropriately.
   :Subdivide Collapse:
      This method combines the two methods, subdividing edges smaller than
      the detail size, and collapsing topology.

.. _bpy.types.Sculpt.detail_type_method:

Detailing
   Dyntopo uses the following different detail methods to create dynamic detail on an object.

   :Relative Detail:
      This method uses a detail size based on the number of pixels, and in turn
      will create topology in that size. Zoom out big details, zoom in small fine details.
   :Constant Detail:
      To keep detail uniform across the entire object, Constant Detail can be used.
      The detail is a divisor of a Blender unit - higher values mean finer details.
   :Brush Detail:
      Giving more control over the topology, with this method you can create topology
      based on the brush size. You can increase and lower topology by resizing the brush itself.
      The detail size is based the size of the brush itself,
      where full detail will create topology the size of the brush radius itself.
   :Manual Detail:
      Similar to constant detail, this value sets a percentage value uniform across the object, but only
      applies detailing changes when using Flood Fill.

.. _bpy.ops.sculpt.detail_flood_fill:

Detail Flood Fill :kbd:`Ctrl-R`
   When using *Constant* or *Manual* *Detailing*, this option is made available,
   allowing you to fill the entire object with a uniform detail, based on the resolution.
