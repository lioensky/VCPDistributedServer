.. highlight:: sh

**********
Contribute
**********

This guide uses French (``fr``) as an example, but other
`language codes <https://www.gnu.org/software/gettext/manual/html_node/Usual-Language-Codes.html>`__ can be used.
Replace ``/fr`` in this guide with the code for your desired language.

The currently available languages can be checked on the
`online translation interface <https://translate.blender.org/projects/blender-manual/manual/>`__
or in the `underlying git repository <https://projects.blender.org/blender/blender-manual-translations>`__.


Simple Contribution
===================

The preferred way to contribute to the translation effort is via the
`web-based interface <https://translate.blender.org/projects/blender-manual/manual>`__, currently hosted on Weblate.

Suggestions for translations can be contributed without logging in. They will be reviewed by the translation team
before being published.

Weblate also provides tools such as the
`glossary <https://translate.blender.org/projects/blender-manual/glossary/>`__ to improve translation consistency.


Advanced Operations
===================

If the web-based interface does not suit your needs, PO-files can be downloaded, edited locally, and uploaded back to
the platform.

.. warning::

   Conflicts may arise if updates occur while editing locally. Resolving conflicts manually will be required. Direct
   commits to the translation repository are no longer permitted.

.. note::

   Uploading or integrating PO files can take several minutes. If a server timeout error appears after ten minutes,
   refresh the page to confirm whether the upload succeeded.


Installing
----------

Before proceeding with translation tasks, ensure the manual builds correctly by following the
:ref:`Getting Started <about-getting-started>` section.


Language Files
^^^^^^^^^^^^^^

Run the following command from the manual's root directory::

   make checkout_locale

You will be prompted to specify the language folder to download. For example, type ``fr`` for French and press
:kbd:`Return`. The command creates a ``locale/fr`` subdirectory after downloading.

Example directory structure:

You should have a directory layout like this::

   blender-manual
      |- locale/
      |  |- fr/
      |  |  |- LC_MESSAGES/
      |- manual/

.. note::

   When using Git from the command line, switch to the ``locale`` directory for updates instead of the
   ``blender-manual`` directory.

Alternatively, download the PO files directly from Weblate by navigating to the ``Files`` menu on the language's page.


PO-File Editor
^^^^^^^^^^^^^^

To edit the PO files, install a PO-file editor to modify the translation files. `Poedit <https://poedit.net/>`__ is
recommended, but other editors are also suitable.


Building with Translations
--------------------------

To build the manual with translations applied run the following commands in a terminal:

- **Linux/macOS**::

     make -e BF_LANG=fr

- **Windows**::

     set BF_LANG=fr
     make html


Editing Translation Files
-------------------------

The PO files in the ``LC_MESSAGES`` folder include:

- ``blender_manual.po``: The main file containing user manual translations.
- ``sphinx.po``: A smaller file for translating the website theme.


#. Use the PO editor to open these files. Each entry represents a section of the manual.
#. Translate any untranslated strings using the input field provided by the editor.
#. Save changes and upload the modified ``.po`` files back to Weblate.

.. tip::

   Sort entries in the editor by source or translation status to make navigation easier.

.. important::

   Build the manual after translating to check for syntax errors, which will appear as warnings will appear during the
   build process.


Maintenance
-----------

.. _translations-fuzzy-strings:

Keeping Track of Fuzzy Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the manual is updated, outdated translations are marked as fuzzy. To track these run::

   make report_po_progress

For a detailed report, run::

   python tools/translations/report_translation_progress.py locale/fr/

This lists files with fuzzy or empty strings. For more options, see::

   python tools/translations/report_translation_progress.py --help


Updating PO Files
^^^^^^^^^^^^^^^^^

Administrators regularly update PO files to match the latest English manual (typically weekly). The last update can be
checked on the
`Blender Manual Translations <https://projects.blender.org/blender/blender-manual-translations>`__ project page.

Translators can update files locally using::

   make update_po

However, uploading these files to Weblate is not permitted.

.. seealso::

   :doc:`/contribute/translate_manual/add_language`
