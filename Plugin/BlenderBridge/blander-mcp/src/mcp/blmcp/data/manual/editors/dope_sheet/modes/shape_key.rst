.. _dope-sheet-shape-key:

****************
Shape Key Editor
****************

The *Shape Key Editor* displays the :doc:`shape keys </animation/shape_keys/introduction>` of the
active object and allows you to create and adjust keyframes for their
:ref:`influence values <bpy.types.ShapeKey.value>`.
This editor is a specialized mode of the :doc:`Dope Sheet </editors/dope_sheet/introduction>`,
focused specifically on shape key animation.

Each row represents a shape key, and each keyframe marker corresponds to a point where the
shape key's value changes over time.
This provides an efficient way to time and refine facial expressions, morph targets,
and other mesh deformations driven by shape keys.

Additional shape key properties, such as names, values, and relative settings,
can be viewed and edited in the *Sidebar*.

.. figure:: /images/editors_dope-sheet_shape-key-editor.png
   :align: center

   The Shape Key Editor.


Usage
=====

- Use the *Shape Key Editor* to keyframe shape key influences over time.
- Adjust timing by moving or scaling keyframes directly in the timeline.
- Combine with other Dope Sheet modes (such as the *Action Editor*) for complex character animation workflows.

See also: :doc:`Shape Key Basics </animation/shape_keys/introduction>` for details on creating
and managing shape keys.
