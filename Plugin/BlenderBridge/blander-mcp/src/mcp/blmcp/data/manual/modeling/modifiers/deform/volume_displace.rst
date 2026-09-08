.. index:: Modeling Modifiers; Volume Displace
.. _bpy.types.VolumeDisplaceModifier:

************************
Volume Displace Modifier
************************

.. reference::

   This modifier is only available for :doc:`Volume Objects </modeling/volumes/index>`.

The *Volume Displace* modifier displaces existing volume grids based on a 3D texture.
It uses the RGB color channels of the texture to displace the volume into the X, Y and Z direction.


Options
=======

.. figure:: /images/modeling_modifiers_deform_volume-displace_panel.png
   :align: right
   :width: 300px

   The Volume Displace modifier.

Texture
   The texture that is evaluated at every voxel to determine how far and in what direction to displace.

   .. note::

      Grayscale textures lead to stretching along one axis.
      It's best to use a color texture.

Strength
   Controls how far voxels are displaced.

Sample Radius
   Smaller values result in better performance, but might cut off the volume outside.

Mid Level
   This should be modified if the texture offsets the entire volume in one direction and you want to center it again.
   For performance reasons, the displaced volume should stay close to its original position.


Example
=======

.. figure:: /images/modeling_modifiers_deform_volume-displace_example.png
   :width: 500px

   A volume displaced with various strengths.
