
******
Curves
******

.. reference::

   :Panel:     :menuselection:`Render --> Curves`

.. _bpy.types.RenderSettings.hair_type:
.. _bpy.types.RenderSettings.hair_subdiv:

.. Editor's Note: This part of this page gets copied into:
.. - :doc:`</render/cycles/render_settings/hair>`

.. --- copy below this line ---

Shape
   :Strand:
      Render curves as a thin strand roughly a pixel wide.
      Curve diameter parameters are ignored with this setting.

   :Strip:
      Render curves as a flat ribbon with rounded normals.

Additional Subdivisions
   Additional subdivisions to be applied on top of the curve resolution set in the
   hair system settings. Increasing this value will smooth out the curves of the strands.
