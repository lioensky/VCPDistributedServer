Paint(bpy_struct)
=================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`CurvesSculpt`, :class:`GpPaint`, :class:`GpSculptPaint`, :class:`GpVertexPaint`, :class:`GpWeightPaint`, :class:`ImagePaint`, :class:`Sculpt`, :class:`VertexPaint`

.. class:: Paint(bpy_struct)


   .. data:: brush

      Active brush (readonly)

      :type: :class:`Brush` | None

   .. data:: brush_asset_reference

      A weak reference to the matching brush asset, used e.g. to restore the last used brush on file load (readonly)

      :type: :class:`AssetWeakReference` | None

   .. data:: cavity_curve

      Editable cavity curve (readonly, never None)

      :type: :class:`CurveMapping`

   .. attribute:: eraser_brush

      Default eraser brush for quickly alternating with the main brush

      :type: :class:`Brush` | None

   .. data:: eraser_brush_asset_reference

      A weak reference to the matching brush asset, used e.g. to restore the last used brush on file load (readonly)

      :type: :class:`AssetWeakReference` | None

   .. attribute:: palette

      Active Palette

      :type: :class:`Palette` | None

   .. attribute:: show_brush

      (default True)

      :type: bool

   .. attribute:: show_brush_on_surface

      (default False)

      :type: bool

   .. attribute:: show_bvh_nodes

      Show the underlying BVH nodes as differently colored faces (default False)

      :type: bool

   .. attribute:: show_jitter_curve

      (default False)

      :type: bool

   .. attribute:: show_low_resolution

      For multires, show low resolution while navigating the view (default False)

      :type: bool

   .. attribute:: show_size_curve

      (default False)

      :type: bool

   .. attribute:: show_strength_curve

      (default False)

      :type: bool

   .. attribute:: tile_offset

      Stride at which tiled strokes are copied (array of 3 items, in [0.01, inf], default (1.0, 1.0, 1.0))

      :type: :class:`mathutils.Vector`

   .. attribute:: tile_x

      Tile along X axis (default False)

      :type: bool

   .. attribute:: tile_y

      Tile along Y axis (default False)

      :type: bool

   .. attribute:: tile_z

      Tile along Z axis (default False)

      :type: bool

   .. data:: unified_paint_settings

      (readonly, never None)

      :type: :class:`UnifiedPaintSettings`

   .. attribute:: use_cavity

      Mask painting according to mesh geometry cavity (default False)

      :type: bool

   .. attribute:: use_sculpt_delay_updates

      Update the geometry when it enters the view, providing faster view navigation (default False)

      :type: bool

   .. attribute:: use_symmetry_feather

      Reduce the strength of the brush where it overlaps symmetrical daubs (default True)

      :type: bool

   .. attribute:: use_symmetry_x

      Mirror brush across the X axis (default False)

      :type: bool

   .. attribute:: use_symmetry_y

      Mirror brush across the Y axis (default False)

      :type: bool

   .. attribute:: use_symmetry_z

      Mirror brush across the Z axis (default False)

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

