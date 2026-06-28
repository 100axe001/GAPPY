"""Current authorization context helpers."""

from __future__ import annotations

from contextvars import ContextVar, Token

from app.core.authorization.context import Context


_current_context: ContextVar[Context | None] = ContextVar(
    "authorization_current_context",
    default=None,
)


def set_current_context(ctx: Context | None) -> Token:
    return _current_context.set(ctx)


def get_current_context() -> Context | None:
    return _current_context.get()


def reset_current_context(token: Token) -> None:
    _current_context.reset(token)
