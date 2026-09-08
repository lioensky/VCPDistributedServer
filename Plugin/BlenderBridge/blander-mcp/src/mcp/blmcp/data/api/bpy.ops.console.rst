Console Operators
=================

.. module:: bpy.ops.console

.. function:: autocomplete()

   Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/console.py\:61 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L61>`__

.. function:: banner()

   Print a message when the terminal initializes

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/console.py\:104 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L104>`__

.. function:: clear(*, scrollback=True, history=False)

   Clear text by type

   :param scrollback: Scrollback, Clear the scrollback history (optional)
   :type scrollback: bool
   :param history: History, Clear the command history (optional)
   :type history: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: clear_line()

   Clear the line and store in history

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: copy(*, delete=False)

   Copy selected text to clipboard

   :param delete: Delete Selection, Whether to delete the selection after copying (optional)
   :type delete: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: copy_as_script()

   Copy the console contents for use in a script

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/console.py\:82 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L82>`__

.. function:: delete(*, type='NEXT_CHARACTER')

   Delete text by cursor position

   :param type: Type, Which part of the text to delete (optional)
   :type type: Literal['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: execute(*, interactive=False)

   Execute the current console line as a Python expression

   :param interactive: interactive, (optional)
   :type interactive: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/console.py\:38 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L38>`__


.. function:: history_append(*, text="", current_character=0, remove_duplicates=False)

   Append history at cursor position

   :param text: Text, Text to insert at the cursor position (optional, never None)
   :type text: str
   :param current_character: Cursor, The index of the cursor (in [0, inf], optional)
   :type current_character: int
   :param remove_duplicates: Remove Duplicates, Remove duplicate items in the history (optional)
   :type remove_duplicates: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: history_cycle(*, reverse=False)

   Cycle through history

   :param reverse: Reverse, Reverse cycle history (optional)
   :type reverse: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: indent()

   Add 4 spaces at line beginning

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: indent_or_autocomplete()

   Indent selected text or autocomplete

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: insert(*, text="")

   Insert text at cursor position

   :param text: Text, Text to insert at the cursor position (optional, never None)
   :type text: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: language(*, language="")

   Set the current language for this console

   :param language: Language, (optional, never None)
   :type language: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/console.py\:136 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L136>`__


.. function:: move(*, type='LINE_BEGIN', select=False)

   Move cursor position

   :param type: Type, Where to move cursor to (optional)
   :type type: Literal['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD']
   :param select: Select, Whether to select while moving (optional)
   :type select: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: paste(*, selection=False)

   Paste text from clipboard

   :param selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only) (optional)
   :type selection: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: scrollback_append(*, text="", type='OUTPUT')

   Append scrollback text by type

   :param text: Text, Text to insert at the cursor position (optional, never None)
   :type text: str
   :param type: Type, Console output type (optional)
   :type type: Literal['OUTPUT', 'INPUT', 'INFO', 'ERROR']
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]

.. function:: select_all()

   Select all the text

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_set()

   Set the console selection

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: select_word()

   Select word at cursor position

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
.. function:: unindent()

   Delete 4 spaces from line beginning

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
