
***************
Troubleshooting
***************

Some common problems people may run into when using drivers.


Scripted Expression
===================

.. figure:: /images/animation_drivers_troubleshooting_autorun-graph-editor.png

   A security warning in the Drivers panel.

.. figure:: /images/advanced_scripting_security_autorun-scripts-dialog.png

   An Auto-run warning in the Info editor's header.

By default Blender will restrict execution of Python scripts.

If using a *Scripted Expression* Driver Type that doesn't follow
the :ref:`Simple Expressions <drivers-simple-expressions>`
subset, you will have to open the file as *Trusted Source*,
or set *Auto Run Python Scripts* in :menuselection:`Preferences --> Save & Load --> Blender Files`.

.. list-table::
   :widths: 40 60

   * - .. figure:: /images/animation_drivers_troubleshooting_autorun-file-browser.png

          The Trusted Source checkbox in the File Browser.

     - .. figure:: /images/animation_drivers_troubleshooting_autorun-user-preference.png

          The Auto Run Python Scripts checkbox in the Preferences.


Rotational Properties are Radians
=================================

Parts of the User Interface may use different units of measurements for angles, rotation.
In the Graph Editor, while working with Drivers, all angles are Radians.
