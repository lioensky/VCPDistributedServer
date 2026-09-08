
************
Introduction
************

Here are some preferences that you may wish to set initially. See the section
:doc:`Preferences </editors/preferences/index>` for the complete list of available settings. The shortcut
:kbd:`Ctrl-Comma` can be used to quickly open the Preferences editor.


.. _autosave-preferences:

Auto-Save Preferences
=====================

By default, a new Blender installation is set to auto-save changes to preferences, so you don't accidentally lose a
change you have made. To disable this behavior, perform these steps:

1. Open the Preferences dialog
2. Click on the small menu at the lower left (shown by 3 lines)
3. Uncheck the box next to "*Auto-Save Preferences*"
4. Click the "*Save Preferences*" button that will appear in the lower left of the dialog. **Don't forget this step,
   as the change will not be saved otherwise.**

To enable auto-save once again, simply follow steps 1-3 above and check the box in step 3.


Language
========

Enable :menuselection:`Edit --> Preferences --> Interface --> Translation`, and choose the *Language* and what to
translate from *Interface*, *Tooltips* and *New Data*.

See :ref:`prefs-interface-translation` for details.


Input
=====

If you have a compact keyboard without a separate number pad, enable
:menuselection:`Preferences --> Input --> Keyboard --> Emulate Numpad`. This gives you the 3D view shortcuts regularly
used on the number pad.

If you do not have a middle mouse button, you can enable
:menuselection:`Preferences --> Input --> Mouse --> Emulate 3 Button Mouse`. This allows you to hold the :kbd:`Alt`
or :kbd:`OSKey` key while dragging with the mouse, to orbit.

See :doc:`Configuring Peripherals <hardware>` for more information about these options, and see
:doc:`Input Preferences </editors/preferences/input>` for details on configuring their settings.


File and Paths
==============

At :menuselection:`Preferences --> File Paths` you can set options such as what *Image Editor* (GIMP, Krita...) and
*Animation Player* to use.

The :ref:`temp-dir` sets where to store files such as temporary renders and auto-saves.

.. tip::

   The ``//`` at the start of each path in Blender means the directory of the currently opened blend-file, used to
   reference relative paths.

See :doc:`File Preferences </editors/preferences/file_paths>` for details.


Save & Load
===========

If you trust the source of your blend-files, you can enable *Auto Run Python Scripts*. This option is meant to protect
you from malicious Python scripts in blend-files that you got from someone else. Many users turn this option on, as
advanced rigs tend to use scripts of some sort. **Use caution, as this is a global setting, and may allow potentially
malicious Python code from an untrusted source to run.**

See Save & Load :ref:`bpy.types.PreferencesFilePaths.use_scripts_auto_execute` Preference.
