ColorManagedDisplaySettings(bpy_struct)
=======================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorManagedDisplaySettings(bpy_struct)

   Color management specific to display device

   .. attribute:: display_device

      Display name. For viewing, this is the display device that will be emulated by limiting the gamut and HDR colors. For image and video output, this is the display space used for writing. (default ``'NONE'``)

      :type: Literal['NONE']

   .. attribute:: emulation

      Control how images in the chosen display are mapped to the physical display (default ``'AUTO'``)

      - ``OFF``
        Off -- Directly output image as produced by OpenColorIO. This is not correct in general, but may be used when the system configuration and actual display device is known to match the chosen display.
      - ``AUTO``
        Automatic -- Display images consistent with most other applications, to preview images and video for export. A best effort is made to emulate the chosen display on the actual display device..

      :type: Literal['OFF', 'AUTO']

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

   - :class:`CompositorNodeConvertToDisplay.display_settings`
   - :class:`ImageFormatSettings.display_settings`
   - :class:`Scene.display_settings`

