
*******
Volumes
*******

Volume rendering is used to render various effects that cannot be represented by hard surfaces alone.

- Smoke, fire or clouds are set up using a volume object or fluid simulation,
  with only a volume shader.
- Meshes can also be used to create such shapes by removing the default surface shader
  and using a volume shader with the mesh shape defining the volume bounds
  and textures defining the volume density.
- Mist is created with a volume shader for the world,
  or with a large mesh object encompassing the scene.
- Absorption in glass is simulated by combining a glass surface shader with refraction
  and a volume absorption shader for the interior of the object.


Shading
=======

Principled Volume
-----------------

:doc:`Principled Volume </render/shader_nodes/shader/volume_principled>`
is a physically-based volume shader that can be used to create a wide range of volume materials.
It supports scattering, absorption and emission in one easy to use node.
Fire can be rendered with blackbody emission.

.. figure:: /images/render_materials_components_volume_principled.jpg
   :align: center

   Smoke and fire rendered with Principled Volume shader.


Volume Components
-----------------

For more control, volume shading components can be manually combined into a custom shader setup.

- :doc:`Volume Absorption </render/shader_nodes/shader/volume_absorption>`
  will absorb part of the light as it passes through the volume.
  This can be used to shade for example black smoke or colored glass objects, or mixed with the Volume Scatter node.
  This node is similar to the transparent BSDF node,
  it blocks part of the light and lets other light pass straight through.
- :doc:`Volume Scatter </render/shader_nodes/shader/volume_scatter>`
  lets light scatter in other directions as it hits particles in the volume.
  The anisotropy defines in which direction the light is more likely to scatter.
  A value of 0 will let light scatter evenly in all directions (similar to the diffuse BSDF node),
  negative values let light scatter mostly backwards, and positive values let light scatter mostly forward.
  This can be used to shade white smoke or clouds for example.
- :doc:`Emission </render/shader_nodes/shader/emission>`
  will emit light from the volume, for example for fire.

.. figure:: /images/render_materials_components_volume_node.jpg
   :align: center

   Volume Absorption, Scatter and Emission


Attributes
----------

When rendering smoke and fire, volume attributes are used to define the shape and shading of the volume.
The Principled Volume shader will use them by default, while custom volume shaders can use
the Attribute node to get attributes such as density, color and temperature.


Density
-------

All volume shaders have a density input.
The density defines how much of the light will interact with the volume,
getting absorbed or scattered, and how much will pass straight through. For effects such as
smoke you would specify a density field to indicate where in the volume there is smoke and
how much (density bigger than 0), and where there is no smoke (density equals 0).

Volumes in the real world consist of particles,
a higher density means there are more particles per unit volume. More particles means there is
a higher chance for light to collide with a particle and get absorbed or scattered,
rather than passing straight through.


Mesh Volumes
============

Meshes used for volume render should be closed and :term:`Manifold`.
That means that there should be no holes in the mesh.
Each edge must be connected to exactly two faces
such that there are no holes or T-shaped faces
where three or more faces are connected to an edge.

Normals must point outside for correct results.
The normals are used to determine if a ray enters or exits a volume,
and if they point in a wrong direction, or there is a hole in the mesh,
then the renderer is unable to decide what is the inside or outside of the volume.

These rules are the same as for rendering glass refraction correctly.


World Volume
============

A volume shader can also be applied to the world, filling the entire space.

Currently, this is most useful for night time or other dark scenes,
as the world surface shader or sun lights will have no effect if a volume shader is used.
This is because the world background is assumed to be infinitely far away,
which is accurate enough for the sun for example.
However, for modeling effects such as fog or atmospheric scattering,
it is not a good assumption that the volume fills the entire space,
as most of the distance between the sun and the earth is empty space.
For such effects it is be better to create a volume object surrounding the scene.
The size of this object will determine how much light is scattered or absorbed.


Multiple Scattering
===================

Real-world effects such as scattering in clouds or subsurface scattering require many
scattering bounces. However, unbiased rendering of such effects can be noisy, so by default
the number of bounces is zero in Cycles, and no support is available in EEVEE.
The effect you get when rendering with zero volume bounces is what is known as
"single scattering", the effect from more bounces is "multiple scattering".

For rendering materials like skin or milk that require multiple scattering,
subsurface scattering is more efficient and easier to control. Particularly the random walk
method can accurately render such materials.

For materials such as clouds or smoke that do not have a well-defined surface,
volume rendering is required. These look best with many scattering bounces,
but in practice one might have to limit the number of bounces to keep render times acceptable.
