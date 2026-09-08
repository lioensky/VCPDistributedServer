Import Curve Operators
======================

.. module:: bpy.ops.import_curve

.. function:: svg(*, filepath="", filter_glob="*.svg", directory="", files=None)

   Load a SVG file

   :param filepath: File Path, Filepath used for importing the file (optional, never None)
   :type filepath: str
   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param directory: directory, (optional, never None)
   :type directory: str
   :param files: File Path, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core/io_curve_svg/__init__.py\:61 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_curve_svg/__init__.py#L61>`__


