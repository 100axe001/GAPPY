"""Shared history processor wiring for agent harnesses."""

from __future__ import annotations

from app.modules.agent.domain.value_objects import HarnessOptions


def build_history_processors(
    options: HarnessOptions,
    *,
    summarization_model: object,
) -> list[object]:
    processors = list(options.history_processors)
    if (
        not options.history_summarization_enabled
        or options.history_summarization_token_limit <= 0
    ):
        return processors

    from pydantic_deep import create_summarization_processor

    processors.append(
        create_summarization_processor(
            model=summarization_model,
            trigger=("tokens", options.history_summarization_token_limit),
            keep=("messages", options.history_summarization_keep_messages),
        )
    )
    return processors
