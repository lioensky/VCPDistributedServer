
************
Introduction
************

EEVEE is Blender's realtime render engine focused on speed and interactivity while achieving the
goal of rendering :abbr:`PBR (Physically Based Rendering)` materials.
EEVEE can be used interactively in the 3D Viewport but also produce high quality final renders.

.. figure:: /images/render_eevee_introduction_viewport.png

   EEVEE in the 3D Viewport -- "Tiger" by Daniel Bystedt.

EEVEE materials are created using the same shader nodes as Cycles, making it easy to render existing
scenes. For Cycles users, this makes EEVEE work great for previewing materials in realtime.

EEVEE is based on rasterization and is not a path tracer.
Instead of computing each ray of light, rasterization determines what surface is visible from the camera.
It then estimates the way light interacts with these surfaces and materials using numerous algorithms.
While EEVEE is designed to use :abbr:`PBR (Physically Based Rendering)` principles,
it is not perfect and Cycles will always provide more physically accurate renders.
For these reasons, EEVEE has a set of :doc:`limitations </render/eevee/limitations/index>`.

.. figure:: /images/render_eevee_introduction_final-render.png

   EEVEE final render -- "Temple" by Dominik Graf.
