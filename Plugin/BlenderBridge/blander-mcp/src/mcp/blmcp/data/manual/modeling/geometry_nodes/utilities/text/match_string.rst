.. index:: Geometry Nodes; Match String
.. _bpy.types.FunctionNodeMatchString:

*****************
Match String Node
*****************

.. figure:: /images/node-types_FunctionNodeMatchString.webp
   :align: center
   :alt: Match String node.

The *Match String* node compares two string values and outputs a Boolean result based on the selected operation.
It is useful for conditional logic involving string comparisons, such as matching object names or attribute values.


Inputs
======

String
   The input string to be evaluated.

Operation
   Determines how the input string is compared to the key:

   :Starts With:
      True if the input string begins with the key.
   :Ends With:
      True if the input string ends with the key.
   :Contains:
      True if the input string contains the key anywhere within it.

Key
   The target string to compare against.


Outputs
=======

Result
   A Boolean value indicating whether the input string matches the key according to the selected operation.
