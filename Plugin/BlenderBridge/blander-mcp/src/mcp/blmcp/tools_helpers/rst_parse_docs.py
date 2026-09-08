# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Shared helpers for docs tools.

Parses RST with docutils, registering stub directives and roles so the
Sphinx-style Blender docs loads cleanly. The stub code
is taken from the Blender User Manuals:

    ./tools/check_source/check_spelling.py

Walking the resulting document tree yields one paragraph per
addressable unit: a prose paragraph, a directive block, a literal or
doctest block, or a list item. Section titles merge into the first
following content node so a bare heading never consumes its own
paragraph slot.
"""

__all__ = (
    "data_dir",
    "doctree_for_path",
    "find_definition_in_doctree",
    "iter_doctrees_for_paths",
    "list_doctree_definitions",
    "split_paragraphs_for_path",
    "split_paragraphs_from_text",
    "split_paragraphs_with_sections_for_path",
    "split_paragraphs_with_sections_from_text",
)

import collections
import io
import os
from collections.abc import (
    Iterable,
    Iterator,
)

import docutils  # pylint: disable=import-error
import docutils.parsers.rst  # pylint: disable=import-error
import docutils.utils  # pylint: disable=import-error
from docutils.parsers.rst import directives, roles  # pylint: disable=import-error

_DocTree = object


def data_dir() -> str:
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.normpath(os.path.abspath(__file__)))),
        "data",
    )


# ---------------------------------------------------------------------------
# Directive and role stubs.

def _directive_ignore(
        name, arguments, options, content, lineno,
        content_offset, block_text, state, state_machine,
):
    """
    Used to explicitly mark as doctest blocks things that otherwise
    wouldn't look like doctest blocks.

    Note this doesn't ignore child nodes.
    """
    text = '\n'.join(content)
    return [docutils.nodes.doctest_block(text, text, codeblock=True)]


_directive_ignore.content = True


def _directive_ignore_recursive(
        name, arguments, options, content, lineno,
        content_offset, block_text, state, state_machine,
):
    """
    Ignore everything under this directive (use with care!)
    """
    return []


_directive_ignore_recursive.content = True


class _DirectivePreserve(docutils.parsers.rst.Directive):
    """
    Keep a directive as a container so the paragraph walker can emit it
    as one unit. Arguments become the signature line; content is
    nested-parsed so inner directives (e.g. ``.. attribute::`` inside a
    ``.. class::``) remain addressable.
    """
    required_arguments = 0
    optional_arguments = 99
    final_argument_whitespace = True
    has_content = True
    option_spec = None

    def run(self):
        container = docutils.nodes.container()
        container["directive_name"] = self.name
        args_str = " ".join(self.arguments) if self.arguments else ""
        if args_str:
            signature = ".. {:s}:: {:s}".format(self.name, args_str)
        else:
            signature = ".. {:s}::".format(self.name)
        container += docutils.nodes.literal_block(signature, signature)
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        return [container]


class _DirectiveLiteralInclude(_DirectivePreserve):
    """
    Variant of ``_DirectivePreserve`` that captures Sphinx
    ``.. literalinclude::`` options (``:lines:``, ``:language:``, etc.)
    and re-emits them on continuation lines in the preserved signature
    block. Needed so downstream scanners that rediscover literalincludes
    from rendered doctree output (e.g. the example collector in
    ``get_python_api_docs``) can honour ``:lines:`` slicing - the base
    class's ``option_spec = None`` drops them on the floor.
    """
    option_spec = {
        "lines": directives.unchanged,
        "language": directives.unchanged,
        "dedent": directives.unchanged,
        "start-after": directives.unchanged,
        "end-before": directives.unchanged,
        "start-at": directives.unchanged,
        "end-at": directives.unchanged,
        "emphasize-lines": directives.unchanged,
        "lineno-start": directives.unchanged,
        "lineno-match": directives.flag,
        "linenos": directives.flag,
        "tab-width": directives.unchanged,
        "encoding": directives.unchanged,
        "pyobject": directives.unchanged,
        "prepend": directives.unchanged,
        "append": directives.unchanged,
        "caption": directives.unchanged,
        "class": directives.unchanged,
        "name": directives.unchanged,
        "force": directives.flag,
    }

    def run(self):
        container = docutils.nodes.container()
        container["directive_name"] = self.name
        args_str = " ".join(self.arguments) if self.arguments else ""
        if args_str:
            sig_line = ".. {:s}:: {:s}".format(self.name, args_str)
        else:
            sig_line = ".. {:s}::".format(self.name)
        lines = [sig_line]
        # Stable ordering so rendered output is reproducible across
        # docutils versions (which may change the options dict type).
        for key in sorted(self.options):
            val = self.options[key]
            if val is None:
                lines.append("   :{:s}:".format(key))
            else:
                lines.append("   :{:s}: {:s}".format(key, val))
        signature = "\n".join(lines)
        container += docutils.nodes.literal_block(signature, signature)
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, container)
        return [container]


class _RoleIgnore(docutils.nodes.Inline, docutils.nodes.TextElement):
    pass


def _role_ignore(
        name, rawtext, text, lineno, inliner,
        options=None, content=None,
):
    if options is None:
        options = {}
    if content is None:
        content = []
    nodes_out, msgs = inliner.parse(text, lineno, memo=inliner, parent=inliner.parent)
    del msgs
    return [_RoleIgnore(text, '', *nodes_out, **options)], []


def _register_stubs() -> None:
    """
    Install all directive and role stubs into docutils' global
    registries. Called once at module import; keeps the loop variables
    scoped to this function rather than leaking into module namespace.
    """
    # API-defining directives: the signature line is the docs, so
    # the full block is preserved verbatim.
    for name in (
            "attribute",
            "class",
            "classmethod",
            "currentmodule",
            "data",
            "decorator",
            "exception",
            "function",
            "method",
            "module",
            "property",
            "staticmethod",
    ):
        directives.register_directive(name, _DirectivePreserve)

    # Literalinclude uses its own subclass so `:lines:` etc. survive
    # into the rendered signature; see `_DirectiveLiteralInclude`.
    directives.register_directive("literalinclude", _DirectiveLiteralInclude)

    # Content-bearing rendering directives: body kept, signature line
    # dropped.
    for name in (
            "admonition",
            "attention",
            "caution",
            "code-block",
            "danger",
            "deprecated",
            "error",
            "hint",
            "important",
            "note",
            # Custom Blender manual directive used for addon metadata
            # (`:Category:`, `:Menu:`, ...). Body keeps the field list.
            "reference",
            "seealso",
            "tip",
            "versionadded",
            "versionchanged",
            "warning",
    ):
        directives.register_directive(name, _directive_ignore)

    # Navigation-only directives: drop entirely.
    for name in (
            "autoclass",
            "automodule",
            "autosummary",
            "contents",
            "glossary",
            "highlight",
            "hlist",
            "include",
            "index",
            "only",
            "parsed-literal",
            "peertube",
            "raw",
            "sectionauthor",
            "toctree",
            "todo",
            "todolist",
            "vimeo",
            "youtube",
    ):
        directives.register_directive(name, _directive_ignore_recursive)

    # Preserve the visible text of every role we encounter - identifiers
    # inside cross-references like `:class:`bpy.types.BlendData` are
    # exactly what we want searchable in the paragraph text.
    #
    # `register_local_role` populates docutils' per-process `_roles`
    # cache directly, bypassing the language-lookup path that otherwise
    # emits an INFO `system_message` on first use. Those INFOs are
    # injected as children of container nodes (e.g. a `figure` grows
    # an empty `legend` wrapping the INFO), which leaks into
    # `astext()` output and differs between warm and cold processes.
    for name in (
            "abbr",
            "attr",
            "bl-icon",
            "class",
            "const",
            "data",
            "doc",
            "exc",
            "file",
            "func",
            "guilabel",
            "kbd",
            "math",
            "menuselection",
            "meth",
            "mod",
            "ref",
            "term",
    ):
        roles.register_local_role(name, _role_ignore)


_register_stubs()


# ---------------------------------------------------------------------------
# Parsing and paragraph walking.


def _default_settings(*, strict: bool = False):
    """
    Build a silent docutils settings object suitable for parsing
    Sphinx-flavoured RST in bulk: warnings go to a per-call sink, the
    line-length limit is relaxed, and the settings mirror those of
    check_spelling.py otherwise.

    When *strict* is ``True``, ``halt_level`` is lowered to ``ERROR``
    so docutils raises ``SystemMessage`` on unknown directives, unknown
    roles, and other malformed constructs. The default (``False``)
    tolerates everything so production parsing never fails on a
    freshly-added directive.

    A fresh object is returned per call; docutils does not contract
    that settings are read-only during parse, so sharing one instance
    across parses risks hidden cross-parse coupling. Per-call cost is
    a few microseconds and is dominated by the parse itself. The
    warning stream is a fresh ``StringIO`` per call so warnings are
    garbage-collected with the parse rather than accumulating in a
    process-global buffer.
    """
    # pylint: disable-next=import-outside-toplevel
    from docutils.frontend import get_default_settings  # type: ignore[import]
    settings = get_default_settings(docutils.parsers.rst.Parser)
    settings.tab_width = 3
    settings.pep_references = False
    settings.rfc_references = False
    settings.syntax_highlight = False
    settings.raw_enabled = True
    settings.file_insertion_enabled = True
    settings.character_level_inline_markup = False
    settings.trim_footnote_reference_space = False
    settings.report_level = 5
    settings.halt_level = 3 if strict else 5
    # Project convention is 120 columns; this is a safe very high limit
    # so docutils never rejects a bundled RST file over line length.
    settings.line_length_limit = 10_000_000
    settings.warning_stream = io.StringIO()
    return settings


def _rst_to_doctree(text: str, filename: str = "<input>", *, strict: bool = False):
    parser = docutils.parsers.rst.Parser()
    doc = docutils.utils.new_document(filename, _default_settings(strict=strict))
    parser.parse(text, doc)
    return doc


def _render_field_list(node) -> str:
    parts: list[str] = []
    for field in node.children:
        if not isinstance(field, docutils.nodes.field):
            continue
        name = ""
        body = ""
        for fc in field.children:
            if isinstance(fc, docutils.nodes.field_name):
                name = fc.astext()
            elif isinstance(fc, docutils.nodes.field_body):
                body = fc.astext().strip()
        parts.append(":{:s}: {:s}".format(name, body))
    return "\n".join(parts)


def _node_text(node) -> str:
    """
    Return a string representation of *node* suitable for inclusion in
    a paragraph. Rawsource is preferred where present; field lists are
    re-serialised with their ``:name:`` markers; otherwise ``astext()``.
    """
    if isinstance(node, docutils.nodes.field_list):
        return _render_field_list(node)
    raw = getattr(node, "rawsource", "")
    if raw:
        return raw
    return node.astext()


def _is_directive_container(node) -> bool:
    return (
        isinstance(node, docutils.nodes.container) and
        node.get("directive_name") is not None
    )


def _walk_paragraphs(doctree):
    """
    Yield paragraph strings from a document tree.

    Sections are traversed transparently; a section title is merged
    into the first following content node so it never consumes its own
    paragraph slot. A preserved directive container is emitted as one
    paragraph covering its signature and any non-directive body, while
    nested directive containers become paragraphs of their own.
    """
    pending_titles: list[str] = []

    def _flush_with_pending(text: str):
        nonlocal pending_titles
        if pending_titles:
            out = "\n\n".join(pending_titles + [text])
            pending_titles = []
            return out
        return text

    def _emit(node):
        nonlocal pending_titles
        if isinstance(node, (docutils.nodes.document, docutils.nodes.section)):
            for child in node.children:
                yield from _emit(child)
            return
        if isinstance(node, docutils.nodes.title):
            pending_titles.append(node.astext())
            return
        if isinstance(node, docutils.nodes.system_message):
            return
        if _is_directive_container(node):
            prelude_parts: list[str] = []
            nested: list = []
            for child in node.children:
                if _is_directive_container(child):
                    nested.append(child)
                else:
                    part = _node_text(child)
                    if part.strip():
                        prelude_parts.append(part)
            if prelude_parts:
                combined = "\n\n".join(prelude_parts)
                yield _flush_with_pending(combined)
            for child in nested:
                yield from _emit(child)
            return
        text = _node_text(node)
        if not text.strip():
            return
        yield _flush_with_pending(text)

    yield from _emit(doctree)
    if pending_titles:
        yield "\n\n".join(pending_titles)


# LRU cache keyed by `(path, mtime)` so the parse runs once per file
# per process lifetime. A manual `OrderedDict` (rather than
# `functools.lru_cache`) lets callers that have already read the file
# feed the text in via `split_paragraphs_from_text`, avoiding a second
# read for the paragraph splitter.
_PARAGRAPH_CACHE_MAX = 8192
_PARAGRAPH_CACHE: collections.OrderedDict[
    tuple[str, float], tuple[str, ...]
] = collections.OrderedDict()


def _cache_get(key: tuple[str, float]) -> tuple[str, ...] | None:
    result = _PARAGRAPH_CACHE.get(key)
    if result is not None:
        _PARAGRAPH_CACHE.move_to_end(key)
    return result


def _cache_put(key: tuple[str, float], value: tuple[str, ...]) -> None:
    _PARAGRAPH_CACHE[key] = value
    if len(_PARAGRAPH_CACHE) > _PARAGRAPH_CACHE_MAX:
        _PARAGRAPH_CACHE.popitem(last=False)


def split_paragraphs_from_text(path: str, mtime: float, text: str) -> list[str]:
    """
    Paragraph list for an RST file whose content is already in memory.
    Populates the same cache used by :func:`split_paragraphs_for_path`,
    so a caller that has already read the file does not pay a second
    read on a cache miss.
    """
    key = (path, mtime)
    cached = _cache_get(key)
    if cached is not None:
        return list(cached)
    doctree = _rst_to_doctree(text, filename=path)
    value = tuple(_walk_paragraphs(doctree))
    _cache_put(key, value)
    return list(value)


def split_paragraphs_for_path(path: str) -> list[str]:
    """
    Return the list of paragraphs for an RST file, cached by
    ``(path, mtime)`` so the parse runs once per file per process
    lifetime.
    """
    mtime = os.stat(path).st_mtime
    key = (path, mtime)
    cached = _cache_get(key)
    if cached is not None:
        return list(cached)
    # Bundled docs are known-UTF-8; `errors="replace"` guards against a
    # future non-UTF-8 byte crashing downstream JSON serialisation.
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    doctree = _rst_to_doctree(text, filename=path)
    value = tuple(_walk_paragraphs(doctree))
    _cache_put(key, value)
    return list(value)


# ---------------------------------------------------------------------------
# Section-aware paragraph walker.


def _walk_paragraphs_with_sections(
        doctree,
) -> Iterator[tuple[str, tuple[str, ...]]]:
    """
    Yield ``(text, section_stack)`` per paragraph.

    *text* is identical to what :func:`_walk_paragraphs` emits (titles
    of enclosing sections are merged into the first following content
    paragraph). *section_stack* is the full tuple of section titles
    from the document root down to the section containing the
    paragraph, so callers can display a breadcrumb or detect whether
    a hit lies within a title-named section.
    """
    section_stack: list[str] = []
    pending_titles: list[str] = []

    def _flush_with_pending(text: str) -> str:
        nonlocal pending_titles
        if pending_titles:
            out = "\n\n".join(pending_titles + [text])
            pending_titles = []
            return out
        return text

    def _emit(node):
        nonlocal pending_titles
        if isinstance(node, docutils.nodes.document):
            for child in node.children:
                yield from _emit(child)
            return
        if isinstance(node, docutils.nodes.section):
            # A section's first `title` child names the section; push
            # it on the stack (for breadcrumb) and into pending_titles
            # (for merge-into-next-content). Remaining children are
            # visited without re-processing the title.
            title_node = None
            for child in node.children:
                if isinstance(child, docutils.nodes.title):
                    title_node = child
                    break
            pushed = False
            if title_node is not None:
                title_text = title_node.astext()
                section_stack.append(title_text)
                pending_titles.append(title_text)
                pushed = True
            for child in node.children:
                if child is title_node:
                    continue
                yield from _emit(child)
            if pushed:
                section_stack.pop()
            return
        if isinstance(node, docutils.nodes.title):
            # Standalone title outside a section wrapper; fall back
            # to the existing merge behaviour.
            pending_titles.append(node.astext())
            return
        if isinstance(node, docutils.nodes.system_message):
            return
        if _is_directive_container(node):
            prelude_parts: list[str] = []
            nested: list = []
            for child in node.children:
                if _is_directive_container(child):
                    nested.append(child)
                else:
                    part = _node_text(child)
                    if part.strip():
                        prelude_parts.append(part)
            if prelude_parts:
                combined = "\n\n".join(prelude_parts)
                yield _flush_with_pending(combined), tuple(section_stack)
            for child in nested:
                yield from _emit(child)
            return
        text = _node_text(node)
        if not text.strip():
            return
        yield _flush_with_pending(text), tuple(section_stack)

    yield from _emit(doctree)
    if pending_titles:
        yield "\n\n".join(pending_titles), tuple(section_stack)


_PARAGRAPH_SECTION_CACHE: collections.OrderedDict[
    tuple[str, float], tuple[tuple[str, tuple[str, ...]], ...]
] = collections.OrderedDict()


def _cache_sections_get(
        key: tuple[str, float],
) -> tuple[tuple[str, tuple[str, ...]], ...] | None:
    result = _PARAGRAPH_SECTION_CACHE.get(key)
    if result is not None:
        _PARAGRAPH_SECTION_CACHE.move_to_end(key)
    return result


def _cache_sections_put(
        key: tuple[str, float],
        value: tuple[tuple[str, tuple[str, ...]], ...],
) -> None:
    _PARAGRAPH_SECTION_CACHE[key] = value
    if len(_PARAGRAPH_SECTION_CACHE) > _PARAGRAPH_CACHE_MAX:
        _PARAGRAPH_SECTION_CACHE.popitem(last=False)


def split_paragraphs_with_sections_from_text(
        path: str, mtime: float, text: str,
) -> list[tuple[str, tuple[str, ...]]]:
    """
    Paragraph + section-stack list for an RST file whose content is
    already in memory. Cached by ``(path, mtime)`` like the plain
    paragraph splitter but with an independent cache so the two
    views don't fight for space.
    """
    key = (path, mtime)
    cached = _cache_sections_get(key)
    if cached is not None:
        return list(cached)
    doctree = _rst_to_doctree(text, filename=path)
    value = tuple(_walk_paragraphs_with_sections(doctree))
    _cache_sections_put(key, value)
    return list(value)


def split_paragraphs_with_sections_for_path(
        path: str,
) -> list[tuple[str, tuple[str, ...]]]:
    """
    Return ``(text, section_stack)`` per paragraph for an RST file,
    cached by ``(path, mtime)``.
    """
    mtime = os.stat(path).st_mtime
    key = (path, mtime)
    cached = _cache_sections_get(key)
    if cached is not None:
        return list(cached)
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    doctree = _rst_to_doctree(text, filename=path)
    value = tuple(_walk_paragraphs_with_sections(doctree))
    _cache_sections_put(key, value)
    return list(value)


def _parse_one_for_worker(path: str, strict: bool = False) -> _DocTree:
    """
    Parse one RST file and return the doctree. Top-level so
    ``ProcessPoolExecutor`` can pickle it as a worker entry point.
    *strict* is passed through to ``_rst_to_doctree``.
    """
    # See `split_paragraphs_for_path` for the `errors="replace"` rationale.
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    return _rst_to_doctree(text, filename=path, strict=strict)


def _iter_parse_doctrees(
        paths_list: list[str],
        jobs: int,
        *,
        strict: bool = False,
) -> Iterator[tuple[str, _DocTree]]:
    """
    Parse every RST file in *paths_list* and yield ``(path, doctree)``
    pairs in input order. Honours *jobs* (``0`` = auto, ``1`` = serial,
    ``>=2`` = process pool). *strict* is forwarded to the worker.
    """
    if jobs == 0:
        jobs = os.cpu_count() or 1

    if jobs == 1 or len(paths_list) < 2:
        for path in paths_list:
            yield path, _parse_one_for_worker(path, strict=strict)
        return

    # pylint: disable-next=import-outside-toplevel
    import itertools
    # pylint: disable-next=import-outside-toplevel
    from concurrent.futures import ProcessPoolExecutor
    # `chunksize=1` (also the default) gives finest-grained load
    # balancing - parse times vary widely between RST files, so larger
    # batches let one worker stall the whole pool on a heavy batch while
    # others idle.
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        yield from zip(
            paths_list,
            pool.map(
                _parse_one_for_worker,
                paths_list,
                itertools.repeat(strict),
                chunksize=1,
            ),
        )


def iter_doctrees_for_paths(
        paths: Iterable[str],
        *,
        jobs: int = 0,
        strict: bool = False,
) -> Iterator[tuple[str, _DocTree]]:
    """
    Yield ``(path, doctree)`` pairs for each RST file in *paths*.

    Bypasses the paragraph cache and walker, giving callers direct access
    to the raw tree for custom traversal.

    *jobs* controls parallelism:
    ``0`` picks ``os.cpu_count()`` automatically. ``1`` parses serially
    in the caller process (no pickling, no pool). ``>=2`` spawns a
    ``ProcessPoolExecutor`` with that many workers; doctrees round-trip
    via pickle (benchmarked at ~7x faster than re-parsing in the
    destination). Pairs are yielded in input order.

    *strict* raises ``docutils.utils.SystemMessage`` on unknown
    directives, unknown roles, and other ERROR-level parse problems
    instead of tolerating them as ``system_message`` nodes in the tree.
    Intended for validation / tests; production callers should leave
    it ``False``.
    """
    yield from _iter_parse_doctrees(list(paths), jobs, strict=strict)


# ---------------------------------------------------------------------------
# Intra-file definition lookup.


def _container_signature_name(container) -> str | None:
    """
    Return the identifier defined by an API-preserving directive
    container, or ``None`` if the first child isn't a signature block.

    Reads the ``literal_block`` emitted by :class:`_DirectivePreserve`
    (always its first child) and extracts the identifier from the
    signature text by plain string splits: everything after ``:: `` and
    before ``(`` is the identifier. Handles ``IntProperty(...)``,
    ``Scene``, ``Scene(ID)``, and dotted forms like ``Scene.foo``.
    """
    if not container.children:
        return None
    first = container.children[0]
    if not isinstance(first, docutils.nodes.literal_block):
        return None
    text = first.astext()
    # Signature is always `.. <directive>:: <rest>`; take everything
    # after the first `:: `.
    _, _, rest = text.partition(":: ")
    if not rest:
        return None
    return rest.split("(", 1)[0].strip() or None


def find_definition_in_doctree(doctree, name: str) -> str | None:
    """
    Search *doctree* for an API-defining directive whose signature
    defines *name*, and return its rendered RST block or ``None``.

    *name* may be dotted (e.g. ``Scene.frame_current``) to locate a
    nested definition - a ``.. class:: Scene`` container holding a
    ``.. attribute:: frame_current``.

    Walks non-directive nodes (sections, paragraphs, ...) transparently
    at each level; only directive containers (those emitted by
    ``_DirectivePreserve``) participate in matching. Returns the block
    rendered via :func:`_walk_paragraphs`, which preserves the signature
    line plus descriptive paragraphs joined with blank lines.

    When a name occurs more than once at the same level (e.g. both
    ``.. function:: Foo`` and ``.. class:: Foo`` in the same file),
    the *first successful* match wins: if the first candidate cannot
    resolve a dotted tail the search falls through to the next sibling
    with the same head name. Duplicate definitions are not expected in
    practice for the Blender API docs.
    """
    parts = name.split(".")
    return _find_definition(doctree, parts)


def doctree_for_path(path: str) -> _DocTree:
    """
    Parse *path* and return its doctree. Convenience over
    :func:`iter_doctrees_for_paths` for single-file lookups.
    """
    return _parse_one_for_worker(path)


_DEFINITION_DIRECTIVES = frozenset({
    "attribute",
    "class",
    "classmethod",
    "data",
    "decorator",
    "exception",
    "function",
    "method",
    "property",
    "staticmethod",
})


def list_doctree_definitions(doctree) -> list[str]:
    """
    Return the sorted, deduplicated top-level API definition
    identifiers in *doctree* - every container emitted by
    ``_DirectivePreserve`` with an extractable signature name
    (``.. class:: Scene``, ``.. function:: IntProperty``, etc.).

    Module-scope directives (``.. module::``, ``.. currentmodule::``)
    are filtered out - they describe the file's module path, not a
    definition the caller can navigate to.

    Nested definitions (e.g. ``.. attribute::`` inside a class)
    are not listed here; callers wanting those can drill in via
    :func:`find_definition_in_doctree` on ``<top>.<nested>``.
    """
    names: set[str] = set()

    def _walk(node):
        for child in node.children:
            if _is_directive_container(child):
                if child.get("directive_name") in _DEFINITION_DIRECTIVES:
                    name = _container_signature_name(child)
                    if name is not None:
                        names.add(name)
                # Don't descend; only top-level definitions are listed.
            elif hasattr(child, "children"):
                _walk(child)

    _walk(doctree)
    return sorted(names)


def _find_definition(node, parts: list[str]) -> str | None:
    if not parts:
        return None
    head = parts[0]
    rest = parts[1:]
    for child in node.children:
        if _is_directive_container(child):
            if _container_signature_name(child) != head:
                continue
            if not rest:
                return "\n\n".join(_walk_paragraphs(child))
            nested = _find_definition(child, rest)
            if nested is not None:
                return nested
            continue
        # Non-container node (section, paragraph, ...): recurse with
        # the full path so a definition sitting inside a section is
        # still reachable.
        if hasattr(child, "children"):
            found = _find_definition(child, parts)
            if found is not None:
                return found
    return None
