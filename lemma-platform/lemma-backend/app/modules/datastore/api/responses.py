from __future__ import annotations


def detail_response(detail_cls, base_cls, entity):
    """Compose a ``*DetailResponse`` from its base ``*Response`` + ``allowed_actions``.

    Mirrors the previous controller pattern of validating the entity into the base
    response model and layering the entity's ``allowed_actions`` on top.
    """
    return detail_cls(
        **base_cls.model_validate(entity).model_dump(),
        allowed_actions=entity.allowed_actions,
    )
