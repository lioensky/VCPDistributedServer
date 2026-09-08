.. _bpy.types.ShaderNodeUVMap:

***********
UV Map Node
***********

.. figure:: /images/node-types_ShaderNodeUVMap.webp
   :align: right
   :alt: UV Map Node.

The *UV Map* node outputs texture coordinates from a specific :ref:`UV map <uv-maps-panel>`.
It is especially useful when working with multiple UV layouts in the same material.
The node is most commonly connected to the *Vector* input of texture nodes,
allowing textures to be placed or manipulated.

.. note::

   Unlike the :doc:`Texture Coordinate Node </render/shader_nodes/input/texture_coordinate>`,
   which only outputs the active render UV map, this node can access any UV map assigned to the object.


Inputs
======

This node has no inputs.


Properties
==========

From Instancer :guilabel:`Cycles Only`
   See the :ref:`From Instancer <cycles-nodes-input-texture-coordinate-from-instancer>`
   option of the :doc:`Texture Coordinate Node </render/shader_nodes/input/texture_coordinate>`.

UV Map
   The name of the :ref:`UV map <uv-maps-panel>` to use.
   This list is populated from the UV maps available on the object's mesh data-block.
   If left unset, the :ref:`Active Render <bpy.types.MeshUVLoopLayer.active_render>` UV map is used.


Outputs
=======

UV
   UV coordinates from the specified UV map.
