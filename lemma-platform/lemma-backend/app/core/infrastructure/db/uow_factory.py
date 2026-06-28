"""Unit of Work Factory for dependency injection.

Provides factory functions that create UoW instances.
Supports both Postgres (production) and SQLite (testing).
"""

from contextlib import asynccontextmanager, AbstractAsyncContextManager
from typing import AsyncGenerator, Protocol, runtime_checkable

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.core.infrastructure.events.message_bus import get_message_bus


@runtime_checkable
class UnitOfWorkFactory(Protocol):
    """Protocol for UoW factories."""

    def __call__(self) -> AbstractAsyncContextManager[SqlAlchemyUnitOfWork]:
        """Create and yield a UoW instance."""
        ...


class SessionUnitOfWorkFactory:
    """Factory that creates UoW from an async session maker.

    Used for production with Postgres.
    """

    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self._session_maker = session_maker

    @asynccontextmanager
    async def __call__(self) -> AsyncGenerator[SqlAlchemyUnitOfWork, None]:
        """Create UoW with auto-commit on success."""
        async with self._session_maker() as session:
            uow = SqlAlchemyUnitOfWork(session, message_bus=get_message_bus())
            try:
                yield uow
            except BaseException:
                await uow.rollback()
                raise
            else:
                try:
                    await uow.commit()
                except BaseException:
                    await uow.rollback()
                    raise


@asynccontextmanager
async def create_uow_from_session_maker(
    session_maker: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[SqlAlchemyUnitOfWork, None]:
    """Create a UoW from a session maker.

    Used for FastAPI dependency injection and general usage.
    """
    async with session_maker() as session:
        uow = SqlAlchemyUnitOfWork(session, message_bus=get_message_bus())
        try:
            yield uow
        except BaseException:
            await uow.rollback()
            raise
        else:
            try:
                await uow.commit()
            except BaseException:
                await uow.rollback()
                raise
