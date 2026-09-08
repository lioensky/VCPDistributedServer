
***********
Keying Sets
***********

.. figure:: /images/editors_timeline_keying-sets.png
   :align: right

   The Active Keying Sets data ID in the Timeline.

Keying Sets are a collection of animated properties that are used to animate
and keyframe multiple properties at the same time.
For example, pressing :kbd:`K` in the 3D Viewport will bring up the available Keying Sets.
Blender will then add keyframes for whichever Keying Set is chosen.
There are some built-in Keying Sets and also custom Keying Sets called "Absolute Keying Sets".


.. _bpy.types.KeyingSets:

Keying Set Panel
================

.. reference::

   :Editor:    Properties
   :Panel:     :menuselection:`Scene --> Keying Set`

This panel is used to add, select, manage "Absolute Keying Sets".

.. figure:: /images/animation_keyframes_keying-sets_scene-keying-set-panel.png

   The Keying Set panel.

.. _bpy.types.KeyingSets.active_index:

Active Keying Set
   A :ref:`List View <ui-list-view>` of Keying Sets in the active scene.
   Selecting a keying set makes it active

   .. -bpy.ops.anim.keying_set_add:

   :bl-icon:`add` Add Empty Keying Set
      Adds an empty Keying Set.

   .. _bpy.ops.anim.keying_set_remove:

   :bl-icon:`remove` Remove Active Keying Set
      Removes the active keying set.

.. _bpy.types.KeyingSet.bl_description:

Description
   A short description of the Keying Set.

.. _bpy.ops.anim.keying_set_export:

Export to File
   Export Keying Set to a Python script ``File.py``.
   To re-add the Keying Set from the ``File.py``, open then run the ``File.py`` from the Text Editor.


.. _bpy.types.KeyingSetPath:

Active Keying Set Panel
-----------------------

.. reference::

   :Editor:    Properties
   :Panel:     :menuselection:`Scene --> Active Keying Set`

This panel is used to add properties to the active Keying Set.

.. figure:: /images/animation_keyframes_keying-sets_scene-active-keying-set-panel.png

   The Active Keying Set panel.

.. _bpy.types.KeyingSetPaths.active_index:

Paths
   A collection of paths in a :ref:`List View <ui-list-view>` each with a *Data Path* to a property
   to add to the active Keying Set.

   .. _bpy.ops.anim.keying_set_path_add:

   :bl-icon:`add` Add Empty Keying Set Path
      Adds an empty path.

   .. _bpy.ops.anim.keying_set_path_remove:

   :bl-icon:`remove` Remove Active Keying Set Path
      Removes the selected path.

.. _bpy.types.KeyingSetPath.id_type:
.. _bpy.types.KeyingSetPath.id:

Target ID-Block
   Set the ID Type and the *Object IDs* data path for the property.

.. _bpy.types.KeyingSetPath.data_path:

Data Path
   Set the rest of the Data Path for the property.

.. _bpy.types.KeyingSetPath.use_entire_array:

Array All Items
   Use *All Items* from the Data Path or select the array index for a specific property.

.. _bpy.types.KeyingSetPath.group_method:

F-Curve Grouping
   This controls what group to add the channels to.

   Keying Set Name, None, Named Group


Keyframing Settings
-------------------

General Override
   These options control all properties in the Keying Set.
   Note that the same settings in *Preferences* override these settings if enabled.

Active Set Override
   These options control individual properties in the Keying Set.

.. _bpy.types.KeyingSet.use_insertkey_override_needed:
.. _bpy.types.KeyingSet.use_insertkey_override_visual:
.. _bpy.types.KeyingSetPath.use_insertkey_override_needed:
.. _bpy.types.KeyingSetPath.use_insertkey_override_visual:

Common Settings
   Needed
      Only insert keyframes where they are needed in the relevant F-Curves.
   Visual
      Insert keyframes based on the visual transformation.


.. _bpy.ops.anim.keyingset_button_add:

Adding Properties to a Keying Set
=================================

.. reference::

   :Menu:      :menuselection:`Context menu --> Add All/Single to Keying Set`
   :Shortcut:  :kbd:`K`

Some ways to add properties to Keying Sets.

:kbd:`RMB` the property in the *User Interface*, then select *Add Single to Keying Set* or *Add All to Keying Set*.
This will add the properties to the active Keying Set, or to a new Keying Set if none exist.

Hover the mouse over the properties, then press :kbd:`K`, to add *Add All to Keying Set*.


.. _bpy.ops.anim.keying_set_active_set:

Set Active Keying Set
=====================

.. reference::

   :Shortcut:  :kbd:`Shift-K`

There are several ways to designate the active keying set:

- Press :kbd:`Shift-K` in the 3D Viewport.
- Select a keying set in the :ref:`Keying Set <bpy.types.KeyingSets>` panel.
- Select a keying set in the :ref:`Keying popover <animation-editors-keying>` in the Timeline header,


.. _whole-character-keying-set:

Whole Character Keying Set
==========================

The built-in *Whole Character* Keying Set is made to keyframe all properties
that are likely to get animated in a character rig.

This keying set ignores bones whose name starts with one of the following prefixes,
as it assumes these are technical bones that are not meant to be animated directly.
The built-in Rigify addon generates such bones, for example.

- COR (Corrective)
- DEF (Deformation)
- GEO (Geometry)
- MCH (Mechanism)
- ORG (Original from meta rig)
- VIS (Visualization)
