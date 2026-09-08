
*****
Shape
*****

.. reference::

   :Panel:     :menuselection:`Particle System --> Hair Shape`

These settings control the shape of hair curves for rendering.

Strand Shape
   A shape parameter that controls the transition in thickness between the root and tip.
   Negative values make the primitive rounded more towards the top,
   the value of zero makes the primitive linear,
   and positive values make the primitive rounded more towards the bottom.

Diameter Root
   Multiplier of the hair width at the root.
Tip
   Multiplier of the hair width at the tip.
Radius Scale
   Multiplier for the *Root* and *Tip* values. This can be used to change the thickness of the hair.

   .. Particle width scaling relative to the object scale.

Close Tip
   Sets the thickness at the tip to zero, even when using a nonzero tip multiplier.
