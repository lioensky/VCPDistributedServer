
********
Controls
********

Auto-Masking
============

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Header --> Auto-Masking`
   :Shortcut:     :kbd:`Alt-A`

These properties automatically mask geometry based on geometric features of the mesh.
It's an quick alternative to frequent manual masking.
These masks are initialized on every new stroke or tool usage. They are also never visible as an overlay.

Note, these properties are applied across all sculpt brushes, however, they can also be configured
per brush in the :ref:`Advanced Brush Settings <sculpt-tool-settings-brush-settings-advanced>`.

These properties can be accessed via a :ref:`bpy.types.UIPieMenu` by pressing :kbd:`Alt-A`.

All auto-masking modes can be combined, which makes the generated auto-mask more specific.
For example it's possible to auto-mask a specific face set,
while excluding disconnected topology and face set boundaries,
and only affect faces that are oriented towards the view via View Normal.

.. _bpy.types.Sculpt.use_automasking_topology:

Topology
   Only vertices that are topologically connected to where you started
   the stroke/tool on are affected. So loose geometry islands will be auto-masked.

   Additionally for the :doc:`Grab </sculpt_paint/sculpting/brushes/grab>` and
   :doc:`Thumb </sculpt_paint/sculpting/brushes/thumb>` brushes, anything that
   is not connected within the brush radius will be auto-masked.
   So even if geometry is connected somewhere,
   it is considered separate if the connection is not within the radius.

.. _bpy.types.Sculpt.use_automasking_face_sets:

Face Sets
   Only vertices that are part of the same face set that you started the stroke/tool on are affected.

.. tip::

   If no topology or face set is visible under the cursor at the start of the stroke,
   the previously auto-masked area will be targeted.
   This is especially useful with the "Projected" falloff shape in the
   :doc:`Falloff Settings </sculpt_paint/brush/falloff>`.

.. _bpy.types.Sculpt.use_automasking_boundary_edges:

Mesh Boundary
   Vertices that are part of open boundary edges are not affected.
   This also includes boundary edges to hidden faces.

   Propagation Steps
      Increases the soft gradient towards the auto-masked boundary edges.
      Each step iterates the distance one edge further.
      This setting is used for both Mesh Boundary and Face Sets Boundary.

   Create Mask
      This will execute the :ref:`sculpt-mask_from_mesh_boundary` operator with the current auto-masking
      settings. This is very useful to visualize the current auto-mask, or to edit the mask further manually.

.. _bpy.types.Sculpt.use_automasking_boundary_face_sets:

Face Sets Boundary
   Vertices that are part of a boundary between face sets are not affected.
   This also includes boundary edges to hidden faces.
   Propagation Steps are shared with Mesh Boundary auto-masking.

   Create Mask
      This will execute the :ref:`bpy.ops.sculpt.mask_from_boundary` operator with the current auto-masking
      settings. This is very useful to visualize the current auto-mask, or to edit the mask further manually.

.. _bpy.types.Sculpt.use_automasking_cavity:

Cavity
   Vertices that are the peaks of the surface curvature are not affected.
   While this auto-mask is primarily meant for painting,
   it can also be used for regular sculpting.

   Factor
      The overall contrast of how strong the cavity is applied. The value of 0.5 is the default,
      but better results can also be achieved on 0.2 if a Custom Curve is used as well.

   Blur
      The number of times the cavity mask is blurred. A value of 0 will give the pure cavity auto-mask.
      Anything higher than 6 will likely have a less visible effect and decrease performance.
      Even though the value is capped to 10, it can be increased up to 25 if typing in the value.

   Custom Curve
      Use a custom curve to fine tweak the cavity auto-mask.
      This is very useful if only small crevices or flat surfaces should be affected.
      Or for example if the contrast should be increased/decreased in a specific way.
   Create Mask
      This will execute the :ref:`bpy.ops.sculpt.mask_from_cavity` operator with the current auto-masking settings.
      This is very useful to visualize the current auto-mask, or to edit the mask further manually.

.. _bpy.types.Sculpt.use_automasking_cavity_inverted:

Cavity (Inverted)
   This is the same as "Cavity", but inverted.
   This means the valleys/crevices of the surface curvature will not be affected.
   It cannot be used at the same time as Cavity and shares all of its settings.
   Enable this to quickly invert the cavity auto-mask.

.. _bpy.types.Sculpt.use_automasking_view_normal:

View Normal
   Only vertices with a :term:`Normal` that face the viewer are affected.
   This is similar to the "Front Faces Only" toggle in the
   :doc:`Brush Setting </sculpt_paint/sculpting/tool_settings/brush_settings>`, to only affect visible geometry.
   The advantage of this auto-mask is that it has more options and works on sculpt mode as a whole.

   Occlusion
      Change the View Normal behavior to only affect vertices that are not occluded by other faces.
      This setting is incompatible with the other Limit and Falloff sliders.
      It also causes a much slower performance.

   Limit
      Determines the range of angles that will be affected. 90 degrees encompasses all that is visible.

   Falloff
      Extends the angular range of the Limit slider with a soft falloff gradient.
      This falloff will visually extend the limit range further.

.. _bpy.types.Sculpt.automasking_start_normal_falloff:
.. _bpy.types.Sculpt.automasking_start_normal_limit:
.. _bpy.types.Sculpt.use_automasking_start_normal:

Area Normal
   Very similar to the View Normal, but uses the Normal of the surface that you started the stroke/tool on.
   This way any direction can be chosen for what vertices will be affected.
   It has the same Limit and Falloff sliders as the View Normal auto-mask.
