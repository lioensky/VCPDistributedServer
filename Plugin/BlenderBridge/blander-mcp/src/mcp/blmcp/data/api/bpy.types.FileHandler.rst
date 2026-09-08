FileHandler(bpy_struct)
=======================

.. currentmodule:: bpy.types


Basic FileHandler for importing a single file
---------------------------------------------

A file handler allows custom drag-and-drop behavior to be associated with a given ``Operator``
(:class:`FileHandler.bl_import_operator`) and set of file extensions
(:class:`FileHandler.bl_file_extensions`). Control over which area of the UI accepts the
drag-in-drop action is specified using the :class:`FileHandler.poll_drop` method.

Similar to operators that use a file select window, operators participating in drag-and-drop, and
only accepting a single file, must define the following property:

.. code-block:: python

    filepath: bpy.props.StringProperty(subtype='FILE_PATH', options={'SKIP_SAVE'})

This ``filepath`` property will be set to the full path of the file dropped by the user.

.. literalinclude:: ./examples/bpy.types.FileHandler.1.py
   :lines: 20-


FileHandler for Importing multiple files and exposing Operator options
----------------------------------------------------------------------

Operators which support being executed with multiple files from drag-and-drop require the
following properties be defined:

.. code-block:: python

    directory: StringProperty(subtype='DIR_PATH', options={'SKIP_SAVE', 'HIDDEN'})
    files: CollectionProperty(type=OperatorFileListElement, options={'SKIP_SAVE', 'HIDDEN'})

These ``directory`` and ``files`` properties will be set with the necessary data from the
drag-and-drop operation.

Additionally, if the operator provides operator properties that need to be accessible to the user,
the :class:`ImportHelper.invoke_popup` method can be used to show a dialog leveraging the standard
:class:`Operator.draw` method for layout and display.

.. literalinclude:: ./examples/bpy.types.FileHandler.2.py
   :lines: 22-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`IMAGE_FH_drop_handler`, :class:`IO_FH_gltf2`, :class:`IO_FH_svg_as_curves`, :class:`NODE_FH_image_node`, :class:`SEQUENCER_FH_image_strip`, :class:`SEQUENCER_FH_movie_strip`, :class:`SEQUENCER_FH_sound_strip`, :class:`VIEW3D_FH_camera_background_image`, :class:`VIEW3D_FH_empty_image`, :class:`VIEW3D_FH_vdb_volume`

.. class:: FileHandler(bpy_struct)

   Extends functionality to operators that manages files, such as adding drag and drop support

   .. attribute:: bl_export_operator

      Operator that can handle export for files with the extensions given in bl_file_extensions (default "", never None)

      :type: str

   .. attribute:: bl_file_extensions

      Formatted string of file extensions supported by the file handler, each extension should start with a "." and be separated by ";".
      For Example: ``".blend;.ble"``
      
      (default "", never None)

      :type: str

   .. attribute:: bl_idname

      If this is set, the file handler gets a custom ID, otherwise it takes the name of the class used to define the file handler (for example, if the class name is "OBJECT_FH_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_FH_hello") (default "", never None)

      :type: str

   .. attribute:: bl_import_operator

      Operator that can handle import for files with the extensions given in bl_file_extensions (default "", never None)

      :type: str

   .. attribute:: bl_label

      The file handler label (default "", never None)

      :type: str

   .. classmethod:: poll_drop(context)

      If this method returns True, can be used to handle the drop of a drag-and-drop action

      :type context: :class:`Context` | None
      :rtype: bool

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

