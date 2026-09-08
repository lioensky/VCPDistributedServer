ActionChannelbagFCurves(bpy_prop_collection)
============================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: ActionChannelbagFCurves(bpy_prop_collection)

   Collection of F-Curves for a specific action slot, on a specific strip

   .. method:: new(data_path, *, index=0, group_name="")

      Add an F-Curve to the channelbag

      :param data_path: Data Path, F-Curve data path to use (never None)
      :type data_path: str
      :param index: Index, Array index (in [0, inf], optional)
      :type index: int
      :param group_name: Group Name, Name of the Group for this F-Curve, will be created if it does not exist yet (optional, never None)
      :type group_name: str
      :return: Newly created F-Curve
      :rtype: :class:`FCurve`

   .. method:: new_from_fcurve(source, *, data_path="")

      Copy an F-Curve into the channelbag. The original F-Curve is unchanged

      :param source: Source F-Curve, The F-Curve to copy
      :type source: :class:`FCurve` | None
      :param data_path: Data Path, F-Curve data path to use. If not provided, this will use the same data path as the given F-Curve (optional, never None)
      :type data_path: str
      :return: Newly created F-Curve
      :rtype: :class:`FCurve`

   .. method:: ensure(data_path, *, index=0, group_name="")

      Returns the F-Curve if it already exists, and creates it if necessary

      :param data_path: Data Path, F-Curve data path to use (never None)
      :type data_path: str
      :param index: Index, Array index (in [0, inf], optional)
      :type index: int
      :param group_name: Group Name, Name of the Group for this F-Curve, will be created if it does not exist yet. This parameter is ignored if the F-Curve already exists (optional, never None)
      :type group_name: str
      :return: Found or newly created F-Curve
      :rtype: :class:`FCurve`

   .. method:: find(data_path, *, index=0)

      Find an F-Curve. Note that this function performs a linear scan of all F-Curves in the channelbag.

      :param data_path: Data Path, F-Curve data path (never None)
      :type data_path: str
      :param index: Index, Array index (in [0, inf], optional)
      :type index: int
      :return: The found F-Curve, or None if it does not exist
      :rtype: :class:`FCurve`

   .. method:: remove(fcurve)

      Remove F-Curve

      :param fcurve: F-Curve to remove (never None)
      :type fcurve: :class:`FCurve` | None

   .. method:: clear()

      Remove all F-Curves from this channelbag


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

   - :class:`ActionChannelbag.fcurves`

