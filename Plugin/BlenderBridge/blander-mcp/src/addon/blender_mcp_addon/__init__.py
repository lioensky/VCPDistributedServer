# SPDX-FileCopyrightText: 2026 Blender Authors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Blender add-on that provides an MCP socket bridge-server.
"""

__all__ = (
    "register",
    "unregister",
)

import bpy  # pylint: disable=import-error
from bpy.props import (
    BoolProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
)  # pylint: disable=import-error

from . import mcp_to_blender_server

_PORT_MIN = 1024
_PORT_MAX = 65535

# Default seconds to wait after registration before auto-starting the server.
# Avoids adding work to Blender's startup sequence.
_AUTOSTART_DELAY = 1.0

# Store the CLI handle, only for correct register/unregister.
_cli_commands: list[object] = []

# This error is shown in the UI & command line when online access isn't enabled.
#
# NOTE(@ideasman42): we could consider `localhost` to be acceptable, this is a grey area
# regarding what counts as "online" or not.
_state_offline_error_message = "Online access must be enabled in the system preferences"


class _State:
    """
    Module-level runtime state that is not persisted across sessions.
    """

    # Communicate to the user if there is a problem.
    # Displayed in the preferences UI when non-empty.
    autostart_error: str = ""

    @classmethod
    def startup_info_set(cls, error: str) -> None:
        """
        Store a startup error message to display in the preferences UI.
        """
        cls.autostart_error = error

    @classmethod
    def startup_info_set_from_exception(cls, ex: Exception) -> None:
        """
        Store a startup exception message to display in the preferences UI
        and print the full traceback to stderr for debugging.
        """
        # NOTE: this is correct but reads like an unhandled exception.
        # import traceback
        # traceback.print_exception(ex)
        cls.autostart_error = str(ex)

    @classmethod
    def startup_info_clear(cls) -> None:
        """
        Clear any startup error so it no longer appears in the preferences UI.
        """
        cls.autostart_error = ""

    @classmethod
    def startup_online_ok_or_error(cls) -> bool:
        """
        Return True when online access is permitted, otherwise store an error and return False.
        """
        if bpy.app.online_access:
            return True
        cls.startup_info_set(_state_offline_error_message)
        if bpy.app.background:
            print("Error: {:s}".format(_state_offline_error_message))
            print("  Use --online-mode to enable online access from the command line")
        return False


class _BlenderMCPPreferences(bpy.types.AddonPreferences):  # type: ignore[misc]
    bl_idname = __package__

    host: StringProperty(  # type: ignore[valid-type]
        name="Host",
        default=mcp_to_blender_server.DEFAULT_HOST,
    )
    port: IntProperty(  # type: ignore[valid-type]
        name="Port",
        default=mcp_to_blender_server.DEFAULT_PORT,
        min=_PORT_MIN,
        max=_PORT_MAX,
    )
    use_autostart: BoolProperty(  # type: ignore[valid-type]
        name="Auto Start",
        description=(
            "Automatically start the MCP bridge server when Blender starts.\n"
            "Without this, you must manually start from the preferences UI.\n"
            "(ignored in background mode)"
        ),
        default=True,
    )
    autostart_delay: FloatProperty(  # type: ignore[valid-type]
        name="Auto Start Delay",
        description=(
            "Seconds to wait after Blender starts before auto-starting the server.\n"
            "Avoids adding overhead to Blender's startup sequence"
        ),
        default=_AUTOSTART_DELAY,
        min=0.0,
        max=30.0,
        step=10,
        precision=1,
        subtype="TIME_ABSOLUTE",
    )

    def _update_use_log(self, _context: bpy.types.Context) -> None:
        mcp_to_blender_server.use_log = self.use_log

    use_log: BoolProperty(  # type: ignore[valid-type]
        name="Log",
        description="Print every tool request and response status to the terminal",
        default=False,
        update=_update_use_log,
    )

    def _update_timer_interval_active(self, _context: bpy.types.Context) -> None:
        # Cached on the server module because the timer callback may fire
        # many times a second, avoid slower preferences lookups.
        mcp_to_blender_server.timer_internal_vars_calc(active=self.timer_interval_active)

    timer_interval_active: FloatProperty(  # type: ignore[valid-type]
        name="Timer Interval",
        description="Seconds between queue polling ticks in interactive mode",
        default=0.25,
        min=0.05,
        max=5.0,
        step=1,
        precision=2,
        subtype='TIME_ABSOLUTE',
        update=_update_timer_interval_active,
    )

    def _update_timer_interval_idle(self, _context: bpy.types.Context) -> None:
        # Cached on the server module because the timer callback may fire
        # many times a second, avoid slower preferences lookups.
        mcp_to_blender_server.timer_internal_vars_calc(idle=self.timer_interval_idle)

    timer_interval_idle: FloatProperty(  # type: ignore[valid-type]
        name="Timer Interval Idle",
        description="Seconds between queue polling ticks while idle (no pending work)",
        default=1.0,
        min=0.1,
        max=10.0,
        step=10,
        precision=2,
        subtype='TIME_ABSOLUTE',
        update=_update_timer_interval_idle,
    )

    def _update_timer_interval_idle_delay(self, _context: bpy.types.Context) -> None:
        # Cached on the server module because the timer callback may fire
        # many times a second, avoid slower preferences lookups.
        mcp_to_blender_server.timer_internal_vars_calc(idle_delay=self.timer_interval_idle_delay)

    timer_interval_idle_delay: FloatProperty(  # type: ignore[valid-type]
        name="Idle Delay",
        description="Seconds of inactivity before switching to the idle polling interval",
        default=5.0,
        min=1.0,
        max=60.0,
        step=100,
        precision=1,
        subtype='TIME_ABSOLUTE',
        update=_update_timer_interval_idle_delay,
    )

    def draw(self, context: bpy.types.Context) -> None:
        del context
        layout = self.layout
        layout.prop(self, "host")
        layout.prop(self, "port")
        layout.prop(self, "use_autostart")
        layout.prop(self, "autostart_delay")
        layout.prop(self, "timer_interval_active")
        layout.prop(self, "timer_interval_idle")
        layout.prop(self, "timer_interval_idle_delay")
        layout.prop(self, "use_log")

        if mcp_to_blender_server.is_running():
            layout.operator("blmcp.server_stop", icon="CANCEL")
            layout.label(text="Server is running", icon="CHECKMARK")
        else:
            layout.operator("blmcp.server_start", icon="PLAY")
            layout.label(text="Server is stopped", icon="X")

        if _State.autostart_error:
            layout.label(text=_State.autostart_error, icon="ERROR")


class _BLMCP_OT_server_start(bpy.types.Operator):  # type: ignore[misc]
    bl_idname = "blmcp.server_start"
    bl_label = "Start MCP Bridge Server"
    bl_description = "Start the MCP socket bridge server that the MCP server can connect to"

    def execute(self, context: bpy.types.Context) -> set[str]:
        from . import execute_interactive

        # Timers do not fire in background mode. Use the CLI command instead:
        # `blender --background file.blend --command blender_mcp`.
        if bpy.app.background:
            self.report({"ERROR"}, "Use `--command blender_mcp` to start the MCP bridge server in background mode")
            return {"CANCELLED"}
        if not _State.startup_online_ok_or_error():
            self.report({"ERROR"}, _state_offline_error_message)
            return {"CANCELLED"}
        # Clear any stale auto-start error so it does not persist in the UI.
        _State.startup_info_clear()
        prefs = context.preferences.addons[__package__].preferences
        mcp_to_blender_server.timer_internal_vars_calc(
            active=prefs.timer_interval_active,
            idle=prefs.timer_interval_idle,
            idle_delay=prefs.timer_interval_idle_delay,
        )
        mcp_to_blender_server.use_log = prefs.use_log
        try:
            mcp_to_blender_server.start(prefs.host, prefs.port)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            _State.startup_info_set_from_exception(ex)
            self.report({"ERROR"}, str(ex))
            return {"CANCELLED"}
        bpy.app.timers.register(
            execute_interactive.run,
            first_interval=mcp_to_blender_server.TIMER_INTERVAL_ACTIVE,
            persistent=True)
        self.report({"INFO"}, "MCP server started on {:s}:{:d}".format(prefs.host, prefs.port))
        return {"FINISHED"}


class _BLMCP_OT_server_stop(bpy.types.Operator):  # type: ignore[misc]
    bl_idname = "blmcp.server_stop"
    bl_label = "Stop MCP Server"
    bl_description = "Stop the MCP Bridge Server"

    def execute(self, context: bpy.types.Context) -> set[str]:
        del context
        from . import execute_interactive

        # Clear any stale auto-start error so it does not persist in the UI.
        _State.startup_info_clear()
        mcp_to_blender_server.stop()
        if bpy.app.timers.is_registered(execute_interactive.run):
            bpy.app.timers.unregister(execute_interactive.run)
        self.report({"INFO"}, "MCP bridge server stopped")
        return {"FINISHED"}


def _autostart_timer() -> None:
    """
    Deferred timer callback that starts the server when ``use_autostart``
    is enabled. Runs after a delay to avoid slowing down Blender's startup.
    """
    from . import execute_interactive

    if not _State.startup_online_ok_or_error():
        return
    prefs = bpy.context.preferences.addons[__package__].preferences
    mcp_to_blender_server.timer_internal_vars_calc(
        active=prefs.timer_interval_active,
        idle=prefs.timer_interval_idle,
        idle_delay=prefs.timer_interval_idle_delay,
    )
    mcp_to_blender_server.use_log = prefs.use_log

    # This isn't expected:
    # - Maybe the operator is explicitly called as part of an automated action.
    # - The user might have set a very long delay for initial startup and
    #   manually enabled before the timer fires.
    # Whatever the case, running multiple servers would cause confusing errors, so don't do it.
    if mcp_to_blender_server.is_running():
        return

    try:
        mcp_to_blender_server.start(prefs.host, prefs.port)
    except Exception as ex:  # pylint: disable=broad-exception-caught
        _State.startup_info_set_from_exception(ex)
        return

    bpy.app.timers.register(
        execute_interactive.run,
        first_interval=mcp_to_blender_server.TIMER_INTERVAL_ACTIVE,
        persistent=True)


def _cli_execute_handler(argv: list[str]) -> int:
    """
    Callback for the CLI: ``blender -c blender_mcp``.
    """
    if not _State.startup_online_ok_or_error():
        return 1
    from .cli import cli_execute
    return cli_execute(argv)


_classes = (
    _BlenderMCPPreferences,
    _BLMCP_OT_server_start,
    _BLMCP_OT_server_stop,
)


def register() -> None:
    for cls in _classes:
        bpy.utils.register_class(cls)
    _cli_commands.append(bpy.utils.register_cli_command("blender_mcp", _cli_execute_handler))

    # Defer auto-start so the server does not slow down Blender's startup.
    if not bpy.app.background:
        if not _State.startup_online_ok_or_error():
            return

        prefs = bpy.context.preferences.addons[__package__].preferences
        if prefs.use_autostart:
            bpy.app.timers.register(
                _autostart_timer,
                first_interval=prefs.autostart_delay,
                persistent=True,
            )


def unregister() -> None:
    from . import execute_interactive

    for cmd in _cli_commands:
        bpy.utils.unregister_cli_command(cmd)
    _cli_commands.clear()

    if bpy.app.timers.is_registered(_autostart_timer):
        bpy.app.timers.unregister(_autostart_timer)

    mcp_to_blender_server.stop()
    if bpy.app.timers.is_registered(execute_interactive.run):
        bpy.app.timers.unregister(execute_interactive.run)
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
