# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
CLI chat client bridging an LLM provider with an MCP server.

Supported providers (selected via subcommand):

* **openai** -- OpenAI-compatible APIs such as llama.cpp.
* **claude** -- Anthropic Messages API (requires ``ANTHROPIC_API_KEY``).

Dependencies: stdlib + ``mcp`` only.

Examples::

   # llama.cpp (default API URL http://localhost:8080)
   python chat_client.py openai --api-url http://localhost:8080

   # Claude
   ANTHROPIC_API_KEY=sk-... python chat_client.py claude --model claude-sonnet-4-20250514
"""

__all__ = (
    "main",
)

import argparse
import asyncio
import json
import os
import urllib.error
import urllib.request

from typing import Any

from mcp import ClientSession, StdioServerParameters  # pylint: disable=import-error,no-name-in-module
from mcp.client.stdio import stdio_client  # pylint: disable=import-error,no-name-in-module


# ---------------------------------------------------------------------------
# OpenAI API helpers

def _api_chat_completions(
    api_url: str,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]],
    model: str | None,
) -> dict[str, Any]:
    """POST to ``/v1/chat/completions`` and return the parsed JSON response."""
    body: dict[str, Any] = {
        "messages": messages,
    }
    if model is not None:
        body["model"] = model
    if tools:
        body["tools"] = tools

    data = json.dumps(body).encode()
    req = urllib.request.Request(
        "{:s}/v1/chat/completions".format(api_url),
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        result: dict[str, Any] = json.loads(resp.read().decode())
        return result


def _mcp_tools_to_openai(mcp_tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convert MCP tool metadata to OpenAI ``tools`` format."""
    result = []
    for t in mcp_tools:
        result.append({
            "type": "function",
            "function": {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["inputSchema"],
            },
        })
    return result


# ---------------------------------------------------------------------------
# Claude API helpers

def _api_claude_messages(
    api_url: str,
    api_key: str,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]],
    opts: dict[str, Any],
) -> dict[str, Any]:
    """POST to ``/v1/messages`` and return the parsed JSON response.

    *opts* must contain ``model`` (str) and ``max_tokens`` (int), and
    may contain ``system`` (str).
    """
    body: dict[str, Any] = {
        "model": opts["model"],
        "max_tokens": opts["max_tokens"],
        "messages": messages,
    }
    if tools:
        body["tools"] = tools
    system = opts.get("system", "")
    if system:
        body["system"] = system

    data = json.dumps(body).encode()
    req = urllib.request.Request(
        "{:s}/v1/messages".format(api_url),
        data=data,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        result: dict[str, Any] = json.loads(resp.read().decode())
        return result


def _mcp_tools_to_claude(mcp_tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convert MCP tool metadata to Claude ``tools`` format."""
    result = []
    for t in mcp_tools:
        result.append({
            "name": t["name"],
            "description": t["description"],
            "input_schema": t["inputSchema"],
        })
    return result


# ---------------------------------------------------------------------------
# Response helpers

# Return type shared by both response processors:
#   (assistant_message, tool_calls, text_reply, turn_done)
#
# - assistant_message: dict to append to the conversation history.
# - tool_calls: list of (id, name, arguments_dict) tuples.
# - text_reply: optional text to display.
# - turn_done: True when the LLM considers the turn finished.
_ResponseTuple = tuple[dict[str, Any], list[tuple[str, str, dict[str, Any]]], str | None, bool]


def _process_openai_response(response: dict[str, Any]) -> _ResponseTuple:
    """Extract structured fields from an OpenAI chat-completions response."""
    choice = response["choices"][0]
    msg = choice["message"]
    finish_reason = choice.get("finish_reason", "")

    tool_calls: list[tuple[str, str, dict[str, Any]]] = []
    raw_tool_calls = msg.get("tool_calls")
    if raw_tool_calls:
        for tc in raw_tool_calls:
            fn = tc["function"]
            try:
                args = json.loads(fn["arguments"])
            except (json.JSONDecodeError, TypeError):
                args = {}
            tool_calls.append((tc["id"], fn["name"], args))

    text = msg.get("content") or None
    done = finish_reason != "tool_calls" and not tool_calls
    return msg, tool_calls, text, done


def _process_claude_response(response: dict[str, Any]) -> _ResponseTuple:
    """Extract structured fields from a Claude messages response."""
    content = response.get("content", [])
    stop_reason = response.get("stop_reason", "")

    tool_calls: list[tuple[str, str, dict[str, Any]]] = []
    text_parts: list[str] = []

    for block in content:
        if block["type"] == "text":
            text_parts.append(block["text"])
        elif block["type"] == "tool_use":
            tool_calls.append((block["id"], block["name"], block.get("input", {})))

    # Build the assistant message to store in history.
    assistant_msg: dict[str, Any] = {"role": "assistant", "content": content}

    text = "\n".join(text_parts) if text_parts else None
    done = stop_reason != "tool_use" and not tool_calls
    return assistant_msg, tool_calls, text, done


# ---------------------------------------------------------------------------
# MCP tool invocation

async def _call_tool(
    session: ClientSession,
    name: str,
    arguments: dict[str, Any],
) -> str:
    """Call an MCP tool and return a text summary of the result."""
    result = await session.call_tool(name, arguments)
    parts: list[str] = []
    for item in result.content:
        if item.type == "text":
            parts.append(item.text)
        elif item.type == "image":
            parts.append("[image]")
        else:
            parts.append("[{:s}]".format(item.type))
    text = "\n".join(parts)
    if result.isError:
        return "ERROR: {:s}".format(text)
    return text


# ---------------------------------------------------------------------------
# Main async loop

async def _run(
    server_command: str,
    provider: str,
    api_url: str,
    opts: dict[str, Any],
    prompt: str | None,
    non_interactive: bool,
) -> None:
    api_key = opts.get("api_key")
    model = opts.get("model")
    if provider == "claude" and not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.")
        return

    # Split the server command into executable + args.
    # Pass environment variables the MCP server needs to connect to Blender.
    # StdioServerParameters only inherits a small safe-list by default.
    env: dict[str, str] = {}
    for key in ("BLENDER_MCP_HOST", "BLENDER_MCP_PORT", "BLENDER_PATH"):
        value = os.environ.get(key)
        if value is not None:
            env[key] = value
    parts = server_command.split()
    params = StdioServerParameters(command=parts[0], args=parts[1:], env=env or None)

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init_result = await session.initialize()
            instructions = init_result.instructions or ""
            tools_result = await session.list_tools()

            mcp_tools = [
                {
                    "name": t.name,
                    "description": t.description or "",
                    "inputSchema": t.inputSchema,
                }
                for t in tools_result.tools
            ]

            if provider == "openai":
                llm_tools = _mcp_tools_to_openai(mcp_tools)
            else:
                llm_tools = _mcp_tools_to_claude(mcp_tools)

            if non_interactive:
                print(
                    "Connected to MCP server ({:d} tools).".format(len(mcp_tools))
                )
            else:
                print(
                    "Connected to MCP server ({:d} tools). "
                    "Type your message or Ctrl-D to quit.".format(len(mcp_tools))
                )

            # Conversation history.
            messages: list[dict[str, Any]] = []

            # OpenAI uses a system message in the messages list;
            # Claude uses a separate `system` parameter.
            system_text = ""
            if instructions:
                if provider == "openai":
                    messages.append({"role": "system", "content": instructions})
                else:
                    system_text = instructions

            single_shot = non_interactive
            while True:
                # Read user input.
                if prompt is not None:
                    user_input = prompt
                    prompt = None
                else:
                    try:
                        user_input = input("\n> ")
                    except (EOFError, KeyboardInterrupt):
                        print()
                        break

                    if not user_input.strip():
                        continue

                messages.append({"role": "user", "content": user_input})

                # LLM loop: keep calling the API until we get a plain text
                # reply (no tool calls).
                while True:
                    try:
                        if provider == "openai":
                            response = _api_chat_completions(
                                api_url, messages, llm_tools, model,
                            )
                        else:
                            assert api_key is not None
                            assert model is not None
                            claude_opts: dict[str, Any] = {
                                "model": model,
                                "max_tokens": opts.get("max_tokens", 4096),
                                "system": system_text,
                            }
                            response = _api_claude_messages(
                                api_url, api_key, messages, llm_tools,
                                claude_opts,
                            )
                    except urllib.error.URLError as ex:
                        print("HTTP error: {:s}".format(str(ex)))
                        break

                    if provider == "openai":
                        assistant_msg, tool_calls, text, done = (
                            _process_openai_response(response)
                        )
                    else:
                        assistant_msg, tool_calls, text, done = (
                            _process_claude_response(response)
                        )

                    # Append the assistant message to history.
                    messages.append(assistant_msg)

                    if tool_calls:
                        if provider == "openai":
                            for tc_id, tc_name, tc_args in tool_calls:
                                print("  -> calling {:s}".format(tc_name))
                                result_text = await _call_tool(
                                    session, tc_name, tc_args,
                                )
                                messages.append({
                                    "role": "tool",
                                    "tool_call_id": tc_id,
                                    "content": result_text,
                                })
                        else:
                            tool_results: list[dict[str, Any]] = []
                            for tc_id, tc_name, tc_args in tool_calls:
                                print("  -> calling {:s}".format(tc_name))
                                result_text = await _call_tool(
                                    session, tc_name, tc_args,
                                )
                                tool_results.append({
                                    "type": "tool_result",
                                    "tool_use_id": tc_id,
                                    "content": result_text,
                                })
                            messages.append({
                                "role": "user",
                                "content": tool_results,
                            })
                        # Loop back to let the LLM process tool results.
                        continue

                    # Plain assistant reply.
                    if text:
                        print("\n{:s}".format(text))

                    if done:
                        break

                # Single-prompt mode: exit after one turn.
                if single_shot:
                    break


# ---------------------------------------------------------------------------
# CLI entry point

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Chat client bridging an LLM provider with an MCP server.",
    )
    parser.add_argument(
        "--server-command",
        default="blender-mcp",
        help="Command to launch the MCP server (default: blender-mcp).",
    )
    parser.add_argument(
        "-p", "--prompt",
        default=None,
        help="Provide the user message on the command line instead of reading from stdin.",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Print the reply and exit after a single turn.",
    )

    subparsers = parser.add_subparsers(dest="provider", required=True)

    # -----------------
    # openai subcommand
    sp_openai = subparsers.add_parser(
        "openai",
        help="Use an OpenAI-compatible API (e.g. llama.cpp).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python chat_client.py openai --api-url http://localhost:8080",
    )
    sp_openai.add_argument(
        "--api-url",
        default="http://localhost:8080",
        help="API base URL (default: http://localhost:8080).",
    )
    sp_openai.add_argument(
        "--model",
        default=None,
        help="Model name for the API request body (optional).",
    )

    # -----------------
    # claude subcommand
    sp_claude = subparsers.add_parser(
        "claude",
        help="Use the Anthropic Messages API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "The ANTHROPIC_API_KEY environment variable must be set.\n"
            "\n"
            "Example:\n"
            "  ANTHROPIC_API_KEY=sk-... python chat_client.py claude --model claude-sonnet-4-20250514"
        ),
    )
    sp_claude.add_argument(
        "--api-url",
        default="https://api.anthropic.com",
        help="API base URL (default: https://api.anthropic.com).",
    )
    sp_claude.add_argument(
        "--model",
        required=True,
        help="Model name (required).",
    )
    sp_claude.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        help="Maximum tokens in the response (default: 4096).",
    )

    args = parser.parse_args()

    opts: dict[str, Any] = {"model": args.model}
    if args.provider == "claude":
        opts["api_key"] = os.environ.get("ANTHROPIC_API_KEY")
        opts["max_tokens"] = args.max_tokens

    try:
        non_interactive: bool = args.non_interactive or args.prompt is not None
        asyncio.run(_run(
            args.server_command,
            args.provider,
            args.api_url,
            opts,
            args.prompt,
            non_interactive,
        ))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
