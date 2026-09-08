
.. highlight:: sh

*****************
Adding a Language
*****************

Preparations
============

If the language you want to translate has not been started by someone else already and you wish to create a set of new
files for the desired language, say 'fr' (French), then you must first use the environment you have created, as guided
in :ref:`Getting Started <about-getting-started>`, in particular
:doc:`/contribute/manual/getting_started/local_editing/install/index` and 
:doc:`/contribute/manual/getting_started/local_editing/build` sections.

This will give you a foundation environment for:

- Creating a new set of translation language from English source.
- Perform ``make`` command to turn translated texts in po files into html files for testing locally.
- Update changes in English texts which have been added by other contributors.

Below examples show the process to create a new set of files for French, language code ``fr``, on Linux platform.
Other platforms might vary slightly but should be mainly the same.

#. `Create a Blender ID <https://id.blender.org/register/>`__ if you have not done so already.
#. Log into `projects.blender.org <https://projects.blender.org/>`__ and
   `Create an Issue <https://projects.blender.org/blender/documentation/issues/new>`__
   requesting for commit access in order to transfer changes to the central repository of the translation team.
#. Open an instance of a console application.
#. Change the current working directory to the directory of ``blender-manual``, where the instance of ``Makefile``
   resides.


Trying the Make Process to Create HTML Files in English
=======================================================

#. Ensure the previous instance of ``build`` directory is removed, if any exists::

      make clean

#. Convert all the ``rst`` files into ``pot`` translation files::

      make gettext

#. Create ``html`` files::

      make html

#. After this, you can actually view the created html files locally
   by opening the ``blender-manual/build/html/index.html`` file.


Creating the Language Entry in the HTML Menu
============================================

#. Create an entry for the language in the html menu by opening file ``./build_files/theme/js/version_switch.js``
   (assuming you are at the ``blender-manual`` subdirectory).
#. Find the table for the languages in ``var all_langs = {..};``.
#. Add the entry: ``"fr": "Fran&ccedil;ais",``, (``"fr": "Français"``). (Notice the Unicode characters.)
#. Commit the updated file::

      git add ./build_files/theme/js/version_switch.js
      git commit -m "HTML: Add French to language menu"

#. Push your changes to the upstream repository::

      git push


Generating the Set of Files for the Target Language
===================================================

#. Check out the current translation repository using the command::

      git clone https://projects.blender.org/blender/blender-manual-translations.git locale

   This will download all language sets available in the repository into the ``locale`` directory of your drive. You
   can go to the ``locale`` directory to see the hidden subdirectory ``.git`` within it, together with directories of
   languages. You'll need to add your own set of files for the language you are trying to translating to.

#. From the ``blender-manual`` directory to generate a set of files for ``fr`` language::

      make update_po

   These files are still in English only, with all ``msgstr`` entries blank.

#. Submit new set of files to the central repository::

      cd locale
      git add fr
      git commit -m "Initial commit language set of files for French"

.. tip::

   - It is recommended you make two environment variables for these directories, in the ``.bashrc`` to make it more
     convenient for changing or scripting batch/shell commands for the process of translation and reviewing results::

        export BLENDER_MAN_EN=$HOME/<directory to make file directory above>/blender-manual
        export BLENDER_MAN_FR=$BLENDER_MAN_EN/locale

   - Newly generated files will contain some placeholders for authors and revision dates etc. If you find the job of
     replacing them repetitive, make use of the script ``change_placeholders.sh`` in the subdirectory
     ``~/blender-manual/tools/util_maintenance``, make a copy of that to your local ``bin`` directory and replace all
     values that were mentioned in the file with your specific details, then after each change to a file, you would do
     following commands to update the file with your personal details, revision date and time, plus generating the
     html files for your language, which you can view using your internet browser::

        $HOME/bin/change_placeholders.sh $BLENDER_MAN_FR
        make -d --trace -w -B -e SPHINXOPTS="-D language='fr'" 2>&1
