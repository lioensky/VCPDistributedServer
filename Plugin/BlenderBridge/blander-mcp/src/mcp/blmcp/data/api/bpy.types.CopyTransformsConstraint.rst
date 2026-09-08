CopyTransformsConstraint(Constraint)
====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: CopyTransformsConstraint(Constraint)

   Copy all the transforms of the target

   .. attribute:: head_tail

      Target along length of bone: Head is 0, Tail is 1 (in [0, 1], default 0.0)

      :type: float

   .. attribute:: mix_mode

      Specify how the copied and existing transformations are combined (default ``'REPLACE'``)

      - ``REPLACE``
        Replace -- Replace the original transformation with copied.
      - ``BEFORE_FULL``
        Before Original (Full) -- Apply copied transformation before original, using simple matrix multiplication as if the constraint target is a parent in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..
      - ``BEFORE``
        Before Original (Aligned) -- Apply copied transformation before original, as if the constraint target is a parent in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale..
      - ``BEFORE_SPLIT``
        Before Original (Split Channels) -- Apply copied transformation before original, handling location, rotation and scale separately, similar to a sequence of three Copy constraints.
      - ``AFTER_FULL``
        After Original (Full) -- Apply copied transformation after original, using simple matrix multiplication as if the constraint target is a child in Full Inherit Scale mode. Will create shear when combining rotation and non-uniform scale..
      - ``AFTER``
        After Original (Aligned) -- Apply copied transformation after original, as if the constraint target is a child in Aligned Inherit Scale mode. This effectively uses Full for location and Split Channels for rotation and scale..
      - ``AFTER_SPLIT``
        After Original (Split Channels) -- Apply copied transformation after original, handling location, rotation and scale separately, similar to a sequence of three Copy constraints.

      :type: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']

   .. attribute:: remove_target_shear

      Remove shear from the target transformation before combining (default False)

      :type: bool

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ... (default "", never None)

      :type: str

   .. attribute:: target

      Target object

      :type: :class:`Object` | None

   .. attribute:: use_bbone_shape

      Follow shape of B-Bone segments when calculating Head/Tail position (default False)

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

