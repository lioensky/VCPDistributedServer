
*******
Options
*******

.. reference::

   :Menu:      :menuselection:`Properties --> Render --> Options` panel.

Backface Culling
   Use backface culling to hide backsides of faces.

X-Ray
   Render the scene transparent. With the slider you can control how
   transparent the scene should appear.

Shadow
   Renders a sharp shadow in the scene.

   Darkness
      Defines how dark the shadow should be rendered. This slider can be adjusted
      between 0 (shadow not visible) and 1 (shadow is black).

   Light Direction
      Controls the direction of the light source that casts the shadows.

   Shadow Shift
      Controls the Shadow termination angle. It can be used to limit self shadowing artifacts.

   Shadow Focus
      Controls the falloff near the edge of the shadow.

Depth of Field
   Use the Depth of Field settings of the active camera in the viewport.
   Only visible when looking through the camera.

   The settings are located on :menuselection:`Properties --> Camera --> Depth of Field` panel.

Outline
   Render the outline of objects in the viewport. The color of the outline can be adjusted.

Specular Highlighting
   Render specular highlights.

   .. note::

      Only available when Lighting is set to *Studio* lighting or when a MatCap
      has been selected that contains a specular pass.

Cavity
   Highlight ridges and valleys in the scene geometry.

   Type
      How to calculate cavities.

      :World: More precise but is slower to calculate.
      :Screen: Fast but does not take the size of the ridges and valleys into account.
      :Both: Use both methods.

   Ridge
      Control the visibility of ridges.

   Valley
      Control the visibility of valleys.
