from redis.asyncio import Redis


class RedisManager:
    def __init__(self, redis_url: str):
        self.redis = Redis.from_url(redis_url, decode_responses=True)

    async def close(self):
        await self.redis.close()
