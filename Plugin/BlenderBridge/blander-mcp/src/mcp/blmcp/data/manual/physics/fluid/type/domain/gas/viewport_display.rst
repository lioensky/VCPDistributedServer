
****************
Viewport Display
****************

.. _bpy.types.FluidDomainSettings.display_thickness:

Thickness
   Factor that scales the thickness of the grid that is currently being displayed.

.. _bpy.types.FluidDomainSettings.display_interpolation:

Interpolation
   Interpolation method to use for the visualization of the fluid grid.

   :Linear:
      Linear interpolation between voxels. Gives good smoothness and speed.
   :Cubic:
      Cubic interpolation between voxels. Gives smoothed high quality interpolation, but is slower.
   :Closest:
      No interpolation between voxels. Gives raw voxels.

.. _bpy.types.FluidDomainSettings.slice_per_voxel:

Slice per Voxel
   Determines how many slices per voxel should be generated.


.. _bpy.types.FluidDomainSettings.use_slice:

Slice
=====

Renders only a single 2D section of the domain object.

.. _bpy.types.FluidDomainSettings.slice_axis:

Axis
   :Auto: Adjust slice direction according to the view direction.
   :X/Y/Z: Slice along the X/Y/Z axis.

.. _bpy.types.FluidDomainSettings.slice_depth:

Position
   Position of the slice relative to the length of the respective domain side.

.. _bpy.types.FluidDomainSettings.show_gridlines:

Gridlines :guilabel:`Closest Interpolation Only`
   Display gridlines to differentiate the underlying cells in the current slice of the fluid domain.


.. _bpy.types.FluidDomainSettings.use_color_ramp:

Grid Display
============

Use a specific color map for the visualization of the simulation field.
This comes in handy during debugging or when making more advanced
adjustments to the simulation. For instance, if the actual color of
a fire simulation is barely visible in the viewport then changing
the color profile can help to see the real size of the flame.

.. _bpy.types.FluidDomainSettings.color_ramp_field:

Field
   The simulation field used in the display options (e.g. density, fuel, heat).

   .. list-table:: Comparison of a fire simulation with and without color mapping.

      * - .. figure:: /images/physics_fluid_type_domain_gas_viewport-display_colormapping-1.png

             Slice view of "fire" grid without color mapping.

        - .. figure:: /images/physics_fluid_type_domain_gas_viewport-display_colormapping-2.png

             Slice view of "fire" grid with color mapping.

.. _bpy.types.FluidDomainSettings.color_ramp_field_scale:

Scale
   Scale the selected simulation field by this value.


.. _bpy.types.FluidDomainSettings.show_velocity:

Vector Display
==============

Visualization options for the vector fields.

.. _bpy.types.FluidDomainSettings.vector_display_type:

Display As
   :Streamlines: Choose to display the vectors as "Streamlines".
   :Needle: Choose to display the vectors as "Needles".
   :MAC Grid:
      Choose to display the vector field as "Marker-And-Cell Grid".

.. _bpy.types.FluidDomainSettings.vector_show_mac_x:
.. _bpy.types.FluidDomainSettings.vector_show_mac_y:
.. _bpy.types.FluidDomainSettings.vector_show_mac_z:

 Mac Grid X, Y, Z :guilabel:`Mac Grid`
   Show an individual X/Y/Z component of the MAC grid.

.. _bpy.types.FluidDomainSettings.vector_scale_with_magnitude:

Magnitude :guilabel:`Streamlines or Needle Only`
   Scale the display vectors by the magnitude of the vectors they represent.

.. _bpy.types.FluidDomainSettings.vector_field:

Field
   The vector field represented by the display vectors (e.g. fluid velocity, external forces).

.. _bpy.types.FluidDomainSettings.vector_scale:

Scale
   Scale the vectors by this size in the viewport.


Advanced :guilabel:`Gridlines Only`
===================================

Advanced coloring options for gridlines.

.. _bpy.types.FluidDomainSettings.gridlines_color_field:

Color Gridlines
   :Flags: Color gridlines with flags.
   :Highlight Range:
      :guilabel:`Grid Display Only`
      Highlight the cells with values of the displayed grid within the range.
      Values between the *Lower Bound* and *Upper Bound* (inclusive) are considered to be within the range.

      .. _bpy.types.FluidDomainSettings.gridlines_lower_bound:

      Lower Bound
         Lower bound of the highlighting range.

      .. _bpy.types.FluidDomainSettings.gridlines_upper_bound:

      Upper Bound
         Upper bound of the highlighting range.

      .. _bpy.types.FluidDomainSettings.gridlines_range_color:

      Color
         Color used to highlight the cells.

      .. _bpy.types.FluidDomainSettings.gridlines_cell_filter:

      Cell Type
         Choose to highlight only a particular type of cells.
