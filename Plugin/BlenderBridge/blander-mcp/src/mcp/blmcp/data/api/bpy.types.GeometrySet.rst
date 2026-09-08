GeometrySet
===========


Accessing Evaluated Geometry
++++++++++++++++++++++++++++

.. literalinclude:: ./examples/bpy.types.GeometrySet.0.py
   :lines: 5-

.. class:: GeometrySet

   Stores potentially multiple geometry components of different types.
   For example, it might contain a mesh, curves and nested instances.

   .. method:: instance_references()
   
      This returns a list of geometries that is indexed by the ``.reference_index``
      attribute of the pointcloud returned by 
      :func:`bpy.types.GeometrySet.instances_pointcloud`.
      It may contain other geometry sets, objects, collections and None values.
   
      :rtype: list[None | bpy.types.Object | bpy.types.Collection | bpy.types.GeometrySet]


   .. method:: instances_pointcloud()
   
      Get a pointcloud that encodes information about the instances of the geometry.
      The returned pointcloud should not be modified.
      There is a point per instance and per-instance data is stored in point attributes.
      The local transforms are stored in the ``instance_transform`` attribute.
      The data instanced by each point is referenced by the ``.reference_index`` attribute,
      indexing into the list returned by :func:`bpy.types.GeometrySet.instance_references`.
   
      :rtype: bpy.types.PointCloud


   .. attribute:: curves

      The curves data-block in the geometry set.
      
      :type: :class:`bpy.types.Curves`


   .. attribute:: grease_pencil

      The Grease Pencil data-block in the geometry set.
      
      :type: :class:`bpy.types.GreasePencil`


   .. attribute:: mesh

      The mesh data-block in the geometry set.
      
      :type: :class:`bpy.types.Mesh`


   .. attribute:: mesh_base

      The mesh data-block in the geometry set without final subdivision.
      
      :type: :class:`bpy.types.Mesh`


   .. attribute:: name

      The name of the geometry set. It can be used for debugging purposes and is not unique.
      
      :type: str


   .. attribute:: pointcloud

      The point cloud data-block in the geometry set.
      
      :type: :class:`bpy.types.PointCloud`


   .. attribute:: volume

      The volume data-block in the geometry set.
      
      :type: :class:`bpy.types.Volume`


   .. staticmethod:: from_evaluated_object(evaluated_object)
   
      Create a geometry set from the evaluated geometry of an evaluated object.
      Typically, it's more convenient to use :func:`bpy.types.Object.evaluated_geometry`.
   
      :param evaluated_object: The evaluated object to create a geometry set from.
      :type evaluated_object: bpy.types.Object



