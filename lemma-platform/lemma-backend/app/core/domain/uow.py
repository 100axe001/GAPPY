from abc import ABC, abstractmethod
from types import TracebackType
from typing import Self


class IUnitOfWork(ABC):
    """Abstract Unit of Work interface."""

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.rollback()

    @abstractmethod
    async def commit(self) -> None:
        """Commit the current transaction."""
        ...

    @abstractmethod
    async def rollback(self) -> None:
        """Rollback the current transaction."""
        ...

    # Repositories will be defined as abstract properties in concrete interfaces per module
    # or we can define a central one if monolithic. Given we have modules,
    # we might want generic access or specific mixins.
    # For simplicity in this mono-repo, we can list them here or use a dynamic approach.
