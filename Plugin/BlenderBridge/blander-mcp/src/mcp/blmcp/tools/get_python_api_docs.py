# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable=C0114  # See tool doc-string.

__all__ = (
    "register",
)

import difflib
import os

from blmcp.tools_helpers.rst_parse_docs import (
    data_dir,
    doctree_for_path,
    find_definition_in_doctree,
    list_doctree_definitions,
)
from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error,no-name-in-module
from mcp.types import ToolAnnotations  # pylint: disable=import-error,no-name-in-module


_DOC_EXT = ".rst"

# Exact-match RST content size is capped.
# Above this, the file is replaced with a dot-point summary of its top-level definitions
# so the agent drills in with a follow-up query.
#
# Why 32 KB:
# - MCP transport ceiling is ~55-60 KB per response (observed overflow at 56 KB);
#   32 KB leaves headroom for JSON wrapping,
#   `examples`, and future growth.
# - Context economy: 32 KB of RST is ~10K tokens, ~5% of a 200K context.
#   Agents exploring an API make many lookups;
#   capping per call keeps cumulative docs under half the window across 20+ queries.
#   A larger cap (say 56 KB / ~18K tokens) risks drowning the conversation in one or two calls.
# - Most bundled files are <10 KB; only outliers like `bpy.ops.object.rst` (~150 KB) cross the cap.
#   Typical lookups are unaffected; oversized files compress ~30x to a listing the agent can navigate.
_SUMMARY_CHAR_THRESHOLD = 32 * 1024


# ---------------------------------------------------------------------------
# General utilities.


def _line_bounds_from_index(content: str, index: int) -> tuple[int, int]:
    """
    Return ``(beg, end)`` of the line in *content* that contains the
    character at *index*. ``content[beg:end]`` is the line without its
    trailing newline.
    """
    beg = content.rfind("\n", 0, index) + 1
    end = content.find("\n", index)
    if end == -1:
        end = len(content)
    return beg, end


# ---------------------------------------------------------------------------
# Path resolution under the API root.


def _resolve_inside(api_path: str, stem: str) -> str | None:
    """
    Return the resolved absolute path of ``<api_path>/<stem>.rst`` if
    the path stays under *api_path* and names an existing file. Returns
    ``None`` when the stem escapes via ``..`` or the file is missing,
    so callers can skip the entry uniformly.

    *api_path* MUST itself be resolved with :func:`os.path.realpath` (no
    symlinks, no trailing separator); the traversal-guard is a
    ``startswith`` check and silently over-accepts if the caller passes
    a denormalised root.
    """
    candidate = os.path.join(api_path, "{:s}{:s}".format(stem, _DOC_EXT))
    candidate_path = os.path.realpath(candidate)
    if not candidate_path.startswith(api_path + os.sep):
        return None
    if not os.path.isfile(candidate_path):
        return None
    return candidate_path


# ---------------------------------------------------------------------------
# Listing helpers.


def _list_direct_child_identifiers(api_path: str, identifier: str) -> list[str]:
    """
    Return the sorted direct-child identifiers of *identifier* found as
    ``<identifier>.<child>.rst`` under *api_path*.

    ``bpy`` has no ``bpy.rst`` but ``bpy.app.rst``, ``bpy.data.rst``, etc.
    exist. Matches exactly one extra dotted component so
    ``bpy.app.handlers`` is not listed under ``bpy``.
    """
    prefix = identifier + "."
    expected_dot_count = prefix.count(".")
    children: list[str] = []
    for name in os.listdir(api_path):
        if not name.endswith(_DOC_EXT) or not name.startswith(prefix):
            continue
        stem = name[:-len(_DOC_EXT)]
        if stem.count(".") != expected_dot_count:
            continue
        children.append(stem)
    children.sort()
    return children


def _list_identifiers_containing_component(api_path: str, identifier: str) -> list[str]:
    """
    Return the sorted identifiers whose dotted path contains *identifier*
    as a whole component, with descendants of a shorter match pruned out.

    Used as a "did you mean" fallback when an agent asks for an
    unqualified name like ``app`` - the tool suggests ``bpy.app`` but
    NOT ``bpy.app.handlers`` / ``bpy.app.icons`` / etc., since the agent
    can drill into them from the shorter identifier. Components match
    exactly (``app`` does NOT match ``bpy.apps`` if that existed).

    Pruning is O(n * max_depth) via bucketing by component count:
    ``buckets[k]`` holds depth-k tuples, and a depth-d tuple is pruned
    when any shorter prefix tuple exists in a shallower bucket (a
    single set lookup per prefix, rather than an O(n) scan of every
    already-kept string).
    """
    # Bucket matching identifiers by number of dotted components.
    # Tuples (not strings) so prefix lookup is one set hit per length.
    buckets: list[set[tuple[str, ...]]] = []
    for name in os.listdir(api_path):
        if not name.endswith(_DOC_EXT):
            continue
        parts = tuple(name[:-len(_DOC_EXT)].split("."))
        if identifier not in parts:
            continue
        while len(buckets) <= len(parts):
            buckets.append(set())
        buckets[len(parts)].add(parts)

    # Walk deepest-first. A tuple at depth d is dropped if any of its
    # shorter prefix tuples (length 1..d-1) exists in the corresponding
    # shallower bucket - the agent can reach it from the shorter one.
    for depth in range(len(buckets) - 1, 1, -1):
        buckets[depth] = {
            t for t in buckets[depth]
            if not any(t[:k] in buckets[k] for k in range(1, depth))
        }

    return sorted(".".join(t) for bucket in buckets for t in bucket)


def _summarize_rst_for_size(identifier: str, path: str, size: int) -> str:
    """
    Build a dot-point summary of the RST at *path* for files that
    exceed :data:`_SUMMARY_CHAR_THRESHOLD`. The header states the file
    was truncated; the body enumerates every top-level definition so
    the agent knows which ``<identifier>.<name>`` follow-ups are
    valid.
    """
    defs = list_doctree_definitions(doctree_for_path(path))
    header = (
        "File too large to inline ({:d} KB, threshold {:d} KB); "
        "definitions listed below. Query individual members as "
        "`{:s}.<name>`:\n\n"
    ).format(size // 1024, _SUMMARY_CHAR_THRESHOLD // 1024, identifier)
    if not defs:
        return header + "(no top-level definitions found)"
    return header + "\n".join("- {:s}".format(d) for d in defs)


def _list_top_level_modules(api_path: str) -> list[str]:
    """
    Return the sorted first-component names that represent real
    Python modules in the bundled API docs.

    A candidate ``X`` qualifies when either:

    - a child RST ``X.<Y>.rst`` exists (namespace splits like ``bpy``
      which has no ``bpy.rst`` but has ``bpy.app.rst`` etc.), or
    - its root ``X.rst`` declares a ``.. module::`` directive
      (self-contained modules like ``blf`` / ``bl_math``).

    Filters out documentation-meta pages such as ``index.rst``,
    ``info_overview.rst``, and ``change_log.rst`` which carry neither
    marker.
    """
    names = os.listdir(api_path)
    rst_names = {name for name in names if name.endswith(_DOC_EXT)}
    firsts = sorted({n[:-len(_DOC_EXT)].split(".", 1)[0] for n in rst_names})
    modules: list[str] = []
    for first in firsts:
        prefix = first + "."
        root_rst = first + _DOC_EXT
        # `name.startswith(prefix)` matches `<first>.rst` itself because
        # the extension's dot overlaps with the namespace separator, so
        # exclude the root file from the child test.
        if any(
            name != root_rst and name.startswith(prefix)
            for name in rst_names
        ):
            modules.append(first)
            continue
        if root_rst not in rst_names:
            continue
        root_path = os.path.join(api_path, root_rst)
        # 4 KB is plenty to reach a top-of-file `.. module::` directive
        # without pulling in the whole body; examples run ~20-200 B in.
        with open(root_path, encoding="utf-8", errors="replace") as fh:
            head = fh.read(4096)
        if head.startswith(".. module::") or "\n.. module::" in head:
            modules.append(first)
    return modules


def _filter_submodules_by_tail(submodules: list[str], tail: str) -> list[str]:
    """
    Keep submodule identifiers whose last dotted component contains
    every character of *tail*, ranked by similarity to *tail* so the
    closest typo-candidates come first.

    The char-subset check trims ``bpy.types``' ~1700 siblings on a
    typo like ``Scne`` to a few hundred entries; the similarity rank
    then lifts ``Scene`` to the top so the agent sees the obvious
    correction without scanning the whole list.
    """
    tail_chars = set(tail)
    keep = [s for s in submodules if tail_chars.issubset(s.rsplit(".", 1)[-1])]

    # Higher score first; full identifier as tie-break keeps output deterministic when scores collide.
    keep.sort(
        key=lambda candidate: (
            -difflib.SequenceMatcher(a=tail, b=candidate.rsplit(".", 1)[-1]).ratio(),
            candidate,
        ),
    )
    return keep


# ---------------------------------------------------------------------------
# RST `literalinclude` extraction
#
# Used for bundling examples.

# Paths in the bundled docs are always unquoted and space-free, so a
# plain `str.split()` on the tail of the directive line yields the path.
_LITERALINCLUDE_PREFIX = ".. literalinclude::"
_LINES_OPTION_PREFIX = ":lines:"


def _lines_option_after(content: str, start: int) -> str | None:
    """
    Scan the indented option block starting at *start* (the first
    character after a directive's newline) and return the ``:lines:``
    value if present. The block ends at the first blank line or any
    line that doesn't begin with leading-blank-space ``:``.

    Other options (``:language:``, ``:dedent:``, ...) are iterated
    past without interpretation; the current tool only acts on
    ``:lines:``.
    """
    pos = start
    while pos < len(content):
        line_end = content.find("\n", pos)
        if line_end == -1:
            line_end = len(content)
        stripped = content[pos:line_end].lstrip()
        if not stripped or not stripped.startswith(":"):
            return None
        if stripped.startswith(_LINES_OPTION_PREFIX):
            return stripped[len(_LINES_OPTION_PREFIX):].strip()
        pos = line_end + 1
    return None


def _apply_lines_spec(text: str, spec: str) -> str:
    """
    Return *text* sliced per Sphinx ``:lines:`` spec. Supports
    comma-separated parts of ``N``, ``N-``, ``-M``, ``N-M`` (all
    1-based, inclusive). Invalid parts are silently skipped so a
    malformed RST never fails the lookup.
    """
    source = text.splitlines(keepends=True)
    total = len(source)
    out: list[str] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        lo, sep, hi = part.partition("-")
        try:
            lo_i = int(lo) if lo else 1
            hi_i = int(hi) if hi else total
        except ValueError:
            continue
        if not sep:
            hi_i = lo_i
        out.extend(source[max(0, lo_i - 1):hi_i])
    return "".join(out)


def _collect_examples(content: str, api_path: str) -> list[dict[str, str]]:
    """
    Scan *content* for ``.. literalinclude:: <path>`` directives, resolve
    each path relative to *api_path* (the directory of the containing
    RST, which for the bundled API docs is always ``data/api/``), and
    return ``[{path, content}, ...]`` for every example file whose
    resolved path stays inside *api_path*.

    Duplicate directives pointing at the same file are deduplicated.
    Missing files and out-of-tree paths are silently skipped so a
    malformed RST never fails the lookup.

    *api_path* MUST itself be resolved with :func:`os.path.realpath`;
    the traversal-guard is a ``startswith`` check and the same caveat
    as :func:`_resolve_inside` applies.
    """
    examples: list[dict[str, str]] = []
    seen: set[tuple[str, str | None]] = set()
    pos = 0
    while (index := content.find(_LITERALINCLUDE_PREFIX, pos)) != -1:
        beg, end = _line_bounds_from_index(content, index)
        pos = end + 1
        # Anything between the line start and the directive must be
        # blank-space only - otherwise the match is inside prose or a
        # comment, not an RST directive at line start.
        if content[beg:index].strip():
            continue
        tokens = content[index + len(_LITERALINCLUDE_PREFIX):end].split()
        if not tokens:
            continue
        filepath_rel = tokens[0].removeprefix("./")
        lines_spec = _lines_option_after(content, end + 1)
        target_path = os.path.realpath(os.path.join(api_path, filepath_rel))
        if not target_path.startswith(api_path + os.sep):
            continue
        # Dedup key includes the slice so two directives pointing at
        # the same file with different `:lines:` each yield distinct
        # excerpts.
        dedup_key = (target_path, lines_spec)
        if dedup_key in seen:
            continue
        seen.add(dedup_key)
        try:
            # Bundled examples are known-UTF-8; `errors="replace"` guards
            # against a future non-UTF-8 byte corrupting JSON serialisation
            # of the tool's result.
            with open(target_path, encoding="utf-8", errors="replace") as fh:
                example_content = fh.read()
        except OSError:
            continue
        if lines_spec is not None:
            example_content = _apply_lines_spec(example_content, lines_spec)
        examples.append({"path": filepath_rel, "content": example_content})
    return examples


# ---------------------------------------------------------------------------
# Tool registration.


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        annotations=ToolAnnotations(
            title="Get Python API Docs",
            readOnlyHint=True,
        )
    )
    def get_python_api_docs(identifier: str) -> dict[str, object]:
        """
        Return the Blender Python API docs for *identifier*, or list
        modules matching a trailing-``*`` discovery pattern.

        *identifier* should be a fully-qualified Python name (e.g.
        ``bpy.app`` or ``bpy.types.Scene.frame_current``).
        The trailing-``*`` forms are supported as discovery entry-points:

        - ``*`` enumerates the top-level modules (``bpy``, ``bmesh``,
          ``mathutils``, ``gpu``, ...).
        - ``X.*`` enumerates the direct-child identifiers under the
          *X* namespace (``bpy.*`` -> ``bpy.app``, ``bpy.context``, ...).

        Both return a ``namespace`` response even when ``X.rst`` would
        otherwise resolve to ``exact``; the ``.*`` form lets an agent
        force the child listing.

        The response always carries ``kind``, ``found``, and ``identifier``.
        The remaining keys depend on ``kind``:

        - ``"exact"`` (``found=True``): ``<identifier>.rst`` was read.
          Extra keys: ``content`` (RST text), ``examples``. When the
          file exceeds 32 KB, ``content`` is replaced with a dot-point
          summary of the file's top-level definitions (prefixed by a
          header noting the truncation) and ``examples`` is empty -
          re-query individual members for their rendered blocks.
        - ``"namespace"`` (``found=True``):
          no ``<identifier>.rst`` but ``<identifier>.<child>.rst`` siblings exist.
          Extra key: ``submodules`` (list of child identifiers).
        - ``"definition"`` (``found=True``):
          *identifier* is defined inside a parent RST
          (e.g. ``bpy.props.IntProperty`` lives in ``bpy.props.rst``).
          Extra keys: ``content`` (rendered block), ``examples``.
        - ``"partial"`` (``found=False``):
          the parent RST was located but the trailing component isn't defined in it.
          Extra keys:
          - ``parent`` the identifier whose RST was loaded.
          - ``available`` top-level definitions in that RST.
          - ``submodules`` sibling identifiers ``<parent>.<child>`` with their own RSTs,
            filtered to those whose last component contains every character of the missing tail.

          For a toctree landing page like ``bpy.types`` ``available`` is empty and ``submodules``
          is the near-miss list; for a self-contained module like ``bpy.props`` it's the reverse.
        - ``"suggestions"`` (``found=False``):
          no direct match, but *identifier* appears as a component of other files.
          Extra key: ``suggestions`` (list of full identifiers).
        - ``"missing"`` (``found=False``): nothing matched.

        ``examples`` (present on the ``exact`` and ``definition`` kinds)
        is a list of ``{path, content}`` entries referenced from this documentation.
        """
        api_path = os.path.join(data_dir(), "api")

        # Support partial match (glob).
        if identifier == "*" or identifier.endswith(".*"):
            if identifier == "*":
                submodules = _list_top_level_modules(api_path)
            else:
                submodules = _list_direct_child_identifiers(
                    api_path, identifier[:-2],
                )
            return {
                "kind": "namespace",
                "found": True,
                "identifier": identifier,
                "submodules": submodules,
            }

        # Exact match: `<identifier>.rst` exists on disk.
        # Return its raw content, or a dot-point summary of its top-level
        # definitions when the file is above the 32 KB cap.
        if (candidate_path := _resolve_inside(api_path, identifier)) is not None:
            # See `_collect_examples` for the `errors="replace"` rationale.
            with open(candidate_path, encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            if len(content) > _SUMMARY_CHAR_THRESHOLD:
                return {
                    "kind": "exact",
                    "found": True,
                    "identifier": identifier,
                    "content": _summarize_rst_for_size(
                        identifier, candidate_path, len(content),
                    ),
                    "examples": [],
                }
            return {
                "kind": "exact",
                "found": True,
                "identifier": identifier,
                "content": content,
                "examples": _collect_examples(content, api_path),
            }

        if (submodules := _list_direct_child_identifiers(api_path, identifier)):
            return {
                "kind": "namespace",
                "found": True,
                "identifier": identifier,
                "submodules": submodules,
            }

        # Intra-file lookup: `bpy.props.IntProperty` has no `bpy.props.IntProperty.rst` of its own,
        # but `bpy.props.rst` contains a `.. function:: IntProperty` block.
        # Progressively strip trailing components until a parent RST exists,
        # then search its doc-tree for the remaining dotted tail.
        parts = identifier.split(".")
        for strip_count in range(1, len(parts)):
            prefix = ".".join(parts[:-strip_count])
            tail = ".".join(parts[-strip_count:])
            prefix_path = _resolve_inside(api_path, prefix)
            if prefix_path is None:
                continue
            doctree = doctree_for_path(prefix_path)
            if (rendered := find_definition_in_doctree(doctree, tail)):
                return {
                    "kind": "definition",
                    "found": True,
                    "identifier": identifier,
                    "content": rendered,
                    "examples": _collect_examples(rendered, api_path),
                }
            # Parent RST located but tail isn't defined there; don't
            # look further up - that would match unrelated identifiers
            # in remoter files.
            return {
                "kind": "partial",
                "found": False,
                "identifier": identifier,
                "parent": prefix,
                "available": list_doctree_definitions(doctree),
                "submodules": _filter_submodules_by_tail(
                    _list_direct_child_identifiers(api_path, prefix), tail,
                ),
            }

        # "Did you mean" fallback: the identifier didn't match as a
        # file or resolve intra-file, but it appears as a dotted
        # component of other files - surface those as suggestions so
        # the agent can retry with a valid name.
        if (suggestions := _list_identifiers_containing_component(api_path, identifier)):
            return {
                "kind": "suggestions",
                "found": False,
                "identifier": identifier,
                "suggestions": suggestions,
            }

        return {"kind": "missing", "found": False, "identifier": identifier}
