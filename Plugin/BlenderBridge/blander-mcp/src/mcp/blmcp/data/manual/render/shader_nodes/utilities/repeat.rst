.. include:: /modeling/geometry_nodes/utilities/repeat_zone.rst
   :start-after: .. --- copy below this line ---
   :end-before: .. --- copy until this line ---

Cycles and EEVEE Differences
============================

The number of iterations in *Cycles* must evaluate to a constant value. This means the number of iterations can't be
driven by :doc:`/render/shader_nodes/input/index` or :doc:`/render/shader_nodes/textures/index`.

.. figure:: /images/repeat-zone-dynamic-iterations-not-supported.png
   
   Error shown when *Cycles* is selected as the active *Render Engine*.

*EEVEE* doesn't have this limitation, so the number of iterations can be driven by any type of node.
