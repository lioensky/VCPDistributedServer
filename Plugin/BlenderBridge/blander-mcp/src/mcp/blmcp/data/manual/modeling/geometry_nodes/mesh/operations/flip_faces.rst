.. index:: Geometry Nodes; Flip Faces
.. _bpy.types.GeometryNodeFlipFaces:

***************
Flip Faces Node
***************

.. figure:: /images/node-types_GeometryNodeFlipFaces.webp
   :align: right
   :alt: Flip Faces node.

The *Flip Faces Node* reverses the order of the vertices and edges of each selected face.
The most common use of this node is to flip the normals of a face.
Any :ref:`face corner domain <attribute-domains>` attributes of selected faces are also reversed.

Though this node is usually used to affect normals, it is not called "Flip Normals" for an important reason.
The node does not actually interact with normals directly. Normals are defined by the
`right hand rule <https://en.wikipedia.org/wiki/Right-hand_rule#Curve_orientation_and_normal_vectors>`__,
so if a face's vertex list is reversed, then its normal will point in the opposite direction.


Inputs
======

Mesh
   Standard geometry input.

Selection
   Whether to flip the direction of each face.
   True values mean the face will be flipped, false means the face will be unaffected.


Output
======

Mesh
   Standard geometry output.
