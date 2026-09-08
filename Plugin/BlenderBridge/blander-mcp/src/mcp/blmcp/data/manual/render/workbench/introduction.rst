
************
Introduction
************

The Workbench Engine is a render engine optimized for fast rendering during modeling and animation preview.
It is not intended to be a render engine that will render final images for a project.
Its primary task is to display a scene in the 3D Viewport when it is being worked on.

.. note::

   While it is not intended to be used for final renders,
   the Workbench render engine can be selected as the *Render Engine* in the Render properties.

By default the 3D Viewport uses Workbench to shade and light objects.
Unlike other render engines such as EEVEE or Cycles, the Workbench engine does not use shader nodes.
Instead, shading settings can be tweaked in the 3D Viewport's :doc:`Shading popover </editors/3dview/display/shading>`
or the render properties when doing final renders.

Workbench supports assigning random colors to objects to make each visually distinct.
Other coloring mechanisms also exist, including; materials, Color Attributes, and textures.

Workbench also has an X-ray mode to see through objects,
along with cavity and shadow shading to help display details in objects.
Workbench supports several lighting mechanisms including studio lighting and MatCaps.

The image below is an excellent example of the Workbench engine's capabilities
using random coloring and shadows to show the details of the model.

.. figure:: /images/render_workbench_introduction_example.png

   Workbench example.
