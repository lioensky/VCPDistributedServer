.. --- copy below this line ---

************
Node Bundles
************

A *bundle* is a container that groups multiple values into one socket.
This makes it possible to pass many values through
a single link, similar to a *struct* in programming.

Bundles reduce the number of exposed inputs and outputs in a node group,
and can contain mixed data types such as geometry, fields, values, objects,
or even nested bundles.

.. figure:: /images/interface-nodes-bundle-example.png
   :align: center

   A cube and cylinder combined into a bundle, then separated again.


Nodes
=====

The following nodes are provided for working with bundles:

.. toctree::
   :maxdepth: 1

   combine_bundle.rst
   separate_bundle.rst
   get_bundle_item.rst
   store_bundle_item.rst
   join_bundle.rst

Both nodes allow adding or removing an arbitrary number of sockets,
with flexible type support.


Usage
=====

Bundles are useful in many workflows:

- **Simplified interfaces** -- group inputs into a single socket for clarity.
- **Physics simulations** -- package all entities and constraints for a solver.
- **Declarative systems** -- store complex structured data for evaluation later.
- **Texture sets** -- combine PBR maps (Base Color, Roughness, Normal) into one socket.


Socket Syncing
==============

Bundles use socket names to match their inputs and outputs.
If two bundle nodes are connected but have mismatched signatures,
Blender can offer to sync them automatically.

- Sync happens automatically when a node is connected for the first time.
- Existing sockets are never updated automatically to avoid overwriting data.
- A :bl-icon:`file_refresh` button (*Sync Sockets*) button appears in the node header when a mismatch is detected,
  allowing manual synchronization.
