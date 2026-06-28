"""Datastore module registration."""

from contextlib import asynccontextmanager

from app.core.log.log import get_logger
from app.core.registry import LemmaModule

logger = get_logger(__name__)


def _routers():
    from app.modules.datastore.api.controllers.record_controller import router as record
    from app.modules.datastore.api.controllers.query_controller import router as query
    from app.modules.datastore.api.controllers.table_controller import router as table
    from app.modules.datastore.api.controllers.file_controller import router as file
    from app.modules.datastore.api.controllers.public_file_controller import (
        router as public_file,
    )
    from app.modules.datastore.api.controllers.signed_file_controller import (
        router as signed_file,
    )
    from app.modules.datastore.api.controllers.changes_controller import (
        router as changes,
    )

    return [record, query, table, file, public_file, signed_file, changes]


def _event_routers():
    from app.modules.datastore.events.handlers import router

    return [router]


@asynccontextmanager
async def _backfill_query_role(app):
    """Ensure the RLS-subject role can read every existing pod schema, so ad-hoc
    datastore queries (run under that role) are scoped. Non-fatal: new tables
    also grant on creation, and queries fail closed."""
    try:
        from app.modules.datastore.api.dependencies import get_schema_manager

        await get_schema_manager().backfill_query_role_grants()
        logger.info("Datastore query role grants ensured")
    except Exception:  # noqa: BLE001
        logger.warning("Failed to ensure datastore query role grants", exc_info=True)
    yield


@asynccontextmanager
async def _close_reindex_queue(context):
    try:
        yield
    finally:
        from app.modules.datastore.infrastructure.reindex_queue import (
            close_datastore_reindex_queue,
        )

        await close_datastore_reindex_queue()


module = LemmaModule(
    name="datastore",
    routers=_routers,
    event_routers=_event_routers,
    api_lifespans=(_backfill_query_role,),
    worker_lifespans=(_close_reindex_queue,),
)
