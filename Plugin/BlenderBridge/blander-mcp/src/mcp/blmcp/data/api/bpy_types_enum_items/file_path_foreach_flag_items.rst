.. _rna_enum_file_path_foreach_flag_items:

File Path Foreach Flag Items
############################

:SKIP_LINKED: Skip Linked.

   Skip paths of linked IDs.
:SKIP_PACKED: Skip Packed.

   Skip paths when their matching data is packed.
:RESOLVE_TOKEN: Resolve Token.

   Resolve tokens within a virtual filepath to a single, concrete, filepath. Currently only used for UDIM tiles.
:SKIP_WEAK_REFERENCES: Skip Weak References.

   Skip weak reference paths. Those paths are typically 'nice to have' extra information, but are not used as actual source of data by the current .blend file.
:SKIP_MULTIFILE: Skip Multi-file.

   Skip paths where a single dir is used with an array of files, eg. sequence strip images or point-caches. In this case only the first file path is processed. This is needed for directory manipulation callbacks which might otherwise modify the same directory multiple times.
:RELOAD_EDITED: Reload Edited.

   Reload data when the path is edited.
