# Optional local overrides (silently skipped when absent).
# Exported so child processes inherit them as environment variables.
-include .env
export

PYTHON ?= python
PYTHON_SOURCE_DIRS_TO_CHECK = mcp/blmcp/ addon/blender_mcp_addon/ chat_client/ _misc/

define HELP_TEXT

Targets
   * test:              Run unit tests.
   * test_rst_parse:    Run unit tests for RST manual/API doc parsing.
   * test_rst_search:   Run unit tests for the RST text-search layer.
   * test_integration:  Run integration tests (requires BLENDER_BIN).
                        Loads .env if present (e.g. ANTHROPIC_API_KEY).
                        Uses .test_venv (delete to force a rebuild).

     List all tests:    make test_integration TESTS_LIST=1
     Run tests:         make test_integration TESTS=TestChatClient.test_name
     Multiple tests:    make test_integration TESTS="test_one test_two"
   * format:            Auto-format Python sources with autopep8.
   * readme_update:     Regenerate the tools listing in readme.rst.

Static Source Code Checking
   * check_license:   Verify SPDX headers in all Python files.
   * check_ascii:     Reject non-ASCII characters in sources.
   * check_mypy:      Run mypy type checking.
   * check_pylint:    Run pylint linting.
   * check_ruff:      Run ruff linting.
   * check_vulture:   Run vulture dead-code detection.
   * check_namespace: Verify __all__ is defined in all Python modules.
   * check_all:       Run all checks (ruff, mypy, vulture, license, ascii, namespace).

Reference Data
   * update_reference_manual:
     Copy RST and Python files from a Blender manual checkout.

     Usage: make update_reference_manual MANUAL_DIR=/path/to/manual

   * update_reference_api:
     Copy RST files from a Blender API reference build.

     Usage: make update_reference_api API_DIR=/path/to/api

Environment Variables
   Variables may be set in a .env file (loaded automatically).

   PYTHON              Python interpreter (default: python).
   BLENDER_BIN         Path to the Blender binary (default: blender).
   BLENDER_MCP         Path to the blender-mcp command (default: blender-mcp).
   BLENDER_PATH        Path to the Blender binary used by the MCP server
                       (default: blender).
   BLENDER_MCP_HOST    Host the MCP addon listens on (default: localhost).
   BLENDER_MCP_PORT    Port the MCP addon listens on (default: 9876).
   BLENDER_MCP_TIMEOUT Startup timeout in seconds for tests (default: 10).
   GLOBAL_TIMEOUT_SCALE
                       Multiply all test timeouts by this factor
                       (default: 1). Useful on slower systems or
                       with slower models.
   BLENDER_MCP_FOREGROUND
                       When set, run Blender in the foreground during tests.
   ANTHROPIC_API_KEY   API key for Claude integration tests.
   ANTHROPIC_MODEL     Model name for Claude tests
                       (default: claude-sonnet-4-20250514).
   USE_LLAMA_CXX       When set, run LLM tests using llama-server.
                       Cannot be combined with USE_ANTHROPIC.
                       Requires LLAMA_SERVER_BIN and
                       LLAMA_SERVER_ARGS.
                       Note: many tests may fail depending on the
                       capability of the model.
   LLAMA_SERVER_BIN    Path to the llama-server binary.
   LLAMA_SERVER_ARGS   Extra arguments for llama-server
                       (e.g. --jinja -m model.gguf).
                       The port is provided by the test harness;
                       do not include --port.
   LLAMA_SERVER_VERBOSE
                       When set, forward llama-server output to
                       the terminal.

endef
export HELP_TEXT

help:
	@echo "$$HELP_TEXT"

test:
	$(PYTHON) tests/test_tool_listing.py
	$(PYTHON) tests/test_rst_parse.py
	$(PYTHON) tests/test_rst_search.py
	$(PYTHON) tests/test_mcp_server.py
	$(PYTHON) tests/test_blender_mcp_with_blender.py

test_rst_parse:
	$(PYTHON) tests/test_rst_parse.py

test_rst_search:
	$(PYTHON) tests/test_rst_search.py

test_integration:
ifdef TESTS_LIST
	@$(PYTHON) _misc/test_integration_tests_list.py
else
	$(PYTHON) tests/integration/test_blender_mcp_with_llm.py $(TESTS)
endif

format:
	@for d in mcp addon _misc tests chat_client; do \
		autopep8 --in-place --recursive $$d || exit 1; \
	done

check_license:
	@$(PYTHON) _misc/check_license.py

check_ascii:
	@$(PYTHON) _misc/check_ascii.py

check_mypy:
	@! $(PYTHON) -m mypy --exclude 'data/api/examples/' $(PYTHON_SOURCE_DIRS_TO_CHECK) 2>&1 | grep -v '^stubs/' | grep ': error:' || \
		{ echo "mypy: found errors"; exit 1; }

check_pylint:
	pylint $(PYTHON_SOURCE_DIRS_TO_CHECK) \
		--disable=C0103,C0115,C0116,C0209,C0413,C0415,R0801,R0903,R0912,R0914,R0915,W0122

check_ruff:
	ruff check $(PYTHON_SOURCE_DIRS_TO_CHECK)

check_vulture:
	vulture $(PYTHON_SOURCE_DIRS_TO_CHECK) \
		--exclude mcp/blmcp/data/api/examples \
		--ignore-decorators '@mcp.tool,@mcp.prompt' \
		--ignore-names 'bl_*,draw,execute,exclude' \
		--min-confidence 61

check_namespace:
	@$(PYTHON) _misc/check_namespace.py --skip mcp/blmcp/data/api/examples $(PYTHON_SOURCE_DIRS_TO_CHECK)

check_all: check_ruff check_mypy check_vulture check_license check_ascii check_namespace

readme_update:
	$(PYTHON) _misc/readme_update_from_tools.py

update_reference_manual:
	@test -n "$(MANUAL_DIR)" || { echo "Usage: make update_reference_manual MANUAL_DIR=/path/to/blender/manual"; exit 1; }
	$(PYTHON) _misc/update_reference_manual.py "$(MANUAL_DIR)"

update_reference_api:
	@test -n "$(API_DIR)" || { echo "Usage: make update_reference_api API_DIR=/path/to/api"; exit 1; }
	$(PYTHON) _misc/update_reference_api.py "$(API_DIR)"
