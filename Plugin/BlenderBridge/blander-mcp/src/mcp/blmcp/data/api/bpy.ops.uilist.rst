Uilist Operators
================

.. module:: bpy.ops.uilist

.. function:: entry_add(*, list_path="", active_index_path="")

   Add an entry to the list after the current active item

   :param list_path: list_path, (optional, never None)
   :type list_path: str
   :param active_index_path: active_index_path, (optional, never None)
   :type active_index_path: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_ui/generic_ui_list.py\:208 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/generic_ui_list.py#L208>`__


.. function:: entry_move(*, list_path="", active_index_path="", direction='UP')

   Move an entry in the list up or down

   :param list_path: list_path, (optional, never None)
   :type list_path: str
   :param active_index_path: active_index_path, (optional, never None)
   :type active_index_path: str
   :param direction: Direction, (optional)

      - ``UP``
        Up -- Move the active entry up.
      - ``DOWN``
        Down -- Move the active entry down.
   :type direction: Literal['UP', 'DOWN']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_ui/generic_ui_list.py\:236 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/generic_ui_list.py#L236>`__


.. function:: entry_remove(*, list_path="", active_index_path="")

   Remove the selected entry from the list

   :param list_path: list_path, (optional, never None)
   :type list_path: str
   :param active_index_path: active_index_path, (optional, never None)
   :type active_index_path: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_ui/generic_ui_list.py\:191 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/generic_ui_list.py#L191>`__


