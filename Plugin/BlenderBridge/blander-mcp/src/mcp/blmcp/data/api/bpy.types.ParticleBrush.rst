ParticleBrush(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleBrush(bpy_struct)

   Particle editing brush

   .. attribute:: count

      Particle count (in [1, 1000], default 10)

      :type: int

   .. data:: curve

      (readonly)

      :type: :class:`CurveMapping` | None

   .. attribute:: length_mode

      (default ``'GROW'``)

      - ``GROW``
        Grow -- Make hairs longer.
      - ``SHRINK``
        Shrink -- Make hairs shorter.

      :type: Literal['GROW', 'SHRINK']

   .. attribute:: puff_mode

      (default ``'ADD'``)

      - ``ADD``
        Add -- Make hairs more puffy.
      - ``SUB``
        Sub -- Make hairs less puffy.

      :type: Literal['ADD', 'SUB']

   .. attribute:: size

      Radius of the brush in pixels (in [1, 32767], default 50)

      :type: int

   .. attribute:: steps

      Brush steps (in [1, 32767], default 10)

      :type: int

   .. attribute:: strength

      Brush strength (in [0.001, 1], default 0.5)

      :type: float

   .. attribute:: use_puff_volume

      Apply puff to unselected end-points (helps maintain hair volume when puffing root) (default False)

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

   - :class:`ParticleEdit.brush`

