
**********
Rigid Body
**********

.. _bpy.ops.rigidbody.mass_calculate:

Calculate Mass
==============

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Rigid Body --> Calculate Mass`

Calculate mass values for rigid body objects based on their volume and density.
The volume is calculated automatically, the density needs to be given based on the object you want to simulate.

Material Preset
   A list of preset density values for real-world materials,
   if a material is not given you can research the density and use the *Custom* preset to input the density manually.

Density
   When the *Custom* *Material Preset* is selected, this is the input density, in kg/m\ :sup:`3`, to use.
