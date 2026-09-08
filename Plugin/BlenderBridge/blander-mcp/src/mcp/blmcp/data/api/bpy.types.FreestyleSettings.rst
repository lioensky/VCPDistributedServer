FreestyleSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FreestyleSettings(bpy_struct)

   Freestyle settings for a ViewLayer data-block

   .. attribute:: as_render_pass

      Renders Freestyle output to a separate pass instead of overlaying it on the Combined pass (default False)

      :type: bool

   .. attribute:: crease_angle

      Angular threshold for detecting crease edges (in [0, 3.14159], default 0.0)

      :type: float

   .. attribute:: kr_derivative_epsilon

      Kr derivative epsilon for computing suggestive contours (in [-1000, 1000], default 0.0)

      :type: float

   .. data:: linesets

      (default None, readonly)

      :type: :class:`Linesets`\ [:class:`FreestyleLineSet`]

   .. attribute:: mode

      Select the Freestyle control mode (default ``'SCRIPT'``)

      - ``SCRIPT``
        Python Scripting -- Advanced mode for using style modules written in Python.
      - ``EDITOR``
        Parameter Editor -- Basic mode for interactive style parameter editing.

      :type: Literal['SCRIPT', 'EDITOR']

   .. data:: modules

      A list of style modules (to be applied from top to bottom) (default None, readonly)

      :type: :class:`FreestyleModules`\ [:class:`FreestyleModuleSettings`]

   .. attribute:: sphere_radius

      Sphere radius for computing curvatures (in [0, 1000], default 1.0)

      :type: float

   .. attribute:: use_culling

      If enabled, out-of-view edges are ignored (default False)

      :type: bool

   .. attribute:: use_material_boundaries

      Enable material boundaries (default False)

      :type: bool

   .. attribute:: use_ridges_and_valleys

      Enable ridges and valleys (default False)

      :type: bool

   .. attribute:: use_smoothness

      Take face smoothness into account in view map calculation (default False)

      :type: bool

   .. attribute:: use_suggestive_contours

      Enable suggestive contours (default False)

      :type: bool

   .. attribute:: use_view_map_cache

      Keep the computed view map and avoid recalculating it if mesh geometry is unchanged (default False)

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

   - :class:`ViewLayer.freestyle_settings`

