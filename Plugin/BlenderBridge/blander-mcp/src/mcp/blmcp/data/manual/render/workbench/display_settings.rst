
****************
Viewport Display
****************

The Workbench engine does not work with shader trees. In various tabs of the Properties
are Viewport Display panels where settings can be adjusted that the Workbench engine uses.


.. _properties-object-viewport-display:

Object
======

The Viewport Display panel in the Object Properties has several settings that
are used by the Workbench Engine.

.. reference::

   :Panel:     :menuselection:`Properties --> Object --> Viewport Display`

Shadow
   When the *Shadow* in the :doc:`/render/workbench/options` is enabled
   this object will cast a shadow.
In Front
   When checked the object will be rendered in front of the other objects in the scene.
Color
   The color to render the object in when object color needs to be rendered.
   The alpha channel can be used to render the object transparent.


.. _properties-material-viewport-display:

Material
========

The Viewport Display panel in the Material Properties has several settings that
are used by the Workbench Engine.

.. reference::

   :Panel:     :menuselection:`Properties --> Material --> Viewport Display`

Color
   The color when rendering the material.
   The alpha channel can be used to render the object transparent.
Metallic
   Changes the amount of specular lighting. This is only available when
   *Specular Lighting* in the :doc:`/render/workbench/options` is enabled.
Roughness
   Changes the amount of roughness for specular lighting. This is only available when
   *Specular Lighting* in the :doc:`/render/workbench/options` is enabled.


.. _properties-world-viewport-display:

World
=====

The Viewport Display panel in the World Properties has several settings that
are used by the Workbench Engine.

.. reference::

   :Panel:     :menuselection:`Properties --> World --> Viewport Display`

Color
   The color of the world background. This color will be rendered
   in the background of the scene.
