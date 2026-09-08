.. index:: Geometry Nodes; Material Selection
.. _bpy.types.GeometryNodeMaterialSelection:

***********************
Material Selection Node
***********************

.. figure:: /images/modeling_geometry-nodes_material_material-selection_node.png
   :align: right
   :alt: Material Selection node.

The *Material Selection* node provides a selection for meshes that use this material.
Since the ``material_index`` is stored on each face, the output will be implicitly interpolated to
a different domain when necessary. For example, every vertex connected to
a selected face will be selected.


Inputs
======

Material
   Standard material input.


Outputs
=======

Selection
   Selection of faces that use the input material.
