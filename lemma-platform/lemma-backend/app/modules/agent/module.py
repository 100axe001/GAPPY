"""Agent module registration."""

from app.core.registry import LemmaModule


def _routers():
    from app.modules.agent.api.controllers.agent_controller import router as agent
    from app.modules.agent.api.controllers.runtime_config_controller import (
        router as runtime_config,
    )
    from app.modules.agent.api.controllers.tool_controller import router as tool
    from app.modules.agent.api.controllers.conversation_controller import (
        router as conversation,
    )
    # serve_router is included before the main widget router (more specific path).
    from app.modules.agent.api.controllers.widget_controller import (
        router as widget,
        serve_router as widget_serve,
    )

    return [agent, runtime_config, tool, conversation, widget_serve, widget]


def _event_routers():
    from app.modules.agent.events.handlers import router

    return [router]


module = LemmaModule(name="agent", routers=_routers, event_routers=_event_routers)
