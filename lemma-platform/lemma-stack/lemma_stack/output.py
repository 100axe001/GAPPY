"""Console output and interactivity helpers.

Every interactive prompt must work non-interactively: when stdin is not a TTY,
`-y` was passed, or LEMMA_STACK_NONINTERACTIVE is set, prompts either take
their default or fail with the flag the caller should pass instead.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

import typer
from rich.console import Console

console = Console()
err_console = Console(stderr=True)


class AdminError(Exception):
    """Fatal, user-facing error; rendered without a traceback."""


def non_interactive() -> bool:
    if os.environ.get("LEMMA_STACK_NONINTERACTIVE"):
        return True
    return not sys.stdin.isatty()


def info(message: str) -> None:
    console.print(message)


def ok(message: str) -> None:
    console.print(f"[green]ok[/green] {message}")


def warn(message: str) -> None:
    err_console.print(f"[yellow]warn[/yellow] {message}")


def fail(message: str) -> "typer.Exit":
    err_console.print(f"[red]error[/red] {message}")
    return typer.Exit(code=1)


def print_json(payload: Any) -> None:
    console.print_json(json.dumps(payload, default=str))


def confirm(question: str, *, default: bool, assume_yes: bool, flag_hint: str = "--yes") -> bool:
    if assume_yes:
        return True
    if non_interactive():
        if default:
            return True
        raise AdminError(f"refusing to continue non-interactively; pass {flag_hint} to confirm")
    return typer.confirm(question, default=default)


def choose(question: str, choices: list[str], *, default: str, flag_hint: str) -> str:
    if non_interactive():
        return default
    return typer.prompt(f"{question} ({'/'.join(choices)})", default=default)
