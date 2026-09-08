
***********
Object Data
***********

These panels can be found in the *Data* tab of the :doc:`/editors/properties_editor`
editor after selecting a mesh object.

Mesh data-block
   The :ref:`Data-Block Menu <ui-data-block>` at the top can be used to make the object point
   to different mesh :doc:`object data </scene_layout/object/introduction>`.


Vertex Groups
=============

Vertex groups can be used to assign a group or weighted group to some operator.
An object can have several weight groups and can be assigned in
:doc:`Weight Paint </modeling/meshes/properties/vertex_groups/vertex_groups>` mode,
or in :doc:`Edit Mode </modeling/meshes/properties/vertex_groups/assigning_vertex_group>` via this panel.

See :doc:`Vertex Groups </modeling/meshes/properties/vertex_groups/introduction>` for more information.


Shape Keys
==========

Shape Keys can be used to transform one shape into another.
See :doc:`/animation/shape_keys/shape_keys_panel` for more information.


UV Maps
=======

UV Maps are used to map a 3D object onto a 2D plane that determines where a texture appears on the 3D object.
Different UV Maps can be used for different textures. For more information see :ref:`uv-maps-panel`.


.. _bpy.ops.geometry.color_attribute_remove:
.. _bpy.ops.geometry.color_attribute_render_set:
.. _modeling-meshes-properties-object_data-color-attributes:

Color Attributes
================

Color data can be applied directly to an object's vertices rather than using a texture or a material.
There are two modes to paint color attributes in.
Use :doc:`Vertex Paint </sculpt_paint/vertex_paint/index>` mode to paint per face corner
by enabling the paint mask in the header.
This is useful to achieve sharp edges in the color attribute on low-poly assets.
Alternatively use Sculpt mode to paint on a much higher vertex count.


.. _bpy.ops.geometry.color_attribute_add:

Creating a New Color Attribute
------------------------------

To create a new Color Attribute select the plus icon next to the list of attributes.
This action will open a pop-up with the following information.

Name
   The name of the Color Attribute which can be referenced elsewhere in Blender.
Domain
   The associated part of the geometry that stores the attribute.
   See :ref:`attribute-domains` for more information.

   :Vertex: Color Attributes are stored per each vertex.
   :Face Corner: Color Attributes are stored per each corner of a face.
Data Type
   The data type to represent colors internally.

   :Color: RGBA color with floating-point precision.
   :Byte Color: RGBA color with 8-bit precision.
Color
   The default color to fill for every element in the domain.


Color Attribute Specials
------------------------

These are operators that are available in the menu to the right of the attribute list.

.. _bpy.ops.geometry.color_attribute_duplicate:

Duplicate Color Attribute
   Creates a copy of the active color attribute in the list.

.. _bpy.ops.geometry.color_attribute_convert:

Convert Color Attribute
   Changes how the color attribute is stored.

   Domain
      The associated part of the geometry that stores the attribute.
      See :ref:`attribute-domains` for more information.

      :Vertex: Color Attributes are stored per each vertex.
      :Face Corner: Color Attributes are stored per each corner of a face.
   Data Type
      The data type to represent colors internally.

      :Color: RGBA color with floating-point precision.
      :Byte Color: RGBA color with 8-bit precision.


.. _bpy.types.AttributeGroup:

Attributes
==========

An attribute is data stored per mesh element. Every attribute has a data type, domain and name.
This panel only lists custom attributes which excludes all the built-in attributes like ``position`` and
other attributes like vertex groups.

See :doc:`Attributes Reference </modeling/geometry_nodes/attributes_reference>` for more information.


Texture Space
=============

Each object can have an automatically generated UV map, these maps can be adjusted here.

See :ref:`Generated UV Properties <properties-texture-space>` for more information.


Remesh
======

Mesh objects, in particular meshes that have been modeled to represent organic objects,
often have geometry that is not particularly uniform.
This can cause problems if the object needs to be :ref:`rigged <animation-rigging>`
or just needs simpler geometry for workflows such as 3D printing.
Remeshing is a technique that rebuilds the geometry with a more uniform topology.
Remeshing can either add or remove the amount of topology depending on the defined resolution.
Remeshing is especially useful for :doc:`sculpting </sculpt_paint/sculpting/index>`,
to generate better topology after blocking out the initial shape.

See :doc:`/modeling/meshes/retopology` for more information.


Geometry Data
=============

Mesh objects can have different types of custom data attached to them.
This data is mostly used internally and can be exported by some :doc:`exporters </files/import_export/index>`.
See :doc:`/modeling/meshes/properties/custom_data` for more information.
