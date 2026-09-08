
*********
Relations
*********

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Object Properties --> Relations`

Parent
   The object to which the selected object is parented to.

.. _bpy.types.Object.parent_type:

Parent Type
   The type of parenting used. See :doc:`parenting </scene_layout/object/editing/parent>`
   for information on the different types.

.. _bpy.types.Object.use_parent_final_indices:

Use Final Indices :guilabel:`Vertex` :guilabel:`3 Vertices`
   Use the final evaluated indices rather than the original mesh indices.

.. _bpy.types.Object.use_camera_lock_parent:

Camera Parent Lock
   When the camera is locked to the view, the root parent is transformed rather than the camera.
   This is useful for camera rigs where you don't want to animate the camera directly.

.. _bpy.types.Object.parent_vertices:

Parent Vertex/Vertices
   Indices of vertices in case of a vertex parenting relation.

.. _bpy.types.Object.track_axis:

Tracking Axis
   Axis that points in the "forward" direction.
   Applies to *Instance Vertices* when *Align to Vertex Normal* is enabled.

.. _bpy.types.Object.up_axis:

Up Axis
   Axis that points in the "upward" direction.
   Applies to *Instance Vertices* when *Align to Vertex Normal* is enabled.

.. _bpy.types.Object.pass_index:

Pass Index
   Defines the index the object will have in the Object Index render pass. See :doc:`passes </render/layers/passes>`
   and :doc:`ID mask </compositing/types/mask/id_mask>` for more information.

   .. note::

      :doc:`Volume Objects </modeling/volumes/introduction>` are not supported.
