from typing import Generic, TypeVar, Type, Optional, TYPE_CHECKING, Any, Union
from uuid import UUID
from pydantic import BaseModel
from sqlalchemy import select, delete
from app.core.domain.repository import IRepository
from app.core.infrastructure.db.base import Base

if TYPE_CHECKING:
    from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork

M = TypeVar("M", bound=Base)
E = TypeVar("E", bound=BaseModel)


class SqlAlchemyRepository(Generic[M, E], IRepository[E]):
    """Base SQLAlchemy repository that uses UoW for session access."""

    def __init__(
        self, uow: "SqlAlchemyUnitOfWork", model_cls: Type[M], entity_cls: Type[E]
    ):
        self.uow = uow
        self.session = uow.session
        self.model_cls = model_cls
        self.entity_cls = entity_cls

    def _to_model(self, entity: E) -> M:
        """Convert entity to model.
        Override this for complex models with relationships.
        """
        # exclude defaults?
        data = entity.model_dump(exclude_unset=True)
        return self.model_cls(**data)

    async def get(self, id: Union[UUID, str, Any]) -> Optional[E]:
        stmt = select(self.model_cls).where(self.model_cls.id == id)
        result = await self.session.execute(stmt)
        instance = result.scalars().first()
        return instance.to_entity() if instance else None

    async def create(self, entity: E) -> E:
        instance = self._to_model(entity)
        self.session.add(instance)
        await self.session.flush()

        # Collect events if entity is an aggregate root
        if hasattr(entity, "collect_events"):
            events = entity.collect_events()
            if events:
                self.uow.collect_events(events)

        return instance.to_entity()

    async def update(self, entity: E) -> E:
        stmt = select(self.model_cls).where(self.model_cls.id == entity.id)
        result = await self.session.execute(stmt)
        instance = result.scalars().first()

        if not instance:
            # If strictly REST, PUT might create if not exists, but here let's fail
            raise ValueError(f"{self.model_cls.__name__} {entity.id} not found")

        data = entity.model_dump(exclude_unset=True)
        for key, value in data.items():
            # Basic field update. Relationships need care.
            if hasattr(instance, key):
                setattr(instance, key, value)

        await self.session.flush()

        # Collect events if entity is an aggregate root
        if hasattr(entity, "collect_events"):
            events = entity.collect_events()
            if events:
                self.uow.collect_events(events)

        return instance.to_entity()

    async def delete(self, id: Union[UUID, str, Any]) -> bool:
        stmt = delete(self.model_cls).where(self.model_cls.id == id)
        result = await self.session.execute(stmt)
        return result.rowcount > 0
