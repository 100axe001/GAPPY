"""Ordered start/stop/reconcile of the installed stack.

Reconcile-by-hash: each container carries a label with a hash of its rendered
config. `up` recreates a container only when the image or args changed,
otherwise it just (re)starts what exists — which is also how upgrades swap
images cleanly.
"""

from __future__ import annotations

from lemma_stack.output import info, ok
from lemma_stack.runtime.base import Runtime
from lemma_stack.stack import health, migrations
from lemma_stack.stack.specs import (
    HASH_LABEL,
    NETWORK_NAME,
    POSTGRES_VOLUME,
    ServiceSpec,
    run_args,
)


def _existing_hash(runtime: Runtime, name: str) -> str | None:
    data = runtime.inspect(name)
    if not data:
        return None
    labels = ((data.get("Config") or {}).get("Labels")) or {}
    return labels.get(HASH_LABEL)


def reconcile(runtime: Runtime, spec: ServiceSpec) -> str:
    """Bring one container to its desired state. Returns the action taken."""
    name = spec.container_name
    current = _existing_hash(runtime, name)
    if current == spec.config_hash():
        if runtime.container_running(name):
            return "unchanged"
        runtime.start_container(name)
        return "started"
    if current is not None:
        runtime.remove_container(name)
        action = "recreated"
    else:
        action = "created"
    runtime.run(*run_args(spec))
    return action


def _gate(runtime: Runtime, spec: ServiceSpec) -> None:
    if spec.wait_healthy and spec.health:
        health.wait_container_healthy(runtime, spec.container_name)
    if spec.wait_http:
        health.wait_http(spec.wait_http)


def up(
    runtime: Runtime,
    specs: list[ServiceSpec],
    manifest,
    *,
    migrate: bool = True,
    on_progress=None,
) -> None:
    """Bring the stack up in order. on_progress(event, detail) is called at
    milestones ('service:<name>', 'migrate', 'ready') for progress reporting."""
    notify = on_progress or (lambda *a, **k: None)
    runtime.ensure_network(NETWORK_NAME)
    runtime.ensure_volume(POSTGRES_VOLUME)

    for spec in specs:
        notify(f"service:{spec.name}", spec.name)
        action = reconcile(runtime, spec)
        info(f"{spec.name}: {action}")
        _gate(runtime, spec)
        if spec.name == "db":
            migrations.ensure_databases(runtime)
        # migrations run after infra + agentbox are up, before the app serves
        if migrate and spec.name == "agentbox":
            notify("migrate", "applying database migrations")
            migrations.run_migrations(runtime, manifest)
    notify("ready", "")
    ok("stack is up")


def down(runtime: Runtime, specs: list[ServiceSpec], *, remove: bool = False) -> None:
    for spec in reversed(specs):
        name = spec.container_name
        if remove:
            runtime.remove_container(name)
            info(f"{spec.name}: removed")
        elif runtime.container_running(name):
            runtime.stop_container(name)
            info(f"{spec.name}: stopped")


def status(runtime: Runtime, specs: list[ServiceSpec]) -> list[dict]:
    rows = []
    for spec in specs:
        data = runtime.inspect(spec.container_name)
        state = (data or {}).get("State") or {}
        health_status = (state.get("Health") or {}).get("Status")
        rows.append(
            {
                "service": spec.name,
                "container": spec.container_name,
                "image": spec.image,
                "running": bool(state.get("Running")),
                "status": state.get("Status") or "absent",
                "health": health_status,
                "ports": [f"127.0.0.1:{host}->{cont}" for host, cont in spec.ports],
            }
        )
    return rows
