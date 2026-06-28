from __future__ import annotations

from rich.text import Text
from textual.widgets import Static


class StatusBar(Static):
    """One-line scope summary: server | org | pod | agent."""

    def update_scope(
        self,
        *,
        server: str,
        org: str | None,
        pod: str | None,
        agent: str | None,
    ) -> None:
        text = Text()
        for label, value in (
            ("server", server),
            ("org", org or "—"),
            ("pod", pod or "—"),
            ("agent", agent or "default"),
        ):
            text.append(f"{label} ", style="dim")
            text.append(str(value), style="bold" if value else "")
            text.append("   ")
        self.update(text)
