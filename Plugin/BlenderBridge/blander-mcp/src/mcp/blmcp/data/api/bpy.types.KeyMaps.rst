KeyMaps(bpy_prop_collection)
============================

.. currentmodule:: bpy.types


Add-on Keymap Registration
++++++++++++++++++++++++++

This example shows how an add-on can register custom keyboard shortcuts.
Keymaps are added to ``keyconfigs.addon`` and removed when unregistered.

Store ``(keymap, keymap_item)`` tuples for safe cleanup, as multiple add-ons may use the same keymap.

.. note::

   Users can customize add-on shortcuts in the Keymap Preferences.
   Add-on keymaps appear under their respective editors and can be
   modified or disabled without editing the add-on code.

   Add-ons should only manipulate keymaps in ``keyconfigs.addon`` and not manipulate the user's keymaps
   because add-on keymaps serve as a default which users may customize.
   Modifying user keymaps directly interferes with users' own preferences.

.. warning::

   Add-ons can add items to existing modal keymaps but cannot create
   new modal keymaps via Python. Use ``modal=True`` when targeting
   an existing modal keymap such as "Knife Tool Modal Map".

.. literalinclude:: ./examples/bpy.types.KeyMaps.1.py
   :lines: 27-

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: KeyMaps(bpy_prop_collection)

   Collection of keymaps

   .. method:: new(name, *, space_type='EMPTY', region_type='WINDOW', modal=False, tool=False)

      Ensure the keymap exists. This will return the one with the given name/space type/region type, or create a new one if it does not exist yet.

      :param name: Name, (never None)
      :type name: str
      :param space_type: Space Type, (optional)
      :type space_type: Literal[:ref:`rna_enum_space_type_items`]
      :param region_type: Region Type, (optional)
      :type region_type: Literal[:ref:`rna_enum_region_type_items`]
      :param modal: Modal, Keymap for modal operators. Modal keymaps are not supported for :class:`KeyConfigs.addons`. (optional)
      :type modal: bool
      :param tool: Tool, Keymap for active tools (optional)
      :type tool: bool
      :return: Key Map, Added key map
      :rtype: :class:`KeyMap`

   .. method:: remove(keymap)

      remove

      :param keymap: Key Map, Removed key map (never None)
      :type keymap: :class:`KeyMap` | None

   .. method:: clear()

      Remove all keymaps.


   .. method:: find(name, *, space_type='EMPTY', region_type='WINDOW')

      find

      :param name: Name, (never None)
      :type name: str
      :param space_type: Space Type, (optional)
      :type space_type: Literal[:ref:`rna_enum_space_type_items`]
      :param region_type: Region Type, (optional)
      :type region_type: Literal[:ref:`rna_enum_region_type_items`]
      :return: Key Map, Corresponding key map
      :rtype: :class:`KeyMap`

   .. method:: find_match(keymap)

      find_match

      :param keymap: Key Map, The key map for comparison
      :type keymap: :class:`KeyMap` | None
      :return: Key Map, Corresponding key map
      :rtype: :class:`KeyMap`

   .. method:: find_modal(name)

      find_modal

      :param name: Operator Name, (never None)
      :type name: str
      :return: Key Map, Corresponding key map
      :rtype: :class:`KeyMap`

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: :class:`bpy.types.Struct` | None
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct`


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :param id: The RNA type identifier.
      :type id: str
      :param default: The value to return when not found.
      :type default: type | None
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   - :class:`bpy_struct.as_pointer`
   - :class:`bpy_struct.driver_add`
   - :class:`bpy_struct.driver_remove`
   - :class:`bpy_struct.get`
   - :class:`bpy_struct.id_properties_clear`
   - :class:`bpy_struct.id_properties_ensure`
   - :class:`bpy_struct.id_properties_ui`
   - :class:`bpy_struct.is_property_hidden`
   - :class:`bpy_struct.is_property_overridable_library`
   - :class:`bpy_struct.is_property_readonly`
   - :class:`bpy_struct.is_property_set`
   - :class:`bpy_struct.items`
   - :class:`bpy_struct.keyframe_delete`
   - :class:`bpy_struct.keyframe_insert`
   - :class:`bpy_struct.keys`
   - :class:`bpy_struct.path_from_id`
   - :class:`bpy_struct.path_from_module`
   - :class:`bpy_struct.path_resolve`
   - :class:`bpy_struct.pop`
   - :class:`bpy_struct.property_overridable_library_set`
   - :class:`bpy_struct.property_unset`
   - :class:`bpy_struct.rna_ancestors`
   - :class:`bpy_struct.type_recast`
   - :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   - :class:`KeyConfig.keymaps`

