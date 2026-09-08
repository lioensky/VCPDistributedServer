.. _meta-ball-editing:

********************
Editing Meta Objects
********************

In addition to having several meta objects in a same family,
you can also have several meta primitives in a single object (just add some more while in Edit Mode).
Each will be an element, with its own shape, editing rings (in the viewport), and settings.


.. _bpy.ops.mball.delete_metaelems:

Deleting Elements
=================

.. reference::

   :Shortcut:  :kbd:`X`, :kbd:`Delete`

You can only delete the active element, no fancy options here.


Conversion
==========

To convert the meta to a real mesh, use :ref:`object-convert-to` in Object Mode.


.. _meta-ball-object-families:

Object Families
===============

A "family" is a way to regroup several meta objects,
producing something very similar to having several metas inside the same object.

It is defined by the left part of an object's name (the one before the first dot).
Remember, an object's name is the one in the *Object Name* field, in most panels,
**not** the *Metaball Name* field, which is the meta data-block's name...
For example, the *family* part of "MetaPlane.001" is ``MetaPlane``.
Each meta object in the same "family" is associated with one another as discussed below.

.. figure:: /images/modeling_metas_editing_family.png
   :align: center
   :width: 450px

   Metaball family.

Families of metas are controlled by a *base* meta object which is identified by
an object name **without** a dot in it. For example,
if we have three metas called ``MetaThing``, ``MetaThing.001``,
``MetaThing.round``, the *base* meta object would be ``MetaThing``.

The *base* meta object determines the basis, the resolution, the threshold,
*and* the transformations. It also has the material and texture area.
In a way, the *base* meta is the "owner" of the other metas in the family
(i.e. it is as if the other metas were "included" or joined into the base one).

.. hint::

   When working with multiple scenes,
   take care naming your meta objects so the *base* is always in the same scene as other metas.

   Failing to do so will give confusing behaviors (like invisible meta objects).


Examples
========

Fig. :ref:`fig-meta-ball-base` shows the *base* meta labeled "B".
The other two *Meta* objects are *children*. Children's selection rings are always black,
while the group's mesh is orange. Because the metas are grouped,
they form a unified mesh which can always be selected by selecting the mesh of any meta in the group.

.. _fig-meta-ball-base:

.. figure:: /images/modeling_metas_editing_base-example.png
   :align: center
   :width: 450px

   Meta ball base.

For example, in Fig. :ref:`fig-meta-ball-base`, only the lower sphere (the parent) has been selected,
and you see that both the parent's mesh *and* all of the children's meshes are now highlighted.

.. _fig-meta-ball-scale:

.. figure:: /images/modeling_metas_editing_base-example-scale.png
   :align: center
   :width: 450px

   Scaling the "base".

The *base* meta object controls the *polygonalization* (mesh structure) for the group, and
as such, also controls the polygonalization for the children (non-base) metas.
If we transform the *base* meta, the children's polygonalization changes.
However, if we transform the children, the polygonalization remains unchanged.

.. hint::

   This discussion of "polygonalization" does *not* mean that the various meshes do not deform
   towards or away from each other (meta objects always influence one another in the usual way,
   within a same family).

   Rather, it means that the underlying mesh structure changes only when the *base* object transforms.
   For example, if you scale the *base*, the children's mesh structure changes.

   In Fig. :ref:`fig-meta-ball-scale`, the *base* has been scaled down,
   which has the effect of scaling the mesh structure of each of the children. As you can see,
   the children's mesh resolution has increased, while the *base* decreased.
   The children did *not* change size!
