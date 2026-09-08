FreestyleLineSet(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FreestyleLineSet(bpy_struct)

   Line set for associating lines and style parameters

   .. attribute:: collection

      A collection of objects based on which feature edges are selected

      :type: :class:`Collection` | None

   .. attribute:: collection_negation

      Specify either inclusion or exclusion of feature edges belonging to a collection of objects (default ``'INCLUSIVE'``)

      - ``INCLUSIVE``
        Inclusive -- Select feature edges belonging to some object in the group.
      - ``EXCLUSIVE``
        Exclusive -- Select feature edges not belonging to any object in the group.

      :type: Literal['INCLUSIVE', 'EXCLUSIVE']

   .. attribute:: edge_type_combination

      Specify a logical combination of selection conditions on feature edge types (default ``'OR'``)

      - ``OR``
        Logical OR -- Select feature edges satisfying at least one of edge type conditions.
      - ``AND``
        Logical AND -- Select feature edges satisfying all edge type conditions.

      :type: Literal['OR', 'AND']

   .. attribute:: edge_type_negation

      Specify either inclusion or exclusion of feature edges selected by edge types (default ``'INCLUSIVE'``)

      - ``INCLUSIVE``
        Inclusive -- Select feature edges satisfying the given edge type conditions.
      - ``EXCLUSIVE``
        Exclusive -- Select feature edges not satisfying the given edge type conditions.

      :type: Literal['INCLUSIVE', 'EXCLUSIVE']

   .. attribute:: exclude_border

      Exclude border edges (default False)

      :type: bool

   .. attribute:: exclude_contour

      Exclude contours (default False)

      :type: bool

   .. attribute:: exclude_crease

      Exclude crease edges (default False)

      :type: bool

   .. attribute:: exclude_edge_mark

      Exclude edge marks (default False)

      :type: bool

   .. attribute:: exclude_external_contour

      Exclude external contours (default False)

      :type: bool

   .. attribute:: exclude_material_boundary

      Exclude edges at material boundaries (default False)

      :type: bool

   .. attribute:: exclude_ridge_valley

      Exclude ridges and valleys (default False)

      :type: bool

   .. attribute:: exclude_silhouette

      Exclude silhouette edges (default False)

      :type: bool

   .. attribute:: exclude_suggestive_contour

      Exclude suggestive contours (default False)

      :type: bool

   .. attribute:: face_mark_condition

      Specify a feature edge selection condition based on face marks (default ``'ONE'``)

      - ``ONE``
        One Face -- Select a feature edge if either of its adjacent faces is marked.
      - ``BOTH``
        Both Faces -- Select a feature edge if both of its adjacent faces are marked.

      :type: Literal['ONE', 'BOTH']

   .. attribute:: face_mark_negation

      Specify either inclusion or exclusion of feature edges selected by face marks (default ``'INCLUSIVE'``)

      - ``INCLUSIVE``
        Inclusive -- Select feature edges satisfying the given face mark conditions.
      - ``EXCLUSIVE``
        Exclusive -- Select feature edges not satisfying the given face mark conditions.

      :type: Literal['INCLUSIVE', 'EXCLUSIVE']

   .. attribute:: linestyle

      Line style settings (never None)

      :type: :class:`FreestyleLineStyle`

   .. attribute:: name

      Line set name (default "", never None)

      :type: str

   .. attribute:: qi_end

      Last QI value of the QI range (in [0, inf], default 0)

      :type: int

   .. attribute:: qi_start

      First QI value of the QI range (in [0, inf], default 0)

      :type: int

   .. attribute:: select_border

      Select border edges (open mesh edges) (default False)

      :type: bool

   .. attribute:: select_by_collection

      Select feature edges based on a collection of objects (default False)

      :type: bool

   .. attribute:: select_by_edge_types

      Select feature edges based on edge types (default False)

      :type: bool

   .. attribute:: select_by_face_marks

      Select feature edges by face marks (default False)

      :type: bool

   .. attribute:: select_by_image_border

      Select feature edges by image border (less memory consumption) (default False)

      :type: bool

   .. attribute:: select_by_visibility

      Select feature edges based on visibility (default False)

      :type: bool

   .. attribute:: select_contour

      Select contours (outer silhouettes of each object) (default False)

      :type: bool

   .. attribute:: select_crease

      Select crease edges (those between two faces making an angle smaller than the Crease Angle) (default False)

      :type: bool

   .. attribute:: select_edge_mark

      Select edge marks (edges annotated by Freestyle edge marks) (default False)

      :type: bool

   .. attribute:: select_external_contour

      Select external contours (outer silhouettes of occluding and occluded objects) (default False)

      :type: bool

   .. attribute:: select_material_boundary

      Select edges at material boundaries (default False)

      :type: bool

   .. attribute:: select_ridge_valley

      Select ridges and valleys (boundary lines between convex and concave areas of surface) (default False)

      :type: bool

   .. attribute:: select_silhouette

      Select silhouettes (edges at the boundary of visible and hidden faces) (default False)

      :type: bool

   .. attribute:: select_suggestive_contour

      Select suggestive contours (almost silhouette/contour edges) (default False)

      :type: bool

   .. attribute:: show_render

      Enable or disable this line set during stroke rendering (default False)

      :type: bool

   .. attribute:: visibility

      Determine how to use visibility for feature edge selection (default ``'VISIBLE'``)

      - ``VISIBLE``
        Visible -- Select visible feature edges.
      - ``HIDDEN``
        Hidden -- Select hidden feature edges.
      - ``RANGE``
        Quantitative Invisibility -- Select feature edges within a range of quantitative invisibility (QI) values.

      :type: Literal['VISIBLE', 'HIDDEN', 'RANGE']

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

   - :class:`Linesets.active`
   - :class:`Linesets.new`
   - :class:`Linesets.remove`
   - :class:`FreestyleSettings.linesets`

