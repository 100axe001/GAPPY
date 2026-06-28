"""PyInstaller entry point for the desktop supervisor sidecar.

The desktop bundles this as ``lemma-supervisor`` and spawns it with no
arguments, so default argv to ``supervise``. With arguments it behaves like
the full ``lemma-stack`` CLI.
"""

from __future__ import annotations

import sys

from lemma_stack.app import main


def run() -> None:
    if len(sys.argv) == 1:
        sys.argv.append("supervise")
    main()


if __name__ == "__main__":
    run()
