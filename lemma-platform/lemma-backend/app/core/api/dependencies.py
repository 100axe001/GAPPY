from typing import AsyncGenerator, Annotated
from fastapi import Depends
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.core.infrastructure.db.session import async_session_maker
from app.core.infrastructure.db.uow_factory import (
    create_uow_from_session_maker,
    SessionUnitOfWorkFactory,
    UnitOfWorkFactory,
)


from app.modules.identity.domain.user_entities import UserEntity
from fastapi import Request, HTTPException, status


async def get_uow() -> AsyncGenerator[SqlAlchemyUnitOfWork, None]:
    """Dependency that provides a Unit of Work instance.

    This handles the session lifecycle: creates a session, yields the UoW,
    and handles commit/rollback automatically via the context manager.
    """
    async with create_uow_from_session_maker(async_session_maker) as uow:
        yield uow


def get_uow_factory() -> UnitOfWorkFactory:
    """Dependency that provides a Unit of Work factory."""
    return SessionUnitOfWorkFactory(async_session_maker)


def get_current_user(request: Request) -> UserEntity:
    """Dependency that provides the current authenticated user."""
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated",
        )
    return user


UoWDep = Annotated[SqlAlchemyUnitOfWork, Depends(get_uow)]
CurrentUser = Annotated[UserEntity, Depends(get_current_user)]
