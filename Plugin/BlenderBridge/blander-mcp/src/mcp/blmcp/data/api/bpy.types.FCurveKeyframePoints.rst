FCurveKeyframePoints(bpy_prop_collection)
=========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop`, :class:`bpy_prop_collection`

.. class:: FCurveKeyframePoints(bpy_prop_collection)

   Collection of keyframe points

   .. method:: insert(frame, value, *, options=set(), keyframe_type='KEYFRAME')

      Add a keyframe point to a F-Curve

      :param frame: X Value of this keyframe point (in [-inf, inf])
      :type frame: float
      :param value: Y Value of this keyframe point (in [-inf, inf])
      :type value: float
      :param options: Keyframe options (optional)

         - ``REPLACE``
           Replace -- Don't add any new keyframes, but just replace existing ones.
         - ``NEEDED``
           Needed -- Only adds keyframes that are needed.
         - ``FAST``
           Fast -- Fast keyframe insertion to avoid recalculating the curve each time.
      :type options: set[Literal['REPLACE', 'NEEDED', 'FAST']]
      :param keyframe_type: Type of keyframe to insert (optional)
      :type keyframe_type: Literal[:ref:`rna_enum_beztriple_keyframe_type_items`]
      :return: Newly created keyframe
      :rtype: :class:`Keyframe`

   .. method:: add(count)

      Add a keyframe point to a F-Curve

      :param count: Number, Number of points to add to the spline (in [0, inf])
      :type count: int

   .. method:: remove(keyframe, *, fast=False)

      Remove keyframe from an F-Curve

      :param keyframe: Keyframe to remove (never None)
      :type keyframe: :class:`Keyframe` | None
      :param fast: Fast, Fast keyframe removal to avoid recalculating the curve each time (optional)
      :type fast: bool

   .. method:: clear()

      Remove all keyframes from an F-Curve


   .. method:: sort()

      Ensure all keyframe points are chronologically sorted


   .. method:: deduplicate()

      Ensure there are no duplicate keys. Assumes that the points have already been sorted


   .. method:: handles_recalc()

      Update handles after modifications to the keyframe points, to update things like auto-clamping


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

   - :class:`FCurve.keyframe_points`

