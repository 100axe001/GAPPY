"""Workspace module registration."""

from app.core.registry import LemmaModule


def _routers():
    from app.modules.workspace.api.controllers.workspace_controller import (
        router as workspace,
    )
    from app.modules.workspace.api.controllers.browser_controller import (
        router as browser,
    )

    return [workspace, browser]


module = LemmaModule(name="workspace", routers=_routers)
