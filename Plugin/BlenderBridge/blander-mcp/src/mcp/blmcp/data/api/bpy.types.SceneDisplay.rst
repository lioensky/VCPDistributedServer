SceneDisplay(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SceneDisplay(bpy_struct)

   Scene display settings for 3D viewport

   .. attribute:: light_direction

      Direction of the light for shadows and highlights (array of 3 items, in [-inf, inf], default (0.57735, 0.57735, 0.57735))

      :type: :class:`mathutils.Vector`

   .. attribute:: matcap_ssao_attenuation

      Attenuation constant (in [0, 100000], default 1.0)

      :type: float

   .. attribute:: matcap_ssao_distance

      Distance of object that contribute to the cavity/edge effect (in [0, 100000], default 0.2)

      :type: float

   .. attribute:: matcap_ssao_samples

      Number of samples (in [1, 500], default 16)

      :type: int

   .. attribute:: render_aa

      Method of anti-aliasing when rendering final image (default ``'8'``)

      - ``OFF``
        No Anti-Aliasing -- Scene will be rendering without any anti-aliasing.
      - ``FXAA``
        Single Pass Anti-Aliasing -- Scene will be rendered using a single pass anti-aliasing method (FXAA).
      - ``5``
        5 Samples -- Scene will be rendered using 5 anti-aliasing samples.
      - ``8``
        8 Samples -- Scene will be rendered using 8 anti-aliasing samples.
      - ``11``
        11 Samples -- Scene will be rendered using 11 anti-aliasing samples.
      - ``16``
        16 Samples -- Scene will be rendered using 16 anti-aliasing samples.
      - ``32``
        32 Samples -- Scene will be rendered using 32 anti-aliasing samples.

      :type: Literal['OFF', 'FXAA', '5', '8', '11', '16', '32']

   .. data:: shading

      Shading settings for OpenGL render engine (readonly)

      :type: :class:`View3DShading` | None

   .. attribute:: shadow_focus

      Shadow factor hardness (in [0, 1], default 0.0)

      :type: float

   .. attribute:: shadow_shift

      Shadow termination angle (in [0, 1], default 0.1)

      :type: float

   .. attribute:: viewport_aa

      Method of anti-aliasing when rendering 3d viewport (default ``'FXAA'``)

      - ``OFF``
        No Anti-Aliasing -- Scene will be rendering without any anti-aliasing.
      - ``FXAA``
        Single Pass Anti-Aliasing -- Scene will be rendered using a single pass anti-aliasing method (FXAA).
      - ``5``
        5 Samples -- Scene will be rendered using 5 anti-aliasing samples.
      - ``8``
        8 Samples -- Scene will be rendered using 8 anti-aliasing samples.
      - ``11``
        11 Samples -- Scene will be rendered using 11 anti-aliasing samples.
      - ``16``
        16 Samples -- Scene will be rendered using 16 anti-aliasing samples.
      - ``32``
        32 Samples -- Scene will be rendered using 32 anti-aliasing samples.

      :type: Literal['OFF', 'FXAA', '5', '8', '11', '16', '32']

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

   - :class:`Scene.display`

