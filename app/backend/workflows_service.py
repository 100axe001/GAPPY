"""
Workflow orchestration surface — triggers pod workflows and drives their human-approval
steps. This is what puts Lemma workflows (agent → human approval → action) in front of the user.
"""
import logging
from typing import Any, Dict, List, Optional

from .sdk_client import get_lemma_pod, run_sync

logger = logging.getLogger("lifeos.workflows")


def _norm(o) -> Any:
    if isinstance(o, (dict, list)):
        return o
    for attr in ("to_dict", "model_dump"):
        if hasattr(o, attr):
            try:
                return getattr(o, attr)()
            except Exception:
                pass
    return o


def _items(o) -> List[Dict[str, Any]]:
    o = _norm(o)
    if isinstance(o, dict):
        return o.get("items", [])
    return o if isinstance(o, list) else []


async def list_workflows() -> List[Dict[str, Any]]:
    pod = get_lemma_pod()
    rows = _items(await run_sync(pod.workflows.list))
    return [{"name": w.get("name"), "description": w.get("description", "")} for w in rows]


async def start_workflow(name: str, entry_inputs: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Create a run and auto-submit its entry form so the run advances to the agent/approval."""
    pod = get_lemma_pod()
    run = _norm(await run_sync(pod.workflows.create_run, name))
    run_id = run.get("id")
    aw = run.get("active_wait") or {}
    node_id = aw.get("node_id")
    if node_id and entry_inputs is not None:
        run = _norm(await run_sync(pod.workflows.submit_form, str(run_id),
                                   node_id=node_id, inputs=entry_inputs))
    return {
        "run_id": str(run_id),
        "status": run.get("status"),
        "waiting_node": (run.get("active_wait") or {}).get("node_id"),
    }


def _run_context(rd: Dict[str, Any]) -> Dict[str, Any]:
    """The run's execution_context is a map of node_id -> that node's output."""
    ctx = rd.get("execution_context") or {}
    if isinstance(ctx.get("nodes"), dict):
        return ctx["nodes"]
    return ctx if isinstance(ctx, dict) else {}


def _preview(nodes: Dict[str, Any]) -> Dict[str, Any]:
    """Build a human-readable preview of what's awaiting approval."""
    if isinstance(nodes.get("parse"), dict):
        p = nodes["parse"]
        return {"kind": "task", "title": p.get("title"), "due_date": p.get("due_date"),
                "priority": p.get("priority"), "category": p.get("category")}
    if isinstance(nodes.get("draft"), dict):
        d = nodes["draft"]
        return {"kind": "email", "subject": d.get("subject"), "body": d.get("body")}
    return {"kind": "generic"}


async def list_approvals() -> List[Dict[str, Any]]:
    """Scan workflow runs for those paused on a human-approval form (not the entry form)."""
    pod = get_lemma_pod()
    out = []
    for wf in await list_workflows():
        name = wf["name"]
        try:
            runs = _items(await run_sync(pod.workflows.runs, name, limit=25))
        except Exception:
            continue
        for r in runs:
            if r.get("status") != "WAITING":
                continue
            run_id = r.get("id")
            try:
                rd = _norm(await run_sync(pod.workflows.run_get, str(run_id)))
            except Exception:
                continue
            aw = rd.get("active_wait") or {}
            node_id = aw.get("node_id")
            if not node_id or node_id == "entry":
                continue
            out.append({
                "run_id": str(run_id),
                "node_id": node_id,
                "workflow": name,
                "label": aw.get("node_label") or "Approval",
                "preview": _preview(_run_context(rd)),
            })
    return out


async def decide(run_id: str, node_id: str, approved: bool) -> Dict[str, Any]:
    pod = get_lemma_pod()
    r = _norm(await run_sync(pod.workflows.submit_form, str(run_id),
                             node_id=node_id, inputs={"approved": bool(approved)}))
    return {"status": r.get("status"), "run_id": str(run_id)}
