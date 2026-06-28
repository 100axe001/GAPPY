"""Icon module registration."""

from app.core.registry import LemmaModule


def _routers():
    from app.modules.icon.api.controllers.icon_controller import router as icon

    return [icon]


module = LemmaModule(name="icon", routers=_routers)
