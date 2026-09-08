
*****
macOS
*****

Quick Start
===========

Open the terminal application,
and run the executable within the app bundle, with commands like this:

.. code-block:: sh

   cd /Applications/Blender.app/Contents/MacOS
   ./Blender

If you need to do this often, you can add this directory to your ``PATH``.

For that you can run the following procedure:

#. Open up a Terminal.
#. Run the following command: ``sudo nano /etc/paths``.
#. Enter your password, when prompted.
#. Go to the bottom of the file, and enter ``/Applications/Blender.app/Contents/MacOS``.
#. Enter :kbd:`Ctrl-X` to quit.
#. Enter :kbd:`Y` to save the modified buffer.

If you then open a new terminal, the following command will work:

.. code-block:: sh

   Blender


Details
=======

macOS uses "files" with the ``.app`` extension called *applications*.
These files are actually folders that appear as files in Finder.
In order to run Blender you will have to specify that path to the Blender executable inside this folder,
to get all output printed to the terminal.
You can start a terminal from :menuselection:`Applications --> Utilities`.
The path to the executable in the ``.app`` folder is ``./Blender.app/Contents/MacOS/Blender``.

If you have Blender installed in the Applications folder, the following command can be used:

.. parsed-literal:: /Applications/Blender.app/Contents/MacOS/Blender

.. figure:: /images/advanced_command-line_launch_macos_mac.png

   Starting Blender from a macOS console window.
