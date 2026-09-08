World Operators
===============

.. module:: bpy.ops.world

.. function:: convert_volume_to_mesh()

   Convert the volume of a world to a mesh. The world's volume used to be rendered by EEVEE Legacy. Conversion is needed for it to render properly

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `startup/bl_operators/world.py\:26 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/world.py#L26>`__

.. function:: new()

   Create a new world Data-Block

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
