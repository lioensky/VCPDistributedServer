.. index:: Geometry Nodes; Random Rotation

********************
Random Rotation Node
********************

.. figure:: /images/node-types_GeometryNodeRandomRotation.webp
   :align: right
   :alt: Random Rotation node.

The *Random Rotation* node generates random rotation values within a specified angular range.
It can be used to randomize the orientation of instances, particles, or elements of a geometry.


Inputs
======

Min Zenith
   The minimum zenith (vertical) rotation angle.
   Defines the lower limit of the random rotation.

Max Zenith
   The maximum zenith (vertical) rotation angle.
   Defines the upper limit of the random rotation.

ID
   An ID to drive the random number generator seed. By default, this input uses the same value
   as the :doc:`/modeling/geometry_nodes/geometry/read/id`, which is the ``id`` attribute of the context
   geometry if it exists, and otherwise the :doc:`index </modeling/geometry_nodes/geometry/read/input_index>`.

   .. tip:: Single Random Value

      By default, the node generates a unique random rotation for each element (based on its ID).
      To generate a single random rotation for the entire geometry, connect a constant value
      (such as an :doc:`/modeling/geometry_nodes/input/constant/integer`) to the *ID* input.

Seed
   A field to :term:`seed` the random number generator. This can be used to produce
   a different set of random rotations even when using the same *ID* input.


Outputs
=======

Rotation
   The output rotation as a rotation socket. This can be used directly
   to orient instances or to drive other transformations in the node tree.
