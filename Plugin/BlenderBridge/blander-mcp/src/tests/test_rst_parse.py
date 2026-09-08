# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Tests for the RST parser used to split bundled docs into paragraphs.

Does not require Blender. Run with::

    python -m unittest tests.test_rst_parse -v
"""

__all__ = ()

import importlib
import os
import sys
import tempfile
import textwrap
import unittest
from typing import Any

import docutils.nodes
import docutils.utils

_REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MCP_DIR = os.path.join(_REPO_DIR, "mcp")
_DATA_DIR = os.path.join(_MCP_DIR, "blmcp", "data")


def _import_rst_parse_docs() -> Any:
    """
    Import and return ``blmcp.tools_helpers.rst_parse_docs``.
    """
    if _MCP_DIR not in sys.path:
        sys.path.insert(0, _MCP_DIR)
    return importlib.import_module("blmcp.tools_helpers.rst_parse_docs")


def _rst_files(root: str) -> list[str]:
    """
    Return a sorted list of every ``*.rst`` file beneath *root*.
    """
    out: list[str] = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".rst"):
                out.append(os.path.join(dirpath, filename))
    out.sort()
    return out


class TestRST(unittest.TestCase):
    """
    Parse every bundled RST file and verify paragraphs are extracted.
    """

    _rst_parse_docs: Any

    @classmethod
    def setUpClass(cls) -> None:
        cls._rst_parse_docs = _import_rst_parse_docs()

    def _assert_parses(self, root: str) -> None:
        files = _rst_files(root)
        self.assertTrue(len(files) > 0, "No RST files found under {:s}".format(root))
        total_paragraphs = 0
        for path in files:
            paragraphs = self._rst_parse_docs.split_paragraphs_for_path(path)
            self.assertIsInstance(paragraphs, list)
            for para in paragraphs:
                self.assertIsInstance(para, str)
                self.assertTrue(para.strip(), "Empty paragraph in {:s}".format(path))
            total_paragraphs += len(paragraphs)
        self.assertGreater(total_paragraphs, 0)

    def _assert_iter_doctrees(self, root: str) -> None:
        files = _rst_files(root)
        self.assertTrue(len(files) > 0, "No RST files found under {:s}".format(root))
        seen: list[str] = []
        # `strict=True` asserts the bundled data contains no unknown
        # directives or roles.
        for path, doc in self._rst_parse_docs.iter_doctrees_for_paths(
                files, strict=True,
        ):
            self.assertIsInstance(
                doc,
                docutils.nodes.document,
                "Non-document yielded for {:s}".format(path),
            )
            seen.append(path)
        self.assertEqual(seen, files)

    def test_parse_api_docs(self) -> None:
        """
        Checks that every bundled API RST file parses into non-empty paragraphs.
        """
        self._assert_parses(os.path.join(_DATA_DIR, "api"))

    def test_parse_user_manual(self) -> None:
        """
        Checks that every bundled user-manual RST file parses into non-empty paragraphs.
        """
        self._assert_parses(os.path.join(_DATA_DIR, "manual"))

    def test_iter_doctrees_api_docs(self) -> None:
        """
        Checks ``iter_doctrees_for_paths`` against every API RST file.
        """
        self._assert_iter_doctrees(os.path.join(_DATA_DIR, "api"))

    def test_iter_doctrees_user_manual(self) -> None:
        """
        Checks ``iter_doctrees_for_paths`` against every manual RST file.
        """
        self._assert_iter_doctrees(os.path.join(_DATA_DIR, "manual"))

    def test_find_definition_in_doctree(self) -> None:
        """
        Checks top-level, nested, and missing lookups against a small
        synthetic RST document.
        """
        text = textwrap.dedent(
            """
            Module Title
            ============

            Top-level prose.

            .. function:: IntProperty(name="", default=0)

               Returns an integer property.

            .. class:: Scene

               The Scene class.

               .. attribute:: frame_current

                  The currently active frame.
            """,
        ).strip()
        doc = self._rst_parse_docs._rst_to_doctree(text, "<test>")

        top_level = self._rst_parse_docs.find_definition_in_doctree(doc, "IntProperty")
        self.assertIsNotNone(top_level)
        self.assertIn("IntProperty", top_level)
        self.assertIn("Returns an integer property", top_level)

        nested = self._rst_parse_docs.find_definition_in_doctree(doc, "Scene.frame_current")
        self.assertIsNotNone(nested)
        self.assertIn("frame_current", nested)
        self.assertIn("currently active frame", nested)

        missing = self._rst_parse_docs.find_definition_in_doctree(doc, "NotDefined")
        self.assertIsNone(missing)

    def test_iter_doctrees_strict_raises_on_unknown_directive(self) -> None:
        """
        Checks that ``strict=True`` raises on an unregistered directive.
        """
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "unknown.rst")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(".. unknown::\n\n   This is unknown.\n")
            with self.assertRaises(docutils.utils.SystemMessage):
                list(self._rst_parse_docs.iter_doctrees_for_paths(
                    [path], strict=True,
                ))

    def test_literalinclude_preserves_options(self) -> None:
        """
        ``:lines:`` and siblings on a literalinclude must survive the
        doctree round-trip so the example-collector in
        ``get_python_api_docs`` can honour them when a ``definition``-kind rendered
        block re-emits the directive.
        """
        text = textwrap.dedent(
            """
            .. class:: Widget

               A widget.

               .. literalinclude:: ./examples/widget.py
                  :lines: 2-4
                  :language: python
            """,
        ).strip()
        doc = self._rst_parse_docs._rst_to_doctree(text, "<test>")
        rendered = self._rst_parse_docs.find_definition_in_doctree(doc, "Widget")
        self.assertIsNotNone(rendered)
        self.assertIn(".. literalinclude:: ./examples/widget.py", rendered)
        self.assertIn(":lines: 2-4", rendered)
        self.assertIn(":language: python", rendered)


if __name__ == "__main__":
    unittest.main()
