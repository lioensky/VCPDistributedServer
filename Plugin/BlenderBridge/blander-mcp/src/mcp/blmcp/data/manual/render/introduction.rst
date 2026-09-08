
************
Introduction
************

Rendering is the process of turning a 3D scene into a 2D image.
Blender includes three render engines with different strengths:

- :doc:`EEVEE </render/eevee/index>` is a physically based realtime renderer.
- :doc:`Cycles </render/cycles/index>` is a physically based path tracer.
- :doc:`Workbench </render/workbench/index>` is designed for layout, modeling and previews.

More renderers from third-party developers are available as
:doc:`add-ons </editors/preferences/extensions>`.
Each renderer has its own render settings to control render quality and performance.

What the render looks like is defined by :doc:`cameras </render/cameras>`,
:doc:`lights </render/lights/index>` and :doc:`materials </render/materials/index>`.
These are shared between EEVEE and Cycles, however some features are only supported in one or the other.

Renders can be split up into :doc:`layers and passes </render/layers/index>`, which can then
be :doc:`composited </compositing/index>` together for creative control, or to combine
with real footage. :doc:`Freestyle </render/freestyle/index>` can be used to
add non-photorealistic line rendering.

Blender supports interactive 3D viewport rendering for all render engines, for quick iteration
on lighting and shading. Once this is done, the final quality image or animation can
be rendered and :doc:`output </render/output/index>`.
