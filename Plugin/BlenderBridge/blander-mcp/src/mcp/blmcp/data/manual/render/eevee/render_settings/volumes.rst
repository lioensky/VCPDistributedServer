.. _bpy.types.SceneEEVEE.volumetric:

*******
Volumes
*******

.. reference::

   :Panel:     :menuselection:`Properties --> Render --> Volumes`

EEVEE simulates volumetric scattering by evaluating all volume objects inside the view frustum.

To achieve this, EEVEE uses several 3D textures which have a high video memory usage.
The texture dimensions can be tweaked using the *Resolution* and *Steps* parameters.

Resolution
   Controls the quality of the volumetric effects. Lower resolution increases video memory usage and quality.

Steps
   Number of steps to compute volumetric effects. Higher count increases video memory usage and quality.
   These samples are distributed along the view depth (view Z axis).

Distribution
   Blend between linear and exponential sample distribution. Higher values put more samples near the camera.

Max Depth
   Maximum surface intersection count used by accurate volume intersection method.
   Will create artifacts if it is exceeded.


Custom Range
============

When working with volume objects, EEVEE automatically computes the best depth range where to compute
the volume sampling and lighting.
In certain situations, this isn't enough and produces sub-optimal sampling which increases noise.
This is particularly the case when using a volume shader inside the *World* or when working with large
number of volume objects.
The custom depth range can be enabled to restrict the computation of volumes to a certain range along
the camera depth and thus increase precision.

Start
   Start distance of the volumetric effect.

End
   End distance of the volumetric effect.

.. seealso:: :ref:`Limitations <eevee-limitations-volumetrics>`.
