
*************
Compatibility
*************

Blender can open blend-files saved with both older versions of the software (backward compatibility),
and newer ones (forward compatibility). This comes with some limitations though.

.. tip::

   When having issues with opening much older (or newer) blend-files, it can help to use a few
   intermediary Blender releases to perform conversions by smaller steps.

.. note::

   Here is a `more exhaustive documentation <https://developer.blender.org/docs/handbook/guidelines/compatibility_handling_for_blend_files/>`__
   about compatibility handling, in the developer's documentation.


Backward Compatibility
======================

Opening older files and converting them for the current version of Blender is usually straight-forward.
It is expected to give very good and usable results.

There can be major feature changes, for which the backward compatibility will only be ensured for
a limited amount of time. For example the changes to the animation system that happened during the
Blender 2.5x project. This will never be less than a full major release cycle (i.e. two years at least).


Forward Compatibility
=====================

Loss of Data
------------

Forward compatibility is inherently harder to ensure, and loss of feature should always be expected
when opening a blend-file saved with a more recent version of Blender.

A warning is shown in the UI when editing a more recent blend-file.
Trying to overwrite it (with a simple 'Save' operation) will also show a confirmation popup,
as this could make that loss of data permanent.


Complete Incompatibility
------------------------

When Blender switches to a new major version release (e.g. from 3.x to 4.0), there can also be major
changes that will make the blend-file fully incompatible with older versions of Blender.

In such cases, older Blender will fail opening (or appending/linking from) the newer blend-file, with a
message stating which minimal version is needed to open it.

In such cases, the last LTS release of the previous release cycle will be kept compatible with the newer
file format version, and will be usable as converter between both versions.

For example, Blender 3.6 LTS can open files from Blender 4.x, and will perform the necessary conversion
such that when re-saved from 3.6, the files become compatible with all 3.x Blender versions.
