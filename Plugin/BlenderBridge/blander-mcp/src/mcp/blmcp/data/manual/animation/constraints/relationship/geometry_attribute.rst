.. index:: Object Constraints; Geometry Attribute Constraint
.. _bpy.types.GeometryAttributeConstraint:

*****************************
Geometry Attribute Constraint
*****************************

The *Geometry Attribute* constraint transforms an object or bone according to a target object's
sampled geometry attribute data. This allows motion and deformation to be driven directly by
procedural geometry outputs, such as positions or orientations from Geometry Nodes.


Options
=======

.. figure:: /images/animation_constraints_relationship_geometry-attribute_panel.png

   Geometry Attribute constraint.

:ref:`Target <rigging-constraints-interface-common-target>`
   The target object to retrieve geometry from.
   The supported geometry types are Mesh, Curve, Point Cloud, and Instance.

Offset with Target Transform
   Apply the target object's world transform on top of the attribute's transform.

Attribute Name
   Name of the sampled attribute.
   The default attribute name is position.

Data Type
   Data type of the sampled attribute. 
   The type will determine which components will be used for transforming the constraint object.

   :Vector:
      Vector data type, affects the location.
   :Quaternion:
      Quaternion data type, affects the rotation.
   :4x4 Matrix:
      4x4 Matrix data type, affects the entire transform.
      Location, Rotation, and Scale components can be toggled separately, but will remove matrix shearing.

Domain
   Domain of the sampled attribute.

   :Point:
      Point domain from a Mesh, Curve, or Point Cloud.
   :Edge:
      Edge domain from a Mesh.
   :Face:
      Face domain from a Mesh.
   :Face Corner:
      Face Corner domain from a Mesh.
   :Spline:
      Spline domain from a Curve.
   :Instance:
      Instance domain from an Instance.

Sample Index
   Index of the geometry element to sample the attribute. 
   Index values are clamped to what is present on the target geometry.

Mix Mode
   Specify how the copied and existing transformations are combined.

   :Replace:
      Replace the original transformation with the transform from the attribute.
   :Before Original (Full):
      Apply copied transformation before original, using simple matrix multiplication as if
      the constraint target is a parent in Full Inherit Scale mode.
      Will create shear when combining rotation and non-uniform scale.
   :Before Original (Split Channels):
      Apply copied transformation before original, handling location, rotation and scale
      separately, similar to a sequence of three Copy constraints.
   :After Original Full:
      Apply copied transformation after original, using simple matrix multiplication as if
      the constraint target is a child in Full Inherit Scale mode.
      Will create shear when combining rotation and non-uniform scale.
   :After Original (Split Channels):
      Apply copied transformation after original, handling location, rotation and scale
      separately, similar to a sequence of three Copy constraints.

:ref:`bpy.types.constraint.influence`
   How strongly the constraint affects the owner.
