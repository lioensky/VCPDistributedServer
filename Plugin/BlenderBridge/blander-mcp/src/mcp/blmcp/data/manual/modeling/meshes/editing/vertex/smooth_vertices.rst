.. _bpy.ops.mesh.vertices_smooth:
.. _tool-mesh-smooth:

***************
Smooth Vertices
***************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Smooth Vertices`,
               :menuselection:`Context Menu --> Smooth Vertices`

Moves the selected vertices so that the surface around them becomes more smooth and rounded.

The following options are available in the :ref:`bpy.ops.screen.redo_last` panel:

Smoothing
   Smoothing factor.
Repeat
   The number of smoothing iterations.
Axes
   Limit the effect to certain axes.

.. list-table::

   * - .. figure:: /images/modeling_modifiers_deform_smooth_mesh-before.png
          :width: 200px

          Mesh before smoothing.

     - .. figure:: /images/modeling_modifiers_deform_smooth_mesh-one-iteration.png
          :width: 200px

          Mesh after one smoothing iteration.

     - .. figure:: /images/modeling_modifiers_deform_smooth_mesh-ten-iterations.png
          :width: 200px

          Mesh after ten smoothing iterations.

.. tip::

   If the mesh has insufficient geometry density and would still look blocky after smoothing,
   you can :doc:`subdivide </modeling/meshes/editing/edge/subdivide>` it first.

   Alternatively, use the :doc:`/modeling/modifiers/generate/subdivision_surface` to subdivide
   and smooth the mesh in one go. This uses a more complex smoothing algorithm, however,
   so the result won't be quite the same.

.. seealso::

   The :doc:`/modeling/modifiers/deform/smooth` performs this operation non-destructively.

.. note::

   The :ref:`Smooth Faces <modeling-meshes-editing-normals-shading>` operator sounds similar to this one
   but is unrelated. It's called *Shade Smooth* in other parts of the UI and merely changes the vertex normals
   to make the mesh *appear* more smooth. It doesn't smooth out vertex positions like *Smooth Vertices* does.
