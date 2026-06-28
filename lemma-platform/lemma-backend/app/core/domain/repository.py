from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, Any, Union
from uuid import UUID
from pydantic import BaseModel
# from app.core.domain.entity import Entity

# Type variable for Entity
E = TypeVar("E", bound=BaseModel)


class IRepository(Generic[E], ABC):
    """Abstract Repository Interface."""

    @abstractmethod
    async def get(self, id: Union[UUID, str, Any]) -> Optional[E]:
        """Get entity by ID."""
        ...

    @abstractmethod
    async def create(self, entity: E) -> E:
        """Create new entity (add to session)."""
        ...

    @abstractmethod
    async def update(self, entity: E) -> E:
        """Update existing entity."""
        ...

    @abstractmethod
    async def delete(self, id: Union[UUID, str, Any]) -> bool:
        """Delete entity by ID."""
        ...
