"""Redis-based Channel Service for event publishing and subscription."""

import json
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any, List, Optional
from redis.asyncio import Redis
from redis.exceptions import RedisError
from app.core.config import settings


class ChannelService:
    """Service to handle Redis key-value operations and Pub/Sub."""

    def __init__(self, redis_url: Optional[str] = None):
        self.redis_url = redis_url
        self._redis: Optional[Redis] = None

    async def connect(self):
        """Establish Redis connection."""
        if not self._redis:
            url = self.redis_url or settings.redis_url
            self._redis = Redis.from_url(
                url,
                decode_responses=True,
                health_check_interval=30,
                socket_keepalive=True,
                max_connections=settings.redis_max_connections,
            )

    async def disconnect(self):
        """Close Redis connection."""
        if self._redis:
            if hasattr(self._redis, "aclose"):
                await self._redis.aclose()
            else:
                await self._redis.close()
            self._redis = None

    async def publish(self, channel: str, message: Any) -> None:
        """Publish a message to a channel."""
        if not self._redis:
            await self.connect()

        payload = message
        if not isinstance(message, (str, bytes)):
            payload = json.dumps(message)

        try:
            await self._redis.publish(channel, payload)  # type: ignore
        except RedisError:
            await self.disconnect()
            await self.connect()
            await self._redis.publish(channel, payload)  # type: ignore

    @asynccontextmanager
    async def subscribe(
        self, channels: List[str]
    ) -> AsyncGenerator[AsyncGenerator[Any, None], None]:
        """Subscribe to channels and yield an event iterator."""
        if not self._redis:
            await self.connect()

        try:
            pubsub = self._redis.pubsub(ignore_subscribe_messages=True)  # type: ignore
            await pubsub.subscribe(*channels)
        except RedisError:
            await self.disconnect()
            await self.connect()
            pubsub = self._redis.pubsub(ignore_subscribe_messages=True)  # type: ignore
            await pubsub.subscribe(*channels)

        async def iterator() -> AsyncGenerator[Any, None]:
            async for message in pubsub.listen():
                if message["type"] == "message":
                    yield message["data"]

        try:
            yield iterator()
        finally:
            await pubsub.unsubscribe()
            if hasattr(pubsub, "aclose"):
                await pubsub.aclose()
            else:
                await pubsub.close()


# Global singleton to be managed by app functionality if needed,
# or we can rely on DI to provide the same instance if we scope it correctly.
# For simplicity, we create a singleton instance we can manage in lifespan.
channel_service = ChannelService()


async def get_channel_service() -> ChannelService:
    """Dependency provider for ChannelService."""
    if not channel_service._redis:
        await channel_service.connect()
    return channel_service
