
*******
Density
*******

.. reference::

   :Mode:      Sculpt Mode
   :Brush:     :menuselection:`Sidebar --> Tool --> Brush Settings --> Advanced --> Brush Type`

The Density brush is specifically meant for use with
:doc:`/sculpt_paint/sculpting/tool_settings/dyntopo`
to remove/add detail in the mesh.

Even when the :ref:`Refine Method <bpy.types.Sculpt.detail_refine_method>`
is set to *Subdivide Edges*, this brush is always able to collapse edges.
This ensures that while focusing on adding detail to your sculpt, the *Density* brush
can always be used to simplify and polish surfaces.

This brush has no effect if Dyntopo is disabled.

.. tip::

   In combination with auto-smooth the brush can polish surfaces while it remeshes them.
   On tube-like geometry it can also shrink and dissolve volumes completely.


Brush Settings
==============

General
-------

.. note::

   More info at :ref:`sculpt-tool-settings-brush-settings-general` brush settings
   and on :ref:`sculpt-tool-settings-brush-settings-advanced` brush settings.
