bpy_extras submodule (bpy_extras.keyconfig_utils)
=================================================

.. module:: bpy_extras.keyconfig_utils

.. function:: addon_keymap_register(keymap_data)

   Register a set of keymaps for addons using a list of keymaps.
   
   See 'blender_default.py' for examples of the format this takes.
   
   :param keymap_data: A list of keymap definitions to register.
   :type keymap_data: list[tuple[str, dict[str, Any], dict[str, Any]]]

.. function:: addon_keymap_unregister(keymap_data)

   Unregister a set of keymaps for addons.
   
   :param keymap_data: A list of keymap definitions to unregister.
   :type keymap_data: list[tuple[str, dict[str, Any], dict[str, Any]]]

.. function:: keyconfig_test(kc)

   Test a key configuration for duplicate key-map item assignments.
   
   :param kc: The key configuration to test.
   :type kc: :class:`bpy.types.KeyConfig`
   :return: True if any duplicates were found.
   :rtype: bool

