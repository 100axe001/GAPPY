"""Factory for the core authorization data service.

This is the single sanctioned place where a unit of work's SQLAlchemy session is
handed to ``AuthorizationDataService``. Services depend on this factory (or the
``AuthorizationService`` it returns) rather than reaching into ``uow.session``
themselves, keeping the service layer free of SQLAlchemy.
"""

from __future__ import annotations

from app.core.authorization.service import AuthorizationDataService
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork


def create_authorization_data_service(
    uow: SqlAlchemyUnitOfWork,
) -> AuthorizationDataService:
    return AuthorizationDataService(uow.session)
