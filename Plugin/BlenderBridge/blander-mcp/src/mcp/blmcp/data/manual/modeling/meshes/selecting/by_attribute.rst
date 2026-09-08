.. _bpy.ops.mesh.select_by_attribute:

************
By Attribute
************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> By Attribute`

Selects the vertices, edges, or faces for which the currently active
:doc:`attribute </modeling/geometry_nodes/attributes_reference>` has a value of True.

The active attribute is the one which is currently selected in the
:ref:`Attributes list <bpy.types.AttributeGroup>` of the :doc:`/editors/properties_editor`.

.. note::

   The attribute must have a :ref:`domain <attribute-domains>` of Vertex, Edge, or Face,
   and a :ref:`type <attribute-data-types>` of Boolean.
