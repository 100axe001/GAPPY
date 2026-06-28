"""Web-search capability: the web_search toolset plus its usage instructions.

Bundling the prompt with the tool keeps the LEMMA harness consistent — every
toolset is realized as a capability — and lets the web-search guidance ride only
when the tool is actually present.
"""

from __future__ import annotations

from pydantic_ai.capabilities import AbstractCapability

from app.modules.agent.domain.prompts import load_web_search_prompt
from app.modules.agent.tools.graceful_toolset import GracefulToolset
from app.modules.agent.tools.web.pydantic_adapter import web_search_toolset


class WebSearchCapability(AbstractCapability[object]):
    """Expose the web_search tool and append its usage prompt."""

    def get_serialization_name(self) -> str | None:  # pragma: no cover - metadata
        return "web_search"

    def get_toolset(self):
        # Graceful so a web-search failure returns an error to the model rather
        # than aborting the run.
        return GracefulToolset(web_search_toolset)

    def get_instructions(self) -> str:
        return load_web_search_prompt()
