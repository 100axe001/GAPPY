from typing import Optional

from sqlalchemy import String, cast, select

from app.core.domain.message_bus import MessageBus
from app.core.infrastructure.db.repository import SqlAlchemyRepository
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.connectors.domain.connect_request import ConnectRequestEntity
from app.modules.connectors.domain.ports import ConnectRequestRepositoryPort
from app.modules.connectors.infrastructure.models import ConnectRequest


class ConnectRequestRepository(
    SqlAlchemyRepository[ConnectRequest, ConnectRequestEntity],
    ConnectRequestRepositoryPort,
):
    """Repository for ConnectRequest operations."""

    def __init__(
        self,
        uow: SqlAlchemyUnitOfWork,
        message_bus: MessageBus | None = None,
    ):
        super().__init__(uow, ConnectRequest, ConnectRequestEntity)
        if message_bus is not None:
            self.uow.set_message_bus(message_bus)

    async def get_by_state(self, state: str) -> Optional[ConnectRequestEntity]:
        """Get connect request by state attribute."""
        stmt = select(ConnectRequest).where(
            cast(ConnectRequest.attributes["state"], String) == f'"{state}"'
        )
        result = await self.session.execute(stmt)
        instance = result.scalars().first()
        return instance.to_entity() if instance else None
