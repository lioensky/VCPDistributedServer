
*****************
Render Properties
*****************

.. reference::

   :Panel:     :menuselection:`Properties --> Render --> Freestyle`

Freestyle can be activated with the checkbox in the header of the Freestyle panel in the *Render* tab.

.. figure:: /images/render_freestyle_render_freestyle-panel.png
   :align: center
   :width: 50%

   Freestyle Render Properties.

.. _bpy.types.RenderSettings.line_thickness_mode:

Line Thickness Mode
   There are two different modes for defining the base line thickness:

   :Absolute:
      The line thickness is given by a user-specified number of pixels.
   :Relative:
      The unit line thickness is scaled by the proportion of the present vertical image resolution to 480 pixels.
      For instance, the "unit line thickness" is 1.0 when the image height set to 480px, 1.5 with 720px
      and 2.0 with 960px.

.. _bpy.types.RenderSettings.line_thickness:

Line Thickness
   Line thickness to use for rendering (only for *Absolute* line thickness).
