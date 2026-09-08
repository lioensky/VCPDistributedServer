.. _bpy.types.BlendTexture:

*****
Blend
*****

The Blend texture generates a smoothly interpolated progression.
This is one of the most frequently used procedural textures.
You can use blend textures to blend other textures together (with *Stencil*),
or to create nice effects (especially with the *Mapping: Normal* trick).

.. note::

   Remember that if you use a ramp to create a custom blending, you may have to use *No RGB*,
   if the *Mapping* value needs an intensity input.

.. figure:: /images/render_materials_legacy-textures_types_blend_panel.png

   Blend Texture panels.


Options
=======

Progression
   Profile of blend.

   Linear
      A linear progression.

Quadratic
   A quadratic progression.
Easing
   A flowing, nonlinear progression.
Diagonal
   A diagonal progression.
Spherical
   A progression with the shape of a three-dimensional ball.
Quadratic Sphere
   A quadratic progression with the shape of a three-dimensional ball.
Radial
   A radial progression: *Horizontal* / *Vertical*.
   The direction of the progression is flipped a quarter turn.
