
***********
Help System
***********

Blender has a range of built-in and web-based help options.


Tooltips
========

.. figure:: /images/getting-started_help_tooltip.png

   Tooltip of the Renderer selector in the Info Editor.

After hovering the mouse cursor over a button or setting for a few moments, a tooltip will appear.


Elements
--------

The context-sensitive tooltip might contain some of these elements:

Short Description
   Related details depending on the control.
Shortcut
   A keyboard or mouse shortcut associated to the tool.
Value
   The value of the property.

   Hovering over a color property will display a large swatch preview of the color and the color's hexadecimal, RGBA,
   and HSVA values.

   .. figure:: /images/getting-started_help_color.png

      Tooltip showing color information.

Library
   Source file of the active object. See also :doc:`/files/linked_libraries/index`.
Disabled (red)
   The reason why the value is not editable.
Python
   When :ref:`Python Tooltips <bpy.types.PreferencesView.show_tooltips_python>` are enabled, a Python expression is
   displayed for :ref:`scripting <scripting-index>` (usually an operator or property).


.. _help-manual-access:
.. _bpy.ops.wm.doc_view_manual_ui_context:

Context-Sensitive Manual Access
===============================

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Context menu --> Online Manual`
   :Shortcut:  :kbd:`F1`

You may want to access help for a tool or area from within Blender.

To do so, hover the cursor over the tool or button you need help with and use the keyboard shortcut or context menu
item to visit pages of this reference manual from within Blender. This opens a web page relating to the button under
the cursor, supporting both tool and value buttons.

.. note::

   We do not currently have 100% coverage. You may see an alert in the info header if a tool does not have a link to
   the manual.

   In other cases, buttons may link to more general sections of the documentation.


.. _help-menu:

Help Menu
=========

Web Links
---------

The first options of this menu provide direct links to Blender-related websites. The same links can also be found in
the :ref:`splash`.

:doc:`Manual </index>`
   This is a link to the Official Blender Manual (which you are now reading).
`Support <https://www.blender.org/support>`__
   Links to various sites, providing both community and professional support.
`User Communities <https://www.blender.org/community/>`__
   Lists of many different community sites and support venues.
`Get Involved <https://www.blender.org/get-involved>`__
   Learn how to give back to the Blender community by contributing to projects or donating.
`Release Notes <https://developer.blender.org/docs/release_notes/>`__
   Link to the release notes for the current Blender version.

----

`Report a Bug <https://projects.blender.org/blender/blender/issues/new?template=.gitea%2fissue_template%2fbug.yaml>`__
   The Blender Bug Tracker (registration needed). For more information on bug reporting, please see
   :doc:`/troubleshooting/report_bug`.


.. _help-system-info:

Save System Info
----------------

This extracts system information which can be useful for including in bug reports, inspecting the configuration, or
diagnosing problems.

You will be prompted to save a text file called ``system-info.txt``.

It contains the following sections:

Blender
   This section shows you the Blender version, details about the build configuration, and the path in which Blender is
   running.
Python
   The version and path of your Python installation.
Directories
   Paths used for scripts, data files, presets and temporary files.

   Those directories are configured using the :doc:`Preferences </editors/preferences/file_paths>` Editor.
FFmpeg
   The version of the installed FFmpeg components and codecs.
Other Libraries
   The version of other libraries used by Blender such as OpenColorIO, Alembic, USD, etc.
GPU
   Shows the GPU vendor, version and the capabilities of your hardware and driver.
Implementation Dependent GPU Limits
   Specific limits on GPU functions related to how the current version of Blender was compiled.
Cycles
   The instruction sets and capabilities of each hardware render device available for use with Cycles.
Enabled Add-Ons
   Lists add-ons currently in use along with their versions and paths.
