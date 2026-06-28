from __future__ import annotations

from pathlib import Path

import typer
from lemma_sdk.openapi_client.models.agent_permissions_replace_request import (
    AgentPermissionsReplaceRequest,
)
from lemma_sdk.openapi_client.models.create_agent_request import CreateAgentRequest
from lemma_sdk.openapi_client.models.update_agent_request import UpdateAgentRequest

from ..confirm import confirm_destructive
from ..io import emit
from ..payload import build_request, read_json
from ..sdk import pod_client
from ..state import run_with_client, state_from_ctx
from .conversations import chat_once, interactive_chat, send_once

app = typer.Typer(help="Agent commands.")
permissions_app = typer.Typer(help="Agent resource permission commands.")
app.add_typer(permissions_app, name="permissions")


@app.command("init")
def init_agent(
    name: str = typer.Argument(..., help="Agent name (slug)."),
    root: Path | None = typer.Option(
        None, "--root", help="Bundle root (default: enclosing pod.json or cwd)."
    ),
    runtime: str | None = typer.Option(
        None,
        "--runtime",
        help="Pin a runtime profile id (omit to use the system default). See `lemma runtime profiles list`.",
    ),
    force: bool = typer.Option(False, "--force", help="Overwrite existing files."),
) -> None:
    """Scaffold an agent bundle (JSON + instruction.md). Edit, then `lemma pods import`."""
    from ...cli_app.scaffold import ScaffoldError, init_resource, report

    try:
        result = init_resource("agent", name, root=root, force=force, runtime=runtime)
    except ScaffoldError as exc:
        raise typer.BadParameter(str(exc)) from exc
    report(result, next_hint="write instruction.md + grants, then `lemma pods import .`")


@app.command("list")
def list_agents(
    ctx: typer.Context,
    pod: str | None = typer.Option(None, "--pod"),
    limit: int = typer.Option(100, "--limit"),
) -> None:
    """List agents in the pod."""
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx,
        lambda client, s: pod_client(client, s, pod).agents.list(limit=limit),
    )
    if result is not None:
        emit(state, result)


@app.command("get")
def get_agent(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    pod: str | None = typer.Option(None, "--pod"),
) -> None:
    """Show an agent."""
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx, lambda client, s: pod_client(client, s, pod).agents.get(agent)
    )
    if result is not None:
        emit(state, result)


@app.command("create")
def create_agent(
    ctx: typer.Context,
    json_payload: str | None = typer.Option(None, "--data", "-d", help="Raw JSON payload."),
    file: Path | None = typer.Option(
        None, "--file", "-f", exists=True, dir_okay=False, readable=True
    ),
    pod: str | None = typer.Option(None, "--pod"),
) -> None:
    """Create an agent from a JSON payload.

    Required: name, instruction. Optional: toolsets, visibility, agent_runtime,
    permissions.grants. Prefer `lemma agent init <name>`; run `lemma agent schema`
    (or `lemma schema agent`) for the full shape and valid enums.
    """
    payload = read_json(json_payload, file, required=True)
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx,
        lambda client, s: pod_client(client, s, pod).agents.create(
            build_request(CreateAgentRequest, payload, context="agent")
        ),
    )
    if result is not None:
        emit(state, result)


@app.command("update")
def update_agent(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    json_payload: str | None = typer.Option(None, "--data", "-d", help="Raw JSON payload."),
    file: Path | None = typer.Option(
        None, "--file", "-f", exists=True, dir_okay=False, readable=True
    ),
    pod: str | None = typer.Option(None, "--pod"),
) -> None:
    """Update an agent from a JSON payload."""
    payload = read_json(json_payload, file, required=True)
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx,
        lambda client, s: pod_client(client, s, pod).agents.update(
            agent, UpdateAgentRequest.from_dict(payload)
        ),
    )
    if result is not None:
        emit(state, result)


@permissions_app.command("get")
def get_agent_permissions(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    pod: str | None = typer.Option(None, "--pod"),
) -> None:
    """Show resource permissions for an agent."""
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx,
        lambda client, s: pod_client(client, s, pod).agents.permissions(agent),
    )
    if result is not None:
        emit(state, result)


@permissions_app.command("replace")
def replace_agent_permissions(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    json_payload: str | None = typer.Option(None, "--data", "-d", help="Raw JSON payload."),
    file: Path | None = typer.Option(
        None, "--file", "-f", exists=True, dir_okay=False, readable=True
    ),
    pod: str | None = typer.Option(None, "--pod"),
) -> None:
    """Replace resource permissions for an agent."""
    payload = read_json(json_payload, file, required=True)
    state = state_from_ctx(ctx)
    result = run_with_client(
        ctx,
        lambda client, s: pod_client(client, s, pod).agents.replace_permissions(
            agent, AgentPermissionsReplaceRequest.from_dict(payload)
        ),
    )
    if result is not None:
        emit(state, result)


@app.command("grant")
def grant_agent(
    name: str = typer.Argument(..., help="Agent name (matches the bundle folder)."),
    specs: list[str] = typer.Argument(
        ...,
        metavar="GRANT...",
        help="name:perms or type:name:perms, e.g. tickets:read,write /knowledge:read app:gmail:use",
    ),
    root: Path | None = typer.Option(None, "--root", help="Bundle root (default: enclosing pod.json or cwd)."),
    show: bool = typer.Option(False, "--print", help="Print grant JSON instead of editing the bundle file."),
) -> None:
    """Add resource grants to an agent's bundle JSON (agents have zero access by default)."""
    from ._authoring import grant_resource

    grant_resource("agent", name, specs, root=root, show=show)


@app.command("schema")
def schema_agent() -> None:
    """Print the JSONC example/shape for an agent bundle file."""
    from ._authoring import print_resource_schema

    print_resource_schema("agent")


@app.command("delete")
def delete_agent(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    pod: str | None = typer.Option(None, "--pod"),
    yes: bool = typer.Option(False, "--yes", "-y"),
) -> None:
    """Delete an agent."""
    state = state_from_ctx(ctx)
    confirm_destructive(f"Delete agent {agent}?", yes)
    result = run_with_client(
        ctx, lambda client, s: pod_client(client, s, pod).agents.delete(agent)
    )
    if result is None:
        emit(state, {"ok": True})


@app.command("chat")
def chat_agent(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    message: str | None = typer.Argument(None),
    pod: str | None = typer.Option(None, "--pod"),
    conversation: str | None = typer.Option(None, "--conversation"),
    title: str | None = typer.Option(None, "--title"),
) -> None:
    """Chat with an agent (interactive without a message)."""
    if message is None:
        interactive_chat(
            ctx, agent=agent, pod=pod, conversation=conversation, title=title
        )
        return
    chat_once(
        ctx,
        agent=agent,
        message=message,
        pod=pod,
        conversation=conversation,
        title=title,
        show_header=True,
        show_user_message=True,
    )


@app.command("run")
def run_agent(
    ctx: typer.Context,
    agent: str = typer.Argument(...),
    message: str = typer.Argument(...),
    pod: str | None = typer.Option(None, "--pod"),
    wait: bool = typer.Option(
        True,
        "--wait/--no-wait",
        help=(
            "Wait for the agent to finish and stream the result (default). "
            "With --no-wait, start the run and return its conversation id to "
            "follow with `lemma conversations stream/get`."
        ),
    ),
    conversation: str | None = typer.Option(None, "--conversation"),
    title: str | None = typer.Option(None, "--title"),
) -> None:
    """Run an agent with a message. Each run is a conversation; --no-wait
    returns the conversation id, which `conversations` commands operate on."""
    if wait:
        chat_once(
            ctx,
            agent=agent,
            message=message,
            pod=pod,
            conversation=conversation,
            title=title,
            show_header=True,
            show_user_message=True,
        )
        return

    # Detached start: create (or reuse) the conversation, post the message,
    # and return its id (status "started") so the caller can follow it via the
    # `conversations` commands. send_once handles the client + output.
    send_once(
        ctx,
        agent=agent,
        message=message,
        pod=pod,
        conversation=conversation,
        title=title,
    )
