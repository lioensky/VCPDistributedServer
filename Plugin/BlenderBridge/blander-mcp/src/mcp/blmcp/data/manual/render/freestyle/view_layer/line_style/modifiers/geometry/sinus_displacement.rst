.. _bpy.types.LineStyleGeometryModifier_SinusDisplacement:

******************
Sinus Displacement
******************

The *Sinus Displacement* modifier adds a sinusoidal displacement to the stroke.

Wavelength
   How wide the undulations are along the stroke.
Amplitude
   How high the undulations are across the stroke.
Phase
   Allows "offsetting" ("moving") the undulations along the stroke.

   .. tip::

      The undulations this modifier produces look exactly the same at a Phase of ``0``
      and any positive or negative multiple of the ``Wavelength`` set on the modifier.
      This can be used for rendering short video sequences with wavy lines
      that can then be seamlessly looped without any visual jumps in the undulations along the line.

.. figure:: /images/render_freestyle_parameter-editor_line-style_modifiers_geometry_sinus-displacement_example.png
   :width: 50%
   :align: center

   Sinus Displacement modifier demo by T.K.
   (`blend-file <https://archive.blender.org/wiki/2015/index.php/File:Toycar_Sinus.zip>`__).
