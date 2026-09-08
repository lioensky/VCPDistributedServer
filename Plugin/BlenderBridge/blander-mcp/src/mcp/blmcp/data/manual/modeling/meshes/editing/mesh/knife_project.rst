.. _bpy.ops.mesh.knife_project:

*************
Knife Project
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Knife Project`

Projects the outline of one or more "cookie cutter" objects onto the edited object and creates
new edges there.

The cutter objects must be :doc:`Curves </modeling/curves/introduction>` or :term:`non-manifold`
meshes (e.g. flat shapes, loose edges).

.. tip::
   :ref:`Select Non-Manifold <bpy.ops.mesh.select_non_manifold>` will highlight the cutting edges
   of mesh objects.

Projection is done along the :doc:`viewing direction </editors/3dview/navigate/align>`.

Usage
=====

#. Select the object(s) that should receive the cut and switch to *Edit Mode*.
#. Select the object(s) that should perform the cut by clicking them with :kbd:`Ctrl-LMB` in the
   3D Viewport or the :doc:`Outliner </editors/outliner/introduction>`.
#. Click :menuselection:`Mesh --> Knife Project` in the menu.

If Blender switches back to *Object Mode* when selecting the cutting objects,
make sure that :menuselection:`Edit --> Lock Object Modes` is checked in the topbar.

Options
=======

Cut Through
   Projects the cut through the entire mesh, including back faces not currently visible.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_text-before.jpg
          :width: 320px

          Before projecting from a text object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_text-after.jpg
          :width: 320px

          Resulting knife projection.

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_mesh-before.jpg
          :width: 320px

          Before projecting from a mesh object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_mesh-after.jpg
          :width: 320px

          Resulting knife projection (extruded after).

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_curve-before.png
          :width: 320px

          Before projecting from a 3D curve object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_curve-after.jpg
          :width: 320px

          Resulting knife projection (extruded after).


Known Limitations
=================

When cutting multiple meshes in Edit Mode at once,
geometry from these meshes does not occlude separate mesh objects behind them.
