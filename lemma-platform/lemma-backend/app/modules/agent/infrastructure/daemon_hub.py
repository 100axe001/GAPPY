"""Connection hub for user daemon websockets and cross-process run routing."""

from __future__ import annotations

import asyncio
import contextlib
import json
from dataclasses import dataclass, field
from uuid import UUID

from fastapi import WebSocket
from pydantic import BaseModel
from redis.asyncio import Redis, ConnectionPool
from redis.exceptions import RedisError

from app.core.config import settings
from app.core.log.log import get_logger
from app.modules.agent.domain.value_objects import (
    AgentEvent,
    AgentEventType,
    AgentRunUsage,
    JsonObject,
    MessageDraft,
    MessageKind,
    MessageRole,
)

logger = get_logger(__name__)


@dataclass(slots=True)
class _DaemonConnection:
    daemon_id: UUID
    user_id: UUID
    websocket: WebSocket
    send_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    run_queues: dict[UUID, asyncio.Queue[AgentEvent]] = field(default_factory=dict)
    command_task: asyncio.Task[None] | None = None
    command_ready: asyncio.Event = field(default_factory=asyncio.Event)


@dataclass(slots=True)
class _RemoteRunSubscription:
    agent_run_id: UUID
    queue: asyncio.Queue[AgentEvent]
    task: asyncio.Task[None]


class AgentRuntimeDaemonHub:
    """Tracks connected user daemons and routes run events back to harnesses."""

    def __init__(self) -> None:
        self._connections: dict[UUID, _DaemonConnection] = {}
        self._remote_runs: dict[UUID, _RemoteRunSubscription] = {}
        self._lock = asyncio.Lock()

    async def register(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
        websocket: WebSocket,
    ) -> None:
        connection = _DaemonConnection(
            daemon_id=daemon_id,
            user_id=user_id,
            websocket=websocket,
        )
        connection.command_task = asyncio.create_task(
            self._listen_for_daemon_commands(connection)
        )
        async with self._lock:
            old_connection = self._connections.get(daemon_id)
            if old_connection is not None and old_connection.command_task is not None:
                old_connection.command_task.cancel()
            self._connections[daemon_id] = connection
        with contextlib.suppress(TimeoutError):
            await asyncio.wait_for(connection.command_ready.wait(), timeout=2)

    async def unregister(self, *, daemon_id: UUID, user_id: UUID) -> None:
        async with self._lock:
            connection = self._connections.get(daemon_id)
            if connection is not None and connection.user_id == user_id:
                del self._connections[daemon_id]
                if connection.command_task is not None:
                    connection.command_task.cancel()
        if connection is not None and connection.command_task is not None:
            with contextlib.suppress(asyncio.CancelledError):
                await connection.command_task

    async def connected(self, *, daemon_id: UUID, user_id: UUID) -> bool:
        return await self._connection_for(daemon_id=daemon_id, user_id=user_id) is not None

    async def start_run(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
        agent_run_id: UUID,
        payload: JsonObject,
    ) -> asyncio.Queue[AgentEvent]:
        connection = await self._connection_for(daemon_id=daemon_id, user_id=user_id)
        queue: asyncio.Queue[AgentEvent] = asyncio.Queue()
        if connection is None:
            if not await _is_daemon_online(daemon_id=daemon_id, user_id=user_id):
                raise RuntimeError("User daemon is not connected")
            run_ready = asyncio.Event()
            task = asyncio.create_task(
                self._listen_for_run_events(
                    agent_run_id=agent_run_id,
                    queue=queue,
                    ready=run_ready,
                )
            )
            async with self._lock:
                self._remote_runs[agent_run_id] = _RemoteRunSubscription(
                    agent_run_id=agent_run_id,
                    queue=queue,
                    task=task,
                )
            # Wait until the run-event subscription is live before telling the
            # daemon to start, otherwise a fast daemon's first events can be
            # published before this subscriber is ready and would be lost.
            with contextlib.suppress(TimeoutError):
                await asyncio.wait_for(run_ready.wait(), timeout=2)
            await self._publish_daemon_command(
                daemon_id=daemon_id,
                user_id=user_id,
                payload={
                    "type": "run.start",
                    "daemon_id": str(daemon_id),
                    "user_id": str(user_id),
                    "agent_run_id": str(agent_run_id),
                    "payload": payload,
                },
            )
            return queue

        connection.run_queues[agent_run_id] = queue
        await self._send(
            connection,
            {
                "type": "run.start",
                "agent_run_id": str(agent_run_id),
                "payload": payload,
            },
        )
        return queue

    async def stop_run(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
        agent_run_id: UUID,
    ) -> None:
        connection = await self._connection_for(daemon_id=daemon_id, user_id=user_id)
        if connection is None:
            await self._publish_daemon_command(
                daemon_id=daemon_id,
                user_id=user_id,
                payload={
                    "type": "run.stop",
                    "daemon_id": str(daemon_id),
                    "user_id": str(user_id),
                    "agent_run_id": str(agent_run_id),
                },
            )
            return
        await self._send(
            connection,
            {
                "type": "run.stop",
                "agent_run_id": str(agent_run_id),
            },
        )

    async def finish_run(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
        agent_run_id: UUID,
    ) -> None:
        connection = await self._connection_for(daemon_id=daemon_id, user_id=user_id)
        if connection is not None:
            connection.run_queues.pop(agent_run_id, None)
        async with self._lock:
            subscription = self._remote_runs.pop(agent_run_id, None)
        if subscription is not None:
            subscription.task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await subscription.task

    async def handle_run_event(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
        message: JsonObject,
    ) -> None:
        connection = await self._connection_for(daemon_id=daemon_id, user_id=user_id)
        try:
            agent_run_id = UUID(str(message["agent_run_id"]))
        except (KeyError, ValueError):
            return

        event_payload = message.get("event", message.get("payload"))
        if connection is not None:
            queue = connection.run_queues.get(agent_run_id)
            if queue is not None:
                await queue.put(
                    _event_from_payload(event_payload, agent_run_id=agent_run_id)
                )
        await self._publish_run_event(
            agent_run_id=agent_run_id,
            payload={
                "agent_run_id": str(agent_run_id),
                "event": event_payload,
            },
        )

    async def _connection_for(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
    ) -> _DaemonConnection | None:
        async with self._lock:
            connection = self._connections.get(daemon_id)
            if connection is None or connection.user_id != user_id:
                return None
            return connection

    async def _send(self, connection: _DaemonConnection, payload: JsonObject) -> None:
        async with connection.send_lock:
            await connection.websocket.send_json(payload)

    async def _listen_for_daemon_commands(
        self,
        connection: _DaemonConnection,
    ) -> None:
        redis: Redis | None = None
        pubsub = None
        channel = _daemon_command_channel(connection.daemon_id)
        try:
            redis = Redis.from_url(settings.redis_url, decode_responses=True)
            pubsub = redis.pubsub(ignore_subscribe_messages=True)
            await pubsub.subscribe(channel)
            await redis.set(_daemon_online_key(connection.daemon_id), str(connection.user_id))
            connection.command_ready.set()
            async for raw_message in pubsub.listen():
                if raw_message.get("type") != "message":
                    continue
                command = _json_dict(raw_message.get("data"))
                if not _matches_daemon_command(command, connection=connection):
                    continue
                await self._send(connection, command)
        except asyncio.CancelledError:
            raise
        except (OSError, RedisError) as exc:
            connection.command_ready.set()
            logger.debug(
                "Daemon command subscriber unavailable",
                daemon_id=str(connection.daemon_id),
                error=str(exc),
            )
        finally:
            connection.command_ready.set()
            if pubsub is not None:
                with contextlib.suppress(Exception):
                    await pubsub.unsubscribe(channel)
                with contextlib.suppress(Exception):
                    await pubsub.aclose()
            if redis is not None:
                with contextlib.suppress(Exception):
                    await redis.delete(_daemon_online_key(connection.daemon_id))
                with contextlib.suppress(Exception):
                    await redis.aclose()

    async def _listen_for_run_events(
        self,
        *,
        agent_run_id: UUID,
        queue: asyncio.Queue[AgentEvent],
        ready: asyncio.Event | None = None,
    ) -> None:
        redis: Redis | None = None
        pubsub = None
        channel = _run_event_channel(agent_run_id)
        try:
            redis = Redis.from_url(settings.redis_url, decode_responses=True)
            pubsub = redis.pubsub(ignore_subscribe_messages=True)
            await pubsub.subscribe(channel)
            if ready is not None:
                ready.set()
            async for raw_message in pubsub.listen():
                if raw_message.get("type") != "message":
                    continue
                message = _json_dict(raw_message.get("data"))
                event_payload = message.get("event", message.get("payload"))
                await queue.put(
                    _event_from_payload(event_payload, agent_run_id=agent_run_id)
                )
        except asyncio.CancelledError:
            raise
        except (OSError, RedisError) as exc:
            if ready is not None:
                ready.set()
            await queue.put(
                AgentEvent(
                    type=AgentEventType.ERROR,
                    data=f"Daemon event subscriber unavailable: {exc}",
                    agent_run_id=agent_run_id,
                )
            )
        finally:
            if ready is not None:
                ready.set()
            if pubsub is not None:
                with contextlib.suppress(Exception):
                    await pubsub.unsubscribe(channel)
                with contextlib.suppress(Exception):
                    await pubsub.aclose()
            if redis is not None:
                with contextlib.suppress(Exception):
                    await redis.aclose()

    async def _publish_daemon_command(
        self,
        *,
        daemon_id: UUID,
        user_id: UUID,
        payload: JsonObject,
    ) -> None:
        payload = {
            **payload,
            "daemon_id": str(daemon_id),
            "user_id": str(user_id),
        }
        await _publish_json(_daemon_command_channel(daemon_id), payload)

    async def _publish_run_event(
        self,
        *,
        agent_run_id: UUID,
        payload: JsonObject,
    ) -> None:
        await _publish_json(_run_event_channel(agent_run_id), payload)


def daemon_mcp_url(conversation_id: UUID) -> str:
    base_url = settings.api_url.rstrip("/")
    return f"{base_url}/agent-runtime/conversations/{conversation_id}/mcp"


def _daemon_command_channel(daemon_id: UUID) -> str:
    return f"agent-runtime:daemon:{daemon_id}:commands"


def _run_event_channel(agent_run_id: UUID) -> str:
    return f"agent-runtime:run:{agent_run_id}:events"


def _daemon_online_key(daemon_id: UUID) -> str:
    return f"agent-runtime:daemon:{daemon_id}:online"


_redis_pool: ConnectionPool | None = None


def _get_redis() -> Redis:
    global _redis_pool  # noqa: PLW0603
    if _redis_pool is None:
        _redis_pool = ConnectionPool.from_url(settings.redis_url, decode_responses=True)
    return Redis(connection_pool=_redis_pool)


async def _publish_json(channel: str, payload: JsonObject) -> None:
    await _get_redis().publish(channel, json.dumps(payload))


async def _is_daemon_online(*, daemon_id: UUID, user_id: UUID) -> bool:
    value = await _get_redis().get(_daemon_online_key(daemon_id))
    return value == str(user_id)


def _json_dict(value: object) -> JsonObject:
    if isinstance(value, bytes):
        value = value.decode()
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return {}
        return parsed if isinstance(parsed, dict) else {}
    return value if isinstance(value, dict) else {}


def _matches_daemon_command(
    command: JsonObject,
    *,
    connection: _DaemonConnection,
) -> bool:
    return (
        command.get("daemon_id") == str(connection.daemon_id)
        and command.get("user_id") == str(connection.user_id)
        and command.get("type") in {"run.start", "run.stop"}
    )


def _event_from_payload(payload: object, *, agent_run_id: UUID) -> AgentEvent:
    if isinstance(payload, AgentEvent):
        return payload
    if not isinstance(payload, dict):
        return AgentEvent(
            type=AgentEventType.ERROR,
            data="Daemon sent an invalid run event",
            agent_run_id=agent_run_id,
        )
    event_type = AgentEventType(payload.get("type", AgentEventType.STATUS.value))
    data = _normalize_event_data(event_type, payload.get("data"))
    return AgentEvent(type=event_type, data=data, agent_run_id=agent_run_id)


def _normalize_event_data(event_type: AgentEventType, data: object) -> object:
    if event_type == AgentEventType.MESSAGE and isinstance(data, dict):
        return _message_draft_from_payload(data)
    if event_type == AgentEventType.USAGE and isinstance(data, dict):
        return AgentRunUsage.model_validate(data)
    if isinstance(data, BaseModel):
        return data
    return data


def _message_draft_from_payload(data: dict) -> MessageDraft:
    """Build a flat MessageDraft from a daemon MESSAGE payload."""

    role = MessageRole(data.get("role", MessageRole.ASSISTANT.value))
    metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else None
    raw_kind = data.get("kind")

    if raw_kind is None:
        # Daemons that only stream text send a plain body under ``text``/``content``.
        body = data.get("text")
        if body is None:
            body = data.get("content")
        return MessageDraft.of_text(
            body if isinstance(body, str) else ("" if body is None else str(body)),
            role=role,
            metadata=metadata,
        )

    kind = MessageKind(raw_kind)
    if kind == MessageKind.TOOL_CALL:
        return MessageDraft.of_tool_call(
            tool_name=str(data.get("tool_name") or "unknown_tool"),
            tool_call_id=str(data.get("tool_call_id") or ""),
            tool_args=data.get("tool_args"),
            role=role,
            metadata=metadata,
        )
    if kind == MessageKind.TOOL_RETURN:
        return MessageDraft.of_tool_return(
            tool_name=data.get("tool_name"),
            tool_call_id=str(data.get("tool_call_id") or ""),
            tool_result=data.get("tool_result"),
            role=role,
            metadata=metadata,
        )
    return MessageDraft(
        role=role,
        kind=kind,
        text=data.get("text"),
        metadata=metadata,
    )


agent_runtime_daemon_hub = AgentRuntimeDaemonHub()
