# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Shared search helpers on top of the RST paragraph splitter.

Both docs tools use these to iterate the bundled corpus and
locate paragraphs. Anything that reads from ``data/api`` or
``data/manual`` and cares about paragraph boundaries belongs here
rather than in an individual tool module.
"""

__all__ = (
    "SEARCH_TOOL_DESCRIPTION",
    "iter_rst_paths",
    "search",
    "with_doc",
)

import math
import os
import re
from typing import Callable, Iterator


# Shared description template for the search_*_docs tools. Both
# tools have identical user-facing semantics; only the corpus
# scope differs. The template is formatted with ``scope_name``
# (the human-readable name of the corpus) at registration time.
SEARCH_TOOL_DESCRIPTION = """
Full-text search over the bundled Blender {scope_name}.

Returns a ranked list of hits. Each hit has:

- ``path``: file path relative to the bundled docs.
- ``text``: the matching paragraph plus ``context``
  paragraphs on either side.
- ``breadcrumb``: the section path containing the hit
  (``Section > Sub-section > ...``).
- ``index``: the hit's position in the result list.
- ``score``: a relevance score; higher is better.

The query is tokenised on whitespace and matched
case-insensitively. Every token must appear somewhere in
the paragraph body, the file path, or an enclosing section
title - in any order. Common English stop-words (``the``,
``a``, ``how``, ``to``, ...) are dropped, so natural
phrasings like ``"how to bake"`` work as expected. Regular
expressions are not supported.

Use ``context`` to pull more surrounding paragraphs into
each hit (symmetric, default 0). Use ``index`` with the
position of a previous hit (same query) to get that hit
alone with its text widened to its enclosing section.

Read-only; consults bundled RST files only.
"""


def with_doc(doc: str) -> Callable[[Callable[..., object]], Callable[..., object]]:
    """
    Decorator that sets the wrapped function's ``__doc__`` from
    *doc*. Used to share the search-tool description between
    ``search_api_docs`` and ``search_manual_docs`` while keeping
    each function defined literally in its own file (so the
    ``@mcp.tool(...)`` decorator the AST-scanning tool-listing
    test looks for is still on the function definition). Stack as
    the inner decorator below ``@mcp.tool(...)`` so MCP sees the
    formatted docstring at registration.
    """
    def decorate(func: Callable[..., object]) -> Callable[..., object]:
        func.__doc__ = doc
        return func
    return decorate


from blmcp.tools_helpers.rst_parse_docs import (
    data_dir,
    split_paragraphs_with_sections_for_path,
    split_paragraphs_with_sections_from_text,
)

_SCOPE_SUBDIRS: dict[str, str] = {
    "api": "api",
    "manual": "manual",
}

# Word tokenizer: splits on whitespace and structural punctuation so
# `api/bpy.data.rst` yields {"api", "bpy", "data", "rst"} and
# `Color Management` yields {"color", "management"}. Shared by
# path-component and section-title bonus computations.
_WORD_SEP_RE = re.compile(r"[-_./\s]+")

# Multiplier on the IDF of a query token that appears as a path
# component. For a common token (IDF ~ 1) this gives a ~10 bonus,
# matching the break-even thinking we started from: a dedicated
# file outranks prose peers but still loses to heavy prose (body
# 20+). Under ~5, dedicated files stay buried; over ~50, path
# matches drown out genuinely-denser prose hits. Rare tokens get
# proportionally more since their body counts are IDF-weighted on
# the same scale; parity across query rarity is the point.
_PATH_MATCH_WEIGHT = 10

# Multiplier on the IDF of a query token that appears in an
# enclosing section title. Sized slightly above
# _PATH_MATCH_WEIGHT because a section title is more specific than
# a filename (a file can cover several topics; a section names
# exactly one), so a title match is the strongest single signal
# that a hit is authoritative.
_TITLE_MATCH_WEIGHT = 15

# Minimum paragraphs of context on each side of a drill-in hit.
# Enough to read a paragraph in its immediate context without
# dumping an entire top-level section back to the caller. The
# caller can request more via `context`; the larger of the two
# wins. The walk is always bounded by the enclosing section,
# regardless of how big the caller's window is, so expansion
# never crosses into a sibling or parent.
_DRILL_IN_MIN_CONTEXT = 3


# Query-side stop-words. Dropped from the token list before the
# AND-match runs so a natural-language query like `"how to bake"`
# does not require every paragraph to also contain `"how"` and
# `"to"` (which would eliminate the vast majority of relevant
# hits). Applied case-insensitively and only to query tokens;
# paragraph text is untouched so a paragraph mentioning a stop-word
# is still findable via its other content.
_STOPWORDS = frozenset({
    "a", "an", "and", "any", "are", "as", "at", "be", "by", "can",
    "do", "does", "for", "from", "how", "if", "in", "is", "it",
    "its", "not", "of", "on", "or", "that", "the", "this", "to",
    "was", "were", "what", "when", "where", "which", "why", "will",
    "with", "you", "your",
})


def _compile_query_pattern(token: str) -> re.Pattern[str]:
    """
    Compile *token* as a case-insensitive regex with word boundaries
    added where they make sense (the token starts or ends with a
    word character). Without boundaries a query of ``obj`` would
    match as a substring of ``object``, inflating scores on
    reference pages that list many similar-looking names. With
    boundaries ``obj`` only matches the three-letter word.
    A dotted query like ``bpy.data`` still matches ``bpy.data``
    because the ``.`` is already a word/non-word transition on both
    sides.
    """
    pattern = re.escape(token)
    if token and re.match(r"\w", token[0]):
        pattern = r"\b" + pattern
    if token and re.search(r"\w$", token):
        pattern = pattern + r"\b"
    return re.compile(pattern, re.IGNORECASE)


def _rel_to_forward_slashes(rel: str) -> str:
    """
    Normalise *rel* to forward-slash form on Windows. No-op on
    platforms where ``os.sep`` is already ``/`` so a file whose
    name legitimately contains a backslash is preserved.
    Factored out so the behaviour can be unit-tested without
    simulating a full Windows filesystem.
    """
    if os.sep == "\\":
        return rel.replace("\\", "/")
    return rel


def iter_rst_paths(scope: str) -> Iterator[tuple[str, str]]:
    """
    Yield ``(abs_path, rel_path)`` for every ``.rst`` file in *scope*.
    *scope* is one of ``"api"`` or ``"manual"``.

    *rel_path* always uses forward-slash separators so path-component
    tokenisation and the JSON output stay consistent across
    platforms; on Windows we rewrite backslashes here once at the
    boundary rather than asking every downstream consumer to know
    about them.
    """
    if scope not in _SCOPE_SUBDIRS:
        raise ValueError("scope must be one of: {:s}".format(", ".join(sorted(_SCOPE_SUBDIRS))))
    root = data_dir()
    base = os.path.join(root, _SCOPE_SUBDIRS[scope])
    for dirpath, dirnames, filenames in os.walk(base):
        # Sort in place so os.walk descends deterministically.
        dirnames.sort()
        for fn in sorted(filenames):
            if not fn.endswith(".rst"):
                continue
            full = os.path.join(dirpath, fn)
            yield full, _rel_to_forward_slashes(os.path.relpath(full, root))


def search(
        query: str,
        scope: str,
        max_results: int,
        context: int,
        index: int | None = None,
) -> dict[str, object]:
    """
    Search the bundled docs in *scope* for *query* and return
    a structured result dict of the shape returned by the search tools.

    The query is tokenised on whitespace. Common English stop-words
    (see :data:`_STOPWORDS`) are stripped from the token list before
    matching; natural-language queries like ``"how to bake"`` reduce
    to ``"bake"`` so every paragraph is not required to also contain
    the stop-words. A paragraph matches when every surviving token
    appears on some part of its match surface - the paragraph body,
    the enclosing file's path (without extension), or the
    ``" > "``-joined section breadcrumb. This lets queries like
    ``"bpy.props IntProperty"`` succeed against a paragraph that
    only mentions IntProperty in its body, because ``bpy.props`` is
    satisfied by the file path. The matcher is AND-over-tokens
    rather than an ordered phrase search. A query consisting
    entirely of stop-words returns an empty hit list.

    The scoring is TF-IDF-weighted across the per-token occurrence
    counts: rare query tokens (appearing in few files) contribute
    more per occurrence than common ones, so a file dense in the
    rare token outranks a file that is merely wordy in the common
    token. Document frequencies are computed per query from one
    corpus walk (no cache).

    Matching paragraphs whose context windows overlap are folded
    into a single hit, provided they share a section; a section
    transition (entering, leaving or moving sideways to a sibling)
    always starts a new hit so the per-hit breadcrumb and title
    bonus reflect exactly the scope of the cluster. The hit's
    ``score`` is the TF-IDF score of the cluster plus two
    additional bonuses: :data:`_PATH_MATCH_WEIGHT` per query token
    appearing as a component of the file path, and
    :data:`_TITLE_MATCH_WEIGHT` per query token per enclosing
    section title that contains it - a query word reinforced at
    multiple levels of the section hierarchy earns credit at each
    level. Both bonuses are scaled by the matching token's IDF on
    the same principle as body content, so rare-query and common-
    query structural matches have parity when compared against body
    counts. Each hit also carries ``breadcrumb``, the ``" > "``-
    joined section path from document root to the seed match
    (empty string when the file has no sections), and ``index``,
    the hit's 0-based position in the returned list. Hits are
    returned ranked by ``score`` descending. ``truncated`` is set
    when the post-rank hit list exceeds *max_results*.

    When *index* is provided the search runs normally, then
    replaces the indexed hit's ``text`` with a window of at least
    :data:`_DRILL_IN_MIN_CONTEXT` paragraphs on each side of the
    seed match, bounded by the enclosing section (so sibling or
    parent sections cannot leak in). If the caller also passes
    ``context``, the larger of the two is used - the caller can
    widen the window but the section boundary is always respected.
    An index outside the current hit range yields an empty hit
    list.
    """
    if context < 0:
        raise ValueError("context must be non-negative")
    max_results = max(1, max_results)
    tokens = [t for t in query.split() if t.lower() not in _STOPWORDS]
    if not tokens:
        return {"hits": [], "truncated": False}

    patterns = [_compile_query_pattern(t) for t in tokens]

    # One walk: collect all matching paragraphs while accumulating
    # per-token document frequencies. Needed together because TF-IDF
    # scoring cannot start until corpus-wide DF is known, but the
    # pre-filter that decides which files to paragraph-split needs
    # the same whole-file pattern checks.
    n_files = 0
    per_token_df = [0] * len(patterns)
    pre_hits: list[
        tuple[str, int, list[tuple[str, tuple[str, ...]]], list[int]]
    ] = []
    for full, rel in iter_rst_paths(scope):
        try:
            # `stat` before `open` so the cache key matches the
            # content we are about to read.
            mtime = os.stat(full).st_mtime
            with open(full, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        n_files += 1
        # The match surface is `body + path + section titles`. A
        # paragraph matches when every query token appears on at
        # least one of these surfaces, not only in body text: a
        # query like `"bpy.props IntProperty"` picks up the
        # IntProperty paragraph in `api/bpy.props.rst` because
        # `bpy.props` is satisfied by the filename even though
        # the body alone mentions only IntProperty.
        #
        # Strip the `.rst` extension so a query of `rst` does
        # not trivially match every file.
        rel_no_ext = os.path.splitext(rel)[0]
        body_present = [bool(p.search(text)) for p in patterns]
        path_present = [bool(p.search(rel_no_ext)) for p in patterns]
        for i in range(len(patterns)):
            if body_present[i] or path_present[i]:
                per_token_df[i] += 1
        # Pre-filter: every token must have some surface somewhere
        # in this file. Cheap early-out before paying the
        # paragraph-split cost.
        if not all(
            body_present[i] or path_present[i]
            for i in range(len(patterns))
        ):
            continue
        paragraphs = split_paragraphs_with_sections_from_text(
            full, mtime, text,
        )
        for idx, (para, sections) in enumerate(paragraphs):
            per_tok_count = [len(p.findall(para)) for p in patterns]
            # A token satisfies the AND rule when it is in the
            # paragraph body (contributes to TF-IDF), in the file
            # path, or in one of the enclosing section titles.
            # The breadcrumb string is a cheap single surface to
            # search for per-paragraph title presence.
            title_surface = " > ".join(sections)
            if all(
                per_tok_count[i] > 0
                or path_present[i]
                or patterns[i].search(title_surface)
                for i in range(len(patterns))
            ):
                pre_hits.append((rel, idx, paragraphs, per_tok_count))

    if not pre_hits:
        return {"hits": [], "truncated": False}

    # Smoothed IDF: `log((N+1)/(df+1)) + 1`. Always >= 1 so a
    # common-everywhere token multiplies per-token count by ~1 and
    # a rare token gives a meaningful boost. The `+1` prevents a
    # zero-weight collapse when df approaches N.
    idfs = [
        math.log((n_files + 1) / (df + 1)) + 1
        for df in per_token_df
    ]

    # Map each path/title sub-token to the IDF of the whole-token it
    # came from. Splitting `bpy.data` (one whitespace-token) yields
    # {"bpy", "data"} which can both match path components; both
    # carry the IDF of `bpy.data`. On collisions (same sub-token
    # from multiple whitespace-tokens) the larger IDF wins so the
    # bonus reflects the more discriminating source signal.
    query_bonus_tokens: dict[str, float] = {}
    for t, idf in zip(tokens, idfs):
        for s in _WORD_SEP_RE.split(t.lower()):
            if s:
                query_bonus_tokens[s] = max(
                    query_bonus_tokens.get(s, 0.0), idf,
                )

    hits: list[dict[str, object]] = []
    last_file: str | None = None
    last_idx = 0
    last_section: tuple[str, ...] = ()
    file_path_bonus = 0.0
    for rel, idx, paragraphs, per_tok_count in pre_hits:
        _, section_stack = paragraphs[idx]
        tfidf_score = sum(c * idf for c, idf in zip(per_tok_count, idfs))
        if rel != last_file:
            # File changed: recompute the per-file path-match bonus.
            # Each query token that appears as a path component adds
            # an IDF-weighted boost so files whose name contains the
            # query outrank similarly-dense prose elsewhere, with the
            # boost scaling by rarity so rare-query and common-query
            # path matches have parity against body counts.
            path_toks = {
                s for s in _WORD_SEP_RE.split(rel.lower()) if s
            }
            file_path_bonus = _PATH_MATCH_WEIGHT * sum(
                idf for q, idf in query_bonus_tokens.items()
                if q in path_toks
            )
        # Per-hit title bonus: each enclosing section contributes
        # independently, so a query word repeated across levels
        # (e.g. `color` in both `Color Management` and `Color Spaces`)
        # earns credit at each level rather than once across the union.
        # Nested sections that keep naming the topic are a stronger
        # signal that the hit is on-subject than one incidental title match.
        # Weighted by IDF on the same principle as the path bonus.
        title_bonus = 0.0
        for title in section_stack:
            title_tokens = {
                s for s in _WORD_SEP_RE.split(title.lower()) if s
            }
            title_bonus += _TITLE_MATCH_WEIGHT * sum(
                idf for q, idf in query_bonus_tokens.items()
                if q in title_tokens
            )
        if (
            rel == last_file and
            idx <= last_idx + 2 * context and
            section_stack == last_section
        ):
            # Window overlap with previous hit AND still in the same
            # section: fold this match in and extend the cluster
            # endpoint. A section transition always starts a fresh
            # hit so the breadcrumb and title bonus reflect exactly
            # the scope of the merged cluster.
            hits[-1]["score"] += tfidf_score  # type: ignore[operator]
            last_idx = idx
            continue
        lo = max(0, idx - context)
        hi = min(len(paragraphs), idx + context + 1)
        hits.append({
            "path": rel,
            "text": "\n\n".join(p[0] for p in paragraphs[lo:hi]),
            # Breadcrumb of the section path down to the seed match.
            # Empty string for files without sections so consumers
            # can always read the field without existence checks.
            "breadcrumb": " > ".join(section_stack),
            # Internal: the paragraph index within its file, used
            # when the caller drills in via the `index` argument
            # so the correct section can be located. Stripped from
            # the public response below.
            "_seed_idx": idx,
            # Float during accumulation so fold additions do not
            # drift per-step; rounded once after the loop below.
            "score": tfidf_score + file_path_bonus + title_bonus,
        })
        last_file, last_idx = rel, idx
        last_section = section_stack

    # Round all scores once, after all folds are settled. Keeps
    # score an integer in the response as LLM consumers expect
    # while avoiding per-fold rounding drift.
    for hit in hits:
        hit["score"] = int(round(hit["score"]))  # type: ignore[arg-type]

    # Python's sort is stable, so equal-count hits preserve walk order.
    hits.sort(key=lambda h: -h["score"])  # type: ignore[operator,return-value]

    truncated = len(hits) > max_results
    if truncated:
        hits = hits[:max_results]

    # Assign the public `index` field as the hit's position in the
    # ranked, truncated list so a caller can pass it back as the
    # `index` argument on a follow-up call.
    for i, hit in enumerate(hits):
        hit["index"] = i

    if index is not None:
        # Drill-in mode: expand the indexed hit's `text` to a
        # window around the seed paragraph, bounded by the
        # enclosing section. The window is at least
        # _DRILL_IN_MIN_CONTEXT paragraphs on each side; the
        # caller can push it wider via `context` (larger of the
        # two wins). Walking stops at the first paragraph outside
        # the seed's section_stack prefix, so sibling and parent
        # sections cannot leak in. An index outside the current
        # hit list returns an empty response.
        if not 0 <= index < len(hits):
            return {"hits": [], "truncated": False}
        hit = dict(hits[index])
        rel_for_expand = str(hit["path"])
        seed_idx = int(hit["_seed_idx"])  # type: ignore[arg-type]
        # Reconstruct the absolute path the same way iter_rst_paths
        # produces it, so the cache key matches and the fetch is a
        # hit rather than a re-parse.
        root = data_dir()
        abs_path = os.path.join(root, *rel_for_expand.split("/"))
        paragraphs_full = split_paragraphs_with_sections_for_path(abs_path)
        _, seed_section = paragraphs_full[seed_idx]
        seed_len = len(seed_section)

        def _in_scope(i: int) -> bool:
            return (
                0 <= i < len(paragraphs_full) and
                paragraphs_full[i][1][:seed_len] == seed_section
            )

        effective = max(_DRILL_IN_MIN_CONTEXT, context)

        lo = seed_idx
        for _ in range(effective):
            if _in_scope(lo - 1):
                lo -= 1
            else:
                break
        hi = seed_idx
        for _ in range(effective):
            if _in_scope(hi + 1):
                hi += 1
            else:
                break

        hit["text"] = "\n\n".join(
            p[0] for p in paragraphs_full[lo:hi + 1]
        )
        hit.pop("_seed_idx", None)
        return {"hits": [hit], "truncated": False}

    # Strip internal fields from the public response.
    for hit in hits:
        hit.pop("_seed_idx", None)
    return {"hits": hits, "truncated": truncated}
