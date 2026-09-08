
***************
Data Properties
***************

.. figure:: /images/grease-pencil_properties_data_panel.png
   :align: right

   Grease Pencil Object Data.

Grease Pencil
   The Grease Pencil :ref:`data-block menu <ui-data-block>` can be used to link the data between objects.


:doc:`Layers </grease_pencil/properties/layers>`
================================================

Strokes can be grouped in 2D layers, a special Grease Pencil layers
that help to organize the drawing order and visibility of the strokes.
Layers can be organized into layer groups.


:doc:`Onion Skinning </grease_pencil/properties/onion_skinning>`
================================================================

Onion skinning is used in animation to see several frames at once and make decisions or
edits based on how the previous/next frames are drawn.


:doc:`Settings </grease_pencil/properties/strokes>`
===================================================

General settings for Grease Pencil strokes.


.. _bpy.types.AttributeGroupGreasePencil:

Attributes
==========

Layers can store :doc:`Custom Attributes </modeling/geometry_nodes/attributes_reference>`.
The attributes are stored on the :ref:`Layer <attribute-domains>` domain.

For example, the :ref:`Layer Adjustments <layer-adjustments>` are stored as layer attributes.

Attributes
   :ref:`List view <ui-list-view>` of all the attributes stored on the layers.

   Name
      Name of the layer attribute.

   Data Type
      The :ref:`Data Type <attribute-data-types>` of the attribute.


:doc:`Vertex Groups </modeling/meshes/properties/vertex_groups/index>`
======================================================================

Vertex groups can be used to assign a group or weighted group to some operator.
An object can have several weight groups and can be assigned in
:doc:`Weight Paint Mode </grease_pencil/modes/weight_paint/index>`.


:ref:`Custom Properties <files-data_blocks-custom-properties>`
==============================================================

Create and manage your own properties to store data in the Grease Pencil's data-block.

.. toctree::
   :maxdepth: 2
   :hidden:

   layers.rst
   onion_skinning.rst
   strokes.rst

