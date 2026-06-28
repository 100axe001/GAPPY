"""Synchronize pod membership into datastore reserved user records."""

from __future__ import annotations

from app.modules.datastore.domain.datastore_entities import (
    ColumnSchema,
    DatastoreDataType,
    DatastoreTableEntity,
)
from app.modules.datastore.domain.errors import DatastoreRecordNotFoundError
from app.modules.datastore.domain.ports import (
    DatastoreSchemaPort,
    DatastoreTableRepositoryPort,
)
from app.modules.datastore.services.record_service import RecordService
from app.modules.datastore.services.table_context import TableContext
from app.modules.pod.domain.events import PodMemberAddedEvent, PodMemberRemovedEvent
from app.core.log.log import get_logger

logger = get_logger(__name__)

_RESERVED_USERS_TABLE = "reserved_users"


class PodMemberSyncService:
    def __init__(
        self,
        table_repository: DatastoreTableRepositoryPort,
        schema_manager: DatastoreSchemaPort,
        record_service: RecordService,
    ):
        self.table_repository = table_repository
        self.schema_manager = schema_manager
        self.record_service = record_service

    async def sync_member_added(self, event: PodMemberAddedEvent) -> None:
        table = await self._ensure_reserved_users_table(event.pod_id)
        context = TableContext.from_table_entity(
            table,
            schema_name=self.schema_manager.get_schema_name(event.pod_id),
            events_enabled=False,
        )

        payload = {
            "user_id": str(event.user_id),
            "email": event.email,
            "first_name": event.first_name or "",
            "last_name": event.last_name or "",
            "role": event.role,
        }

        try:
            await self.record_service.get_record(
                context, str(event.user_id), event.user_id
            )
            await self.record_service.update_record(
                context,
                str(event.user_id),
                payload,
                event.user_id,
            )
        except DatastoreRecordNotFoundError:
            await self.record_service.create_record(context, payload, event.user_id)

    async def sync_member_removed(self, event: PodMemberRemovedEvent) -> None:
        table = await self.table_repository.get_by_datastore_and_name(
            event.pod_id,
            _RESERVED_USERS_TABLE,
        )
        if not table:
            return

        context = TableContext.from_table_entity(
            table,
            schema_name=self.schema_manager.get_schema_name(event.pod_id),
            events_enabled=False,
        )

        try:
            await self.record_service.delete_record(
                context, str(event.user_id), event.user_id
            )
        except DatastoreRecordNotFoundError:
            return

    async def _ensure_reserved_users_table(self, pod_id):
        table = await self.table_repository.get_by_datastore_and_name(
            pod_id,
            _RESERVED_USERS_TABLE,
        )
        if table:
            return table

        columns = [
            ColumnSchema(name="user_id", type=DatastoreDataType.TEXT, required=True),
            ColumnSchema(name="email", type=DatastoreDataType.TEXT),
            ColumnSchema(name="first_name", type=DatastoreDataType.TEXT),
            ColumnSchema(name="last_name", type=DatastoreDataType.TEXT),
            ColumnSchema(name="role", type=DatastoreDataType.TEXT),
        ]

        entity = DatastoreTableEntity(
            pod_id=pod_id,
            table_name=_RESERVED_USERS_TABLE,
            columns=columns,
            primary_key_column="user_id",
            enable_rls=False,
        )

        table = await self.table_repository.create(entity)
        await self.schema_manager.create_table(
            pod_id,
            _RESERVED_USERS_TABLE,
            "user_id",
            columns,
            enable_rls=False,
        )
        return table
