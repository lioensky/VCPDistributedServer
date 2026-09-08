.. _bpy.types.ShaderNodeOutputAOV:

***************
AOV Output Node
***************

.. figure:: /images/node-types_ShaderNodeOutputAOV.webp
   :align: right
   :alt: AOV Output Node.

Shader AOVs (Arbitrary Output Variables) provide custom render passes for arbitrary shader node components.
As an artist this can be a good way to debug or tweak very fine details of a scene in post-processing.
To use shader AOVs create the pass in the :ref:`Shader AOV <bpy.types.AOV>` panel
then reference that pass with the *AOV Output* shading node.
Shader AOVs can be added or removed in the *Shader AOV* panel.

.. tip::

   The *AOV Output* node can be used in Material and World shader nodes.


Inputs
======

Color
   Output a color variable; as the name suggest can be used for a color but also a normal value.
Value
   Output a single numerical value.


Properties
==========

Name
   The name of the render pass to assign the input value to.
   This property has the same *Name* that is specified in the :ref:`Shader AOV <bpy.types.AOV>` panel.


Outputs
=======

This node has no outputs.
