SpaceNodeOverlay(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SpaceNodeOverlay(bpy_struct)

   Settings for display of overlays in the Node Editor

   .. attribute:: preview_shape

      Preview shape used by the node previews (default ``'FLAT'``)

      - ``FLAT``
        Flat -- Use the default flat previews.
      - ``3D``
        3D -- Use the material preview scene for the node previews.

      :type: Literal['FLAT', '3D']

   .. attribute:: show_context_path

      Display breadcrumbs for the editor's context (default True)

      :type: bool

   .. attribute:: show_named_attributes

      Show when nodes are using named attributes (default True)

      :type: bool

   .. attribute:: show_overlays

      Display overlays like colored or dashed wires (default True)

      :type: bool

   .. attribute:: show_previews

      Display each node's preview if node is toggled (default False)

      :type: bool

   .. attribute:: show_reroute_auto_labels

      Label reroute nodes based on the label of connected reroute nodes (default False)

      :type: bool

   .. attribute:: show_timing

      Display each node's last execution time (default False)

      :type: bool

   .. attribute:: show_wire_color

      Color node links based on their connected sockets (default True)

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

   - :class:`SpaceNodeEditor.overlay`

