
*******
Options
*******

Auto Normalize
   Ensures that all deforming vertex groups add up to one while painting.
   When this option is turned off, then all weights of a point can have any value between 0 and 1.
   However, when vertex groups are used as deform groups for character animation
   then Blender always interprets the weight values relative to each other.
   That is, Blender always does a normalization over all deform bones.
   Hence in practice it is not necessary to maintain a strict normalization and
   further normalizing weights should not affect animation at all.

   This option works most intuitively when used to maintain normalization while
   painting on top of weights that are already normalized with another tool.
