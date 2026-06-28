"""Main screen: pod-level resources with async loading."""

from __future__ import annotations

from typing import Any

from textual import on, work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import DataTable, Footer, Header, ListItem, ListView, Static

from ..data import RESOURCE_VIEWS, cell_value, load_rows, resource_view
from ..widgets.status_bar import StatusBar


class PodScreen(Screen[None]):
    BINDINGS = [
        ("r", "refresh", "Refresh"),
        ("c", "chat", "Chat"),
        ("s", "pick_server", "Server"),
        ("o", "pick_org", "Org"),
        ("p", "pick_pod", "Pod"),
        ("q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.active_view = RESOURCE_VIEWS[0].name
        self.current_rows: list[dict[str, Any]] = []

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield StatusBar(id="status-bar")
        with Horizontal(id="body"):
            with Vertical(id="nav"):
                yield Static("Pod resources", classes="heading")
                yield ListView(
                    *(
                        ListItem(Static(view.title), id=f"nav-{view.name}")
                        for view in RESOURCE_VIEWS
                    ),
                    id="resource-nav",
                )
            yield DataTable(id="resources", cursor_type="row")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#resource-nav", ListView).index = 0
        self.refresh_status()
        self.reload()

    # ------------------------------------------------------------ loading

    def reload(self) -> None:
        table = self.query_one("#resources", DataTable)
        table.loading = True
        self.load_view(self.active_view)

    @work(thread=True, exclusive=True, group="resources")
    def load_view(self, view_name: str) -> None:
        app = self.app
        try:
            rows = load_rows(app.state, view_name)  # type: ignore[attr-defined]
        except Exception as exc:
            app.call_from_thread(self._show_error, view_name, str(exc))
            return
        app.call_from_thread(self._show_rows, view_name, rows)

    def _show_rows(self, view_name: str, rows: list[dict[str, Any]]) -> None:
        if view_name != self.active_view:
            return
        view = resource_view(view_name)
        table = self.query_one("#resources", DataTable)
        table.loading = False
        table.clear(columns=True)
        for column in view.columns:
            table.add_column(column.replace("_", " ").title(), key=column)
        self.current_rows = rows
        for row in rows:
            table.add_row(*(cell_value(row, column) for column in view.columns))
        if not rows:
            self.notify(f"No {view.title.lower()} in this pod.", timeout=3)

    def _show_error(self, view_name: str, message: str) -> None:
        if view_name != self.active_view:
            return
        table = self.query_one("#resources", DataTable)
        table.loading = False
        table.clear(columns=True)
        self.current_rows = []
        self.notify(message, severity="error", timeout=6)

    def refresh_status(self) -> None:
        app = self.app
        self.query_one("#status-bar", StatusBar).update_scope(
            server=app.state.server,  # type: ignore[attr-defined]
            org=app.current_org_id,  # type: ignore[attr-defined]
            pod=app.current_pod_id,  # type: ignore[attr-defined]
            agent=app.agent,  # type: ignore[attr-defined]
        )

    # ---------------------------------------------------------- navigation

    @on(ListView.Selected, "#resource-nav")
    def _nav_selected(self, event: ListView.Selected) -> None:
        if event.item.id and event.item.id.startswith("nav-"):
            self.active_view = event.item.id.removeprefix("nav-")
            self.reload()

    @on(DataTable.RowSelected, "#resources")
    def _row_selected(self, event: DataTable.RowSelected) -> None:
        if event.cursor_row < 0 or event.cursor_row >= len(self.current_rows):
            return
        row = self.current_rows[event.cursor_row]
        if self.active_view == "agents":
            agent = str(row.get("name") or "")
            if agent:
                self.app.open_chat(agent=agent)  # type: ignore[attr-defined]
        elif self.active_view == "conversations":
            conversation_id = str(row.get("id") or "")
            if conversation_id:
                self.app.open_chat(  # type: ignore[attr-defined]
                    conversation_id=conversation_id,
                    title=str(row.get("title") or "") or None,
                )

    # ------------------------------------------------------------- actions

    def action_refresh(self) -> None:
        self.refresh_status()
        self.reload()

    def action_chat(self) -> None:
        self.app.open_chat()  # type: ignore[attr-defined]

    def action_pick_server(self) -> None:
        self.app.pick_server()  # type: ignore[attr-defined]

    def action_pick_org(self) -> None:
        self.app.pick_org()  # type: ignore[attr-defined]

    def action_pick_pod(self) -> None:
        self.app.pick_pod()  # type: ignore[attr-defined]
