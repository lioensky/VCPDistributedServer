.. highlight:: sh

*******************
Building the Manual
*******************

Converting the RST-files into pretty HTML pages is simple.

Open a terminal or Command Prompt in the ``~/blender-manual`` directory and simply run::

   make

.. tip::

   On Microsoft Windows you can simply open the ``make.bat`` file to easily run the command without having to open the
   Command Prompt and typing commands.

This is the command you should use when building the docs, however, other commands are available by typing ``make
help``. This command will convert the RST-files into HTML pages and automatically open your default web browser to
view the result. The command will continue to run and watch for changes made to the RST-files and refresh the HTML
pages as necessary.

.. note::

   The converted pages can also be viewed manually by browsing the build directory: ``~/blender-manual/build/html``.
   For example to open the home page, open ``build/html/index.html`` to read the manual.

The building process may take several minutes the first time (or after any major changes), but for subsequent changes
it should only take a few seconds.
