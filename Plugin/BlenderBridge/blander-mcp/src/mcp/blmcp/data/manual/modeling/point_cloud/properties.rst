
**********************
Point Cloud Properties
**********************

Attributes
==========

The *Attributes* panel displays the available data fields associated with each point in the point cloud.
These attributes define characteristics like point position, size, color, and motion.

Use the :ref:`List View <ui-list-view>` interface to browse, create, edit, or remove attributes.


Attribute Types
---------------

The following are common built-in attributes supported by point cloud objects:

.. seealso::

   For more attribute types used across Blender's geometry system, refer to :ref:`geometry-nodes_builtin-attributes`.

.. list-table::
   :widths: 10 10 10 50
   :header-rows: 1

   * - Name
     - Type
     - Domain
     - Description

   * - ``position``
     - *Vector*
     - *Point*
     - Stores the 3D coordinates of each point in the object's local space.

   * - ``radius``
     - *Float*
     - *Point*
     - Defines the visual radius (size) of each point when rendered or displayed.

   * - ``color``
     - *Color*
     - *Point*
     - The display color of the point. Used in viewport rendering or shading.

   * - ``id``
     - *Integer*
     - *Point*
     - A unique identifier assigned to each point. Useful for persistent referencing.

   * - ``velocity``
     - *Vector*
     - *Point*
     - Indicates the directional movement and speed of the point (e.g., for simulations or motion blur).

Custom Attributes
   Custom attribute can be given to particles to hold a custom characteristic.

   Name
      The name of the attribute.
   Data Type
      The type of data to store in the attribute.

      :Float: Floating-point value
      :Integer: 32-bit integer
      :Vector: 3D vector with floating-point values
      :Color: RGBA color with floating-point precision
      :Byte Color: RGBA color with 8-bit precision
      :String: Text string

   Domain
      The type of element the attribute is stored in.
      Currently, attributes can only be stored per *Point*.


Custom Properties
=================

Custom properties can also be assigned to point cloud objects themselves.
These properties are stored at the object level and not per point.

See the :ref:`Custom Properties <files-data_blocks-custom-properties>`
documentation for more information on how to add and use them.

