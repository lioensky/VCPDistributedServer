.. _bpy.types.ShaderNodeAttribute:

**************
Attribute Node
**************

.. figure:: /images/node-types_ShaderNodeAttribute.webp
   :align: right
   :alt: Attribute Node.

The *Attribute* node allows you to retrieve attributes attached to an object or mesh.


Inputs
======

This node has no inputs.


Properties
==========

Attribute Type
   Specifies the type of the attribute.

   :Geometry:
      The attribute is associated with the geometry of the object, and its value varies from
      vertex to vertex, or within the volume of the object.

      Most geometry attributes are directly accessible through the various input nodes, except for these:

      Ocean Foam
         Gives a scalar defining where foam might appear when using
         an :doc:`Ocean Modifier </modeling/modifiers/physics/ocean>`.
         This depends on the name you give this property.

      .. seealso::

         For a full list of options see `This Thread <https://blender.stackexchange.com/questions/14262#14267>`__
         on the Blender Stack Exchange.
   :Object:
      The attribute name specifies a :ref:`custom property <files-data_blocks-custom-properties>` name,
      or an RNA path to a built-in property (like the single property :ref:`driver variables <drivers-variables>`).

      The values of attributes of this type are defined once per object. The name or path is looked up
      first in the object data-block, followed by the mesh data-block if not found.
      Custom properties have priority over built-in ones.

      The property value must be an integer, float, boolean, or a vector of 1 to 4 floats or ints; properties of other
      types are ignored. If a suitable property is not found, all sockets of the node, including *Alpha*, output 0.

      .. tip::

         The ``color`` attribute will output the value of the Color field in
         the :ref:`Viewport Display <properties-object-viewport-display>` panel of
         the object, unless overridden by a custom property.
   :Instancer:
      Similar to *Object*, but the attribute is looked up in the instancer particle system settings,
      followed by :doc:`Geometry Node instance </modeling/geometry_nodes/instances>` attributes
      (searching from the innermost instancing layer to outer ones), and finally in the instancer object.
      If the current object is not instanced, or the property is not found, it falls back to the *Object* mode.

      .. warning::

         Currently only up to 4 layers of Geometry Node instancing are searched.
   :View Layer:
      The attribute is looked up in the current :doc:`View Layer </render/layers/introduction>`,
      :doc:`Scene </scene_layout/scene/introduction>` and :doc:`World </render/lights/world>`, using the same lookup
      logic as *Object*, and likewise producing all zero outputs including *Alpha* if not found. Attributes of this
      type have the same uniform value throughout the whole Render Layer.

      .. tip::

         This gives access to a number of useful built-in properties, for example:

         ``color`` or ``world.color``
            Outputs the value of the :ref:`Color <bpy.types.World.color>` field in the Viewport Display
            panel of the World properties.
         ``render.resolution_x``, ``render.resolution_y``
            Outputs the current :doc:`rendering resolution </render/output/properties/format>`.
         ``camera.data.angle_x``, ``camera.data.angle_y``,
            Outputs the effective field of view of the active :doc:`Camera </render/cameras>`.

      .. seealso::

         An alternative method to access the same set of properties is to use driver
         :ref:`Context Properties <bpy.types.DriverVariable.type>`,
         possibly with a :ref:`manually emulated <driver-attribute-node-emulation>` lookup fallback chain.

Name
   The name of the attribute to retrieve.


Outputs
=======

Color
   RGB color interpolated from the attribute.
Vector
   XYZ vector interpolated from the attribute.
Factor
   Scalar value interpolated from the attribute.
Alpha
   Alpha channel of the attribute, when available. If the attribute has no alpha channel, generally defaults to 1.

.. warning::

   Currently, only *View Layer* attributes are supported in shaders used for the :doc:`World </render/lights/world>`
   or :doc:`Light Objects </render/lights/light_object>`.
