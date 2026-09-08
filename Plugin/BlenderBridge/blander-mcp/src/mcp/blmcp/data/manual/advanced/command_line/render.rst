.. _command_line-render:

*******************************
Rendering From The Command Line
*******************************

In some situations we want to increase the render speed,
access Blender remotely to render something or build scripts that use the command line.

One advantage of using the command line is that we do not need a graphical display
(no need for X server on Linux for example)
and consequently we can render via a remote shell (typically SSH).

- See :doc:`Command Line Arguments </advanced/command_line/arguments>`
  for a full list of arguments
  (for example to specify which scene to render, the end frame number, etc.), or simply run:

.. code-block:: sh

   blender --help

- See :ref:`Command Line Launching <command_line-launch-index>`
  for specific instructions on launching Blender from the command line.

.. note::

   Arguments are executed in the order they are given!

   The following command will not work, since the output and extension are set after Blender is told to render:

   .. code-block:: sh

      blender -b file.blend -a -x 1 -o //render

   The following command will behave as expected:

   .. code-block:: sh

      blender -b file.blend -x 1 -o //render -a

   **Always** position ``-f`` or ``-a`` as the last arguments.


Single Image
------------

.. code-block:: sh

   blender -b file.blend -f 10

``-b``
   Render in the background (without UI).
``file.blend``
   Path to the blend-file to render.
``-f 10``
   Render only the 10th frame.

.. code-block:: sh

   blender -b file.blend -o /project/renders/frame_##### -F OPEN_EXR -f -2

``-o /project/renders/frame_#####``
   Path of where to save the rendered image, using five padded zeros for the frame number.
``-F OPEN_EXR``
   Override the image format specified in the blend-file and save to an OpenEXR image.
``-f -2``
   Render only the second last frame.

.. warning::

   Arguments are case sensitive! ``-F`` and ``-f`` are not the same.


Animation
---------

.. code-block:: sh

   blender -b file.blend -a

``-a``
   Render the whole animation using all the settings saved in the blend-file.

.. code-block:: sh

   blender -b file.blend -E CYCLES -s 10 -e 500 -t 2 -a

``-E CYCLES``
   Use the "Cycles Render" engine.
   For a list of available render engines, run ``blender -E help``.
``-s 10 -e 500``
   Set the start frame to ``10`` and the end frame to ``500``.
``-t 2``
   Use only two threads.


Cycles
------

In addition to the options above, which apply to all render engines,
Cycles has additional options to further control its behavior.
See :ref:`Cycles Render Options <command-line-args-cycles-render-options>`
