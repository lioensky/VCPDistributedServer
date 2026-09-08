.. highlight:: sh

***********
Maintenance
***********

Adding/Removing/Moving Files
============================

When RST-files are added or removed the corresponding locale files are added or removed automatically by the update
script. However, if files need to be moved please use this Python script::

   python tools/utils_maintenance/rst_remap.py start

RST-files can then be freely moved and the remap script will move the locale file after::

   python tools/utils_maintenance/rst_remap.py finish

It is best to avoid moving/renaming files as this breaks URLs and without this script translators will lose all their
work in these files. Please ask an administrator if you think something should be renamed/moved.

.. note::

   This script also works for image file names.


.. _about-contribute-guides-release:

Release Checklist
=================

- Create a release branch (``blender-3.2-release/``)
- Update the splash image: ``interface_splash_current.png`` in the release branch.
- Increase the ``conf.py: blender_version`` variable in the trunk version.
