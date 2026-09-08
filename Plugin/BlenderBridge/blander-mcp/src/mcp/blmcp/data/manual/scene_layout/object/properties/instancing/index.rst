
##############
  Instancing
##############

.. note::

   Geometry nodes provides a more flexible way to instance objects, with the
   :doc:`/modeling/geometry_nodes/instances/instance_on_points`.

Vertices
   This creates an instance of all children of this object on each vertex
   (for mesh objects only).
Faces
   This creates an instance of all children of this object on each face
   (for mesh objects only).
Collection
   This creates an instance of the collection with the transformation of the object.
   Collection instancers can be animated using actions,
   or can get a :doc:`Library Override </files/linked_libraries/library_overrides>`.

.. toctree::
   :maxdepth: 2

   verts.rst
   faces.rst
   collection.rst
