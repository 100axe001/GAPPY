"""Workflow module registration."""

from app.core.registry import LemmaModule


def _routers():
    from app.modules.workflow.api.flow_controller import router as flow
    from app.modules.workflow.api.flow_run_controller import router as flow_run

    return [flow, flow_run]


def _event_routers():
    # handlers.py also defines 4 streaq tasks/crons that register on import.
    from app.modules.workflow.events.handlers import router

    return [router]


module = LemmaModule(name="workflow", routers=_routers, event_routers=_event_routers)
