
######################
  Installing Blender
######################

Blender is released approximately every three months. You can keep up to date with the latest changes through the
`release notes <https://www.blender.org/download/releases/>`__.


System Requirements
===================

Blender is available for download on Windows, macOS, and Linux. Always check that your graphics drivers are up to date
and that OpenGL is properly supported. Blender has a set of `minimum and recommended requirements
<https://www.blender.org/download/requirements/>`__; so make sure these are met before trying to install Blender.

Support for other hardware such as graphic tablets and 3D mice are covered later in
:doc:`Configuring Hardware </getting_started/configuration/hardware>`.


Download Blender
================

Blender offers a variety of different binary packages to choose from depending on their level of stability. Each
package has the trade off of newest features versus stability. The package that is right for you depends on your
requirements for those two. A studio, for example, might want to have *long-term support*, while a hobbyist may want
newer features, while others may just want to test upcoming features. Each package described below has something just
right for everyone.

`Stable Release <https://www.blender.org/download/>`__
   A package that contains the latest features and is considered stable without regressions. A new stable version is
   available roughly every three months.

`Long-term Support <https://www.blender.org/download/lts/>`__
   A package designed for long-lasting projects requiring a very stable version of Blender. :abbr:`LTS
   (Long-Term-Support)` releases are supported for two years and will not have any new features, API changes or
   improvements. A new long-term support version is available every year. *These LTS releases will occasionally have
   minor patches (such as 4.2.6) which improve stability or fix critical bugs.*

`Daily Builds <https://builder.blender.org/download/>`__
   A package updated daily to include the newest changes in development. These versions are automatically built on a
   schedule.  They are not as thoroughly tested as the release types above, and might break or crash. Builds marked as
   **Alpha** are still undergoing major changes and feature additions, while those marked **Beta** are
   feature-complete and are under development for refinement and stability.

   Stability can be expected to increase from Alpha to Beta to Release Candidate (RC) to a final release.

`Build from Source <https://developer.blender.org/docs/handbook/building_blender/>`__
   Blender's source code is available for free to either reference or to build and use. While normal users are
   **not** expected to compile Blender, it does have advantages:

   - Blender is always up to date.
   - It allows access to any version or branch where a feature is being developed.
   - It can be freely customized.
   - Curious users can look through the source code and make small changes to see the effects to better understand how
     Blender works.

The procedure for installing a binary, either the latest stable release or a daily build, is the same. Follow the
steps for your platform listed below.

.. note::

   Blender is designed to not require an internet connection, so it doesn't have a built-in update system. This means
   you will need to update Blender yourself by following the platform-specific upgrade steps described in the sections
   below.


Installation Guides
===================

.. toctree::
   :maxdepth: 1

   linux.rst
   macos.rst
   windows.rst
   steam.rst
