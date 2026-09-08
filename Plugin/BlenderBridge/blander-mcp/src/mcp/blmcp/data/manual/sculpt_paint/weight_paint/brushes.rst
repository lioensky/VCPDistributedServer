
*******
Brushes
*******

Brush Types
===========

See :ref:`Brush Type <sculpt-tool-settings-brush-type>`.

Available brush types are listed here, together with brushes from the
*Essentials* asset library using them.


Draw
   Brushes: Paint

   Paints a specified weight over the object.

   Blend
      The brush :term:`Blend Modes` defines in which way the weight value is
      applied to the vertex group while painting.

      Mix
         In this Blending mode the Weight value defines the *target weight*
         that will eventually be reached when you paint long enough on the same
         location of the mesh. And the strength determines how many strokes
         you need to place at the target weight. Note that for strength = 1.0
         the target weight is painted immediately and for Weight = 0.0 the brush just does nothing.
      Add
         In this Blending mode the specified weight value is *added* to the vertex weights.
         The strength determines which fraction of the weight gets added per stroke.
         However, the brush will not paint weight values above 1.0.
      Subtract
         In this Blending mode the specified weight value is *subtracted* from the vertex weights.
         The strength determines which fraction of the weight gets removed per stroke.
         However, the brush will not paint weight values below 0.0.
      Lighten
         In this Blending mode the specified weight value is interpreted as the target weight.
         Very similar to the Mix Blending mode, but only weights below the target weight are affected.
         Weights above the target weight remain unchanged.
      Darken
         This Blending mode is very similar to the Lighten Blending mode.
         But only weights above the target weight are affected.
         Weights below the target weight remain unchanged.
      Multiply
         Multiplies the vertex weights with the specified weight value.
         This is somewhat like subtract, but the amount of removed weight is now
         dependent on the Weight value itself.
      Blur
         Smooths out the weighting of adjacent vertices. In this mode the Weight
         Value is ignored. The strength defines how much the smoothing is applied.

Blur
   Brushes: Blur

   Smooths out the weighting of adjacent vertices. In this mode the Weight
   Value is ignored. The strength defines how much the smoothing is applied.

Average
   Brushes: Average

   Smooths weights by painting the average resulting weight from all weights under the brush.

Smear
   Brushes: Smear

   Smudges weights by grabbing the weights under the brush and "dragging" them.
   This can be imagined as a finger painting tool.
