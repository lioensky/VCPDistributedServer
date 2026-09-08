
****************
Curve Properties
****************

Hair Curves have different properties than regular Curve objects;
these properties are documented below.


Attributes
==========

The *Attributes* panel contains different hair characteristics such as the position and color of hair strands.

Use the :ref:`List View <ui-list-view>` to manage attributes.

.. seealso::

   See the :doc:`Attribute Reference </modeling/geometry_nodes/attributes_reference>` for details on attributes.


Surface
=======

.. _bpy.types.Curves.surface:

Surface
   The curve surface is an optional mesh that is used to anchor the curves, and behave as a scalp for hair grooming.
   When adding a new Curves object via the **Add Menu** the active object is automatically set as the surface.

   To set a new surface press :kbd:`Ctrl-P` and select *Object (Attach Curves to Surface)*
   in the *Set Parent To* pop-up menu. This option can be seen as part of the Curves settings in the Properties
   Editor.

   .. figure:: /images/sculpt-paint_sculpting_curves-surface.png

.. _bpy.types.Curves.surface_uv_map:

Surface UV Map
   The name of the attribute on the surface mesh used to define the attachment of each curve.

   .. note::

      If the UV from the surface changed,
      run :ref:`Snap to Nearest Surfaces <bpy.ops.curves.snap_curves_to_surface>` to re-attach the curves.
