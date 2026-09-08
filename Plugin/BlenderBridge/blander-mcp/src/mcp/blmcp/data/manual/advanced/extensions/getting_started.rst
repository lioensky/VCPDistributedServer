.. _extensions-getting_started:
.. index:: Extensions

************************
How to Create Extensions
************************

Creating an extension takes only a few steps:

#. Open the directory containing the add-on code or theme file.
#. Add a `blender_manifest.toml <#manifest>`__  file with all the required meta-data ``(name, maintainer, ...)``.
#. Use the :ref:`Blender command-line tool <command-line-args-extension-build>` to build the extension .zip file.

How to publish to the `Blender Extensions Platform <https://extensions.blender.org>`__:

- :ref:`Install from Disk <prefs-extensions-install>` to test if everything is working well.
- `Upload the .zip file <https://extensions.blender.org/submit/>`__ (this step requires Blender ID).

The extension will be held for `review <https://extensions.blender.org/approval-queue/>`__,
and published once the moderation team approves it.


Extension files
===============

An extension is shared as a ``.zip`` archive containing a manifest file and other files.
The expected files depend on the extension type.


Add-on extension
----------------

:ref:`Add-ons <extensions-addons>` need at least the manifest and an ``__init__.py`` file,
while more complex add-ons have a few different .py files or wheels together.

.. code-block:: text

   my_extension-0.0.1.zip
   ├─ __init__.py
   ├─ blender_manifest.toml
   └─ (...)


Theme extension
---------------

A theme extension only needs the manifest and the .xml theme file.

.. code-block:: text

   my_extension-0.0.1.zip
   ├─ blender_manifest.toml
   └─ theme.xml

.. note::

   Extensions can optionally have all its files inside a folder (inside the archive).
   This is a common behavior when saving a repository as ZIP from version-control platforms.


.. _extensions-manifest:

Manifest
========

A manifest is a file with all the meta-data required for an extension to be processed.
This example is a good starting point to the ``blender_manifest.toml`` that should be inside the ``.zip``.

.. code-block:: toml

   schema_version = "1.0.0"

   # Example of manifest file for a Blender extension
   # Change the values according to your extension
   id = "my_example_extension"
   version = "1.0.0"
   name = "My Example Extension"
   tagline = "This is another extension"
   maintainer = "Developer name"
   # Supported types: "add-on", "theme"
   type = "add-on"

   # # Optional: link to documentation, support, source files, etc
   # website = "https://extensions.blender.org/add-ons/my-example-package/"

   # # Optional: tag list defined by Blender and server, see:
   # # https://docs.blender.org/manual/en/dev/advanced/extensions/tags.html
   # tags = ["Animation", "Sequencer"]

   blender_version_min = "4.2.0"
   # # Optional: Blender version that the extension does not support, earlier versions are supported.
   # # This can be omitted and defined later on the extensions platform if an issue is found.
   # blender_version_max = "5.1.0"

   # License conforming to https://spdx.org/licenses/ (use "SPDX: prefix)
   # https://docs.blender.org/manual/en/dev/advanced/extensions/licenses.html
   license = [
     "SPDX:GPL-3.0-or-later",
   ]
   # # Optional: required by some licenses.
   # copyright = [
   #   "2002-2024 Developer Name",
   #   "1998 Company Name",
   # ]

   # # Optional: list of supported platforms. If omitted, the extension will be available in all operating systems.
   # platforms = ["windows-x64", "macos-arm64", "linux-x64"]
   # # Other supported platforms: "windows-arm64", "macos-x64"

   # # Optional: bundle 3rd party Python modules.
   # # https://docs.blender.org/manual/en/dev/advanced/extensions/python_wheels.html
   # wheels = [
   #   "./wheels/hexdump-3.3-py3-none-any.whl",
   #   "./wheels/jsmin-3.0.1-py3-none-any.whl",
   # ]

   # # Optional: add-ons can list which resources they will require:
   # # * files (for access of any filesystem operations)
   # # * network (for internet access)
   # # * clipboard (to read and/or write the system clipboard)
   # # * camera (to capture photos and videos)
   # # * microphone (to capture audio)
   # #
   # # If using network, remember to also check `bpy.app.online_access`
   # # https://docs.blender.org/manual/en/dev/advanced/extensions/addons.html#internet-access
   # #
   # # For each permission it is important to also specify the reason why it is required.
   # # Keep this a single short sentence without a period (.) at the end.
   # # For longer explanations use the documentation or detail page.
   #
   # [permissions]
   # network = "Need to sync motion-capture data to server"
   # files = "Import/export FBX from/to disk"
   # clipboard = "Copy and paste bone transforms"

   # # Optional: advanced build settings.
   # # https://docs.blender.org/manual/en/dev/advanced/extensions/command_line_arguments.html#command-line-args-extension-build
   # [build]
   # # These are the default build excluded patterns.
   # # You only need to edit them if you want different options.
   # paths_exclude_pattern = [
   #   "__pycache__/",
   #   "/.git/",
   #   "/*.zip",
   # ]

Required values:
   :blender_version_min: Minimum supported Blender version - use at least ``4.2.0``.
   :id: Unique identifier for the extension.
   :license: List of :ref:`licenses <extensions-licenses>`,
      use `SPDX license identifier <https://spdx.org/licenses/>`__.
   :maintainer: Maintainer of the extension.
   :name: Complete name of the extension.
   :schema_version: Internal version of the file format - use ``1.0.0``.
   :tagline: One-line short description, up to 64 characters - cannot end with punctuation.
   :type: "add-on", "theme".
   :version: Version of the extension - must follow `semantic versioning <https://semver.org/>`__.

Optional values:
   :blender_version_max: Blender version that the extension does not support, earlier versions are supported.
   :website: Website for the extension.
   :copyright: Some licenses require a copyright, copyrights must be "Year Name" or "Year-Year Name".
   :tags: List of tags. See the :ref:`list of available tags <extensions-tags>`.
   :platforms:
      List of supported platforms. If omitted, the extension will be available in all operating systems.
      The available options are
      ["windows-x64", "windows-arm64", "macos-x64", "macos-arm64", "linux-x64"]
   :wheels: List of relative file-paths :ref:`Python Wheels <extensions-python_wheels>`.
   :permissions:
      Add-ons can list which resources they require. The available options are
      *files*, *network*, *clipboard*, *camera*, *microphone*.
      Each permission should be followed by an explanation (short single-sentence, up to 64 characters, with no end
      punctuation).

Optional values for "build":
   These values are only used by the :ref:`build <command-line-args-extension-build>` sub-command.

   :paths:
      A list of file-paths relative to the manifest to include when building the package.

   :paths_exclude_pattern:
      A list of file-path patterns to exclude include when building the package.

      The pattern matching is compatible with `gitignore <https://git-scm.com/docs/gitignore>`__.

      Note that setting this value isn't supported when ``paths`` is also declared.

   If the ``[build]`` table isn't declared the following default is used:

   .. code-block:: toml

      [build]
      paths_exclude_pattern = [
        "__pycache__/",
        ".git",
        "*.zip",
      ]

Reserved:
   These values **must not** be declared in a TOML and are reserved for internal use.

   - ``[build.generated]``


.. note::

   All the values present in the manifest file must be filled
   (i.e., cannot be empty, nor text ``""``, nor list ``[]``).

   If you don't want to set one of the optional values just exclude it from the manifest altogether.


Command-line
============

Extensions can be built, validated & installed via command-line.

Build
-----

To build the package defined in the current directory use the following commands:

.. code:: bash

   blender --command extension build

See :ref:`build <command-line-args-extension-build>` docs.

Validate
--------

To validate the manifest without building the package:

.. code:: bash

   blender --command extension validate

You may also validate a package without having to extract it first.

.. code:: bash

   blender --command extension validate add-on-package.zip

See :ref:`validate <command-line-args-extension-validate>` docs.

.. seealso::

   :ref:`command_line-args-extensions`.

Publish
-------

To automate the publishing of updates on the Extension Platform check the `CI/CD documentation <https://developer.blender.org/docs/features/extensions/ci_cd/>`__.


Third party extension sites
===========================

If you want to host the extensions yourself, see the :ref:`extensions-create_repo-index` docs.
