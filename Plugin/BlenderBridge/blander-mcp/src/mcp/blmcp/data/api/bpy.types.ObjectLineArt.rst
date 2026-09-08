ObjectLineArt(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ObjectLineArt(bpy_struct)

   Object Line Art settings

   .. attribute:: crease_threshold

      Angles smaller than this will be treated as creases (in [0, 3.14159], default 2.44346)

      :type: float

   .. attribute:: intersection_priority

      The intersection line will be included into the object with the higher intersection priority value (in [0, 255], default 0)

      :type: int

   .. attribute:: usage

      How to use this object in Line Art calculation (default ``'INHERIT'``)

      - ``INHERIT``
        Inherit -- Use settings from the parent collection.
      - ``INCLUDE``
        Include -- Generate feature lines for this object's data.
      - ``OCCLUSION_ONLY``
        Occlusion Only -- Only use the object data to produce occlusion.
      - ``EXCLUDE``
        Exclude -- Don't use this object for Line Art rendering.
      - ``INTERSECTION_ONLY``
        Intersection Only -- Only generate intersection lines for this collection.
      - ``NO_INTERSECTION``
        No Intersection -- Include this object but do not generate intersection lines.
      - ``FORCE_INTERSECTION``
        Force Intersection -- Generate intersection lines even with objects that disabled intersection.

      :type: Literal['INHERIT', 'INCLUDE', 'OCCLUSION_ONLY', 'EXCLUDE', 'INTERSECTION_ONLY', 'NO_INTERSECTION', 'FORCE_INTERSECTION']

   .. attribute:: use_crease_override

      Use this object's crease setting to overwrite scene global (default False)

      :type: bool

   .. attribute:: use_intersection_priority_override

      Use this object's intersection priority to override collection setting (default False)

      :type: bool

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

   - :class:`Object.lineart`

