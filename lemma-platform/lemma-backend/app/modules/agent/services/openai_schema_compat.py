"""JSON-schema compatibility for OpenAI-compatible model providers.

Some OpenAI-compatible providers (notably Fireworks' GLM models) cannot resolve
``$ref`` -> ``#/$defs/...`` in tool/output JSON schemas server-side. They reject
the request with e.g.::

    Error resolving schema reference '#/$defs/DisplayResourceType':
    AttributeError("'NoneType' object has no attribute 'lookup'")

pydantic-ai's default OpenAI transformer keeps ``$defs``/``$ref`` in place and
relies on the provider to resolve them (OpenAI itself does). Any tool whose
arguments include a Pydantic model or enum (e.g. ``display_resource``'s
``DisplayResourceType``) therefore breaks on these providers.

We swap in a transformer that first inlines every non-recursive ``$ref`` — so no
provider-side reference resolution is ever needed — then applies the normal
OpenAI strict-mode normalisation. Inlining is provider-agnostic and safe:
fully-inlined schemas are equivalent and accepted by OpenAI too. Recursive
schemas (which cannot be inlined) keep a minimal ``$defs``/``$ref`` structure,
exactly as before.
"""

from __future__ import annotations

from pydantic_ai._json_schema import (
    InlineDefsJsonSchemaTransformer,
    JsonSchema,
    JsonSchemaTransformer,
)
from pydantic_ai.profiles import DEFAULT_PROFILE, ModelProfile
from pydantic_ai.profiles.openai import (
    OpenAIJsonSchemaTransformer,
    openai_model_profile,
)


class InlineDefsOpenAIJsonSchemaTransformer(JsonSchemaTransformer):
    """OpenAI strict-mode transformer that first inlines ``$defs``/``$ref``."""

    def transform(self, schema: JsonSchema) -> JsonSchema:
        # Unused: walk() composes two concrete transformers instead.
        return schema

    def walk(self) -> JsonSchema:
        inlined = InlineDefsJsonSchemaTransformer(
            self.schema, strict=self.strict
        ).walk()
        openai = OpenAIJsonSchemaTransformer(inlined, strict=self.strict)
        result = openai.walk()
        # Propagate strict-compatibility so pydantic-ai infers each tool/output
        # `strict` flag from the actual (post-inline) schema, not our default.
        self.is_strict_compatible = openai.is_strict_compatible
        return result


def openai_compatible_model_profile(model_name: str) -> ModelProfile:
    """Default OpenAI profile, but with ``$defs`` inlined in tool schemas.

    Keeps every other trait pydantic-ai picks for the model and only overrides
    the JSON-schema transformer.
    """
    base = openai_model_profile(model_name) or DEFAULT_PROFILE
    return base.update(
        ModelProfile(json_schema_transformer=InlineDefsOpenAIJsonSchemaTransformer)
    )
