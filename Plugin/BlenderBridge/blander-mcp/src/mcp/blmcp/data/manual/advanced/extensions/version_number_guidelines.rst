.. _extensions-version_number_guidelines:
.. index:: Version Number Guidelines

*************************
Version Number Guidelines
*************************

The Blender Extensions platform doesn't mandate any particular version numbering
scheme, so if you already have a versioning scheme that you use for your
extension, feel free to continue using that.

However, if you don't have an existing version numbering scheme, we recommend
following the guidelines below.

Add-on Extensions
=================

Add-ons should follow `semantic versioning <https://semver.org/>`_ in spirit.

Semantic versioning was designed for software libraries with APIs, and that's
not (typically) what add-ons are. Rather, add-ons provide user-facing
functionality, and therefore semantic versioning doesn't strictly apply.

Nevertheless, we recommend following the *spirit* of semantic versioning with
add-ons in the following way:

- Version numbers should use the **MAJOR.MINOR.PATCH** format (e.g. 2.3.1).

- **The MAJOR number** should be incremented for changes that remove or alter
  existing functionality in such a way that users can't just continue using the
  add-on as they previously were. Rules of thumb:

   - If the new version doesn't work with data created for/by the previous
     version, increment the MAJOR number.
   - If the user needs to relearn anything non-trivial about the add-on to
     continue using it as they already were, increment the MAJOR number.

- **The MINOR number** should be incremented when introducing new functionality,
  but *without* significantly affecting existing functionality. Rule of thumb:

   - If new functionality was introduced, but the user can simply ignore it (if
     desired) and continue working with the add-on as they already were,
     increment the MINOR number.

- **The PATCH number** should be incremented for bug fixes and small changes
  that don't affect the add-on's intended functionality. Rule of thumb:

   - If the new version isn't notably different from an end-user perspective
     aside from bug fixes, increment the PATCH number.

These guidelines won't cover every possible situation, but hopefully they give a
good sense of how to approach the common cases. Extension developers should use
their best judgment when dealing with situations not covered well by these
guidelines.

Theme Extensions
================

Theme extensions don't have the same considerations as add-on extensions, and
therefore don't need to follow anything like semantic versioning. Instead, we
recommend following these guidelines:

- Version numbers should use a **X.Y.Z** format (e.g. 2.3.1).
- **X** should be incremented for "substantial" visual changes or reworks of the
  theme.
- **Y** should be used for "tracks" of the theme for different Blender versions
  (see below).
- **Z** should be incremented for minor visual tweaks or visual "bug" fixes.


Tracks
======

New Blender versions can sometimes introduce breaking changes in Blender's
Python API or even change how entire features work. If this affects your
extension, you may want to maintain two "tracks" of your extension concurrently:
one for Blender "old" and one for Blender "new".

You can use version numbering to accomplish this in a reasonably clear way. For
example, if your extension is currently on version 1.2.1, and you wish to
release a new version for the breaking changes in Blender "new", you can release
that new version as version 1.3.0. Then if you need to make bug fixes in the
version of the extension for Blender "old", you can still increment the patch
number to 1.2.2, 1.2.3, etc. In effect, 1.2.x and 1.3.x are two different
"tracks" of the extension, each of which can continue to get new releases.

Alternatively, you can increment the major version number for the tracks,
particularly if you expect to do more than just bug fixes for the older tracks.
Either way, we strongly recommend against only incrementing the patch version
for these kinds of updates: you never know when you might need to make a bug fix
release.

.. note::

   Make sure to correctly indicate the Blender versions that each version of
   your extension is compatible with in their manifest file. You can also update
   Blender version compatibility of already-uploaded versions of your add-on from
   the extensions website.
