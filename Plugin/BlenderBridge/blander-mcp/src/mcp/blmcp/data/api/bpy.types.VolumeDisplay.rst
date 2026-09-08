VolumeDisplay(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: VolumeDisplay(bpy_struct)

   Volume object display settings for 3D viewport

   .. attribute:: density

      Thickness of volume display in the viewport (in [1e-05, inf], default 1.0)

      :type: float

   .. attribute:: interpolation_method

      Interpolation method to use for volumes in solid mode (default ``'LINEAR'``)

      - ``LINEAR``
        Linear -- Good smoothness and speed.
      - ``CUBIC``
        Cubic -- Smoothed high quality interpolation, but slower.
      - ``CLOSEST``
        Closest -- No interpolation.

      :type: Literal['LINEAR', 'CUBIC', 'CLOSEST']

   .. attribute:: slice_axis

      (default ``'AUTO'``)

      - ``AUTO``
        Auto -- Adjust slice direction according to the view direction.
      - ``X``
        X -- Slice along the X axis.
      - ``Y``
        Y -- Slice along the Y axis.
      - ``Z``
        Z -- Slice along the Z axis.

      :type: Literal['AUTO', 'X', 'Y', 'Z']

   .. attribute:: slice_depth

      Position of the slice (in [0, 1], default 0.5)

      :type: float

   .. attribute:: use_slice

      Perform a single slice of the domain object (default False)

      :type: bool

   .. attribute:: wireframe_detail

      Amount of detail for wireframe display (default ``'COARSE'``)

      - ``COARSE``
        Coarse -- Display one box or point for each intermediate tree node.
      - ``FINE``
        Fine -- Display box for each leaf node containing 8×8 voxels.

      :type: Literal['COARSE', 'FINE']

   .. attribute:: wireframe_type

      Type of wireframe display (default ``'BOXES'``)

      - ``NONE``
        None -- Don't display volume in wireframe mode.
      - ``BOUNDS``
        Bounds -- Display single bounding box for the entire grid.
      - ``BOXES``
        Boxes -- Display bounding boxes for nodes in the volume tree.
      - ``POINTS``
        Points -- Display points for nodes in the volume tree.

      :type: Literal['NONE', 'BOUNDS', 'BOXES', 'POINTS']

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

   - :class:`Volume.display`

