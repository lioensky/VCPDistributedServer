GeometryAttributeConstraint(Constraint)
=======================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: GeometryAttributeConstraint(Constraint)

   Create a constraint-based relationship with an attribute from geometry

   .. attribute:: apply_target_transform

      Apply the target object's world transform on top of the attribute's transform (default False)

      :type: bool

   .. attribute:: attribute_name

      Name of the attribute to retrieve the transform from (default "", never None)

      :type: str

   .. attribute:: data_type

      Select data type of attribute (default ``'VECTOR'``)

      - ``VECTOR``
        Vector -- Vector data type, affects position.
      - ``QUATERNION``
        Quaternion -- Quaternion data type, affects rotation.
      - ``FLOAT4X4``
        4x4 Matrix -- 4x4 Matrix data type, affects transform.

      :type: Literal['VECTOR', 'QUATERNION', 'FLOAT4X4']

   .. attribute:: domain

      Attribute domain (default ``'POINT'``)

      :type: Literal['POINT', 'EDGE', 'FACE', 'FACE_CORNER', 'CURVE', 'INSTANCE']

   .. attribute:: mix_loc

      Mix Location (default False)

      :type: bool

   .. attribute:: mix_mode

      Specify how the copied and existing transformations are combined (default ``'REPLACE'``)

      - ``REPLACE``
        Replace -- Replace the original transformation with the transform from the attribute.
      - ``BEFORE_FULL``
        Before Original (Full) -- Apply copied transformation before original, using simple matrix multiplication as if the constraint target is a parent in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..
      - ``BEFORE_SPLIT``
        Before Original (Split Channels) -- Apply copied transformation before original, handling location, rotation and scale separately, similar to a sequence of three Copy constraints.
      - ``AFTER_FULL``
        After Original (Full) -- Apply copied transformation after original, using simple matrix multiplication as if the constraint target is a child in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..
      - ``AFTER_SPLIT``
        After Original (Split Channels) -- Apply copied transformation after original, handling location, rotation and scale separately, similar to a sequence of three Copy constraints.

      :type: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER_SPLIT']

   .. attribute:: mix_rot

      Mix Rotation (default False)

      :type: bool

   .. attribute:: mix_scl

      Mix Scale (default False)

      :type: bool

   .. attribute:: sample_index

      Sample Index (in [0, inf], default 0)

      :type: int

   .. attribute:: target

      Target geometry object

      :type: :class:`Object` | None

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
   - :class:`Constraint.name`
   - :class:`Constraint.type`
   - :class:`Constraint.is_override_data`
   - :class:`Constraint.owner_space`
   - :class:`Constraint.target_space`
   - :class:`Constraint.space_object`
   - :class:`Constraint.space_subtarget`
   - :class:`Constraint.mute`
   - :class:`Constraint.enabled`
   - :class:`Constraint.show_expanded`
   - :class:`Constraint.is_valid`
   - :class:`Constraint.active`
   - :class:`Constraint.influence`
   - :class:`Constraint.error_location`
   - :class:`Constraint.error_rotation`

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
   - :class:`Constraint.bl_rna_get_subclass`
   - :class:`Constraint.bl_rna_get_subclass_py`

