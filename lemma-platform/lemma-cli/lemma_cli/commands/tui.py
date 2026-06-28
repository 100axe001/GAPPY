from __future__ import annotations

from pathlib import Path

import typer

app = typer.Typer(help="Open Lemma terminal interfaces.")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    pod: str | None = typer.Option(None, "--pod", help="Pod id/slug to open."),
    agent: str | None = typer.Option(None, "--agent", help="Default chat agent."),
    config_file: Path = typer.Option(Path("~/.lemma/config.json"), "--config-file"),
) -> None:
    """Open the main Lemma TUI."""
    if ctx.invoked_subcommand is None:
        # Import Textual lazily — it is heavy (~3s) and only the `tui` command
        # needs it; importing at module top taxes every other CLI invocation.
        from ..tui.main import run_pod_tui

        run_pod_tui(pod=pod, agent=agent, config_file=config_file.expanduser())
