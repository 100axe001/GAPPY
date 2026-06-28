# Agent Surfaces

`agent_surfaces` connects external platforms to pod-scoped agent conversations.
It owns platform ingress, identity resolution, conversation linking, and outbound
delivery. The `agent` module owns conversations, messages, agent runs, harness
execution, and SSE.

Supported platforms:

- Slack
- Microsoft Teams
- WhatsApp
- Telegram
- Gmail
- Outlook

## Flow

1. A webhook, local receiver, or integration trigger enters the surface module.
2. Webhook security validates the request when enabled.
3. A platform adapter parses the raw payload into `ParsedInboundSurfaceEvent`.
4. The ingress service resolves the surface installation and internal user.
5. Duplicate inbound messages are ignored.
6. A `agent_surface_conversation_links` row maps the external thread to an
   `agent_conversations` row.
7. The agent conversation receives a user message and starts an agent run.
8. The agent worker executes the run through the normal agent harness.
9. Assistant text messages are sent back to the original platform thread as
   they are produced by the run observer.

Webhook handlers return quickly; model output is not streamed inside webhook
requests.

## Storage

Primary tables:

- `agent_surfaces`
- `agent_surface_external_users`
- `agent_surface_conversation_links`

`agent_surfaces.agent_id` is nullable. Null means the surface talks to the pod
default agent. A named-agent surface stores `agent_id` and the API resolves
`agent_name` for display.

Conversation metadata stores the useful search/debug keys:

- `source = "agent_surfaces"`
- `surface_id`
- `surface_platform`
- `external_channel_id`
- `external_thread_id`
- `external_user_id`
- `external_message_id`

## API

Surface management routes live under pod resources:

- `POST /pods/{pod_id}/surfaces`
- `GET /pods/{pod_id}/surfaces`
- `GET /pods/{pod_id}/surfaces/{surface_id}`
- `PATCH /pods/{pod_id}/surfaces/{surface_id}`
- `PATCH /pods/{pod_id}/surfaces/{surface_id}/toggle`
- `GET /pods/{pod_id}/surfaces/platforms/{platform}/checklist`

Webhook routes:

- `POST /surfaces/webhooks/{platform}` for platform-level webhooks.
- Matching `GET` routes handle platform verification callbacks.

Standalone/local mode can also run outbound receivers for surfaces that do not
have a public webhook URL:

- Telegram local receivers use Bot API long polling after clearing the webhook when `ENABLE_TELEGRAM_POLLING_MODE=true`.
- Slack local receivers use Socket Mode when `ENABLE_SLACK_SOCKET_MODE=true`.

Both receiver types publish the same surface webhook event as the HTTP
controller, so ingress routing and agent execution stay shared.

## Layout

Every platform lives in one package under `platforms/<platform>/` with the
same shape:

- `adapter.py` — implements `SurfacePlatformAdapterPort` (parse, enrich,
  sender profile, send message, processing indicator); registered in
  `infrastructure/adapters/registry.py`.
- `parser.py` — stateless inbound payload parsing to `ParsedInboundSurfaceEvent`
  via `parse(payload, headers)`.
- `service.py` — outbound platform API operations used by the adapter and tools.
- `models.py` — tool params/results and attachment models.
- `tools.py` — `build_<platform>_surface_toolset(credentials)` for agent runs.
- `client.py` (where needed) — low-level API client helpers (Slack SDK wiring,
  Teams Graph/Bot Framework tokens).

Shared helpers (attachment selection/coercion, prompt rendering) live in
`platforms/common.py`; Gmail/Outlook share `platforms/email_common.py` and
`platforms/email_models.py`.

## Tools

Surface platform tools are attached to agent runs through the agent toolset
resolver when the conversation metadata indicates a surface context
(`infrastructure/adapters/platform_tool_factory.py`). The tool factory resolves
credentials and routing data from the surface link and agent context, then
builds the per-platform toolset from `platforms/<platform>/tools.py`.

## Testing

The e2e suite uses mocked platform servers for outbound delivery and fixtures
copied from real event logs for Slack and Teams ingress. It covers surface CRUD,
webhook verification, chat ingress, conversation reuse, agent-run completion
egress, signup/contact linking, and email triggers.

Key files live under [tests/e2e](tests/e2e) with one full-flow file per platform.

Useful commands:

```bash
PYTHONPATH=. uv run pytest app/modules/agent_surfaces/tests/e2e
PYTHONPATH=. uv run pytest app/modules/agent_surfaces/tests/unit
```

## Debugging

Raw webhook logging can be enabled with:

- `SURFACE_RAW_WEBHOOK_LOG_DIR`
- `SURFACE_RAW_WEBHOOK_LOG_SOURCES`

Example:

```bash
SURFACE_RAW_WEBHOOK_LOG_DIR=/tmp/lemma-surface-webhooks
SURFACE_RAW_WEBHOOK_LOG_SOURCES=slack,teams
```

This writes JSONL payloads that can be promoted into fixtures when platform
behavior changes.
