
***************
Viewport Render
***************

Viewport rendering lets you create quick preview renders from the current viewpoint
(rather than from the active camera, as would be the case with a regular render).

You can use *Viewport Render* to render both images and animations.

Below is a comparison between the Viewport render and a final render using
the Cycles Renderer.

.. list-table:: Model by © 2016 pokedstudio.com

   * - .. figure:: /images/editors_3dview_viewport-render_example-workbench-render.jpg
          :width: 320px

          Viewport render using Solid Mode.

     - .. figure:: /images/editors_3dview_viewport-render_example-eevee-render.jpg
          :width: 320px

          Viewport render using Material Preview Mode.

     - .. figure:: /images/editors_3dview_viewport-render_example-cycles-render.jpg
          :width: 320px

          Full render.

.. note::

   Viewport rendering only works for the Workbench and EEVEE render engines.
   It's not supported for Cycles.

.. tip::

   Disable overlays to get a render without "clutter" like rigs, empties and so on.


Settings
========

For the most part, *Viewport Render* uses the current viewport settings.
Some settings are located in the properties of the render engine
that is used to render the view.

Solid mode uses the render settings of Workbench;
Material Preview mode uses the render settings of EEVEE.

Additionally, some output settings are used too:

- Resolution
- Aspect
- Output path
- File format


Rendering
=========

Activating *Viewport Render* will render from the current active view.
This means that if you are not in an active camera view,
a virtual camera is used to match the current perspective.
To get an image from the camera point of view,
enter the active camera view with :kbd:`Numpad0`.

As with a normal render, you can abort it with :kbd:`Esc`.

.. _bpy.ops.render.opengl:

Render a Still Image
   To render a still image, use :menuselection:`3D Viewport --> View --> Render Viewport Preview`.
Render an Animation
   To render an animation, use :menuselection:`3D Viewport --> View --> Render Playblast`.
Render Keyframes
   To render an animation, but only those frames that have a keyframe, use 
   :menuselection:`3D Viewport --> View --> Render Playblast on Keyframes`. This only renders those frames for which
   the selected objects have an animation key. The other frames are still written to the output, but will simply
   repeat the last-rendered frame.

   For example, when a six-frame animation is rendered, and the selected objects have a key on frames 3 and 5, the
   following frames will be output:

   #. The 1st frame is always rendered.
   #. The 1st frame is repeated because there is no key on this frame.
   #. The 3rd frame is rendered.
   #. The 3rd frame is repeated because there is no key on this frame.
   #. The 5th frame is rendered.
   #. The 5th frame is repeated because there is no key on this frame.

.. tip::

   You can limit the viewport render to a particular region with
   :ref:`Render Regions <editors-3dview-navigate-render-region>`.
