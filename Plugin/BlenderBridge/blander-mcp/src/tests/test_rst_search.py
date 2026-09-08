# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Unit tests for the RST text-search layer.

Each test writes a synthetic RST corpus to a tempdir and calls
``rst_doc_search.search`` directly. No MCP subprocess is spawned;
the MCP wiring is already covered by ``test_mcp_server.py``.
Synthetic corpora keep assertions stable against upstream changes
to the bundled docs and let individual tests control the exact
paragraph structure under test.

Run with::

    python -m unittest tests.test_rst_search -v
"""

__all__ = ()

import contextlib
import importlib
import os
import sys
import tempfile
import unittest
from collections.abc import Iterator
from unittest import mock
from typing import Any

_REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MCP_DIR = os.path.join(_REPO_DIR, "mcp")


def _import_search_modules() -> tuple[Any, Any]:
    """
    Import and return ``(rst_doc_search, rst_parse_docs)`` from the
    local checkout, adding the mcp directory to ``sys.path`` once.
    """
    if _MCP_DIR not in sys.path:
        sys.path.insert(0, _MCP_DIR)
    rst_doc_search = importlib.import_module("blmcp.tools_helpers.rst_doc_search")
    rst_parse_docs = importlib.import_module("blmcp.tools_helpers.rst_parse_docs")
    return rst_doc_search, rst_parse_docs


@contextlib.contextmanager
def _synthetic_corpus(files: dict[str, str]) -> Iterator[str]:
    """
    Write *files* (rel-path -> RST content) under a tempdir and patch
    ``data_dir`` so search helpers resolve paths against the tempdir.
    Paths in *files* should begin with ``api/`` or ``manual/``.

    Clears the paragraph cache on entry and exit so stale doctrees
    from the real corpus (or prior tests) cannot leak in.
    """
    rst_doc_search, rst_parse_docs = _import_search_modules()
    with tempfile.TemporaryDirectory() as tmp:
        for rel, content in files.items():
            full = os.path.join(tmp, rel)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as fh:
                fh.write(content)
        rst_parse_docs._PARAGRAPH_CACHE.clear()
        rst_parse_docs._PARAGRAPH_SECTION_CACHE.clear()
        # `from ... import data_dir` binds the name locally, so
        # patch the consumer module, not the definer.
        with (
            mock.patch.object(rst_doc_search, "data_dir", return_value=tmp),
            mock.patch.object(rst_parse_docs, "data_dir", return_value=tmp),
        ):
            yield tmp
        rst_parse_docs._PARAGRAPH_CACHE.clear()
        rst_parse_docs._PARAGRAPH_SECTION_CACHE.clear()


def _search(**kwargs: Any) -> dict[str, Any]:
    """
    Convenience wrapper around ``rst_doc_search.search`` that applies
    defaults useful to most tests here.
    """
    rst_doc_search, _ = _import_search_modules()
    params = {
        "max_results": 10,
        "context": 0,
    }
    params.update(kwargs)
    return rst_doc_search.search(**params)


# ---------------------------------------------------------------------------
# AND-match across tokens (any order, anywhere in paragraph).


class TestAndMatchSemantics(unittest.TestCase):
    """
    Query tokens must all appear in a single paragraph but may do so
    in any order, with arbitrary intervening content.
    """

    def test_adjacent_in_order_matches(self) -> None:
        """
        Baseline: tokens appearing adjacent and in order still match.
        """
        corpus = {
            "manual/a.rst": "To bake a normal map, click Apply.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake normal map", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_tokens_reordered_still_match(self) -> None:
        """
        Same paragraph, query tokens in a different order: still a hit.
        The order-independent matcher should not care.
        """
        corpus = {
            "manual/a.rst": "To bake a normal map, click Apply.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="map bake normal", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_tokens_separated_by_other_words_match(self) -> None:
        """
        Tokens need not be adjacent: ``bake unwrap`` matches a
        paragraph that has other words between them.
        """
        corpus = {
            "manual/b.rst": "Bake the texture, then unwrap the mesh.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake unwrap", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/b.rst", paths)

    def test_missing_token_rejects_paragraph(self) -> None:
        """
        A paragraph missing one query token must not match, even if
        other tokens are heavily present.
        """
        corpus = {
            "manual/c.rst": "Only bake, no m-word here.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake normal", scope="manual")
        self.assertEqual(result["hits"], [])

    def test_case_insensitive_still_matches(self) -> None:
        """
        Regression: the matcher stays case-insensitive after the
        rewrite from single regex to per-token list.
        """
        corpus = {
            "manual/e.rst": "bake this thoroughly.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="BAKE", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/e.rst", paths)


# ---------------------------------------------------------------------------
# Stop-word filtering on query tokens.


class TestStopWordFiltering(unittest.TestCase):
    """
    Common English stop-words in the query are dropped before
    matching. They do not require paragraphs to also contain them
    (under AND-match) and do not affect paragraph content rules.
    """

    def test_stopwords_reduce_query_to_content_words(self) -> None:
        """
        ``"how to bake"`` finds the same paragraph as ``"bake"``:
        the stop-words ``how`` and ``to`` are dropped, leaving one
        token that matches the paragraph.
        """
        corpus = {
            "manual/a.rst": "The user can bake a normal map here.\n",
        }
        with _synthetic_corpus(corpus):
            result_phrased = _search(query="how to bake", scope="manual")
            result_plain = _search(query="bake", scope="manual")
        self.assertEqual(
            [h["path"] for h in result_phrased["hits"]],
            [h["path"] for h in result_plain["hits"]],
        )
        self.assertTrue(result_phrased["hits"])

    def test_stopword_only_query_returns_empty(self) -> None:
        """
        A query made entirely of stop-words has no surviving tokens
        after filtering and returns an empty hit list, like an empty
        query.
        """
        corpus = {
            "manual/a.rst": "The user can bake a normal map here.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="how to", scope="manual")
        self.assertEqual(result, {"hits": [], "truncated": False})

    def test_stopword_stripping_is_case_insensitive(self) -> None:
        """
        Stop-words are stripped regardless of case: ``"HOW TO Bake"``
        reduces to a single content token ``"Bake"`` and matches the
        paragraph.
        """
        corpus = {
            "manual/a.rst": "User can bake a normal map here.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="HOW TO Bake", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_stopword_in_content_does_not_affect_matching(self) -> None:
        """
        Stop-word filtering applies only to the query side; a
        paragraph containing stop-words is not special-cased and is
        still findable via its content words.
        """
        corpus = {
            "manual/a.rst": "How the shading workflow is documented.\n",
        }
        with _synthetic_corpus(corpus):
            # Query contains only content words; paragraph has
            # stop-words interleaved.
            result = _search(query="shading workflow", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_stopwords_mixed_with_content_leave_content_only(self) -> None:
        """
        ``"how is the workflow"`` reduces to ``"workflow"``: the
        paragraph must contain ``workflow`` but not any of the
        dropped stop-words.
        """
        corpus = {
            "manual/match.rst": "The rendering workflow can be long.\n",
            "manual/stopwords_only.rst": "How is the pipeline configured.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="how is the workflow", scope="manual")
        paths = {h["path"] for h in result["hits"]}
        self.assertIn("manual/match.rst", paths)
        # Not matched: paragraph lacks `workflow`, even though it
        # has all the stop-words the query mentioned.
        self.assertNotIn("manual/stopwords_only.rst", paths)


# ---------------------------------------------------------------------------
# Section-title boost.


def _rst_section(title: str, body: str, underline: str = "=") -> str:
    """
    Return an RST fragment with *title* as a section heading, followed
    by *body* as the section's content. *underline* picks the level
    (``=`` top, ``-`` next, ``~`` deeper).
    """
    rule = underline * max(len(title), 3)
    return "{:s}\n{:s}\n\n{:s}\n".format(title, rule, body)


class TestSectionTitleBoost(unittest.TestCase):
    """
    A query token that matches a section title enclosing the hit
    contributes a fixed score bonus. Title matches are more specific
    than filename matches (a file can cover several topics; a
    section names exactly one) so the bonus outranks similarly-dense
    prose elsewhere.
    """

    def test_title_match_beats_prose_density(self) -> None:
        """
        File A has the query in its section title and one body
        mention. File B has no title match but many body mentions.
        Despite lower body density, File A ranks first because of
        the title bonus.
        """
        corpus = {
            # File A: title contains 'subdivision' and 'surface'.
            "manual/a.rst": _rst_section(
                "Subdivision Surface Modifier",
                "Applies a subdivision surface algorithm.\n",
            ),
            # File B: title is unrelated; the words appear five
            # times in prose.
            "manual/b.rst": _rst_section(
                "General Tips",
                "A subdivision surface helps; "
                "subdivision surface is useful; "
                "the subdivision surface modifier exists; "
                "you might want subdivision surface; "
                "try subdivision surface sometime.",
            ),
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="subdivision surface", scope="manual",
            )
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(paths[0], "manual/a.rst")

    def test_subsection_title_match(self) -> None:
        """
        A nested section title contributes to the title bonus the
        same as a top-level title: the query sees the full enclosing
        stack.
        """
        corpus = {
            "manual/a.rst": (
                _rst_section(
                    "Rendering",
                    _rst_section(
                        "Color Spaces",
                        "Configure each display view here.\n",
                        underline="-",
                    ),
                )
            ),
            "manual/b.rst": "color spaces are useful.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="color spaces", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(paths[0], "manual/a.rst")

    def test_no_title_file_has_no_boost(self) -> None:
        """
        A file without section titles earns no title bonus: its
        ``score`` equals its body-derived count.
        """
        corpus = {
            "manual/a.rst": "The bake operator bakes the mesh.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake", scope="manual")
        self.assertEqual(len(result["hits"]), 1)
        # Raw body count for "bake" in that paragraph is 2 (bake,
        # bakes doesn't match as substring 'bake' -> actually 'bake'
        # matches 'bakes' too because 'bakes' contains 'bake').
        # Just assert no title bonus was applied: count stays small
        # (< _TITLE_MATCH_WEIGHT).
        self.assertLess(result["hits"][0]["score"], 15)

    def test_title_and_path_bonuses_stack(self) -> None:
        """
        When the query matches both the file path and the section
        title, both bonuses apply additively. Verify the combined
        hit outscores either bonus alone.
        """
        corpus = {
            # Both path components and title contain 'color' and
            # 'management': path bonus + title bonus.
            "manual/render/color_management/index.rst": _rst_section(
                "Color Management",
                "Configure scene color management here.\n",
            ),
            # Path match only: title is unrelated.
            "manual/render/color_management/unrelated.rst": _rst_section(
                "Tips",
                "This page discusses color and management separately.\n",
            ),
            # Title match only: path is unrelated.
            "manual/other.rst": _rst_section(
                "Color Management",
                "Prose about color and management.\n",
            ),
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="color management", scope="manual",
            )
        # index.rst has path(+20) + title(+30) bonuses; the others
        # get only one of the two.
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(
            paths[0], "manual/render/color_management/index.rst",
        )

    def test_title_bonus_scales_with_nested_match_depth(self) -> None:
        """
        Two files each have a section hierarchy mentioning the
        query word. File A repeats the word at every nesting level;
        File B mentions it in one title only. A ranks higher - the
        bonus credits each enclosing title independently, so deeper
        reinforcement scores higher than an incidental single-level
        match.
        """
        file_a = _rst_section(
            "Color Primer",
            _rst_section(
                "Color Management",
                _rst_section(
                    "Color Spaces",
                    "The unique_match_needle appears here.\n",
                    underline="~",
                ),
                underline="-",
            ),
        )
        file_b = _rst_section(
            "Rendering Primer",
            _rst_section(
                "Color Management",
                _rst_section(
                    "Display Configuration",
                    "The unique_match_needle appears here.\n",
                    underline="~",
                ),
                underline="-",
            ),
        )
        corpus = {
            "manual/file_a.rst": file_a,
            "manual/file_b.rst": file_b,
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="color unique_match_needle", scope="manual",
            )
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(paths[0], "manual/file_a.rst")
        self.assertEqual(paths[1], "manual/file_b.rst")

    def test_hit_without_title_match_still_returned(self) -> None:
        """
        Regression: a match that contains no title-boost
        contribution is still returned as a hit (just with a lower
        score), not filtered out.
        """
        corpus = {
            # No section title; just a paragraph with content match.
            "manual/a.rst": "The bake workflow is documented in detail.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)


# ---------------------------------------------------------------------------
# Breadcrumb field.


class TestBreadcrumb(unittest.TestCase):
    """
    Every hit carries a ``breadcrumb`` string naming the section
    hierarchy from the file's root title down to the hit.
    """

    def test_nested_sections_joined_with_arrows(self) -> None:
        """
        Root > middle > leaf section containing the match yields
        ``"Root > Middle > Leaf"``.
        """
        content = (
            _rst_section(
                "Root",
                _rst_section(
                    "Middle",
                    _rst_section(
                        "Leaf",
                        "The unique_match_needle is here.\n",
                        underline="~",
                    ),
                    underline="-",
                ),
            )
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            result = _search(query="unique_match_needle", scope="manual")
        self.assertEqual(len(result["hits"]), 1)
        self.assertEqual(
            result["hits"][0]["breadcrumb"],
            "Root > Middle > Leaf",
        )

    def test_single_section_breadcrumb(self) -> None:
        """
        A file with only a top-level title reports a single-element
        breadcrumb.
        """
        content = _rst_section(
            "Only Title",
            "The unique_match_needle is here.\n",
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            result = _search(query="unique_match_needle", scope="manual")
        self.assertEqual(
            result["hits"][0]["breadcrumb"],
            "Only Title",
        )

    def test_no_section_file_empty_breadcrumb(self) -> None:
        """
        A file with no section titles yields an empty-string
        breadcrumb. The key must still exist so consumers don't
        need presence checks.
        """
        with _synthetic_corpus({
            "manual/a.rst": "The unique_match_needle sits alone.\n",
        }):
            result = _search(query="unique_match_needle", scope="manual")
        self.assertEqual(len(result["hits"]), 1)
        self.assertIn("breadcrumb", result["hits"][0])
        self.assertEqual(result["hits"][0]["breadcrumb"], "")

    def test_cluster_merge_preserves_seed_breadcrumb(self) -> None:
        """
        When cluster-folding absorbs later matches into the first
        hit, the first match's breadcrumb is preserved (we do not
        change the field when folding).
        """
        content = _rst_section(
            "Outer",
            _rst_section(
                "Inner",
                (
                    "The unique_match_needle first.\n"
                    "\n"
                    "Intermediate paragraph without the word.\n"
                    "\n"
                    "The unique_match_needle again.\n"
                ),
                underline="-",
            ),
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            result = _search(
                query="unique_match_needle",
                scope="manual",
                context=1,
            )
        self.assertEqual(len(result["hits"]), 1)
        self.assertEqual(
            result["hits"][0]["breadcrumb"],
            "Outer > Inner",
        )

    def test_adjacent_sibling_sections_do_not_fold(self) -> None:
        """
        Two matches at adjacent paragraph indices but in sibling
        sub-sections do not merge into one cluster, even when the
        context window would otherwise make them overlap. Each
        hit keeps its own breadcrumb so the consumer sees the
        actual section context of each match.
        """
        content = _rst_section(
            "Outer",
            (
                _rst_section(
                    "Alpha",
                    "The unique_match_needle alpha.\n",
                    underline="-",
                ) +
                _rst_section(
                    "Beta",
                    "The unique_match_needle beta.\n",
                    underline="-",
                )
            ),
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            result = _search(
                query="unique_match_needle",
                scope="manual",
                # Index-wise adjacent: without the section check,
                # this window would fold the two matches together.
                context=1,
            )
        breadcrumbs = sorted(h["breadcrumb"] for h in result["hits"])
        self.assertEqual(
            breadcrumbs,
            ["Outer > Alpha", "Outer > Beta"],
        )

    def test_parent_child_section_boundary_does_not_fold(self) -> None:
        """
        A match in a parent section followed by an adjacent match
        in a nested child section stays as two hits. The parent
        match keeps its parent-only breadcrumb; the child match
        gets the full nested breadcrumb - neither steals the
        other's section context.
        """
        content = _rst_section(
            "Parent",
            (
                "The unique_match_needle at parent level.\n"
                "\n"  # blank line before the nested heading
                + _rst_section(
                    "Child",
                    "The unique_match_needle in child.\n",
                    underline="-",
                )
            ),
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            result = _search(
                query="unique_match_needle",
                scope="manual",
                context=1,
            )
        breadcrumbs = sorted(h["breadcrumb"] for h in result["hits"])
        self.assertEqual(
            breadcrumbs,
            ["Parent", "Parent > Child"],
        )

    def test_all_hits_carry_breadcrumb_field(self) -> None:
        """
        Shape regression: every hit dict has the ``breadcrumb`` key
        regardless of whether a section stack exists.
        """
        corpus = {
            "manual/with_section.rst": _rst_section(
                "A", "The unique_match_needle here.\n",
            ),
            "manual/bare.rst": "The unique_match_needle sits bare.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="unique_match_needle", scope="manual")
        for hit in result["hits"]:
            self.assertIn("breadcrumb", hit)
            self.assertIsInstance(hit["breadcrumb"], str)


# ---------------------------------------------------------------------------
# TF-IDF ranking across tokens of differing document frequency.


class TestIdfWeighting(unittest.TestCase):
    """
    Multi-token queries rank results using TF-IDF. Rare tokens
    contribute more to ``score`` per occurrence than common
    tokens, so a file dense in the rare token beats one that is
    merely verbose in the common token.
    """

    def test_rare_token_density_outranks_common_token_density(self) -> None:
        """
        Corpus of 10 files. ``color`` appears in every file;
        ``management`` appears in only two. Only those two files
        match the AND query. Between them, the file with more of
        the rare token (``management``) beats the one with more of
        the common token (``color``).
        """
        corpus: dict[str, str] = {}
        # Eight files containing only 'color' - they inflate df(color)
        # but do not match the AND query (no 'management').
        for i in range(8):
            corpus["manual/only_color_{:d}.rst".format(i)] = (
                "This page discusses color briefly.\n"
            )
        # File A: low color, high management. Both tokens present.
        corpus["manual/file_a.rst"] = (
            "The color page. management management management concept.\n"
        )
        # File B: high color, low management. Both tokens present.
        corpus["manual/file_b.rst"] = (
            "The color color color color page. management once.\n"
        )
        with _synthetic_corpus(corpus):
            result = _search(query="color management", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        # Only file_a and file_b pass the AND match; file_a's
        # rare-token density wins.
        self.assertEqual(paths[0], "manual/file_a.rst")
        self.assertIn("manual/file_b.rst", paths)
        self.assertEqual(len(paths), 2)

    def test_single_token_query_ranks_by_count(self) -> None:
        """
        For a single-token query the IDF factor is a constant
        across all hits, so ranking collapses back to occurrence
        count: higher-count file first.
        """
        corpus = {
            "manual/few.rst": "bake once.\n",
            "manual/many.rst": "bake bake bake bake bake here.\n",
            "manual/mid.rst": "bake bake twice.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(
            paths,
            ["manual/many.rst", "manual/mid.rst", "manual/few.rst"],
        )

    def test_idf_happens_after_stopword_filter(self) -> None:
        """
        Stop-words are stripped before TF-IDF runs, so a query like
        ``"how is the color"`` reduces to ``"color"`` and never
        computes or applies a weight for the dropped words.
        """
        corpus = {
            "manual/match.rst": "The color page is useful.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="how is the color", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/match.rst", paths)

    def test_zero_df_token_returns_no_hits(self) -> None:
        """
        A query token that is absent from every file in scope
        cannot satisfy the AND-match, so the search returns an
        empty, well-formed response - no division-by-zero or
        infinite weight from the smoothed IDF formula leaks out.
        """
        corpus = {
            "manual/a.rst": "bake the mesh.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="nonexistent_token_xyzzy", scope="manual")
        self.assertEqual(result, {"hits": [], "truncated": False})

    def test_idf_scaling_lifts_rare_token_path_match(self) -> None:
        """
        A file whose name contains a rare query token outranks a
        prose-heavy rival whose body count would exceed a flat path
        bonus. With IDF-scaled bonuses the path boost grows for
        rare tokens so the structural signal stays authoritative.
        """
        corpus: dict[str, str] = {}
        # Eight filler files inflate df(color) so color becomes the
        # common token (df=10, IDF ~ 1).
        for i in range(8):
            corpus["manual/filler_{:d}.rst".format(i)] = (
                "This file mentions color once.\n"
            )
        # File X: 'unique_xyzzy' appears only here (df=1, high IDF)
        # and its filename contains the rare token; body mentions
        # each query term once.
        corpus["manual/unique_xyzzy.rst"] = (
            "This page discusses color and unique_xyzzy together.\n"
        )
        # File Y: rival with heavy color prose and one rare mention,
        # but no path bonus.
        corpus["manual/prose_heavy.rst"] = (
            "color color color color color color color color color "
            "color color color color color color color color color "
            "color color color unique_xyzzy appears once.\n"
        )
        with _synthetic_corpus(corpus):
            result = _search(query="color unique_xyzzy", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(paths[0], "manual/unique_xyzzy.rst")

    def test_common_token_path_bonus_unchanged(self) -> None:
        """
        Regression guard: for a single-token common query, the path
        bonus magnitudes stay close to the pre-scaling values
        (IDF ~ 1 when the token is in every file). Ordering and
        rough score size match expectations from the flat-bonus era.
        """
        corpus = {
            "manual/bake.rst": "The bake workflow is described.\n",
            "manual/other.rst": "Procedures that bake things.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake", scope="manual")
        # Path-named file wins.
        self.assertEqual(result["hits"][0]["path"], "manual/bake.rst")
        # Magnitude: IDF ~= 1 for 'bake' appearing in all files, so
        # the bonus is ~_PATH_MATCH_WEIGHT * 1 = ~10 on top of body.
        # Assert the score is in a sane window rather than an exact
        # value (IDF is not exactly 1 due to smoothing).
        self.assertGreater(result["hits"][0]["score"], 10)
        self.assertLess(result["hits"][0]["score"], 20)

    def test_multi_token_path_bonus_uses_per_token_idf(self) -> None:
        """
        For a multi-token query where only one token is in the path,
        the bonus reflects that token's IDF specifically - not a
        blended or largest-IDF applied to the whole query.
        """
        corpus: dict[str, str] = {}
        # 'color' is in every file (common, IDF ~ 1).
        for i in range(9):
            corpus["manual/filler_{:d}.rst".format(i)] = (
                "color content here.\n"
            )
        # Path contains only 'color' (common); 'unique_xyzzy' is
        # rare but not in path. The path bonus should be modest
        # (IDF of 'color'), not amplified by the rare token.
        corpus["manual/color_page.rst"] = (
            "The color page mentions unique_xyzzy once.\n"
        )
        # Rival has neither token in path; both tokens once in body.
        corpus["manual/other.rst"] = (
            "Plain text color with unique_xyzzy inline.\n"
        )
        with _synthetic_corpus(corpus):
            result = _search(
                query="color unique_xyzzy", scope="manual",
            )
        scores = {h["path"]: h["score"] for h in result["hits"]}
        # The path-named file wins because of the color path bonus,
        # but its margin over the rival is modest (the bonus is
        # IDF('color') * _PATH_MATCH_WEIGHT, not the rare-token
        # IDF). Without per-token IDF mapping, the bonus would
        # instead reflect the larger rare-token IDF and the margin
        # would be much bigger.
        self.assertIn("manual/color_page.rst", scores)
        self.assertIn("manual/other.rst", scores)
        self.assertGreater(
            scores["manual/color_page.rst"],
            scores["manual/other.rst"],
        )
        margin = (
            scores["manual/color_page.rst"]
            - scores["manual/other.rst"]
        )
        # Margin should be bounded near _PATH_MATCH_WEIGHT (~10),
        # not near _PATH_MATCH_WEIGHT * rare_IDF (~20-30).
        self.assertLess(margin, 15)

    def test_rare_and_common_multi_token_zero_match(self) -> None:
        """
        Mixed query where one token exists and another does not:
        the AND-match fails globally and the search returns
        ``{hits: [], truncated: false}`` without producing a
        partial-match hit.
        """
        corpus = {
            "manual/a.rst": "bake the mesh.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="bake nonexistent_token_xyzzy", scope="manual",
            )
        self.assertEqual(result, {"hits": [], "truncated": False})


# ---------------------------------------------------------------------------
# Cross-platform path handling.


class TestPlatformPaths(unittest.TestCase):
    """
    Paths in the response use forward slashes regardless of the
    platform the server runs on. On Windows the raw rel path from
    ``os.path.relpath`` uses backslashes, which would prevent the
    path-component tokenizer from splitting them and would leak
    backslashes into the JSON response.
    """

    def test_rel_normalizer_rewrites_backslashes_on_windows(self) -> None:
        """
        The normaliser converts backslashes to forward slashes only
        when ``os.sep`` is a backslash. Direct unit test of the
        helper so the Windows branch is exercised even when the
        host filesystem is Unix.
        """
        rst_doc_search, _ = _import_search_modules()
        with mock.patch.object(rst_doc_search.os, "sep", "\\"):
            self.assertEqual(
                rst_doc_search._rel_to_forward_slashes("manual\\sub\\a.rst"),
                "manual/sub/a.rst",
            )

    def test_rel_normalizer_preserves_backslashes_on_unix(self) -> None:
        """
        On systems where ``os.sep`` is ``/``, the normaliser is a
        no-op; a literal backslash in a filename survives untouched.
        """
        rst_doc_search, _ = _import_search_modules()
        with mock.patch.object(rst_doc_search.os, "sep", "/"):
            self.assertEqual(
                rst_doc_search._rel_to_forward_slashes("manual/odd\\name.rst"),
                "manual/odd\\name.rst",
            )

    def test_returned_path_uses_forward_slashes(self) -> None:
        """
        End-to-end: hits carry a path with forward slashes only, so
        both the path-component tokenizer (used for the path bonus)
        and JSON consumers see consistent separators on every OS.
        """
        corpus = {
            "manual/sub_dir/a.rst": "The unique_match_needle is here.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="unique_match_needle", scope="manual")
        self.assertEqual(len(result["hits"]), 1)
        self.assertNotIn("\\", result["hits"][0]["path"])
        self.assertEqual(
            result["hits"][0]["path"], "manual/sub_dir/a.rst",
        )


# ---------------------------------------------------------------------------
# Score-composition invariants.


class TestScoreComposition(unittest.TestCase):
    """
    Invariants about how per-hit scores are composed, independent
    of the specific weight values.
    """

    def test_path_bonus_counted_once_per_hit_not_accumulated(self) -> None:
        """
        The per-file path bonus is cached on the ``rel != last_file``
        edge and re-used across every hit from that file. This test
        locks the invariant by comparing a path-named file against
        a structurally identical but non-path-named rival: the
        per-hit score delta should be the same constant across all
        hits, not grow with hit index (which is what would happen
        if the bonus were accidentally accumulated into
        ``file_path_bonus`` across iterations).
        """
        sections = (
            _rst_section(
                "Alpha Heading",
                "The needle_xyzzy in alpha.\n",
                underline="-",
            ) +
            _rst_section(
                "Beta Heading",
                "The needle_xyzzy in beta.\n",
                underline="-",
            ) +
            _rst_section(
                "Gamma Heading",
                "The needle_xyzzy in gamma.\n",
                underline="-",
            )
        )
        # Wrap both under a single root section so the walker emits
        # three distinct sibling sub-sections (non-folding).
        corpus = {
            "manual/needle_xyzzy.rst": _rst_section("Root", sections),
            "manual/unrelated.rst": _rst_section("Root", sections),
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="needle_xyzzy", scope="manual", max_results=10,
            )
        named = sorted(
            h["score"] for h in result["hits"]
            if h["path"] == "manual/needle_xyzzy.rst"
        )
        rival = sorted(
            h["score"] for h in result["hits"]
            if h["path"] == "manual/unrelated.rst"
        )
        self.assertEqual(len(named), 3)
        self.assertEqual(len(rival), 3)
        # Every paired hit has the same delta - the path bonus. If
        # the bonus were accumulating across iterations, later
        # hits in `needle_xyzzy.rst` would have larger deltas.
        deltas = [n - r for n, r in zip(named, rival)]
        self.assertEqual(len(set(deltas)), 1)
        # And the delta must be positive (path match DID contribute).
        self.assertGreater(deltas[0], 0)


# ---------------------------------------------------------------------------
# Truncation preserves top-scored hits.


class TestMaxResultsTruncation(unittest.TestCase):
    """
    When the post-rank hit list exceeds ``max_results``, the
    response keeps the highest-scored hits, not the first-found
    ones. ``truncated`` reports the overflow.
    """

    def test_truncation_keeps_the_highest_scores(self) -> None:
        """
        Five files with monotonically increasing body counts of the
        query token (hence monotonically increasing scores). A
        query with ``max_results=3`` must return the top three
        by score (not by walk order) with ``truncated=True``.
        """
        # Each file has a title so no path bonus interferes with the
        # ordering; the only score signal is TF-IDF body density.
        corpus: dict[str, str] = {}
        for i in range(1, 6):
            body = " ".join(["needle_xyzzy"] * i) + " padding.\n"
            corpus["manual/f{:d}.rst".format(i)] = _rst_section(
                "Page {:d}".format(i), body,
            )
        with _synthetic_corpus(corpus):
            result = _search(
                query="needle_xyzzy", scope="manual", max_results=3,
            )
        self.assertTrue(result["truncated"])
        self.assertEqual(len(result["hits"]), 3)
        # Top 3 by body count are files 5, 4, 3 (highest-first).
        paths = [h["path"] for h in result["hits"]]
        self.assertEqual(
            paths,
            ["manual/f5.rst", "manual/f4.rst", "manual/f3.rst"],
        )
        # Scores are in strictly descending order.
        scores = [h["score"] for h in result["hits"]]
        self.assertEqual(scores, sorted(scores, reverse=True))


# ---------------------------------------------------------------------------
# Extended match surface: body + path + section titles.


class TestExtendedMatchSurface(unittest.TestCase):
    """
    A paragraph matches when every query token appears in its body,
    the file's path, or one of its enclosing section titles.
    """

    def test_path_token_completes_and_match(self) -> None:
        """
        Motivating case: ``"bpy.props IntProperty"`` should match a
        paragraph about IntProperty inside ``api/bpy.props.rst``
        even though the paragraph body never repeats ``bpy.props``.
        The filename carries the ``bpy.props`` token; the body
        carries ``IntProperty``; the AND rule is satisfied across
        the combined surface.
        """
        corpus = {
            "api/bpy.props.rst": (
                ".. function:: IntProperty(default=0)\n"
                "\n"
                "   Integer property definition.\n"
            ),
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="bpy.props IntProperty", scope="api",
            )
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("api/bpy.props.rst", paths)

    def test_title_token_completes_and_match(self) -> None:
        """
        A section heading can satisfy a query token that is absent
        from the paragraph body. A paragraph mentioning only
        ``bake`` inside a ``Color Management`` section matches
        ``"color management bake"`` via the enclosing title.
        """
        content = _rst_section(
            "Color Management",
            "The bake step runs at export time.\n",
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            result = _search(
                query="color management bake", scope="manual",
            )
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_body_only_match_still_works(self) -> None:
        """
        Regression guard: a paragraph with every query token in its
        body continues to match, with no help from path or title.
        """
        corpus = {
            "manual/neutral.rst": (
                "The bake and unwrap workflow is documented here.\n"
            ),
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake unwrap", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/neutral.rst", paths)

    def test_rst_extension_stripped_from_path_surface(self) -> None:
        """
        The file extension is stripped before path matching, so a
        query of ``rst`` does not trivially match every file.
        """
        corpus = {
            "manual/unrelated.rst": "Content without the needle word.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="rst", scope="manual")
        self.assertEqual(result["hits"], [])

    def test_path_only_match_has_lower_score_than_body_match(self) -> None:
        """
        A paragraph that matches only via path has no TF-IDF body
        contribution. A paragraph in the same file that also has
        the token in its body scores higher. Keeps path-only
        matches from eclipsing real body matches in ranking.
        """
        # File path and one paragraph's body both contain
        # `needle_xyzzy`; the other paragraph has only the path
        # surface. Two sibling sections so the paragraphs don't
        # fold into a single hit.
        content = _rst_section(
            "Root",
            (
                _rst_section(
                    "Alpha",
                    "Paragraph about needle_xyzzy in body.\n",
                    underline="-",
                ) +
                _rst_section(
                    "Beta",
                    "Paragraph with no direct mention here.\n",
                    underline="-",
                )
            ),
        )
        with _synthetic_corpus({"manual/needle_xyzzy.rst": content}):
            result = _search(
                query="needle_xyzzy", scope="manual", max_results=10,
            )
        scores_by_breadcrumb = {
            h["breadcrumb"]: h["score"] for h in result["hits"]
        }
        # Both matched (via the combined surface).
        self.assertIn("Root > Alpha", scores_by_breadcrumb)
        self.assertIn("Root > Beta", scores_by_breadcrumb)
        # Alpha paragraph has a body occurrence; Beta doesn't.
        self.assertGreater(
            scores_by_breadcrumb["Root > Alpha"],
            scores_by_breadcrumb["Root > Beta"],
        )


# ---------------------------------------------------------------------------
# Word-boundary matching: no substring matches inside longer words.


class TestWordBoundaryMatching(unittest.TestCase):
    """
    Query tokens are matched with word boundaries so a short token
    does not accidentally match inside a longer word. Without this,
    reference dumps that list many similar-looking names trivially
    win on body density.
    """

    def test_obj_does_not_match_inside_object(self) -> None:
        """
        Motivating case: ``obj`` must not match substring-wise
        inside ``object`` / ``object_data`` / ``outliner_ob_*``.
        A file that only mentions ``object`` does not contribute
        hits for the token ``obj``.
        """
        corpus = {
            "manual/only_objects.rst": (
                "This page discusses object object_data and "
                "outliner_ob_light across many paragraphs.\n"
            ),
            "manual/real_obj.rst": (
                "Import an .obj file into the scene.\n"
                "\n"
                "The obj format is widely supported.\n"
            ),
        }
        with _synthetic_corpus(corpus):
            result = _search(query="obj", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/real_obj.rst", paths)
        self.assertNotIn("manual/only_objects.rst", paths)

    def test_dotted_identifier_still_matches(self) -> None:
        """
        A dotted query like ``bpy.data`` still matches the literal
        string ``bpy.data`` inside a paragraph because the ``.`` is
        already a word/non-word transition on both sides, so the
        added boundaries do not hurt.
        """
        corpus = {
            "manual/a.rst": "The bpy.data collection holds scene data.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bpy.data", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_whole_word_still_matches(self) -> None:
        """
        The boundary rule only tightens matches; a plain whole-word
        token still matches the word exactly. Regression guard.
        """
        corpus = {
            "manual/a.rst": "The bake operator runs before export.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake", scope="manual")
        paths = [h["path"] for h in result["hits"]]
        self.assertIn("manual/a.rst", paths)

    def test_substring_inside_longer_word_no_longer_matches(self) -> None:
        """
        Recall trade-off: a query of ``bake`` no longer matches
        paragraphs that only contain ``bakes`` or ``baked`` without
        the bare word. Stemming / morphological variants are out of
        scope; this test documents the current precision-over-
        recall choice.
        """
        corpus = {
            "manual/a.rst": "Everything is bakes and baking here.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(query="bake", scope="manual")
        self.assertEqual(result["hits"], [])


# ---------------------------------------------------------------------------
# Drill-in: pass back a hit's index to expand its enclosing section.


class TestIndexDrillIn(unittest.TestCase):
    """
    Each hit carries a 0-based ``index`` field. Passing that value
    back as the ``index`` argument on a follow-up call with the
    same query replaces the hit's ``text`` with the full content of
    its enclosing section (including sub-sections).
    """

    def test_hits_carry_zero_based_index(self) -> None:
        """
        The hit list's ``index`` field matches the hit's position in
        the returned list, so callers can hand an integer back
        unchanged.
        """
        corpus: dict[str, str] = {}
        for i in range(4):
            body = "unique_match_needle " * (i + 1) + "padding.\n"
            corpus["manual/f{:d}.rst".format(i)] = _rst_section(
                "Page {:d}".format(i), body,
            )
        with _synthetic_corpus(corpus):
            result = _search(
                query="unique_match_needle", scope="manual",
            )
        for i, hit in enumerate(result["hits"]):
            self.assertEqual(hit["index"], i)

    def test_drill_in_expands_to_enclosing_section(self) -> None:
        """
        Drilling into a hit replaces its ``text`` with every
        paragraph of the enclosing section - including sibling
        paragraphs the original windowed hit did not show.
        """
        section_body = (
            "First paragraph mentions unique_match_needle.\n"
            "\n"
            "Second paragraph without the word.\n"
            "\n"
            "Third paragraph with trailing content.\n"
        )
        content = _rst_section("Target", section_body)
        with _synthetic_corpus({"manual/a.rst": content}):
            baseline = _search(
                query="unique_match_needle", scope="manual",
            )
            self.assertTrue(baseline["hits"])
            drilled = _search(
                query="unique_match_needle", scope="manual",
                index=baseline["hits"][0]["index"],
            )
        self.assertEqual(len(drilled["hits"]), 1)
        self.assertFalse(drilled["truncated"])
        text = drilled["hits"][0]["text"]
        # Every paragraph of the section is present, not only the
        # seed match.
        self.assertIn("First paragraph", text)
        self.assertIn("Second paragraph", text)
        self.assertIn("Third paragraph", text)

    def test_drill_in_includes_nested_sub_sections(self) -> None:
        """
        Expansion follows the section_stack as a prefix, so the
        leaf section AND any nested sub-sections belong to the
        expanded text. A hit inside a top-level section sees its
        whole sub-tree.
        """
        nested = _rst_section(
            "Child",
            "Grandchild content here.\n",
            underline="-",
        )
        parent_body = (
            "Parent paragraph with unique_match_needle present.\n"
            "\n"
            + nested
        )
        content = _rst_section("Parent", parent_body)
        with _synthetic_corpus({"manual/a.rst": content}):
            baseline = _search(
                query="unique_match_needle", scope="manual",
            )
            drilled = _search(
                query="unique_match_needle", scope="manual",
                index=baseline["hits"][0]["index"],
            )
        text = drilled["hits"][0]["text"]
        # Parent content AND nested child content both included.
        self.assertIn("Parent paragraph", text)
        self.assertIn("Grandchild content here", text)

    def test_out_of_range_index_returns_empty(self) -> None:
        """
        An index outside the current hit list returns an empty
        response rather than raising. Callers get predictable
        behaviour when they reuse an index from a different query
        or ask for one past the result set.
        """
        corpus = {
            "manual/a.rst": "unique_match_needle here.\n",
        }
        with _synthetic_corpus(corpus):
            result = _search(
                query="unique_match_needle", scope="manual", index=99,
            )
        self.assertEqual(result, {"hits": [], "truncated": False})

    def test_drill_in_caps_at_default_window(self) -> None:
        """
        A large section does not dump the whole thing back to the
        caller. Default drill-in returns a few paragraphs on each
        side of the seed, not the entire section.
        """
        # 20 paragraphs in one section; only the middle one carries
        # the needle so the seed is centred in the section.
        paragraphs = [
            "Paragraph {:02d} placeholder.".format(i) for i in range(20)
        ]
        paragraphs[10] = "Paragraph 10 with unique_match_needle here."
        body = "\n\n".join(paragraphs) + "\n"
        content = _rst_section("Page", body)
        with _synthetic_corpus({"manual/a.rst": content}):
            baseline = _search(
                query="unique_match_needle", scope="manual",
            )
            drilled = _search(
                query="unique_match_needle", scope="manual",
                index=baseline["hits"][0]["index"],
            )
        text = drilled["hits"][0]["text"]
        # Window is a few paragraphs; should not include distant
        # edges of the section.
        self.assertIn("unique_match_needle", text)
        self.assertNotIn("Paragraph 00", text)
        self.assertNotIn("Paragraph 19", text)

    def test_drill_in_stops_at_sibling_section(self) -> None:
        """
        The window never crosses into a sibling section, even when
        the sibling's paragraphs are only one index away from the
        seed. Content from a different section is never included.
        """
        content = _rst_section(
            "Root",
            (
                _rst_section(
                    "Alpha",
                    "The needle_xyzzy sits at the end of Alpha.\n",
                    underline="-",
                ) +
                _rst_section(
                    "Beta",
                    "Beta sibling content that must not appear.\n",
                    underline="-",
                )
            ),
        )
        with _synthetic_corpus({"manual/a.rst": content}):
            baseline = _search(query="needle_xyzzy", scope="manual")
            drilled = _search(
                query="needle_xyzzy", scope="manual",
                index=baseline["hits"][0]["index"],
            )
        text = drilled["hits"][0]["text"]
        self.assertIn("needle_xyzzy", text)
        self.assertNotIn("Beta sibling content", text)

    def test_drill_in_caller_context_widens_window(self) -> None:
        """
        When the caller passes ``context`` larger than the default
        drill-in minimum, the window honours the caller's value
        (up to the section boundary).
        """
        paragraphs = [
            "Paragraph {:02d} body.".format(i) for i in range(12)
        ]
        paragraphs[0] = "Paragraph 00 with unique_match_needle."
        body = "\n\n".join(paragraphs) + "\n"
        content = _rst_section("Page", body)
        with _synthetic_corpus({"manual/a.rst": content}):
            baseline = _search(
                query="unique_match_needle", scope="manual",
            )
            drilled_default = _search(
                query="unique_match_needle", scope="manual",
                index=baseline["hits"][0]["index"],
            )
            drilled_wide = _search(
                query="unique_match_needle", scope="manual",
                index=baseline["hits"][0]["index"],
                context=10,
            )
        default_text = drilled_default["hits"][0]["text"]
        wide_text = drilled_wide["hits"][0]["text"]
        # Default window is small; paragraph near the far edge of
        # the section is absent.
        self.assertNotIn("Paragraph 10", default_text)
        # Wide window includes the requested number of trailing
        # paragraphs.
        self.assertIn("Paragraph 10", wide_text)

    def test_drill_in_response_omits_internal_fields(self) -> None:
        """
        The internal paragraph-index field used for expansion must
        not leak into the public response. The drilled hit has only
        the documented keys.
        """
        corpus = {
            "manual/a.rst": _rst_section(
                "Page",
                "unique_match_needle sits alone.\n",
            ),
        }
        with _synthetic_corpus(corpus):
            baseline = _search(
                query="unique_match_needle", scope="manual",
            )
            drilled = _search(
                query="unique_match_needle", scope="manual",
                index=baseline["hits"][0]["index"],
            )
        expected_keys = {"path", "text", "breadcrumb", "index", "score"}
        self.assertEqual(set(drilled["hits"][0].keys()), expected_keys)
        # And the non-drill path too.
        for hit in baseline["hits"]:
            self.assertEqual(set(hit.keys()), expected_keys)


if __name__ == "__main__":
    unittest.main()
