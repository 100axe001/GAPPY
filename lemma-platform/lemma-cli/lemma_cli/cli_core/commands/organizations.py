from __future__ import annotations

import typer

from ..context import (
    remember_org,
    render_session_selection,
    resolve_org,
    selected_org,
)
from ..io import emit
from ..io import list_items
from ..select import select_from_items
from ..state import run_with_client, state_from_ctx

app = typer.Typer(
    help="Organization commands.",
    invoke_without_command=True,
    no_args_is_help=False,
)


def _orgs(client):  # type: ignore[no-untyped-def]
    return getattr(client, "orgs", None) or client.organizations


@app.callback()
def orgs_root(
    ctx: typer.Context,
    limit: int = typer.Option(100, "--limit"),
) -> None:
    """Open the organization selector."""
    if ctx.invoked_subcommand is not None:
        return
    select_organization(ctx, limit=limit)


@app.command("list")
def list_organizations(
    ctx: typer.Context,
    limit: int = typer.Option(100, "--limit"),
) -> None:
    """List organizations available to the current user."""
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx,
        lambda client, s: _mark_current(
            _orgs(client).list(limit=limit), selected_org(s, required=False)
        ),
    )
    if result is not None:
        emit(state, result)


@app.command("select")
def select_organization(
    ctx: typer.Context,
    name: str | None = typer.Argument(
        None, help="Organization id, slug, or name. Omit for an interactive picker."
    ),
    limit: int = typer.Option(100, "--limit"),
    export: bool = typer.Option(
        False,
        "--export",
        "-x",
        help='Print only `export LEMMA_*` lines, for: eval "$(lemma orgs select X -x)".',
    ),
    save_default: bool = typer.Option(
        False,
        "--save-default",
        help="Also persist as this server's default org (survives new shells).",
    ),
) -> None:
    """Set the active organization for THIS shell session only.

    Prints `export LEMMA_ORG_ID=…`; apply with `eval "$(lemma orgs select <name> -x)"`.
    Change the persistent per-server default with `--save-default` or
    `lemma config set-default-org`.
    """
    state = state_from_ctx(ctx)

    def run(client, s):  # type: ignore[no-untyped-def]
        if name:
            return resolve_org(client, name)
        items = list_items(_orgs(client).list(limit=limit))
        return select_from_items(
            items, label="organization", current_id=selected_org(s, required=False)
        )

    selected = run_with_client(ctx, run)
    if not selected:
        return
    org_id = str(selected.get("id") or "")
    if save_default:
        remember_org(state, org_id, clear_pod=True)
    display = str(selected.get("name") or selected.get("slug") or org_id)
    render_session_selection(
        state,
        env={"LEMMA_ORG_ID": org_id},
        label="org",
        name=display,
        command_hint=f"lemma orgs select {display}",
        export_only=export,
        saved=save_default,
    )


@app.command("get")
def get_organization(
    ctx: typer.Context,
    org: str = typer.Argument(..., help="Organization id, slug, or name."),
) -> None:
    """Show one organization."""
    state = state_from_ctx(ctx)
    result = run_with_client(ctx, lambda client, _s: _orgs(client).get(org))
    if result is not None:
        emit(state, result)


@app.command("create")
def create_organization(
    ctx: typer.Context,
    name: str = typer.Argument(...),
) -> None:
    """Create an organization."""
    state = state_from_ctx(ctx)
    result = run_with_client(ctx, lambda client, _s: _orgs(client).create(name=name))
    if result is not None:
        emit(state, result)


def _mark_current(payload, selected_id: str | None):  # type: ignore[no-untyped-def]
    items = list_items(payload)
    if not items:
        return payload
    for item in items:
        item["active"] = bool(selected_id and str(item.get("id")) == selected_id)
    if isinstance(payload, dict):
        next_payload = dict(payload)
        next_payload["items"] = items
        return next_payload
    return items
