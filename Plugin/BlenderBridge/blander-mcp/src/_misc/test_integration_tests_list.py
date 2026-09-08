# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
List all integration test names from ``TestChatClient``.

This exists so ``make test_integration TESTS_LIST=1`` can display available
tests without running them. The ``unittest`` loader discovers test methods, and
each is printed as ``ClassName.method_name`` - the format accepted by the
``TESTS=`` argument when running tests.

The output format strips the full module path so the user sees only the
class-qualified test name (e.g. ``TestChatClient.test_cube_creation``),
which can be copied directly into ``make test_integration TESTS=...``.
"""

__all__ = (
    "main",
)


def main() -> None:
    import sys
    import unittest

    sys.path.insert(0, ".")
    from src.tests.integration.test_blender_mcp_with_llm import TestChatClient
    for test in unittest.TestLoader().loadTestsFromTestCase(TestChatClient):
        assert isinstance(test, unittest.TestCase)
        test_id = test.id()
        # `test.id()` returns e.g.
        # `tests.integration.test_blender_mcp_with_llm.TestChatClient.test_name`.
        # Extract `TestChatClient.test_name` by taking the last two dot-separated parts.
        class_name = test_id.rsplit(".", 2)[-2]
        method_name = test_id.rsplit(".", 1)[-1]
        print(class_name + "." + method_name)


if __name__ == "__main__":
    main()
