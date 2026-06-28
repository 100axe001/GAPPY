from __future__ import annotations

from .cli_core.app import LAZY_GROUPS, app as app
from .cli_core.app import main as _cli_main

# Registered lazily alongside the core groups (see cli_core/lazy.py): the TUI
# module only loads when its group is actually used. Local-stack install and
# management now lives in the separate `lemma-admin` tool.
LAZY_GROUPS.setdefault(
    "tui", ("lemma_cli.commands.tui", "app", "Open Lemma terminal interfaces.", False)
)


def main() -> None:
    _cli_main()


__all__ = ["app", "main"]
