from __future__ import annotations

from pathlib import Path

from .app import LemmaTuiApp


def run_pod_tui(*, pod: str | None, agent: str | None, config_file: Path) -> None:
    LemmaTuiApp(pod=pod, agent=agent, config_file=config_file).run()
