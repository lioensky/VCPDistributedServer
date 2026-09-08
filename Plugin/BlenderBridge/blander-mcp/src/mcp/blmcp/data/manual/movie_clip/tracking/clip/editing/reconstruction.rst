
**************
Reconstruction
**************

Scene orientation tools can be used for orienting object to bundles.


.. _bpy.ops.clip.set_origin:

Set Origin
==========

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Set Origin`

Transform camera in a way which makes active track to be moved to a scene origin.
Only translation is applied to the camera.


.. _bpy.ops.clip.set_plane:

Set Floor
=========

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Set Floor`

Use selected three markers to define a floor.
Camera will be transformed in a way which makes the selected markers to be flat (have Z = 0).


Set Wall
========

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Set Wall`

Similar to the floor orientation, but defines a wall (selected tracks are placed onto the XZ plane).


.. _bpy.ops.clip.set_axis:

Set X/Y Axis
============

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Set X/Y Axis`

Transform camera in a way which makes active track to become on X or Y axis.
No translation is applied, meaning scene origin which was specified before will be preserved.


.. _bpy.ops.clip.set_scale:

Set Scale
=========

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Set Scale`

Scale camera or tracking object in a way which makes distance
between two selected tracks match the given value in *Distance*.


.. _bpy.ops.clip.apply_solution_scale:

Apply Solution Scale
====================

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Apply Solution Scale`

Similar to :ref:`bpy.ops.clip.set_scale`, but actually modifies the tracking data.


.. _bpy.ops.clip.track_to_empty:

Link Empty to Track
===================

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> Link Empty to Track`

Creates new empty in 3D Viewport and appends constraint which parts it to the active track.


.. _bpy.ops.clip.bundles_to_mesh:

3D Markers to Mesh
==================

.. reference::

   :Mode:      Tracking
   :Menu:      :menuselection:`Reconstruction --> 3D Markers to Mesh`

Creates a mesh which vertices matches positions of reconstructed tracks.
It is required to have motion solved first before using this operator.
Only tracks from the current tracking object will be used.
The intention of this operator is to give a nice starting point for a manual mesh reconstruction.
