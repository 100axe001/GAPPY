---
name: integration-creator
description: Generate or regenerate a Lemma integration package from an OpenAPI spec inside lemma-connectors. Use this when adding a new provider package, improving generated package quality, or regenerating an existing app with the expected naming, typing, and binary-result behavior.
---

# Integration Creator

Use this skill when working inside `lemma-connectors` to add or regenerate a
provider package from an OpenAPI spec.

## What this skill is for

- generating typed transport clients from OpenAPI specs
- generating canonical provider schema models
- generating typed tool input/output models
- generating operation/resource modules
- keeping operation names logical and agent-friendly
- preserving typed binary/file results
- validating that the package imports and discovery surface are solid

## Required package shape

Each app package should contain:

- `client.py`
- `generated/client/`
- `generated/pydantic_models.py`
- `generated/pydantic_model_registry.json`
- `generated/openapi_metadata.json`
- `generated/tool_types.py`
- `resources/__init__.py`
- `resources/<resource>.py`

Operation coverage should be near-full for the in-scope provider API surface.

## Generator contract

- Tool names stay explicit and provider-level.
- Operation names come from cleaned provider `operationId` values, not raw path
  ancestry.
- Resource files group related operations together.
- Tool and operation input/output models must be real typed Pydantic models.
- Binary or file-like endpoints must surface `BinaryContentResult`, not
  placeholder `dict[str, object]` wrappers.
- Preserve provider wire-format strings when the API uses url-safe/base64-like
  encodings that should not be eagerly decoded by Pydantic, such as Gmail
  message body data and raw MIME payloads.
- Descriptions should help an agent choose and use the operation.

## Quality rules

- Prefer fixing the generator once over hand-editing many generated files.
- Do not keep awkward names like `users_messages_list` when the provider intent
  is clearly `messages_list`.
- Do not include low-value text like "backed by this tool".
- Preserve useful provider field descriptions on generated models.
- Keep Slack admin endpoints excluded.
- Expect Jira and similarly large specs to need extra validation and occasional
  provider-specific post-processing patches.
- Generated runtime execution must handle reserved-identifier parameters cleanly,
  for example mapping a public `format` field onto generated client parameters
  like `format_`.

## Workflow

Use the exact commands and validation checklist in
[references/workflow.md](references/workflow.md).

## Done bar

Before considering the work complete:

- the app package imports successfully
- info client discovery works
- operation names are sensible
- output schemas are real typed schemas
- binary/file endpoints expose `BinaryContentResult`
- tests and compile checks pass
