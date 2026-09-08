.. _command_line-index:

#######################################
  Using Blender From The Command Line
#######################################

The *Console Window*, also called a *Terminal*, is an operating system text window that displays
messages about Blender's operations, status, and internal errors.

When Blender is manually started from a terminal,
Blender output is shown in the *Console Window* it is started from.

Use Cases:

- For :ref:`rendering animation <command_line-render>`.
- For automation and batch processing which require launching Blender
  with different :ref:`arguments <command_line-args>`.
- For Python development, to see the output of the ``print()`` function.
- If Blender exits unexpectedly, the messages may indicate the cause or error.
- When troubleshooting, to see the output of ``--debug`` messages.

See: :ref:`command_line-launch-index`
for specific instructions on launching Blender from the command line.

.. tip::

   Closing the *Console Window* will also close Blender, losing any unsaved work.


Launching from the Command Line
===============================

.. toctree::
   :hidden:

   launch/index.rst

- :doc:`launch/linux`
- :doc:`launch/macos`
- :doc:`launch/windows`


Arguments
=========

.. toctree::
   :hidden:

   Arguments <arguments.rst>

- :ref:`command-line-args-render-options`
- :ref:`command-line-args-cycles-render-options`
- :ref:`command-line-args-format-options`
- :ref:`command-line-args-animation-playback-options`
- :ref:`command-line-args-window-options`
- :ref:`command-line-args-python-options`
- :ref:`command-line-args-network-options`
- :ref:`command-line-args-logging-options`
- :ref:`command-line-args-debug-options`
- :ref:`command-line-args-gpu-options`
- :ref:`command-line-args-misc-options`


Sub-Commands
============

.. toctree::
   :maxdepth: 2

   extension_arguments.rst


Workflows
=========

.. toctree::

   render.rst
