bpy_extras submodule (bpy_extras.io_utils)
==========================================

.. module:: bpy_extras.io_utils

.. function:: orientation_helper(axis_forward='Y', axis_up='Z')

   A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
   with specified default values (axes).
   
   :param axis_forward: The default forward axis.
   :type axis_forward: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param axis_up: The default up axis.
   :type axis_up: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :return: A class decorator.
   :rtype: Callable[[type], type]

.. function:: axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z')

   Each argument is an axis
   where the first 2 are a source and the second 2 are the target.
   
   :param from_forward: Source forward axis.
   :type from_forward: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param from_up: Source up axis.
   :type from_up: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param to_forward: Target forward axis.
   :type to_forward: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :param to_up: Target up axis.
   :type to_up: Literal['X', 'Y', 'Z', '-X', '-Y', '-Z']
   :return: The conversion matrix.
   :rtype: :class:`mathutils.Matrix`

.. function:: axis_conversion_ensure(operator, forward_attr, up_attr)

   Function to ensure an operator has valid axis conversion settings, intended
   to be used from :class:`bpy.types.Operator.check`.
   
   :param operator: the operator to access axis attributes from.
   :type operator: :class:`bpy.types.Operator`
   :param forward_attr: attribute storing the forward axis
   :type forward_attr: str
   :param up_attr: attribute storing the up axis
   :type up_attr: str
   :return: True if the value was modified.
   :rtype: bool

.. function:: create_derived_objects(depsgraph, objects)

   This function takes a sequence of objects, returning their instances.
   
   :param depsgraph: The evaluated depsgraph.
   :type depsgraph: :class:`bpy.types.Depsgraph`
   :param objects: A sequence of objects.
   :type objects: Sequence[:class:`bpy.types.Object`]
   :return: A dictionary where each key is an object from ``objects``,
      values are lists of (object, matrix) tuples representing instances.
   :rtype: dict[:class:`bpy.types.Object`, list[tuple[:class:`bpy.types.Object`, :class:`mathutils.Matrix`]]]

.. function:: poll_file_object_drop(context)

   A default implementation for FileHandler poll_drop methods. Allows for both the 3D Viewport and
   the Outliner (in ViewLayer display mode) to be targets for file drag and drop.
   
   :param context: The context.
   :type context: :class:`bpy.types.Context`
   :return: Whether the drop target is valid.
   :rtype: bool

.. function:: unpack_list(list_of_tuples)

   Flatten a sequence of tuples into a single list.
   
   :param list_of_tuples: A sequence of tuples to unpack.
   :type list_of_tuples: Sequence[tuple]
   :return: A flat list of all values.
   :rtype: list

.. function:: unpack_face_list(list_of_tuples)

   Unpack a list of faces (triangles or quads) into a flat list,
   padding triangles with a zero to fit into groups of four.
   
   :param list_of_tuples: A sequence of face index tuples (3 or 4 elements each).
   :type list_of_tuples: Sequence[tuple[int, ...]]
   :return: A flat list of face indices, padded with zeros.
   :rtype: list[int]

.. function:: path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None)

   Return a filepath relative to a destination directory, for use with
   exporters.
   
   :param filepath: the file path to return,
      supporting blenders relative '//' prefix.
   :type filepath: str
   :param base_src: the directory the *filepath* is relative to
      (normally the blend file).
   :type base_src: str
   :param base_dst: the directory the *filepath* will be referenced from
      (normally the export path).
   :type base_dst: str
   :param mode: the method used to reference the path.
   :type mode: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
   :param copy_subdir: the subdirectory of *base_dst* to use when mode='COPY'.
   :type copy_subdir: str
   :param copy_set: collect from/to pairs when mode='COPY',
      pass to *path_reference_copy* when exporting is done.
   :type copy_set: set[tuple[str, str]] | None
   :param library: The library this path is relative to.
   :type library: :class:`bpy.types.Library` | None
   :return: the new filepath.
   :rtype: str

.. function:: path_reference_copy(copy_set, report=<built-in function print>)

   Execute copying files of path_reference
   
   :param copy_set: set of (from, to) pairs to copy.
   :type copy_set: set[tuple[str, str]]
   :param report: function used for reporting warnings, takes a string argument.
   :type report: Callable[[str], None]

.. function:: unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.')

   Helper function for storing unique names which may have special characters
   stripped and restricted to a maximum length.
   
   :param key: Unique item this name belongs to, name_dict[key] will be reused
      when available.
      This can be the object, mesh, material, etc instance itself.
      Any hashable object associated with the *name*.
   :type key: Any
   :param name: The name used to create a unique value in *name_dict*.
   :type name: str
   :param name_dict: This is used to cache namespace to ensure no collisions
      occur, this should be an empty dict initially and only modified by this
      function.
   :type name_dict: dict[Any, str]
   :param name_max: Maximum length of the name. When ``-1`` the name is unlimited.
   :type name_max: int
   :param clean_func: Function to call on *name* before creating a unique value.
   :type clean_func: Callable[[str], str] | None
   :param sep: Separator to use when between the name and a number when a
      duplicate name is found.
   :type sep: str
   :return: A unique name.
   :rtype: str

.. class:: ExportHelper


   .. method:: check(_context)

      Validate the filepath and axis conversion settings.
      
      :return: True when a property was updated.
      :rtype: bool

   .. method:: invoke(context, _event)

      Invoke the file selector for exporting, setting a default filepath
      based on the current blend file name.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :return: The operator return value.
      :rtype: set[str]



.. class:: ImportHelper


   .. method:: check(_context)

      Validate axis conversion settings.
      
      :return: True when a property was updated.
      :rtype: bool

   .. method:: invoke(context, _event)

      Invoke the file selector for importing.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :return: The operator return value.
      :rtype: set[str]

   .. method:: invoke_popup(context, confirm_text='')

      Invoke as a popup confirmation dialog when a filepath is already set,
      otherwise fall back to the file selector.
      
      :param context: The context.
      :type context: :class:`bpy.types.Context`
      :param confirm_text: Label for the confirm button,
         defaults to the operator label.
      :type confirm_text: str
      :return: The operator return value.
      :rtype: set[str]



