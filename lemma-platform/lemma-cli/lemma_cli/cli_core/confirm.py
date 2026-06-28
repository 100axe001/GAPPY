from __future__ import annotations

import sys

import typer

from .state import fail


def confirm_destructive(message: str, yes: bool) -> None:
    """Prompt before a destructive operation unless --yes was passed.

    Non-interactive sessions must pass --yes explicitly.
    """
    if yes:
        return
    if not sys.stdin.isatty():
        fail("Refusing to proceed without --yes in non-interactive mode.")
    if not typer.confirm(message):
        raise typer.Exit(code=1)
