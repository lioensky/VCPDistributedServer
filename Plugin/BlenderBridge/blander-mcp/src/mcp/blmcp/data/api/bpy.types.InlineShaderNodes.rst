InlineShaderNodes
=================


Inline Shader Nodes
+++++++++++++++++++

.. literalinclude:: ./examples/bpy.types.InlineShaderNodes.0.py
   :lines: 5-

.. class:: InlineShaderNodes

   An inlined shader node tree.

   .. attribute:: node_tree

      The inlined node tree.
      
      :type: :class:`bpy.types.NodeTree`


   .. staticmethod:: from_light(light)
   
      Create an inlined shader node tree from a light.
   
      :param light: The light to online the node tree of.
      :type light: bpy.types.Light

   .. staticmethod:: from_material(material)
   
      Create an inlined shader node tree from a material.
   
      :param material: The material to inline the node tree of.
      :type material: bpy.types.Material

   .. staticmethod:: from_world(world)
   
      Create an inlined shader node tree from a world.
   
      :param world: The world to inline the node tree of.
      :type world: bpy.types.World



