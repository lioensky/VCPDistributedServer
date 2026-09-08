MeshLoopTriangle(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshLoopTriangle(bpy_struct)

   Tessellated triangle in a Mesh data-block

   .. data:: area

      Area of this triangle (in [0, inf], default 0.0, readonly)

      :type: float

   .. data:: index

      Index of this loop triangle (in [0, inf], default 0, readonly)

      :type: int

   .. data:: loops

      Indices of mesh loops that make up the triangle (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: material_index

      Material slot index of this triangle (in [0, inf], default 0, readonly)

      :type: int

   .. data:: normal

      Local space unit length normal vector for this triangle (array of 3 items, in [-1, 1], default (0.0, 0.0, 0.0), readonly)

      :type: :class:`mathutils.Vector`

   .. data:: polygon_index

      Index of mesh face that the triangle is a part of (in [0, inf], default 0, readonly)

      :type: int

   .. data:: split_normals

      Local space unit length custom normal vectors of the face corners of this triangle (multi-dimensional array of 3 * 3 items, in [-1, 1], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), readonly)

      :type: :class:`bpy_prop_array`\ [float]

   .. data:: use_smooth

      (default False, readonly)

      :type: bool

   .. data:: vertices

      Indices of triangle vertices (array of 3 items, in [0, inf], default (0, 0, 0), readonly)

      :type: :class:`bpy_prop_array`\ [int]

   .. data:: center

      The midpoint of the face.

      (readonly)

   .. data:: edge_keys


      (readonly)

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

   - :class:`Mesh.loop_triangles`

