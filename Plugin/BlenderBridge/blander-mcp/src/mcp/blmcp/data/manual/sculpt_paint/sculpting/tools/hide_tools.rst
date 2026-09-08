
******************
Hide Gesture Tools
******************

.. reference::

   :Mode:      Sculpt Mode

Hide gesture tools hide all selected vertices within the selection area and any of their connected
edges and faces.
Holding :kbd:`Ctrl` while performing the selection reveals the vertices, edges, and faces.

Pressing :kbd:`LMB` with any of these tools without also dragging reveals all elements of a mesh.

All hide gesture tools can be activated in the Toolbar and are comprised of the following:

.. _tool-box-hide:

Box Hide
========

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Box Hide`


Hides vertices and connected edges and faces based on a
:ref:`box gesture <gesture-tool-box>`.

.. _tool-lasso-hide:

Lasso Hide
==========

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Lasso Hide`

Hides vertices and connected edges and faces based on a
:ref:`lasso gesture <gesture-tool-lasso>`.

.. _tool-line-hide:

Line Hide
=========

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Line Mask`

Hides vertices and connected edges and faces based on a
:ref:`line gesture <gesture-tool-line>`.

.. _tool-polyline-hide:

Polyline Hide
=============

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Polyline Mask`

Hides vertices and connected edges and faces based on a
:ref:`polyline gesture <gesture-tool-polyline>`.

.. note::

    The Polyline Hide tool does not support showing all vertices via pressing :kbd:`LMB`.

Tool Settings
=============

Visibility Area
   Determines whether all vertices inside or outside the selected area should be affected.

   :Inside:
      All vertices and connected elements inside the selection area will be hidden.
   :Outside:
      All vertices and connected elements outside the selection area will be hidden.